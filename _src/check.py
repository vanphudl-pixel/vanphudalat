"""Quality gate. Run AFTER build_site.py. Exit code 1 on any problem.
Checks: every language has every article, no forbidden claims, every internal link
and image on every page resolves to a real file, sitemap is valid."""
import importlib, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
LANGS = ["en", "ru", "zh", "ko", "ja", "th", "id", "ms", "vi", "de", "fr", "es", "he"]
BASE = "https://vanphudalat.com/"
problems = []

C = {l: importlib.import_module(f"content.{l}").C for l in LANGS}
_EV = importlib.import_module("content.ev").EV
_XA = importlib.import_module("content.extra_a").ART
_XB = importlib.import_module("content.extra_b").ART
ref = C["en"]
for l in LANGS:
    c = C[l]
    for sec in ["ui", "home", "routes", "blog"]:
        miss = set(ref[sec]) - set(c[sec])
        if miss:
            problems.append(f"{l}: section {sec} missing keys {miss}")
    if list(c["articles"]) != list(ref["articles"]):
        problems.append(f"{l}: article keys/order differ from en")
    slugs = [a[0] for a in c["articles"].values()]
    if len(slugs) != len(set(slugs)):
        problems.append(f"{l}: duplicate article slugs")
    for k, a in c["articles"].items():
        if len(a) != 7:
            problems.append(f"{l}/{k}: article tuple must have 7 fields")
        elif not (HERE.parent / "img" / f"{a[5]}.jpg").exists():
            problems.append(f"{l}/{k}: image img/{a[5]}.jpg does not exist")
    # Business rules: never mention driving licences, never state electric-scooter range in km
    # covers the language file, the electric-scooter page (ev.py) and the extra rental articles (extra_a/extra_b)
    txt = repr(c) + repr(_EV.get(l)) + repr(_XA.get(l)) + repr(_XB.get(l))
    for pat in [r"licen", r"(?<!с)права", r"驾照", r"면허", r"免許", r"ใบขับขี่", r"\bSIM\b", r"\blesen\b", r"bằng lái", r"Führerschein", r"\bpermis\b", r"licencia", r"carnet de conducir", r"carné", r"רישיון",
                r"\d+\s?(km|公里|км|กม|킬로)\s*(per charge|на заряд|充电|충전|充電|ต่อการชาร์จ|mỗi lần sạc)",
                r"(per charge|par charge|por carga|pro (Akku)?ladung|mỗi lần sạc|на (одном |полном )?заряде|充满电约|満充電で約|완충 시 약|1회 충전 약|ชาร์จเต็มวิ่ง|sekali isi|setiap cas|בטעינה|לטעינה)",
                r"120\s?(kg|кг|公斤|กก|ק\"ג)",
                r"\d[\d.,\u00a0\u202f ]*\d\s?(đ\b|₫|донг|ดอง|דונג|越南盾|ドン)", r"120[.,\u00a0\u202f ]?000\s?VND|\b120k\b"]:
        if re.search(pat, txt, re.I):
            problems.append(f"{l}: forbidden wording /{pat}/")

# every page: internal links and images must exist
pages = list(ROOT.rglob("index.html"))
pages = [p for p in pages if "_src" not in p.parts]
for p in pages:
    html = p.read_text(encoding="utf-8")
    page_url = BASE + str(p.parent.relative_to(ROOT)).replace("\\", "/").strip(".") + "/"
    page_url = page_url.replace("//", "/").replace("https:/", "https://")
    for ref_ in re.findall(r'(?:href|src)="([^"]+)"', html):
        if ref_.startswith(("http", "mailto:", "tel:", "data:", "#", "weixin:")):
            continue
        target = urlparse(urljoin(page_url, ref_)).path.lstrip("/")
        f = ROOT / target
        if target.endswith("/") or target == "":
            f = f / "index.html"
        if not f.exists():
            problems.append(f"broken link on {p.relative_to(ROOT)} -> {ref_}")

try:
    r = ET.parse(ROOT / "sitemap.xml").getroot()
    locs = [e.text for e in r.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    for u in locs:
        if not (ROOT / u.replace(BASE, "") / "index.html").exists():
            problems.append(f"sitemap url has no page: {u}")
except Exception as e:
    problems.append(f"sitemap invalid: {e}")

print(f"pages: {len(pages)}, sitemap urls: {len(locs) if 'locs' in dir() else '?'}")
if problems:
    print("PROBLEMS:")
    print("\n".join(problems[:50]))
    sys.exit(1)
print("ALL CHECKS PASSED")
