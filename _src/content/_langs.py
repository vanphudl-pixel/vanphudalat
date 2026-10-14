"""Languages added after the original 13. A language is listed in NEW only once all its files exist:
content/<l>.py (C, EV_, ART_), content/<l>_maps.py (MAPS: one entry per map module, spot texts keyed by spot id)."""
import importlib
NEW = ["it"]
META = {  # label in the language bar, og:locale, rental landing slug
    "it": ("IT", "it_IT", "noleggio-scooter-dalat"),
    "nl": ("NL", "nl_NL", "scooter-huren-dalat"),
    "km": ("ខ្មែរ", "km_KH", "dalat-motorbike-rental"),
    "lo": ("ລາວ", "lo_LA", "dalat-motorbike-rental"),
    "my": ("မြန်မာ", "my_MM", "dalat-motorbike-rental"),
}
def maps(l, mod):
    e = importlib.import_module(f"content.{l}_maps").MAPS[mod]
    return {k: (dict(v) if isinstance(v, dict) else v) for k, v in e.items()}
def inject(T, modname):
    m = modname.split(".")[-1]
    for l in NEW:
        T[l] = maps(l, m)
