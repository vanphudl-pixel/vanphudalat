"""Submit changed (or all) site URLs to IndexNow -> Bing, Yandex, Seznam, Naver..."""
import json, os, re, subprocess, sys, urllib.request
HOST = "vanphudalat.com"
KEY = "d2a209e24c9141768098a0a31253582c"
BASE = f"https://{HOST}/"

def all_urls():
    xml = open("sitemap.xml", encoding="utf-8").read()
    return re.findall(r"<loc>([^<]+)</loc>", xml)

def changed_urls(before):
    out = subprocess.run(["git", "diff", "--name-only", before, "HEAD"], capture_output=True, text=True).stdout.split()
    urls = []
    for f in out:
        if f.startswith(("_src/", ".github/")) or not f.endswith("index.html"):
            continue
        d = f[: -len("index.html")]
        urls.append(BASE + d)
    return urls

before = os.environ.get("BEFORE", "")
msg = os.environ.get("MSG", "")
if os.environ.get("ALL") == "true" or "[indexnow-all]" in msg or not before or set(before) == {"0"}:
    urls = all_urls()
else:
    urls = changed_urls(before)
sitemap = set(all_urls())
urls = [u for u in dict.fromkeys(urls) if u in sitemap]
print(f"{len(urls)} URLs")
if not urls:
    sys.exit(0)
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"{BASE}{KEY}.txt", "urlList": urls[:10000]}).encode()
for ep in ["https://api.indexnow.org/indexnow", "https://yandex.com/indexnow", "https://www.bing.com/indexnow"]:
    req = urllib.request.Request(ep, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(ep, r.status)
    except urllib.error.HTTPError as e:
        print(ep, e.code, e.read()[:200])
    except Exception as e:
        print(ep, "ERR", e)
for u in urls[:20]:
    print(" ", u)
