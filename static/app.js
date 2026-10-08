const $ = id => document.getElementById(id);
const esc = t => String(t ?? "").replace(/[&<>]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));

const TEXT = {
  en: {
    pageTitle: "AutoDoc – Vehicle Fault Diagnosis Assistant", language: "Language",
    subtitle: "AI vehicle diagnostics", question: "What's wrong with your car?",
    description: "Describe it the way you would to a mechanic. AutoDoc works out the likely causes, what to check, and how urgent it is.",
    descriptionPlaceholder: "e.g. It struggles to start in the morning, shakes at idle, and there's black smoke when I accelerate. Fuel use has doubled this month.",
    vehicleDetails: "Vehicle details", improvesAccuracy: "· improves accuracy",
    makeModel: "Make / model", year: "Year", mileage: "Mileage (km)", fuel: "Fuel",
    petrol: "Petrol", diesel: "Diesel", hybrid: "Hybrid", transmission: "Transmission",
    manual: "Manual", automatic: "Automatic", codesLabel: "OBD-II codes (optional)",
    diagnose: "✨ Diagnose my car", guidance: "Guidance only. Always confirm repairs with a qualified mechanic.",
    rwandaNote: "General vehicle guidance shown in Kinyarwanda or English; this is not a verified Rwanda repair-history or pricing database. Follow your vehicle's manual and consult a qualified mechanic in Rwanda.",
    dataNote: "Uses general OBD-II references and example service intervals; check your vehicle manufacturer's schedule.",
    examples: [
      "Car struggles to start and shakes at idle",
      "Black smoke and weak acceleration (diesel)",
      "Steering wheel vibrates when braking at speed",
      "Engine overheats in traffic, sweet smell"
    ],
    loading: "Analyzing…", analyzing: "AutoDoc is analysing symptoms, codes and vehicle history…",
    serverError: "Could not reach the server.", validationError: "Please describe the problem or enter an OBD-II code.",
    aiOnly: "Offline rule-based mode", aiSetup: "Add an ANTHROPIC_API_KEY for AI analysis.",
    urgent: "⚠ Safety:", urgentAdvice: "this may be urgent. Stop driving if the vehicle feels unsafe and see a mechanic promptly.",
    noMatch: "No strong match. Add more detail or codes, or visit a mechanic for a scan.",
    basedOn: "Based on:", matchLabel: "Match:", recommendedChecks: "Recommended checks",
    maintenanceAdvice: "Maintenance advice:", maintenanceCheck: "Maintenance check",
    every: "every", dueSoon: "⚠ due soon", kmLeft: "km left", obdCodes: "OBD-II codes",
    aiSummary: "AI diagnosis summary", safeToDrive: "Safe to drive?", consultMechanic: "Consult a mechanic",
    highUrgencyWarning: "this may be urgent. Avoid driving until a mechanic has checked the vehicle.",
    urgency: "urgency", likelihood: "Likelihood:", repairCheck: "DIY-friendly check",
    mechanicRecommended: "Mechanic recommended", disclaimerTitle: "Disclaimer:",
    disclaimer: "Guidance based on your inputs, not a certified diagnosis. A qualified mechanic must confirm the fault before any repair.",
    askFollowup: "💬 Ask AutoDoc a follow-up", followupPlaceholder: "Answer a question or ask anything",
    send: "Send", thinking: "Thinking…", followupFailed: "Sorry, that failed. Please try again.",
    notInList: "Not in built-in list", low: "Low", medium: "Medium", high: "High",
    saveHistory: "Save History", exportHistory: "Export CSV", savedHistory: "Saved history",
    noSavedHistory: "No saved history yet.", loadHistory: "Load", savedDiagnosis: "Vehicle diagnosis",
    saved: "Saved", descriptionRequired: "Please describe the car issue before saving.",
    exportEmpty: "There is no saved history to export.", exportSuccess: "History exported to CSV.",
    savedEntry: "Saved diagnosis", history: "History", diagnosis: "Diagnosis", diagnosisTime: "Diagnosis time"
  },
  rw: {
    pageTitle: "AutoDoc – Gufasha kumenya ikibazo cy'imodoka", language: "Ururimi",
    subtitle: "Gusuzuma imodoka hakoreshejwe ubwenge buhangano",
    question: "Imodoka yawe ifite ikihe kibazo?",
    description: "Sobanura ikibazo nk'uko wagisobanurira umukanishi. AutoDoc igaragaza ibishobora kuba byateye ikibazo, ibyo kugenzura n'uburemere bwacyo.",
    descriptionPlaceholder: "Urugero: Imodoka iragora kwaka mu gitondo, iranyeganyega idakora kandi isohora umwotsi w'umukara iyo nyihase. Ikoresha lisansi nyinshi muri iyi minsi.",
    vehicleDetails: "Amakuru y'imodoka", improvesAccuracy: "· afasha gusuzuma neza",
    makeModel: "Uruganda / ubwoko bw'imodoka", year: "Umwaka yakozwemo",
    mileage: "Ibirometero yakoze (km)", fuel: "Ubwoko bwa lisansi",
    petrol: "Lisansi", diesel: "Mazutu", hybrid: "Imodoka ikoresha amashanyarazi na lisansi",
    transmission: "Ubwoko bwa gearbox", manual: "Gearbox y'intoki", automatic: "Gearbox yikora",
    codesLabel: "Kode za OBD-II (si ngombwa)", diagnose: "✨ Suzuma ikibazo cy'imodoka",
    guidance: "Aya ni amakuru rusange gusa. Buri gihe saba umukanishi ubifitiye ubumenyi kwemeza ikibazo n'ibikenewe gusanwa.",
    rwandaNote: "Inama rusange zerekanwa mu Kinyarwanda cyangwa Icyongereza; iyi porogaramu ntirimo inyandiko zemejwe z'ibibazo by'imodoka zo mu Rwanda cyangwa ibiciro byo gusanwa. Kurikiza igitabo cy'imodoka yawe kandi ugishe inama umukanishi wujuje ibisabwa mu Rwanda.",
    dataNote: "Ikoresha amakuru rusange ya OBD-II n'ibihe by'ingenzi byo gusuzuma imodoka. Reba gahunda yihariye y'uruganda rw'imodoka yawe.",
    examples: [
      "Imodoka iragora kwaka kandi iranyeganyega idakora",
      "Umwotsi w'umukara n'imodoka idafite intege (mazutu)",
      "Volanti iranyeganyega iyo mfata feri imodoka yihuta",
      "Moteri irashyuha cyane mu muhanda kandi hari impumuro idasanzwe"
    ],
    loading: "Irimo gusuzuma…", analyzing: "AutoDoc irimo gusuzuma ibimenyetso, kode n'amakuru y'imodoka…",
    serverError: "Ntabwo ibasha kugera kuri seriveri.",
    validationError: "Sobanura ikibazo cy'imodoka cyangwa wandike kode ya OBD-II.",
    aiOnly: "Uburyo bukoresha amategeko bubasha gukora nta murandasi",
    aiSetup: "Shyiramo ANTHROPIC_API_KEY kugira ngo ukoreshe isuzuma rya AI.",
    urgent: "⚠ Icyitonderwa:",
    urgentAdvice: "iki kibazo gishobora kuba gikomeye. Hagarika gutwara niba imodoka itizewe, maze ushake umukanishi vuba.",
    noMatch: "Nta kibazo gihuye neza n'ibimenyetso. Sobanura byinshi, ongeraho kode, cyangwa usabe umukanishi gusuzuma imodoka.",
    basedOn: "Bishingiye kuri:", matchLabel: "Ijanisha rihuye n'ibimenyetso:",
    recommendedChecks: "Ibyo umukanishi agenzura", maintenanceAdvice: "Inama zo kwita ku modoka:",
    maintenanceCheck: "Isuzuma ry'ibikorwa byo kwita ku modoka", every: "buri",
    dueSoon: "⚠ igihe cyo kubikora kiri hafi", kmLeft: "km zisigaye",
    obdCodes: "Kode za OBD-II", aiSummary: "Incamake y'isuzuma rya AI",
    safeToDrive: "Ese kuyitwara ni umutekano?", consultMechanic: "Gisha inama umukanishi",
    highUrgencyWarning: "iki kibazo gishobora kuba gikomeye. Irinde gutwara kugeza umukanishi asuzumye imodoka.",
    urgency: "uburemere", likelihood: "Amahirwe yo kuba ari byo:",
    repairCheck: "Igenzura wakorera wenyine",
    mechanicRecommended: "Ni byiza ko umukanishi abigenzura", disclaimerTitle: "Icyitonderwa:",
    disclaimer: "Izi nama zishingiye ku makuru watanze kandi si isuzuma ryemejwe. Umukanishi ubifitiye ubumenyi agomba kwemeza ikibazo mbere yo gusana.",
    askFollowup: "💬 Baza AutoDoc ikindi kibazo", followupPlaceholder: "Subiza ikibazo cyangwa ubaze ikindi",
    send: "Ohereza", thinking: "Tekereza gato…", followupFailed: "Ntibyakunze. Ongera ugerageze.",
    notInList: "Iyi kode ntiri ku rutonde rwubatswe muri porogaramu",
    low: "Gito", medium: "Hagati", high: "Kinini",
    saveHistory: "Bika amateka", exportHistory: "Kohereza CSV", savedHistory: "Amateka yanditswe",
    noSavedHistory: "Nta mateka yanditswe aracyari.", loadHistory: "Gusubira", savedDiagnosis: "Isuzuma ry'imodoka",
    saved: "Yabitswe", descriptionRequired: "Andika ikibazo cy'imodoka mbere yo kubika.",
    exportEmpty: "Nta mateka yanditswe ahari yo kohereza.", exportSuccess: "Amateka yoherejwe muri CSV.",
    savedEntry: "Isuzuma ryabitswe", history: "Amateka", diagnosis: "Isuzuma", diagnosisTime: "Igihe cy'isuzuma"
  }
};

