"""AutoDoc – AI-Based Vehicle Fault Diagnosis & Maintenance Assistant (Flask)."""
import os

from flask import Flask, jsonify, render_template, request

from diagnosis import ai, engine, localization

try:  # optional .env support
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)


def _vehicle(data: dict) -> dict:
    try:
        km = int(data.get("km") or 0)
    except ValueError:
        km = 0
    return {"model": data.get("model", "").strip(), "year": data.get("year", ""),
            "km": km, "fuel": data.get("fuel", "Petrol"),
            "transmission": data.get("transmission", "Manual"),
            "description": data.get("description", "").strip(),
            "codes": data.get("codes", ""),
            "language": "rw" if data.get("language") == "rw" else "en"}


@app.get("/")
def index():
    return render_template("index.html", ai_enabled=ai.available())


@app.post("/api/diagnose")
def api_diagnose():
    v = _vehicle(request.get_json(force=True, silent=True) or {})
    if not v["description"] and not v["codes"]:
        message = localization.text(
            "Please describe the problem or enter an OBD-II code.", v["language"])
        return jsonify(error=message), 400
    rules = engine.diagnose(v["description"], v["km"], v["fuel"], v["codes"])
    if ai.available():
        try:
            report, history = ai.analyze(v, rules)
            return jsonify(mode="ai", report=report, history=history,
                           rules=localization.translate_rules(rules, v["language"]))
        except Exception as exc:  # network, quota, bad JSON ... -> degrade gracefully
            app.logger.warning("AI failed, using rules: %s", exc)
    return jsonify(mode="rules", rules=localization.translate_rules(rules, v["language"]))


@app.post("/api/chat")
def api_chat():
    data = request.get_json(force=True, silent=True) or {}
    if not ai.available():
        message = localization.text(
            "AI follow-up needs ANTHROPIC_API_KEY.",
            "rw" if data.get("language") == "rw" else "en")
        return jsonify(error=message), 503
    try:
        language = "rw" if data.get("language") == "rw" else "en"
        return jsonify(answer=ai.follow_up(
            data.get("history", []), data.get("question", ""), language))
    except Exception as exc:
        return jsonify(error=str(exc)), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=os.getenv("DEBUG") == "1")
