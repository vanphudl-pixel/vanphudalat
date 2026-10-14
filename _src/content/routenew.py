"""Self-drive day route 'New attractions 2026' (north–west–south loop): Langbiang Land, Mongo Land, Hoang Long Ohayo,
a strawberry farm. Same idea as the popular 1-day group tours, ridden by motorbike. Coordinates, cid and hours from
Google Maps (2026-10-15). Prices are not stated (paid at each gate). vi + en for now."""
from content import photomap as _PM
from content._route import total as _total

SPOTS = [
    ("lbland", 12.0195968, 108.4350209, "8552890741202824890",  True,  "7:00–20:00"),
    ("mongo",  11.9157314, 108.3392217, "5245936244841217186",  False, "7:00–17:30"),
    ("ohayo",  11.9082017, 108.4594297, "18005656562938649855", False, "7:30–17:30"),
    ("otome",  11.9182023, 108.4320300, "860639258293494253",   True,  "24h"),
]
ROUTE = True
CENTER = _PM.CENTER
SLUG = "route-new-attractions"
PDF = "VanPhu-Dalat-Route-New-Attractions"
GUIDES = {}
LANGS = ["vi", "en"]
NCENTER = 4
LEGW = 210
MAPH = 460
H1PT = 21
MAXKM = 13.0
RINGS = (2, 5, 10)
SIDE = {}
JITTER = {}
TOTAL = _total(SPOTS)
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]
T = {
"vi": {
 "title": "Đà Lạt 1 ngày tự túc: lộ trình các điểm mới 2026 bằng xe máy | Văn Phú",
 "h1": "Đà Lạt 1 ngày tự túc: lộ trình điểm mới 2026",
 "desc": "Tự chạy xe máy lộ trình các khu vui chơi mới ở Đà Lạt: Langbiang Land, Mongo Land, Hoàng Long Ohayo và vườn dâu — thứ tự đi, giờ gợi ý, khoảng cách, chỉ đường và PDF miễn phí.",
 "lead": "Lộ trình 1 ngày giống các tour \"điểm mới\", nhưng bạn tự chạy xe máy, tự chọn giờ và ở lại bao lâu tùy thích. 4 điểm theo thứ tự hợp lý: lên phía Bắc tới Langbiang Land, vòng sang Tà Nung, xuống đèo Mimosa và ghé vườn dâu trên đường về.",
 "center": "Thứ tự đi (1–4)",
 "season_h": "Lịch trình gợi ý",
 "season": [("7:30", "nhận xe tại tiệm hoặc khách sạn, chạy lên Langbiang Land"), ("10:00", "sang Mongo Land ở Tà Nung — đồi cỏ, máng trượt, thú"), ("12:30", "ăn trưa trên đường về trung tâm"), ("14:00", "Hoàng Long Ohayo trên đèo Mimosa"), ("16:00", "hái dâu ở vườn dâu, trả xe trước 21:00")],
 "tips_h": "Lưu ý",
 "tips": [f"Cả vòng khoảng {TOTAL} km đường chim bay, đường thực tế dài hơn và nhiều dốc (Tà Nung, đèo Mimosa) — nên đi Honda Air Blade 125cc; một pin xe máy điện (khoảng 35–40 km) không đủ.",
          "Vé vào cửa mua tại cổng từng điểm; nhiều nơi kèm một đồ uống (theo đánh giá của khách) — xem giá tại điểm.",
          "Đổ đầy xăng trước khi lên Tà Nung — trên đèo ít cây xăng.",
          "Đường Tà Nung và đèo Mimosa nhiều khúc cua — chạy chậm, không vượt ở khúc cua."],
 "leg": "từ điểm trước", "total": "Cả vòng (tiệm → các điểm → tiệm): khoảng {km} km đường chim bay",
 "s": {
  "lbland": ("Langbiang Land", "Buổi sáng", "Khu vui chơi gia đình gần chân Langbiang: máng trượt, xe go-kart, vườn thú nhỏ, công viên khủng long, hồ cá koi và khu hái dâu (theo đánh giá của khách)."),
  "mongo": ("Mongo Land", "Buổi sáng", "Khu vui chơi giữa đồi thông ở Tà Nung: máng trượt cầu vồng, trượt cỏ, thú như capybara, lạc đà; cách trung tâm khoảng nửa giờ chạy xe."),
  "ohayo": ("Hoàng Long Ohayo", "Buổi chiều", "Vườn phong cách Nhật trên đèo Mimosa: bonsai, hồ cá koi, nhiều góc chụp ảnh; vé kèm đồ uống (theo đánh giá của khách)."),
  "otome": ("Vườn dâu Otome Farm", "Chiều muộn", "Vườn dâu và atiso có mái che gần trung tâm — tự hái, trả tiền theo cân; trời mưa vẫn đi được."),
 }},
"en": {
 "title": "Da Lat Day Trip by Motorbike: New Attractions 2026 Route | Van Phu",
 "h1": "Da Lat Self-Guided Day Trip: New Attractions 2026",
 "desc": "Ride the Da Lat 'new attractions' day tour yourself: Langbiang Land, Mongo Land, Hoang Long Ohayo and a strawberry farm — stop order, suggested times, distances, directions and a free PDF.",
 "lead": "The same day out as the popular 'new attractions' group tours, but on your own motorbike — your timing, as long as you like at each stop. 4 stops in a sensible order: north to Langbiang Land, across to Ta Nung, down Mimosa Pass and a strawberry farm on the way back.",
 "center": "Stop order (1–4)",
 "season_h": "Suggested plan",
 "season": [("7:30", "pick up the bike at our shop or your hotel, ride to Langbiang Land"), ("10:00", "on to Mongo Land in Ta Nung — grass hills, slides, animals"), ("12:30", "lunch on the way back towards the centre"), ("14:00", "Hoang Long Ohayo on Mimosa Pass"), ("16:00", "pick strawberries at the farm, return the bike before 21:00")],
 "tips_h": "Good to know",
 "tips": [f"The loop is about {TOTAL} km in a straight line, longer by road and hilly (Ta Nung, Mimosa Pass) — take a Honda Air Blade 125cc; one electric-scooter battery (about 35–40 km) is not enough.",
          "Entrance tickets are sold at each gate; many include a drink (according to visitor reviews) — check prices on site.",
          "Fill up before Ta Nung — few petrol stations on the pass.",
          "The Ta Nung road and Mimosa Pass have many bends — ride slowly and never overtake on a bend."],
 "leg": "from the previous stop", "total": "Whole loop (shop → stops → shop): about {km} km in a straight line",
 "s": {
  "lbland": ("Langbiang Land", "Morning", "Family theme park near the foot of Lang Biang: slides, go-karts, a small zoo, a dinosaur park, a koi pond and strawberry picking (according to visitor reviews)."),
  "mongo": ("Mongo Land", "Morning", "Theme park among pine hills in Ta Nung: rainbow slide, grass sledding, animals such as capybaras and a camel; about half an hour's ride from the centre."),
  "ohayo": ("Hoang Long Ohayo", "Afternoon", "Japanese-style garden on Mimosa Pass: bonsai, koi ponds, many photo spots; the ticket includes a drink (according to visitor reviews)."),
  "otome": ("Otome Farm strawberries", "Late afternoon", "Covered strawberry and artichoke farm near the centre — pick your own, pay by weight; fine on a rainy day."),
 }},
}
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l
_Q = {"lbland": "Langbiang Land", "mongo": "Mongo Land Đà Lạt", "ohayo": "Hoàng Long Ohayo Đà Lạt", "otome": "Otome Farm Đà Lạt"}
def img_link(sid):
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