let language = localStorage.getItem("autodocLanguage") === "rw" ? "rw" : "en";
let history = [];
const STORAGE_KEY = "autodocHistory";
const tr = key => TEXT[language][key] || key;
const urgencyText = value => tr(({Low:"low",Medium:"medium",High:"high"})[value] || value);

function loadHistory() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    return Array.isArray(saved) ? saved : [];
  } catch (e) {
    return [];
  }
}

function saveHistory() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
  } catch (e) {
    // Ignore storage quota issues.
  }
}

function applyLanguage() {
  document.documentElement.lang = language;
  document.title = tr("pageTitle");
  const langEl = $("language");
  if (langEl) {
    langEl.value = language;
    langEl.setAttribute("aria-label", tr("language"));
  }
  document.querySelectorAll("[data-i18n]").forEach(e => { e.textContent = tr(e.dataset.i18n); });
  document.querySelectorAll("[data-i18n-placeholder]").forEach(e => {
    e.placeholder = tr(e.dataset.i18nPlaceholder);
  });
  $("goBtn").textContent = tr("diagnose");
  const saveBtn = $("saveHistoryBtn");
  if (saveBtn) saveBtn.textContent = tr("saveHistory");
  const exportBtn = $("exportHistoryBtn");
  if (exportBtn) exportBtn.textContent = tr("exportHistory");
  $("ex").replaceChildren();
  TEXT[language].examples.forEach(text => {
    const e = document.createElement("span");
    e.className = "chip";
    e.textContent = text;
    e.onclick = () => { $("desc").value = text; };
    $("ex").appendChild(e);
  });
  renderHistoryList();
}

