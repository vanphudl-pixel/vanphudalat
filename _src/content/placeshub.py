"""'Places to visit in Da Lat by motorbike' hub (pillar page): every sightseeing spot from the theme maps, de-duplicated,
grouped by direction from Xuan Huong Lake, with straight-line km from the shop, hours, EV/gas, links to the theme map and
to our article when there is one. Spot texts come from the theme-map modules; only the 3 extra waterfalls are written here
(coordinates, cid and hours from Google Maps, 2026-10-15). Languages: vi + en first; add a language by adding it to T."""
import math
from content import photomap as PM, pagodamap as PG, churchmap as CH, cloudmap as CL

LANGS = ["vi", "en"]
SLUG = {"vi": "dia-diem-du-lich-da-lat", "en": "places-to-visit-in-da-lat"}
UPDATED = "2026-10-15"

# extra spots not on a theme map: id, lat, lng, cid, ev, hours
EXTRA = [
    ("prenn",   11.8772111, 108.4705572, "796795773573826149",  False, "6:30–17:00"),
    ("voi",     11.8230091, 108.3364973, "5705245422110093707", False, "—"),
    ("pongour", 11.6893042, 108.2656291, "9280240154432551472", False, "7:30–17:00"),
]
EXTRA_T = {
 "vi": {"prenn": ("Thác Prenn", "Buổi sáng", "Khu du lịch dưới chân đèo Prenn, có lối đi phía sau màn nước; cùng đường với thác Datanla."),
        "voi": ("Thác Voi (Nam Ban)", "Buổi sáng", "Thác rộng, nước mạnh cạnh chùa Linh Ẩn; đường xuống dốc, đá trơn. Khách đánh giá cho biết thác có lúc tạm đóng — hỏi trước khi đi."),
        "pongour": ("Thác Pongour", "Buổi sáng", "Thác rộng nhất quanh Đà Lạt, nước chảy qua nhiều bậc đá; đi theo quốc lộ khoảng 1–1,5 giờ mỗi chiều.")},
 "en": {"prenn": ("Prenn Waterfall", "Morning", "Park at the foot of Prenn Pass with a walkway behind the water; on the same road as Datanla."),
        "voi": ("Elephant Falls (Nam Ban)", "Morning", "Wide, powerful falls next to Linh An Pagoda; steep path and wet rocks. Recent reviews say the falls are sometimes closed — ask before you go."),
        "pongour": ("Pongour Waterfall", "Morning", "The widest falls around Da Lat, water over many rock terraces; about 1–1.5 hours each way on the highway.")},
}
GUIDE = {"pink": "domainedemarie", "caudat": "caudat", "caudatsky": "caudat", "datanla": "waterfalls", "prenn": "waterfalls", "voi": "waterfalls", "pongour": "waterfalls"}

def _km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))

def _zone(lat, lng):
    c = PM.CENTER
    if _km(c, (lat, lng)) < 2.6: return "center"
    dx = (lng - c[1]) * math.cos(math.radians(c[0])); dy = lat - c[0]
    b = (math.degrees(math.atan2(dx, dy)) + 360) % 360
    if b >= 315 or b < 45: return "north"
    if b < 135: return "east"
    if b < 235: return "south"
    return "west"

def spots(l):
    """[(sid, lat, lng, cid, ev, hours, (name, best, desc), zone, module or None)] — de-duplicated by position"""
    out = []
    for M in (PM, PG, CH, CL):
        for sid, lat, lng, cid, ev, h in M.SPOTS:
            if any(_km((o[1], o[2]), (lat, lng)) < 0.12 for o in out): continue
            out.append((sid, lat, lng, cid, ev, h, M.T[l]["s"][sid], _zone(lat, lng), M))
    for sid, lat, lng, cid, ev, h in EXTRA:
        out.append((sid, lat, lng, cid, ev, h, EXTRA_T[l][sid], _zone(lat, lng), None))
    return out

