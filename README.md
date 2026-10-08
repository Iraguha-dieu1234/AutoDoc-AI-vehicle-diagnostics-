# AutoDoc – AI-Based Vehicle Fault Diagnosis & Maintenance Assistant

Describe a car problem in English or Kinyarwanda (plus optional model, mileage, fuel, OBD-II codes) and
get ranked likely faults, recommended checks, urgency, and maintenance advice. The interface and
built-in rule-based guidance can be switched between English and Kinyarwanda. **Guidance only – a
qualified mechanic must confirm every repair.**

The built-in fault and service references are general automotive guidance, not a verified database
of Rwanda-specific repair records, parts availability, or prices. Service intervals vary by vehicle;
check the owner's manual and consult a qualified mechanic in Rwanda.

## How it works
1. `diagnosis/engine.py` – rule engine. Extracts symptoms from free text (regex keywords), reads OBD-II
   codes, and scores faults using weights in `data/faults.json`, filtered by fuel type and mileage.
2. `diagnosis/ai.py` – optional LLM layer (Anthropic API). It receives the vehicle data, the owner's
   description and the rule engine's hints, and returns a structured JSON report plus follow-up chat.
3. `app.py` – Flask server with `/api/diagnose` and `/api/chat`. With no API key it runs fully offline.

## Run on Windows
Open PowerShell in the project folder, then create the virtual environment and install
the dependencies (only needed once):
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the app with `run_windows.bat` or run this in PowerShell:
```powershell
.\.venv\Scripts\python.exe app.py
```
Keep that terminal window open while presenting, wait for `Running on
http://127.0.0.1:5000`, then open that address in your browser. Activating the
virtual environment alone does not start the server.

The project works offline by default using its built-in rule-based diagnosis. No `.env`
file or API key is needed. To enable optional AI analysis and follow-up chat, copy
`.env.example` to `.env` and add an `ANTHROPIC_API_KEY`; those AI features require
internet access. On Windows, use `Copy-Item .env.example .env`, then edit `.env`.

Run the tests with:
```powershell
.\.venv\Scripts\python.exe -m pytest
```

### Run on macOS or Linux
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000` and keep the terminal running.

### Troubleshooting
- `ERR_CONNECTION_REFUSED`: the Flask server is not running. Start it with
  `run_windows.bat` and leave its terminal window open.
- `Address already in use`: another app is using port 5000. Stop that app, or in
  PowerShell run `$env:PORT=5001` before starting AutoDoc and open
  `http://127.0.0.1:5001`.
- If startup reports a missing package, run the dependency installation command above
  from the project folder.

## Knowledge base (`data/`)
| File | Content |
|---|---|
| `dtc_codes.csv` | OBD-II diagnostic trouble codes (SAE J2012 generic codes) |
| `service_intervals.csv` | Typical manufacturer service intervals in km |
| `faults.json` | 14 common faults: symptom weights, codes, mileage range, checks, advice |
| `symptoms.json` | Symptom labels and the keyword patterns used to read free text |

### Using a larger real dataset
Add rows to the files above, or build `faults.json` from public data such as NHTSA complaints
(https://www.nhtsa.gov/data), Kaggle car-maintenance/fault datasets, or your garage's repair records.
Keep the same JSON schema and the engine picks it up with no code changes.

## Project layout
```
app.py  requirements.txt  .env.example  README.md
diagnosis/{engine.py, ai.py}   data/   templates/index.html   static/{style.css, app.js}   tests/
```