function renderHistoryList() {
  const list = $("historyList");
  if (!list) return;
  const saved = loadHistory();
  if (!saved.length) {
    list.innerHTML = `<div class="card quiet"><small>${esc(tr("noSavedHistory"))}</small></div>`;
    return;
  }
  list.innerHTML = saved.map(item => `
    <div class="history-item">
      <div>
        <div class="history-label">${esc(item.title || tr("savedDiagnosis"))}</div>
        <div class="history-meta">${esc(new Date(item.date).toLocaleString())}</div>
      </div>
      <button class="alt small" data-history-id="${esc(item.id)}">${esc(tr("loadHistory"))}</button>
    </div>
  `).join("");
  list.querySelectorAll("[data-history-id]").forEach(button => {
    button.addEventListener("click", () => {
      const id = button.dataset.historyId;
      const entry = saved.find(item => String(item.id) === String(id));
      if (!entry) return;
      $("desc").value = entry.description || "";
      $("model").value = entry.model || "";
      $("year").value = entry.year || "";
      $("km").value = entry.km || "";
      $("fuel").value = entry.fuel || "Petrol";
      $("trans").value = entry.transmission || "Manual";
      $("codes").value = entry.codes || "";
      language = entry.language === "rw" ? "rw" : "en";
      localStorage.setItem("autodocLanguage", language);
      applyLanguage();
      $("desc").focus();
    });
  });
}

const langEl = $("language");
if (langEl) {
  langEl.addEventListener("change", () => {
    language = langEl.value === "rw" ? "rw" : "en";
    localStorage.setItem("autodocLanguage", language);
    applyLanguage();
  });
}
applyLanguage();
history = loadHistory();
renderHistoryList();

