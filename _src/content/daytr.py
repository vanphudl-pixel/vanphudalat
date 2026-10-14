"""Loader for the day-trip set in the 16 languages beyond vi/en: route maps (routenew 'rn', routecheckin 'rc'),
the day hub (dayhub) and hub reference prices (placeshub_price). One file per language: content/dt_<l>.py with
COMMON, RN, RC, RN_P, RC_P, SLUG, DAY, FREE, FREE_REL, MARKET, HP, NOTE. Tips use {total} (filled with the route's km)."""
import importlib
LANGS = ["ru", "zh", "ko", "ja", "th", "id", "ms", "de", "fr", "es", "he", "it", "nl", "km", "lo", "my"]
_FREE = ["lake", "square"]
_REL = ["cathedral", "pink", "thanhtam", "camly", "dusinh", "thanhmau", "linhson", "linhquang", "tau", "vanhanh", "linhan", "linhphuoc"]
def _m(l): return importlib.import_module(f"content.dt_{l}")
def route(key, total):
    out = {}
    for l in LANGS:
        m = _m(l); d = dict(m.COMMON); d.update(getattr(m, key.upper()))
        d["tips"] = [x.format(total=total) for x in d["tips"]]
        out[l] = d
    return out
def route_price(key): return {l: getattr(_m(l), key.upper() + "_P") for l in LANGS}
def day(): return {l: _m(l).SLUG for l in LANGS}, {l: _m(l).DAY for l in LANGS}
def hub_price():
    P, LAB, NOTE = {}, {}, {}
    for l in LANGS:
        m = _m(l); p = {k: m.FREE for k in _FREE}; p.update({k: m.FREE_REL for k in _REL}); p["market"] = m.MARKET; p.update(m.HP)
        P[l] = p; LAB[l] = m.COMMON["price_l"]; NOTE[l] = m.NOTE
    return P, LAB, NOTE
