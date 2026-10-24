"""Nha Trang – Da Lat bus map — website page (/nha-trang-da-lat-bus-map/) and printable PDF.
Where buses and limousines from Nha Trang arrive / leave in Da Lat. Companies kept only when two or more booking sites /
guides (redBus, 12Go, mia.vn) list them on the route and the Da Lat office matches a Google Maps listing (2026-10-24).
New listings carry a Google Maps place_id (ChIJ…) instead of a numeric cid. No fares or timetables: they change often."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid or place_id, ok on electric scooter, hours ("—" = not listed on Google Maps)
SPOTS = [
    ("benxe",   11.9269457, 108.4457730, "2479135965201090611",          True, "24h"),
    ("futa",    11.9409987, 108.4314483, "ChIJpZaXsS0TcTERO4MKfFKisJs",  True, "—"),
    ("sinh",    11.9442863, 108.4401768, "ChIJM9tXBSYTcTERR9YA7RdZdtg",  True, "8:00–17:00"),
    ("lachong", 11.9415908, 108.4247341, "ChIJeYhILbhtcTERPPwl6AroVxM",  True, "24h"),
    ("anphu",   11.9380082, 108.4354291, "3300600387922755092",          True, "07:00–21:00"),
    ("hm",      11.9407553, 108.4541227, "7304723431791610941",          True, "—"),
]
CENTER = _PM.CENTER
SLUG = "nha-trang-da-lat-bus-map"
PDF = "VanPhu-Dalat-Nha-Trang-Bus-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 6
LEGW = 200
MAPH = 440
H1PT = 22
MAXKM = 5.0
RINGS = (1, 2, 4)
SIDE = {}
JITTER = {}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("How to Get from Nha Trang to Da Lat: Bus & Limousine Map | Van Phu", "Nha Trang – Da Lat Bus Map",
 "How to get from Nha Trang to Da Lat by bus or limousine: about 135–150 km, 3–4 hours over Khanh Le Pass. Map of the Da Lat bus station and the Da Lat offices of FUTA, The Sinh Tourist, Lac Hong, An Phu and HM, with directions and a free PDF.",
 "Nha Trang to Da Lat is about 135–150 km and 3–4 hours over Khanh Le Pass. Small limousine vans (9–11 seats) usually pick you up at your hotel in Nha Trang and drop you at your hotel in Da Lat; big buses stop at the bus station or at the company's office. This map shows where they arrive and leave in Da Lat. Fares and timetables change often — check when you book.",
 "In Da Lat (1–6)", "Good to know",
 [("Travel time", "about 3–4 hours; buses with many stops take longer"), ("Limousine or bus", "limousine vans are faster and usually go hotel to hotel; big buses are cheaper and leave from stations and offices"), ("Khanh Le Pass", "a long, winding mountain road — take motion-sickness pills before you go if you need them"), ("Booking", "book a day ahead at weekends and holidays; ask for door drop-off when you book")],
 "Tips",
 ["Sit near the front if you get car-sick; the pass has many bends.", "Keep your passport, phone and money with you, not in the luggage hold.", "Da Lat is much colder than Nha Trang — keep a jacket in your hand luggage.", "Arriving early? Our shop opens at 4:30 AM daily, so you can pick up a bike right after the bus."],
 [("Da Lat Intercity Bus Station", "Day & night", "Main bus station on To Hien Thanh Street; FUTA (Phuong Trang) and other big buses to and from Nha Trang stop here. Ticket counters and restrooms."),
  ("FUTA (Phuong Trang) – Le Quy Don office", "Daytime", "FUTA city office near the centre; buy tickets here and ask about the free shuttle to the bus station or your hotel."),
  ("The Sinh Tourist Da Lat", "Daytime", "Office on Bui Thi Xuan Street, close to the centre; open-tour buses to Nha Trang and Mui Ne."),
  ("Lac Hong Limousine – Da Lat office", "Day & night", "Office on Hoang Dieu Street; limousine vans with massage seats to Nha Trang, hotel pick-up in the centre."),
  ("An Phu Travel", "Day & evening", "Office on Pham Ngu Lao Street with a waiting area; double-cabin limousine buses with a toilet on the Nha Trang route."),
  ("HM Happycar (Hoang Minh)", "—", "Office in the Pham Hong Thai area; cabin limousine buses to Nha Trang.")])
T["vi"] = _mk("Đi từ Nha Trang lên Đà Lạt: bản đồ nhà xe, limousine | Văn Phú", "Bản đồ nhà xe Nha Trang – Đà Lạt",
 "Đi từ Nha Trang lên Đà Lạt bằng xe khách hoặc limousine: khoảng 135–150 km, 3–4 tiếng qua đèo Khánh Lê. Bản đồ bến xe Đà Lạt và văn phòng tại Đà Lạt của Phương Trang (FUTA), The Sinh Tourist, Lạc Hồng, An Phú, HM — có chỉ đường và PDF miễn phí.",
 "Nha Trang – Đà Lạt khoảng 135–150 km, đi 3–4 tiếng qua đèo Khánh Lê. Xe limousine nhỏ (9–11 chỗ) thường đón tại khách sạn ở Nha Trang và trả tận khách sạn ở Đà Lạt; xe khách lớn dừng ở bến xe hoặc văn phòng nhà xe. Bản đồ này cho biết các xe đến và đi ở đâu tại Đà Lạt. Giá vé và giờ chạy thay đổi thường xuyên — hỏi khi đặt vé.",
 "Tại Đà Lạt (1–6)", "Nên biết",
 [("Thời gian", "khoảng 3–4 tiếng; xe dừng nhiều thì lâu hơn"), ("Limousine hay xe khách", "limousine nhanh hơn, thường đón trả tận khách sạn; xe khách lớn rẻ hơn, đi từ bến và văn phòng"), ("Đèo Khánh Lê", "đường núi dài, nhiều khúc cua — ai say xe nên uống thuốc trước"), ("Đặt vé", "cuối tuần, lễ Tết nên đặt trước một ngày; hỏi trả tận nơi khi đặt")],
 "Lưu ý",
 ["Hay say xe thì ngồi gần phía trước; đèo rất nhiều cua.", "Giữ hộ chiếu, điện thoại và tiền bên người, không để trong khoang hành lý.", "Đà Lạt lạnh hơn Nha Trang nhiều — để áo khoác trong túi xách tay.", "Đến sớm? Tiệm mở cửa 4:30 sáng mỗi ngày, xuống xe là nhận xe máy được ngay."],
 [("Bến xe Liên tỉnh Đà Lạt", "Cả ngày đêm", "Bến xe chính trên đường Tô Hiến Thành; Phương Trang (FUTA) và các xe khách lớn tuyến Nha Trang dừng tại đây. Có quầy vé và nhà vệ sinh."),
  ("Phương Trang (FUTA) – văn phòng Lê Quý Đôn", "Ban ngày", "Văn phòng FUTA gần trung tâm; mua vé tại đây và hỏi xe trung chuyển miễn phí ra bến hoặc về khách sạn."),
  ("The Sinh Tourist Đà Lạt", "Ban ngày", "Văn phòng trên đường Bùi Thị Xuân, gần trung tâm; xe open tour đi Nha Trang, Mũi Né."),
  ("Lạc Hồng Limousine – VP Đà Lạt", "Cả ngày đêm", "Văn phòng trên đường Hoàng Diệu; limousine ghế massage đi Nha Trang, đón tại khách sạn trung tâm."),
  ("An Phú Travel", "Ngày và tối", "Văn phòng trên đường Phạm Ngũ Lão, có chỗ ngồi chờ; xe phòng đôi có nhà vệ sinh tuyến Nha Trang."),
  ("HM Happycar (Hoàng Minh)", "—", "Văn phòng ở khu Phạm Hồng Thái; xe limousine giường phòng đi Nha Trang.")])

from content.nhatrangbusmap_tr import TR as _TR
for _l, _v in _TR.items():
    T[_l] = _mk(*_v)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"benxe": "Bến xe liên tỉnh Đà Lạt", "futa": "Phương Trang 2 Lê Quý Đôn", "sinh": "The Sinh Tourist Bùi Thị Xuân",
      "lachong": "Lạc Hồng Limousine Hoàng Diệu", "anphu": "An Phú Travel Phạm Ngũ Lão", "hm": "HM Happycar Hoàng Minh"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid] + " Đà Lạt")