function saveCurrentDiagnosis(payload) {
  const entry = {
    id: Date.now() + Math.random(),
    title: payload.title || (language === "rw" ? "Isuzuma rya modoka" : "Vehicle diagnosis"),
    date: new Date().toISOString(),
    description: $("desc").value,
    model: $("model").value,
    year: $("year").value,
    km: $("km").value,
    fuel: $("fuel").value,
    transmission: $("trans").value,
    codes: $("codes").value,
    language
  };
  const saved = loadHistory();
  const next = [entry, ...saved.filter(item => item.description || item.date)].slice(0, 8);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
  history = next;
  renderHistoryList();
  return entry;
}

const saveHistoryBtn = $("saveHistoryBtn");
if (saveHistoryBtn) {
  saveHistoryBtn.addEventListener("click", () => {
    const description = $("desc").value.trim();
    if (!description) {
      alert(tr("descriptionRequired"));
      $("desc").focus();
      return;
    }
    saveCurrentDiagnosis({ title: tr("savedEntry") });
    saveHistoryBtn.textContent = tr("saved");
    setTimeout(() => {
      saveHistoryBtn.textContent = tr("saveHistory");
    }, 1200);
  });
}

const exportHistoryBtn = $("exportHistoryBtn");
if (exportHistoryBtn) {
  exportHistoryBtn.addEventListener("click", () => {
    const saved = loadHistory();
    if (!saved.length) {
      alert(tr("exportEmpty"));
      return;
    }
    const header = ["date", "language", "description", "model", "year", "km", "fuel", "transmission", "codes"];
    const rows = saved.map(item => [
      item.date || "",
      item.language || "en",
      (item.description || "").replace(/\r?\n/g, " "),
      item.model || "",
      item.year || "",
      item.km || "",
      item.fuel || "",
      item.transmission || "",
      item.codes || ""
    ]);
    const csv = [header, ...rows].map(row => row.map(v => `"${String(v).replace(/"/g, '""')}"`).join(",")).join("\n");
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "autodoc_history.csv";
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
    alert(tr("exportSuccess"));
  });
}

$("goBtn").onclick = async () => {
  const body = { description: $("desc").value, model: $("model").value, year: $("year").value,
    km: $("km").value, fuel: $("fuel").value, transmission: $("trans").value,
    codes: $("codes").value, language };
  const b = $("goBtn"), o = $("out");
  b.disabled = true; b.textContent = tr("loading");
  o.innerHTML = `<div class="card ai"><span class="spin"></span>${esc(tr("analyzing"))}</div>`;
  try {
    const r = await fetch("/api/diagnose", { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(body) });
    const d = await r.json();
    if (!r.ok) { o.innerHTML = `<div class="card warn">${esc(d.error || tr("validationError"))}</div>`; return; }
    if (d.mode === "ai") { history = d.history; renderAI(d.report); } else renderRules(d.rules);
    saveCurrentDiagnosis({ title: (language === "rw" ? "Isuzuma" : "Diagnosis") + " " + new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }) });
    o.scrollIntoView({ behavior: "smooth" });
  } catch (e) { o.innerHTML = `<div class="card warn">${esc(tr("serverError"))}</div>`; }
  finally { b.disabled = false; b.textContent = tr("diagnose"); }
};

const DISC = () => `<div class="card warn"><b>${esc(tr("disclaimerTitle"))}</b> ${esc(tr("disclaimer"))}</div>`;
const table = rows => `<div class="scroll"><table>${rows}</table></div>`;

