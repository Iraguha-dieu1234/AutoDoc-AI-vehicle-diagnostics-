"""Optional LLM layer (Anthropic API). Falls back to the rule engine when no key is set."""
import json
import os

SYSTEM = """You are AutoDoc, an expert automotive diagnostic assistant with the knowledge of a senior
master technician. Analyse the vehicle data and the owner's description. Be specific to the
make/model/age/mileage where possible and reason from symptom combinations. Rank causes by
likelihood. Never claim certainty; the final repair must be confirmed by a qualified mechanic.
Flag safety-critical issues (brakes, overheating, steering, fuel leaks, fire risk) clearly.
Use the response language requested in the user prompt. For Rwanda, make advice practical
for the stated vehicle and conditions; mention dusty roads or traffic only when relevant.
Do not invent Rwanda-specific repair prices, parts availability, or vehicle-history data."""

ANALYSIS_FORMAT = """Reply with ONLY a JSON object:
{"summary":"2-3 sentences","urgency":"High|Medium|Low","safe_to_drive":"short statement",
"causes":[{"name":"","likelihood":0-100,"why":"","checks":[""],"diy":true}],
"questions":["up to 3 follow-up questions"],"maintenance":["advice"],
"codes":[{"code":"","meaning":""}]}
Give 3 to 5 causes."""

MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5")


def available() -> bool:
    return bool(os.getenv("ANTHROPIC_API_KEY"))


def _client():
    import anthropic  # imported lazily so the app runs without the SDK
    return anthropic.Anthropic()


def build_prompt(vehicle: dict, rule_hints: dict) -> str:
    hints = "; ".join(c["name"] for c in rule_hints["causes"]) or "none"
    codes = "; ".join(f'{c["code"]} ({c["meaning"]})' for c in rule_hints["codes"]) or "(none)"
    return (
        f"VEHICLE: {vehicle.get('model') or 'unknown'}, year {vehicle.get('year') or 'unknown'}, "
        f"{vehicle.get('km') or 'unknown'} km, {vehicle.get('fuel')}, {vehicle.get('transmission')}.\n"
        f"OWNER DESCRIPTION: {vehicle.get('description') or '(none)'}\n"
        f"RESPONSE LANGUAGE: {'Kinyarwanda' if vehicle.get('language') == 'rw' else 'English'}.\n"
        "Give general diagnostic guidance, not a certified repair or Rwanda-specific dataset claim. "
        "Use the vehicle manufacturer's specifications when intervals or parts differ.\n"
        f"OBD-II CODES: {codes}\n"
        f"REFERENCE ENGINE HINTS (rule-based, may be incomplete): {hints}"
    )


def analyze(vehicle: dict, rule_hints: dict) -> tuple[dict, list]:
    """Returns (report_dict, message_history)."""
    prompt = build_prompt(vehicle, rule_hints)
    msg = _client().messages.create(
        model=MODEL, max_tokens=2000, system=f"{SYSTEM}\n{ANALYSIS_FORMAT}",
        messages=[{"role": "user", "content": prompt}])
    text = msg.content[0].text.strip()
    text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    report = json.loads(text)
    history = [{"role": "user", "content": prompt},
               {"role": "assistant", "content": text}]
    return report, history


def follow_up(history: list, question: str, language: str = "en") -> str:
    response_language = "Kinyarwanda" if language == "rw" else "English"
    msgs = history + [{"role": "user", "content":
        f"Answer in {response_language}. Follow-up from the owner "
        "(answer conversationally in plain text, concise, "
        "keep safety caveats): " + question}]
    msg = _client().messages.create(
        model=MODEL, max_tokens=800,
        system=f"{SYSTEM}\nAnswer conversationally in concise plain text.",
        messages=msgs)
    return msg.content[0].text