ZONES = ["center", "north", "east", "south", "west"]
T = {
"vi": {
 "title": "Địa điểm du lịch Đà Lạt 2026: {n} điểm đi bằng xe máy, chia theo hướng | Văn Phú",
 "h1": "Địa điểm du lịch Đà Lạt 2026: {n} điểm đi bằng xe máy",
 "desc": "{n} địa điểm du lịch Đà Lạt chia theo 5 hướng: khoảng cách từ tiệm, giờ mở cửa, giờ đẹp, đi xe máy điện được không, chỉ đường và 14 bản đồ PDF miễn phí.",
 "lead": "Tất cả điểm tham quan trên các bản đồ của chúng tôi, gom vào một trang và chia theo hướng từ hồ Xuân Hương — để bạn tự chạy xe máy, đi gọn từng cụm trong một buổi. Mỗi điểm có khoảng cách từ tiệm, giờ mở cửa, giờ đẹp và nút chỉ đường.",
 "updated": "Cập nhật", "toc": "Mục lục", "places_h": "Danh sách theo hướng",
 "km": "km từ tiệm (đường chim bay)", "hours": "Giờ mở cửa", "best": "Đẹp nhất", "dir": "Chỉ đường", "themap": "Bản đồ", "guide": "Bài hướng dẫn",
 "ev": "Đi xe máy điện được", "gas": "Nên đi Honda Air Blade 125cc (đường dốc / xa)",
 "map_h": "Bản đồ tất cả các điểm",
 "zones": {
  "center": ("Trung tâm Đà Lạt có gì chơi?", "Các điểm trong bán kính khoảng 2,5 km quanh hồ Xuân Hương — đi bộ kết hợp xe máy điện là thoải mái."),
  "north": ("Phía Bắc Đà Lạt có gì?", "Hướng Thung lũng Tình Yêu, các đồi săn mây và núi Langbiang (Lạc Dương)."),
  "east": ("Phía Đông Đà Lạt có gì?", "Hướng Trại Mát, chùa Linh Phước, đồi Hòn Bồ và đồi chè Cầu Đất."),
  "south": ("Phía Nam Đà Lạt có gì?", "Hướng đèo Prenn: thác Datanla, hồ Tuyền Lâm, Thiền viện Trúc Lâm và các thác lớn xa hơn."),
  "west": ("Phía Tây Đà Lạt có gì?", "Hướng làng hoa Vạn Thành, nhà thờ Du Sinh và đường Tà Nung."),
 },
 "themes_h": "Bản đồ chủ đề (có PDF in được)",
 "faq_h": "Hỏi nhanh",
 "faq": [
  ("Đi Đà Lạt 1 ngày bằng xe máy nên đi những đâu?",
   "Buổi sáng dạo hồ Xuân Hương, chợ Đà Lạt và Crazy House ở trung tâm; buổi chiều xuống phía Nam: thác Datanla, hồ Tuyền Lâm và Thiền viện Trúc Lâm (khoảng 5–7 km). Có 2–3 ngày thì thêm bình minh ở đồi chè Cầu Đất và núi Langbiang.", [("day", "Đà Lạt 1 ngày tự túc"), ("routes", "5 cung đường xe máy"), ("art:days3", "Lịch trình 3 ngày")]),
  ("Đi xe máy điện được những điểm nào?",
   "{ev_n} trong {n} điểm (chấm xanh) đi xe máy điện thoải mái — chủ yếu ở trung tâm và các điểm gần. Một pin đi khoảng 25–30 km (mỗi xe có 2 pin, tổng khoảng 50–60 km), đổi pin tại tiệm 20.000 VND. Các điểm xa hoặc dốc nên đi Honda Air Blade 125cc: {gas_names}.", [("ev", "Thuê xe máy điện Đà Lạt")]),
  ("Trời mưa ở Đà Lạt nên đi đâu?",
   "Mùa mưa (khoảng tháng 5–11) mưa thường vào buổi chiều: đi điểm xa buổi sáng, chiều chọn điểm gần trung tâm có mái che như Dinh Bảo Đại, ga Đà Lạt, chùa Linh Phước hoặc ngồi quán cà phê view. Tránh thác và đường đèo khi mưa lớn.", [("map:cafemap", "Bản đồ cà phê view"), ("art:weather", "Thời tiết Đà Lạt theo tháng")]),
  ("Mùa nào đi Đà Lạt đẹp nhất?",
   "Mùa khô (tháng 12–4) trời nắng ráo, đường khô, hợp chạy xe đi xa. Theo mùa hoa: dã quỳ cuối tháng 10–12, cỏ hồng tháng 11–12, mai anh đào cuối tháng 1–2. Festival Hoa Đà Lạt lần thứ 11 dự kiến 19–31/12/2026.", [("map:sunflowermap", "Bản đồ hoa dã quỳ"), ("map:festivalmap", "Festival Hoa Đà Lạt 2026")]),
  ("Các điểm cách tiệm Văn Phú bao xa?",
   "Khoảng cách ghi trên trang là đường chim bay từ tiệm (1/15/5 Thông Thiên Học); đường thực tế dài hơn, nhất là đường đèo. Các điểm trung tâm đều trong khoảng {center_max} km; xa nhất là {far_name} (≈ {far_km} km đường chim bay).", []),
  ("Có bản đồ Đà Lạt in được không?",
   "Có — mỗi bản đồ chủ đề bên dưới đều có file PDF 2 trang miễn phí: bản đồ, danh sách điểm, giờ mở cửa và mã QR chỉ đường.", [("map:photomap", "Bản đồ điểm check-in")]),
 ],
 "cta_h": "Thuê xe máy đi các điểm này",
 "cta": "150.000 VND/ngày cho mọi xe · không cọc tiền mặt (giữ hộ chiếu hoặc CCCD) · giao xe tận khách sạn trung tâm khi thuê từ 2 ngày · tiệm mở cửa 4:30 sáng.",
},
"en": {
 "title": "Places to Visit in Da Lat 2026: {n} Spots by Motorbike, by Direction | Van Phu",
 "h1": "Places to Visit in Da Lat 2026: {n} Spots by Motorbike",
 "desc": "{n} places to visit in Da Lat in 5 directions: distance from our shop, opening hours, best time, whether an electric scooter is fine, directions and 14 free PDF maps.",
 "lead": "Every sight from our maps on one page, grouped by direction from Xuan Huong Lake — so you can ride yourself and see one cluster per half day. Each place has the distance from our shop, opening hours, the best time and one-tap directions.",
 "updated": "Updated", "toc": "Contents", "places_h": "Places by direction",
 "km": "km from our shop (straight line)", "hours": "Hours", "best": "Best time", "dir": "Directions", "themap": "Map", "guide": "Guide",
 "ev": "Fine on an electric scooter", "gas": "Better on a Honda Air Blade 125cc (hills / far)",
 "map_h": "Map of all places",
 "zones": {
  "center": ("What is there to do in central Da Lat?", "Places within about 2.5 km of Xuan Huong Lake — easy on foot and by electric scooter."),
  "north": ("What is north of Da Lat?", "Towards the Valley of Love, the cloud-hunting hills and Lang Biang Mountain (Lac Duong)."),
  "east": ("What is east of Da Lat?", "Towards Trai Mat, Linh Phuoc Pagoda, Hon Bo hill and the Cau Dat tea hills."),
  "south": ("What is south of Da Lat?", "Towards Prenn Pass: Datanla Waterfall, Tuyen Lam Lake, Truc Lam Monastery and the bigger falls further out."),
  "west": ("What is west of Da Lat?", "Towards Van Thanh flower village, Du Sinh Church and the Ta Nung road."),
 },
 "themes_h": "Theme maps (with printable PDFs)",
 "faq_h": "Quick answers",
 "faq": [
  ("What should I see in Da Lat in one day by motorbike?",
   "In the morning, Xuan Huong Lake, Da Lat Market and Crazy House in the centre; in the afternoon ride south to Datanla Waterfall, Tuyen Lam Lake and Truc Lam Monastery (about 5–7 km). With 2–3 days, add sunrise at the Cau Dat tea hills and Lang Biang Mountain.", [("day", "Day trip on your own"), ("routes", "5 motorbike routes"), ("art:days3", "3-day itinerary")]),
  ("Which places can I reach on an electric scooter?",
   "{ev_n} of the {n} places (green dots) are fine on an electric scooter — mostly in the centre and nearby. One battery lasts about 25–30 km (each bike comes with 2 batteries, about 50–60 km in total), and a battery swap at our shop costs 20,000 VND. For far or steep places take a Honda Air Blade 125cc: {gas_names}.", [("ev", "Electric scooter rental in Da Lat")]),
  ("Where should I go in Da Lat when it rains?",
   "In the rainy season (roughly May–November) rain usually comes in the afternoon: ride to far places in the morning, then pick covered places near the centre such as the Bao Dai Summer Palace, the railway station, Linh Phuoc Pagoda or a café with a view. Avoid waterfalls and passes in heavy rain.", [("map:cafemap", "View café map"), ("art:weather", "Da Lat weather by month")]),
  ("When is the best time to visit Da Lat?",
   "The dry season (December–April) brings sunny days and dry roads, good for long rides. For flowers: wild sunflowers late October–December, pink grass November–December, cherry blossoms late January–February. The 11th Da Lat Flower Festival is planned for 19–31 December 2026.", [("map:sunflowermap", "Wild sunflower map"), ("map:festivalmap", "Da Lat Flower Festival 2026")]),
  ("How far are the places from the Van Phu shop?",
   "Distances on this page are straight-line from our shop (1/15/5 Thong Thien Hoc); the road is longer, especially over passes. All central places are within about {center_max} km; the farthest is {far_name} (≈ {far_km} km in a straight line).", []),
  ("Is there a printable map of Da Lat?",
   "Yes — every theme map below has a free 2-page PDF: the map, the list of places, opening hours and QR codes for directions.", [("map:photomap", "Photo spot map")]),
 ],
 "cta_h": "Rent a motorbike for these places",
 "cta": "150,000 VND per day for every bike · no cash deposit (we hold your passport or ID card) · free delivery to central hotels for 2+ days · shop opens at 4:30 am.",
},
}

# other languages
from content import placeshub_tr1 as _t1, placeshub_tr2 as _t2
for _m in (_t1, _t2):
    SLUG.update(_m.SLUG); EXTRA_T.update(_m.EXTRA); T.update(_m.T)
LANGS = ["en", "ru", "zh", "ko", "ja", "th", "id", "ms", "vi", "de", "fr", "es", "he", "it", "nl", "km", "lo", "my"]
for _l in LANGS:
    assert set(T[_l]) == set(T["en"]), _l
    assert set(T[_l]["zones"]) == set(ZONES) and len(T[_l]["faq"]) == len(T["en"]["faq"]), _l