function renderAI(r) {
  const u = ["High","Medium","Low"].includes(r.urgency) ? r.urgency : "Medium";
  let h = `<div class="card ai"><h2>${esc(tr("aiSummary"))}<span class="tag ${u}">${esc(urgencyText(u))} ${esc(tr("urgency"))}</span></h2>
    <p class="sum" style="margin:0 0 8px">${esc(r.summary)}</p><div><b>${esc(tr("safeToDrive"))}</b> ${esc(r.safe_to_drive || tr("consultMechanic"))}</div></div>`;
  if (u === "High") h += `<div class="card warn"><b>${esc(tr("urgent"))}</b> ${esc(tr("highUrgencyWarning"))}</div>`;
  (r.causes || []).forEach((c, i) => {
    const p = Math.max(0, Math.min(100, +c.likelihood || 0));
    h += `<div class="card"><h2>${i+1}. ${esc(c.name)}<span class="pill">${esc(c.diy ? tr("repairCheck") : tr("mechanicRecommended"))}</span></h2>
      <div class="mu">${esc(tr("likelihood"))} ${p}%</div><div class="bar"><i style="width:${p}%"></i></div>
      <p style="margin:0 0 6px">${esc(c.why)}</p><b>${esc(tr("recommendedChecks"))}</b><ul>${(c.checks||[]).map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>`;
  });
  if ((r.codes||[]).length) h += `<div class="card"><h2>${esc(tr("obdCodes"))}</h2>${table(r.codes.map(c => `<tr><td><b>${esc(c.code)}</b></td><td>${esc(c.meaning)}</td></tr>`).join(""))}</div>`;
  if ((r.maintenance||[]).length) h += `<div class="card"><h2>${esc(tr("maintenanceAdvice"))}</h2><ul>${r.maintenance.map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>`;
  h += `<div class="card ai"><h2>${esc(tr("askFollowup"))}</h2>
    ${(r.questions||[]).length ? '<div class="chips" style="margin-bottom:8px">' + r.questions.map(q => `<span class="chip" onclick="$('fq').value=this.textContent">${esc(q)}</span>`).join("") + "</div>" : ""}
    <div id="chat"></div><div class="row"><input id="fq" placeholder="${esc(tr("followupPlaceholder"))}"><button class="go" id="fb" onclick="follow()">${esc(tr("send"))}</button></div></div>${DISC()}`;
  $("out").innerHTML = h;
  $("fq").addEventListener("keydown", e => { if (e.key === "Enter") follow(); });
}

function renderRules(r) {
  let h = `<div class="card"><span class="pill">${esc(tr("aiOnly"))}</span> ${esc(tr("aiSetup"))}</div>`;
  if (r.safety_warning) h += `<div class="card warn"><b>${esc(tr("urgent"))}</b> ${esc(tr("urgentAdvice"))}</div>`;
  if (!r.causes.length) h += `<div class="card">${esc(tr("noMatch"))}</div>`;
  r.causes.forEach((c, i) => {
    h += `<div class="card"><h2>${i+1}. ${esc(c.name)}<span class="tag ${c.severity}">${esc(urgencyText(c.severity))} ${esc(tr("urgency"))}</span></h2>
      <div class="mu">${esc(tr("matchLabel"))} ${c.match_pct}%</div><div class="bar"><i style="width:${c.match_pct}%"></i></div>
      <small>${esc(tr("basedOn"))} ${esc(c.evidence.join(" · ") || "mileage")}</small>
      <br><b>${esc(tr("recommendedChecks"))}</b><ul>${c.checks.map(x => `<li>${esc(x)}</li>`).join("")}</ul><b>${esc(tr("maintenanceAdvice"))}</b> ${esc(c.advice)}</div>`;
  });
  if (r.codes.length) h += `<div class="card"><h2>${esc(tr("obdCodes"))}</h2>${table(r.codes.map(c => `<tr><td><b>${esc(c.code)}</b></td><td>${esc(c.meaning === "Not in built-in list" ? tr("notInList") : c.meaning)}</td></tr>`).join(""))}</div>`;
  if (r.maintenance.length) h += `<div class="card"><h2>${esc(tr("maintenanceCheck"))}</h2>${table(r.maintenance.map(m => `<tr><td>${esc(m.item)}</td><td>${esc(tr("every"))} ${m.interval_km.toLocaleString()} km</td><td>${m.due_soon ? esc(tr("dueSoon")) : `~${m.km_left.toLocaleString()} ${esc(tr("kmLeft"))}`}</td></tr>`).join(""))}</div>`;
  $("out").innerHTML = h + DISC();
}

async function follow() {
  const i = $("fq"), q = i.value.trim(); if (!q) return;
  const c = $("chat"); i.value = "";
  c.insertAdjacentHTML("beforeend", `<div class="bub me">${esc(q)}</div><div class="bub bot" id="pend"><span class="spin"></span>${esc(tr("thinking"))}</div>`);
  try {
    const r = await fetch("/api/chat", { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({ history, question: q, language }) });
    const d = await r.json();
    $("pend").textContent = d.answer || d.error;
    if (d.answer) history = [...history, { role: "user", content: q }, { role: "assistant", content: d.answer }];
  } catch (e) { $("pend").textContent = tr("followupFailed"); }
  $("pend").removeAttribute("id");
}
