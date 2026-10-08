"""Rule-based diagnostic engine driven by the CSV/JSON knowledge base in /data."""
import csv
import json
import re
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def _load():
    faults = json.loads((DATA / "faults.json").read_text(encoding="utf-8"))
    sym = json.loads((DATA / "symptoms.json").read_text(encoding="utf-8"))
    with open(DATA / "dtc_codes.csv", encoding="utf-8") as f:
        dtc = {r["code"]: r["meaning"] for r in csv.DictReader(f)}
    with open(DATA / "service_intervals.csv", encoding="utf-8") as f:
        service = [(r["item"], int(r["interval_km"])) for r in csv.DictReader(f)]
    patterns = {k: re.compile(v) for k, v in sym["keywords"].items()}
    return faults, sym["labels"], patterns, dtc, service


FAULTS, LABELS, PATTERNS, DTC, SERVICE = _load()
CODE_RE = re.compile(r"[PBCU][0-9A-F]{4}")


def extract_symptoms(text: str) -> list[str]:
    """Turn a free-text description into symptom keys."""
    t = (text or "").lower()
    return [k for k, p in PATTERNS.items() if p.search(t)]


def extract_codes(text: str) -> list[str]:
    return CODE_RE.findall((text or "").upper())


def rank_faults(symptoms, codes, km=0, fuel="Petrol", top=4):
    results = []
    for f in FAULTS:
        if f["fuel"] and f["fuel"].lower() != (fuel or "").lower():
            continue
        total = sum(f["symptoms"].values())
        matched = [s for s in symptoms if s in f["symptoms"]]
        hit_codes = [c for c in codes if c in f["codes"]]
        score = sum(f["symptoms"][s] for s in matched) + 4 * len(hit_codes)
        if score == 0:
            continue
        if km:
            score *= 0.7 if km < f["km_min"] else 1
            score += 0.5 if km >= f["km_min"] else 0
        pct = min(100, round(score / max(total * 0.7, 1) * 100))
        results.append({
            "name": f["name"], "severity": f["severity"], "match_pct": pct,
            "score": round(score, 2),
            "evidence": [LABELS[s] for s in matched]
                        + [f"{c} {DTC.get(c, '')}".strip() for c in hit_codes],
            "checks": f["checks"], "advice": f["advice"],
        })
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top]


def maintenance_status(km: int):
    out = []
    for item, interval in SERVICE:
        remainder = km % interval
        left = 0 if km and remainder == 0 else interval - remainder
        out.append({"item": item, "interval_km": interval, "km_left": left,
                    "due_soon": left < interval * 0.15})
    return out


def diagnose(description="", km=0, fuel="Petrol", codes_text=""):
    symptoms = extract_symptoms(description)
    codes = list(dict.fromkeys(extract_codes(codes_text) + extract_codes(description)))
    causes = rank_faults(symptoms, codes, km, fuel)
    urgent = any(s in symptoms for s in ("overheat", "brake", "white", "smell"))
    return {
        "symptoms": [LABELS[s] for s in symptoms],
        "codes": [{"code": c, "meaning": DTC.get(c, "Not in built-in list")} for c in codes],
        "causes": causes,
        "safety_warning": urgent or any(c["severity"] == "High" for c in causes[:1]),
        "maintenance": maintenance_status(km) if km else [],
    }
