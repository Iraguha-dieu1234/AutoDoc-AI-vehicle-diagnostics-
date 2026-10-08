"""Translations for the built-in rule-based diagnosis content."""
from copy import deepcopy

RW = {
    "Please describe the problem or enter an OBD-II code.":
        "Sobanura ikibazo cy'imodoka cyangwa wandike kode ya OBD-II.",
    "AI follow-up needs ANTHROPIC_API_KEY.":
        "Ikiganiro n'ubwenge buhangano gisaba gushyiramo ANTHROPIC_API_KEY.",
    "Difficult to start / cranks slowly": "Biragora kuyatsa / moteri izunguruka buhoro",
    "Won't crank, only clicks": "Ntiyatsa, humvikana gukanda gusa",
    "Engine stalls": "Moteri irazima",
    "Rough idle / shaking": "Moteri iranyeganyega idakora",
    "High fuel consumption": "Imodoka ikoresha lisansi cyangwa mazutu nyinshi",
    "Black smoke": "Umwotsi w'umukara",
    "White smoke": "Umwotsi w'umweru",
    "Blue smoke": "Umwotsi w'ubururu",
    "Loss of power": "Imodoka yagize intege nke",
    "Overheating": "Moteri irashyuha birenze",
    "Knocking / ticking noise": "Ijwi ryo gukomanga cyangwa gutiktika",
    "Squealing / weak brakes": "Feri ziravuza cyangwa ntizifata neza",
    "Vibration when braking": "Imodoka iranyeganyega iyo ufata feri",
    "Steering pulls / vibrates": "Imodoka ijya ku ruhande cyangwa volanti iranyeganyega",
    "Check engine light on": "Itara rya Check Engine ryaka",
    "Gear slipping / hard shifts": "Gare iranyerera cyangwa guhindura gare biragora",
    "Oil leak / low oil": "Amavuta ya moteri arava cyangwa ni make",
    "Battery light / dim lights": "Itara rya batiri ryaka cyangwa amatara acanye buhoro",
    "AC not cooling": "Kondisiyoneri ntikonjesha",
    "Burning / fuel smell": "Impumuro yo gushya cyangwa ya lisansi",
    "Worn spark plugs / ignition coil": "Buji zishaje cyangwa bobine yo gucana yangiritse",
    "Clogged air filter / dirty MAF sensor": "Akayunguruzo k'umwuka kazibye cyangwa sensor ya MAF yanduye",
    "Fuel injector or fuel pump problem": "Ikibazo cya injector cyangwa pompe ya lisansi",
    "Weak battery / alternator / starter": "Batiri, alternateur cyangwa starter bifite intege nke",
    "Turbo / EGR / DPF issue (diesel)": "Ikibazo cya turbo, EGR cyangwa DPF (moteri ya mazutu)",
    "Burning oil – worn rings / valve seals": "Moteri irimo gutwika amavuta – piston rings cyangwa valve seals bishaje",
    "Coolant leak / thermostat / head gasket": "Amazi akonjesha arava, thermostat cyangwa gasket ya moteri byangiritse",
    "Worn brake pads / warped rotors": "Plaquettes za feri zishaje cyangwa disiki za feri zigondamye",
    "Wheel balance / alignment / suspension wear": "Balance, alignment cyangwa ibice bya suspension byashaje",
    "Oxygen sensor / catalytic converter fault": "Ikibazo cya oxygen sensor cyangwa catalytic converter",
    "Vacuum leak / intake gasket / throttle body dirt": "Umwuka urinjira aho utagenewe, gasket ya intake cyangwa throttle body byanduye",
    "Automatic/manual gearbox wear or low fluid": "Gearbox ishaje cyangwa amavuta yayo ari make",
    "Timing belt/chain or valvetrain wear": "Timing belt/chain cyangwa ibice bya valvetrain byashaje",
    "AC refrigerant leak / compressor": "Gazi ya AC irava cyangwa compressor yangiritse",
    "Inspect spark plugs for wear, oil or carbon fouling":
        "Suzuma niba buji zishaje, zifite amavuta cyangwa imyanda y'umukara.",
    "Swap coils between cylinders to see if misfire follows":
        "Umukanishi ashobora guhinduranya bobine kugira ngo amenye niba ikibazo gikurikira bobine.",
    "Check ignition wiring": "Suzuma insinga za sisitemu yo gucana.",
    "Replace plugs at the manufacturer interval (iridium 80–100k km, copper 30–50k km).":
        "Hindura buji ukurikije amabwiriza y'uruganda rw'imodoka; intera iterwa n'ubwoko bwa buji na moteri.",
    "Inspect and replace the air filter": "Suzuma akayunguruzo k'umwuka, ugahindure niba kazibye.",
    "Clean MAF sensor with dedicated cleaner": "Sukura sensor ya MAF ukoresheje umuti wabugenewe.",
    "Look for intake hose cracks": "Shaka niba umuyoboro winjiza umwuka ufite çatika cyangwa uva.",
    "Replace the air filter every 15–30k km, sooner on dusty roads.":
        "Hindura akayunguruzo k'umwuka hakurikijwe igitabo cy'imodoka; imihanda irimo umukungugu ishobora gusaba kugasuzuma kenshi.",
    "Measure fuel pressure": "Pima igitutu cya lisansi.",
    "Test injector spray pattern / balance": "Suzuma uburyo injector zitera lisansi n'uko zingana.",
    "Replace fuel filter if due": "Hindura akayunguruzo ka lisansi niba igihe cyabyo kigeze.",
    "Use quality fuel; replace the fuel filter every 40–60k km.":
        "Koresha lisansi cyangwa mazutu yujuje ibisabwa n'uruganda; hindura akayunguruzo ukurikije igitabo cy'imodoka.",
    "Test battery voltage (12.4–12.7 V off, 13.8–14.5 V running)":
        "Pima umuriro wa batiri; umukanishi agereranye ibipimo n'ibisabwa na batiri n'imodoka.",
    "Clean battery terminals": "Sukura aho insinga zifatira kuri batiri.",
    "Load-test alternator and starter": "Suzuma alternateur na starter biri ku kazi.",
    "Batteries typically last 3–5 years; test annually after year 3.":
        "Igihe batiri imara kiratandukana; isuzumishe kenshi uko igenda ishaje.",
    "Inspect boost hoses and turbo for leaks": "Suzuma imiyoboro ya turbo niba idacitse cyangwa iva.",
    "Clean or test EGR valve": "Sukura cyangwa usuzume valve ya EGR.",
    "Check DPF soot level / force regeneration": "Suzuma DPF n'ingano y'umwanda; regeneration ikorwe n'umukanishi ufite ibikoresho.",
    "Occasional long highway runs help DPF regeneration; use correct low-ash oil.":
        "Imodoka ifite DPF ikeneye gukurikiza amabwiriza y'uruganda; ntihatirwe regeneration utabanje gusuzumwa n'umukanishi.",
    "Check oil level weekly": "Suzuma urugero rw'amavuta ya moteri buri gihe.",
    "Compression / leak-down test": "Pima compression ya moteri no kumenya niba hari aho umwuka ucikira.",
    "Inspect PCV valve": "Suzuma valve ya PCV.",
    "Use the oil grade specified; top up and monitor consumption.":
        "Koresha ubwoko n'ingano y'amavuta byateganyijwe n'uruganda; ongeraho ayabura kandi ukurikirane uko agabanuka.",
    "STOP driving if temperature is red": "Hagarika imodoka niba igipimo cy'ubushyuhe kiri mu mutuku.",
    "Check coolant level when cold": "Suzuma amazi akonjesha moteri imaze gukonja.",
    "Pressure-test cooling system; test for exhaust gas in coolant":
        "Umukanishi asuzume pressure ya cooling system n'uko nta myuka ya moteri ivanze n'amazi akonjesha.",
    "Change coolant every 4–5 years; never open the radiator cap hot.":
        "Hindura coolant hakurikijwe igitabo cy'imodoka; ntukingure radiator igihe moteri ishyushye.",
    "Measure pad thickness (replace under 3 mm)": "Pima ubunini bwa plaquettes; umukanishi yemeze niba zikeneye guhindurwa.",
    "Inspect rotors for grooves / runout": "Suzuma disiki za feri niba zifite imirongo cyangwa zigondamye.",
    "Check brake fluid level and colour": "Suzuma urugero n'ibara ry'amavuta ya feri.",
    "Replace pads before metal contact; brake fluid every 2 years.":
        "Hindura plaquettes mbere y'uko ibyuma bikoranaho; igihe cyo guhindura brake fluid kigenwa n'igitabo cy'imodoka.",
    "Check tyre pressures and wear pattern": "Suzuma umwuka uri mu mapine n'uko amapine ashaje.",
    "Wheel balance and 4-wheel alignment": "Suzuma balance n'uko amapine ahagaze (alignment).",
    "Inspect tie-rod ends, ball joints, bushings": "Suzuma tie-rod ends, ball joints na bushings.",
    "Rotate tyres every 8–10k km; align yearly.":
        "Hinduranya amapine kandi ukore alignment uko amabwiriza y'uruganda abivuga; imihanda itameze neza ishobora kwihutisha isuzuma.",
    "Read O2 sensor live data": "Soma amakuru ya oxygen sensor akoresheje icyuma gisuzuma imodoka.",
    "Check exhaust for leaks before the cat": "Suzuma niba umwuka utava mu muyoboro wa exhaust mbere ya catalytic converter.",
    "Inspect cat for rattle / overheating": "Suzuma catalytic converter niba ivuga urusaku cyangwa ishyuha birenze.",
    "Fix misfires early – they destroy catalytic converters.":
        "Kosora ikibazo cya misfire hakiri kare kugira ngo kitangiza catalytic converter.",
    "Listen for hissing; smoke-test intake": "Umva niba hari ijwi ryo gusohoka k'umwuka; umukanishi ashobora kugerageza intake akoresheje umwotsi.",
    "Clean throttle body": "Sukura throttle body ukoresheje uburyo buboneye.",
    "Inspect vacuum hoses": "Suzuma imiyoboro ya vacuum niba itacitse cyangwa idacometse neza.",
    "Clean throttle body every 50–60k km.":
        "Sukura throttle body gusa igihe isuzuma ribigaragaje cyangwa igihe uruganda rubiteganya.",
    "Check transmission fluid level and colour": "Suzuma urugero n'ibara ry'amavuta ya gearbox.",
    "Scan transmission module": "Soma amakuru ya mudule ya gearbox ukoresheje icyuma gisuzuma imodoka.",
    "Inspect clutch (manual) free play": "Suzuma uko clutch ya gearbox y'intoki ikora.",
    "Change transmission fluid every 60–100k km.":
        "Hindura amavuta ya gearbox ukurikije ubwoko bwa gearbox n'amabwiriza y'uruganda.",
    "Check belt replacement history": "Reba niba hari inyandiko y'igihe timing belt yahinduriwe.",
    "Inspect belt for cracks / chain for slack": "Suzuma timing belt niba itacitse n'uko chain itarekuye.",
    "Check cam/crank sensor correlation": "Suzuma uko camshaft na crankshaft sensors zihura.",
    "Replace timing belt at 90–100k km – failure can destroy the engine.":
        "Hindura timing belt ku ntera igenwa n'uruganda; kuyica bishobora kwangiza moteri cyane.",
    "Check compressor clutch engagement": "Suzuma niba compressor ya AC yinjira mu kazi neza.",
    "Leak test with UV dye": "Shaka aho gazi iva ukoresheje uburyo bwa UV.",
    "Replace cabin filter": "Hindura akayunguruzo k'umwuka winjira mu modoka.",
    "Service the AC every 2 years.": "Suzumisha AC hakurikijwe igitabo cy'imodoka n'uko ikora.",
    "Engine oil + filter": "Amavuta ya moteri n'akayunguruzo",
    "Air filter": "Akayunguruzo k'umwuka",
    "Fuel filter": "Akayunguruzo ka lisansi cyangwa mazutu",
    "Spark plugs": "Buji",
    "Transmission fluid": "Amavuta ya gearbox",
    "Timing belt": "Timing belt",
    "Coolant (or 4–5 yrs)": "Coolant (cyangwa igihe cyagenwe n'uruganda)",
    "Brake pads inspection": "Isuzuma rya plaquettes za feri",
    "Random/multiple cylinder misfire": "Misfire muri silindiri nyinshi cyangwa zitandukanye",
    "Cylinder 1 misfire": "Misfire muri silindiri ya 1",
    "Cylinder 2 misfire": "Misfire muri silindiri ya 2",
    "Cylinder 3 misfire": "Misfire muri silindiri ya 3",
    "Cylinder 4 misfire": "Misfire muri silindiri ya 4",
    "MAF sensor range/performance": "Imikorere cyangwa igipimo cya sensor ya MAF",
    "System too lean (bank 1)": "Uruvange rwa lisansi n'umwuka rurimo lisansi nke (banki ya 1)",
    "System too rich (bank 1)": "Uruvange rurimo lisansi nyinshi (banki ya 1)",
    "System too lean (bank 2)": "Uruvange rurimo lisansi nke (banki ya 2)",
    "Catalyst efficiency below threshold": "Catalytic converter ntikora neza nk'uko byitezwe",
    "Catalyst efficiency below threshold (bank 2)": "Catalytic converter ya banki ya 2 ntikora neza nk'uko byitezwe",
    "Coolant thermostat below regulating temp": "Thermostat ya coolant ntigeze ku bushyuhe buteganyijwe",
    "Crankshaft position sensor circuit": "Umurongo w'amashanyarazi wa crankshaft position sensor",
    "EGR flow insufficient": "Umwuka unyura muri EGR ntuhagije",
    "Fuel rail pressure too low": "Igitutu cya lisansi muri rail kiri hasi cyane",
    "Turbo underboost": "Turbo ntitanga igitutu gihagije",
    "Idle control system": "Sisitemu igenzura uko moteri ikora idafashwe na gaz",
    "System voltage low": "Umuriro wa sisitemu uri hasi",
    "Transmission control system fault": "Ikibazo muri sisitemu igenzura gearbox",
    "Crank/cam correlation": "Ihuzabikorwa rya crankshaft na camshaft",
    "Coolant temp sensor circuit": "Umurongo w'amashanyarazi wa sensor y'ubushyuhe bwa coolant",
    "Not in built-in list": "Iyi kode ntiri ku rutonde rwubatswe muri porogaramu",
}


def text(value: str, language: str = "en") -> str:
    """Translate a built-in English string when Kinyarwanda is requested."""
    return RW.get(value, value) if language == "rw" else value


def translate_rules(report: dict, language: str = "en") -> dict:
    """Return a translated copy of rule results without changing severity/code values."""
    if language != "rw":
        return report

    translations = deepcopy(RW)

    def translate(value):
        if isinstance(value, str):
            return translations.get(value, value)
        if isinstance(value, list):
            return [translate(item) for item in value]
        if isinstance(value, dict):
            return {key: translate(item) for key, item in value.items()}
        return value

    return translate(report)
