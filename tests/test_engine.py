import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from diagnosis import engine


def test_symptom_extraction():
    s = engine.extract_symptoms("Hard to start, black smoke and weak acceleration")
    assert {"start", "black", "power"} <= set(s)


def test_kinyarwanda_symptom_extraction():
    s = engine.extract_symptoms(
        "Imodoka iragora kwaka, iranyeganyega kandi isohora umwotsi w'umukara")
    assert {"start", "rough", "black"} <= set(s)
    assert "vib" not in s


def test_code_extraction():
    assert engine.extract_codes("scanner shows p0300 and P0171") == ["P0300", "P0171"]


def test_misfire_ranks_ignition_first():
    r = engine.diagnose("rough idle and shaking", km=120000, codes_text="P0301")
    assert "spark plugs" in r["causes"][0]["name"].lower()


def test_diesel_only_fault_hidden_for_petrol():
    r = engine.diagnose("black smoke and loss of power", km=150000, fuel="Petrol")
    assert all("diesel" not in c["name"].lower() for c in r["causes"])


def test_safety_warning_on_overheating():
    assert engine.diagnose("engine overheating")["safety_warning"]


def test_maintenance_schedule():
    m = engine.maintenance_status(7500)
    assert m[0]["item"].startswith("Engine oil") and m[0]["due_soon"]


def test_maintenance_is_due_at_exact_interval():
    oil = engine.maintenance_status(8000)[0]
    assert oil["km_left"] == 0
    assert oil["due_soon"]


def test_codes_from_description_and_codes_field_are_combined_once():
    result = engine.diagnose(
        "P0300 appeared after scanning; engine is rough",
        codes_text="P0301, P0300",
    )
    assert [code["code"] for code in result["codes"]] == ["P0301", "P0300"]
