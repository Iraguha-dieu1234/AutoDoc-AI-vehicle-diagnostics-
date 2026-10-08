from pathlib import Path
import sys
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from diagnosis import ai, engine, localization
import app as webapp


def test_rule_results_are_translated_without_changing_codes_or_severity():
    english = engine.diagnose("rough idle and shaking", km=120000, codes_text="P0301")
    kinyarwanda = localization.translate_rules(english, "rw")

    assert english["causes"][0]["name"] == "Worn spark plugs / ignition coil"
    assert kinyarwanda["causes"][0]["name"] == "Buji zishaje cyangwa bobine yo gucana yangiritse"
    assert kinyarwanda["causes"][0]["severity"] == english["causes"][0]["severity"]
    assert kinyarwanda["codes"][0]["code"] == "P0301"
    assert kinyarwanda["codes"][0]["meaning"] == "Misfire muri silindiri ya 1"


def test_unknown_language_defaults_to_english():
    message = "Please describe the problem or enter an OBD-II code."
    assert localization.text(message, "fr") == message


def test_kinyarwanda_diagnosis_advice_is_translated():
    result = engine.diagnose("moteri irashyuha", km=90000)
    localized = localization.translate_rules(result, "rw")

    assert localized["safety_warning"]
    assert localized["causes"]
    assert localized["causes"][0]["checks"][0] == "Hagarika imodoka niba igipimo cy'ubushyuhe kiri mu mutuku."


def test_diagnosis_api_returns_kinyarwanda_rule_results(monkeypatch):
    monkeypatch.setattr(webapp.ai, "available", lambda: False)
    response = webapp.app.test_client().post("/api/diagnose", json={
        "description": "moteri irashyuha",
        "language": "rw",
    })

    assert response.status_code == 200
    assert response.json["rules"]["causes"][0]["name"].startswith("Amazi akonjesha")


def test_diagnosis_api_localizes_validation_error(monkeypatch):
    monkeypatch.setattr(webapp.ai, "available", lambda: False)
    response = webapp.app.test_client().post("/api/diagnose", json={"language": "rw"})

    assert response.status_code == 400
    assert response.json["error"].startswith("Sobanura ikibazo")


def test_ai_prompt_requests_selected_language():
    prompt = ai.build_prompt({"language": "rw"}, {"causes": [], "codes": []})
    assert "RESPONSE LANGUAGE: Kinyarwanda." in prompt


def test_ai_follow_up_uses_conversational_system_prompt(monkeypatch):
    calls = {}

    class Messages:
        def create(self, **kwargs):
            calls.update(kwargs)
            return SimpleNamespace(content=[SimpleNamespace(text="Have a mechanic inspect it.")])

    monkeypatch.setattr(ai, "_client", lambda: SimpleNamespace(messages=Messages()))
    assert ai.follow_up([], "Can I keep driving?") == "Have a mechanic inspect it."
    assert "ONLY a JSON object" not in calls["system"]
    assert "concise plain text" in calls["system"]
