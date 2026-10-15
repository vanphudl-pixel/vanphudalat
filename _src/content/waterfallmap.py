"""Da Lat waterfalls map — website page (/waterfalls-map/) and printable PDF.
6 waterfalls open to visitors within reach of a day ride. Coordinates, cid and hours from Google Maps (2026-10-15);
ticket prices are reference prices (placeshub_price + recent Google reviews). Left out: Hang Cop (Tiger Cave) and Gougah
(closed to visitors per 2026 reviews/guides), Tam Tham (hard trek, no proper road), Ankroet (poor upkeep per reviews),
Bobla and Dambri (too far for a day ride from Da Lat)."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours ("—" = not listed on Google Maps)
SPOTS = [
    ("camly",      11.9418046, 108.4208479, "3717547526993202889",  True,  "7:00–17:00"),
    ("datanla",    11.9034324, 108.4496999, "17928424083927973989", True,  "7:30–16:30"),
    ("prenn",      11.8769509, 108.4707101, "16983086886745196739", True,  "8:00–17:00"),
    ("lienkhuong", 11.7491438, 108.3834120, "6273367862966626372",  False, "—"),
    ("voi",        11.8230091, 108.3364973, "5705245422110093707",  False, "—"),
    ("pongour",    11.6893042, 108.2656291, "9280240154432551472",  False, "7:30–17:00"),
]
CENTER = _PM.CENTER
SLUG = "waterfalls-map"
PDF = "VanPhu-Dalat-Waterfalls-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 6
LEGW = 200
MAPH = 470
H1PT = 22
MAXKM = 36.0
RINGS = (5, 15, 30)
SIDE = {}
JITTER = {}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["vi"] = _mk("Các thác đẹp ở Đà Lạt: bản đồ 6 thác nước đi xe máy | Văn Phú", "Bản đồ các thác đẹp ở Đà Lạt",
 "Bản đồ 6 thác nước đẹp quanh Đà Lạt đang đón khách: Datanla, Prenn, Cam Ly, Liên Khương, thác Voi, Pongour — khoảng cách, giờ mở cửa, giá vé tham khảo, chỉ đường và PDF miễn phí.",
 "6 thác đang đón khách, từ thác Cam Ly ngay trong thành phố tới Pongour rộng nhất vùng. Datanla, Prenn và Liên Khương nằm cùng một hướng theo QL20 về phía Nam, tiện ghé liền một chuyến; thác Voi rẽ sang Nam Ban. Giá vé ghi trong từng thác là giá tham khảo, có thể thay đổi.",
 "Các thác (1–6)", "Nên biết",
 [("Mùa mưa", "thác nhiều nước và hùng vĩ hơn, nước thường đục; mùa khô nước ít và trong hơn"), ("Giờ mở cửa", "phần lớn khoảng 7:00–17:00 — nên đi buổi sáng"), ("Giày", "đường xuống thác dốc, đá ướt trơn — mang giày bám"), ("Tạm ngưng", "thác Hang Cọp và Gougah hiện không đón khách nên không có trên bản đồ")],
 "Lưu ý",
 ["Cam Ly, Datanla, Prenn gần trung tâm — đi xe máy điện được; Liên Khương, thác Voi, Pongour xa — nên đi Honda Air Blade 125cc.",
  "Không tắm hoặc lội ở chân thác, nhất là sau mưa — nước lên rất nhanh.",
  "QL20 qua đèo Prenn có nhiều xe tải và xe khách — chạy sát lề phải, không vượt ở khúc cua.",
  "Giá vé là giá tham khảo tổng hợp tháng 10/2026 — kiểm tra tại cổng."],
 [("Thác Cam Ly", "Buổi sáng", "Thác nhỏ ngay trong thành phố, có vườn quanh thác; vé khoảng 60.000 VND. Nước chảy qua thành phố nên đôi khi có mùi (theo đánh giá của khách) — hợp ghé nhanh."),
  ("Thác Datanla", "Buổi sáng", "Thác lớn gần trung tâm nhất, giữa rừng thông đèo Prenn; xuống thác bằng máng trượt (alpine coaster) khoảng 2,4 km hoặc đi bộ, có zipline. Vé vào khoảng 30.000–50.000 VND, trò chơi tính thêm."),
  ("Thác Prenn", "Buổi sáng", "Trong khu du lịch dưới chân đèo Prenn, có lối đi sau màn nước. Khách gần đây ghi nhận vé khoảng 110.000–220.000 VND và nhiều dịch vụ trong khu đóng — nhiều người thấy chưa đáng giá vé."),
  ("Thác Liên Khương", "Buổi sáng", "Thác rộng sát QL20 gần sân bay Liên Khương; ngắm từ các quán cà phê, nhà hàng nhìn ra thác; đẹp lúc bình minh (theo đánh giá của khách)."),
  ("Thác Voi (Nam Ban)", "Buổi sáng", "Thác lớn, nước mạnh, cạnh chùa Linh Ẩn; vé khoảng 30.000–60.000 VND. Đánh giá gần đây cho biết thác có lúc tạm đóng — khi đó vẫn ngắm được từ chùa Linh Ẩn."),
  ("Thác Pongour", "Cả ngày", "Thác rộng nhất quanh Đà Lạt, nước đổ qua nhiều bậc đá; vé khoảng 20.000–50.000 VND, xe điện xuống thác khoảng 15.000 VND mỗi chiều. Bậc thang trơn sau mưa.")])
T["en"] = _mk("Da Lat Waterfalls Map: 6 Waterfalls to Ride To | Van Phu", "Da Lat Waterfalls Map",
 "Map of 6 waterfalls around Da Lat that are open to visitors: Datanla, Prenn, Cam Ly, Lien Khuong, Elephant Falls and Pongour — distances, opening hours, reference ticket prices, directions and a free PDF.",
 "6 waterfalls open to visitors, from Cam Ly in the city to Pongour, the widest in the region. Datanla, Prenn and Lien Khuong sit on the same road south (QL20), so they fit in one ride; Elephant Falls is a turn-off towards Nam Ban. Ticket prices under each waterfall are for reference and can change.",
 "Waterfalls (1–6)", "Good to know",
 [("Rainy season", "more water and more dramatic falls, but the water is often muddy; in the dry season there is less water and it is clearer"), ("Opening hours", "most about 7:00–17:00 — go in the morning"), ("Shoes", "paths down are steep and wet rocks are slippery — wear shoes with grip"), ("Closed", "Hang Cop (Tiger Cave) and Gougah falls are not open to visitors now, so they are not on the map")],
 "Tips",
 ["Cam Ly, Datanla and Prenn are close to the centre — fine on an electric scooter; Lien Khuong, Elephant Falls and Pongour are farther — take a Honda Air Blade 125cc.",
  "Don't swim or wade at the foot of a waterfall, especially after rain — the water rises fast.",
  "QL20 over Prenn Pass has many trucks and coaches — keep to the right and don't overtake on bends.",
  "Ticket prices are reference prices collected in October 2026 — check at the gate."],
 [("Cam Ly Waterfall", "Morning", "Small waterfall right in the city with gardens around it; ticket about 60,000 VND. The stream runs through town, so it can smell at times (according to visitor reviews) — good for a quick stop."),
  ("Datanla Waterfall", "Morning", "The closest big waterfall, in pine forest on Prenn Pass; ride down on the 2.4 km alpine coaster or walk, zipline too. Entry about 30,000–50,000 VND, rides extra."),
  ("Prenn Waterfall", "Morning", "Inside a resort at the foot of Prenn Pass, with a path behind the water. Recent visitors report tickets of about 110,000–220,000 VND and many facilities closed — many feel it is not worth the price."),
  ("Lien Khuong Waterfall", "Morning", "Wide waterfall right by QL20 near Lien Khuong airport; watch it from cafés and restaurants facing the falls; lovely at sunrise (according to visitor reviews)."),
  ("Elephant Falls (Nam Ban)", "Morning", "Big, powerful waterfall next to Linh An Pagoda; ticket about 30,000–60,000 VND. Recent reviews say it is sometimes temporarily closed — you can still see it from Linh An Pagoda."),
  ("Pongour Waterfall", "All day", "The widest waterfall around Da Lat, flowing over many rock tiers; ticket about 20,000–50,000 VND, buggy down to the falls about 15,000 VND each way. Steps are slippery after rain.")])

from content.waterfallmap_tr import TR as _TR
for _l, _v in _TR.items():
    T[_l] = _mk(*_v)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"camly": "Thác Cam Ly Đà Lạt", "datanla": "Thác Datanla Đà Lạt", "prenn": "Thác Prenn Đà Lạt", "lienkhuong": "Thác Liên Khương",
      "voi": "Thác Voi Nam Ban", "pongour": "Thác Pongour"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
