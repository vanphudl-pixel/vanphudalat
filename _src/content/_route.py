"""Helpers for self-drive route maps (ordered stops, start and end at the Van Phu shop)."""
import math
SHOP = (11.9510676, 108.4384077)
def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))
def legs(spots):
    pts = [SHOP] + [(s[1], s[2]) for s in spots] + [SHOP]
    return [km(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
def total(spots): return round(sum(legs(spots)))
