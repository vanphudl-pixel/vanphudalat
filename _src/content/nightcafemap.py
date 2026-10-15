"""Da Lat night-view cafés — cafés on the eastern hills (Xuan Truong – Trai Mat) facing the greenhouse valley, whose lights
come on after dark. List chosen by the shop owner (2026-10-15). Coordinates, cid and hours from Google Maps (2026-10-15);
prices only as "guests report" from Google reviews. All 6 sit in one small area, so the PDF map is projected around the
cluster (PROJ_CENTER, no distance rings); distances in the list stay "from Xuan Huong Lake" like the other maps."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid, ok on electric scooter, hours
SPOTS = [
    ("chenhvenh", 11.9664740, 108.4884956, "15648223900754745181", True, "7:00–22:30"),
    ("changvang", 11.9523410, 108.4921398, "12614283922321401960", True, "15:00–22:30"),
    ("loicuagio", 11.9499840, 108.4911826, "12805385481593888229", True, "6:30–22:00"),
    ("viyeu",     11.9459645, 108.4885109, "5303741118304316169",  True, "24h"),
    ("vuthi",     11.9425307, 108.4868226, "43638923006999716",    True, "7:00–23:00"),
    ("maycay",    11.9429711, 108.4855475, "6324389856862809670",  True, "7:30–22:00"),
]
CENTER = _PM.CENTER
PROJ_CENTER = (11.9500, 108.4885)
SLUG = "night-view-cafe-map"
PDF = "VanPhu-Dalat-Night-View-Cafe-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 6
LEGW = 260
MAPH = 470
H1PT = 21
MAXKM = 6.0
RINGS = ()
SIDE = {}
JITTER = {"vuthi": (10, 6), "maycay": (-12, -4)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["vi"] = _mk("Cà phê view nhà kính về đêm Đà Lạt: bản đồ 6 quán | Văn Phú", "Bản đồ cà phê view đêm Đà Lạt",
 "Bản đồ 6 quán cà phê view nhà kính về đêm ở Đà Lạt: Chênh Vênh, Chạng Vạng, Lời Của Gió, Vì Yêu Mà Đến, Làng Vũ Thị, Nhà Mây Cây — giờ mở cửa, giá khách ghi nhận, chỉ đường và PDF miễn phí.",
 "6 quán trên đồi phía Đông thành phố (Xuân Trường – Trại Mát), nhìn xuống thung lũng nhà kính. Đến lúc hoàng hôn, ngồi tới khi đèn nhà kính sáng lên khắp thung lũng. Các quán gần nhau, cách tiệm Văn Phú khoảng 5–6 km.",
 "Các quán (1–6)", "Nên biết",
 [("Giờ đẹp", "từ hoàng hôn (khoảng 17:30) tới tối, khi đèn nhà kính dưới thung lũng sáng lên"), ("Lạnh", "trên đồi buổi tối rất lạnh và nhiều gió — mang áo ấm"), ("Cuối tuần", "rất đông — đến trước hoàng hôn để có chỗ đẹp"), ("Mùa mưa", "chiều tối hay mưa, sương mù có thể che view")],
 "Lưu ý",
 ["Cả 6 quán cách tiệm khoảng 5–6 km — xe máy điện đi về thoải mái.",
  "Đường lên các quán dốc, tối và hay có sương — bật đèn, chạy chậm.",
  "Không uống rượu bia khi lái xe.",
  "Thuê 1 ngày tính tới 21:00 — muốn ngồi quán tối muộn thì thuê từ 2 ngày để giữ xe qua đêm.",
  "Giá ghi trong từng quán là khách ghi nhận trên Google Maps, có thể thay đổi."],
 [("Chênh Vênh Coffee Chill", "Hoàng hôn – tối", "Bãi cỏ rộng trên đồi nhìn xuống cánh đồng nhà kính; buổi tối có lửa trại, có đồ ăn (theo đánh giá của khách)."),
  ("Chạng Vạng (tiệm nướng)", "Hoàng hôn – tối", "Quán nướng trên sườn dốc đường Huỳnh Tấn Phát, ngắm hoàng hôn rồi đèn nhà kính; mở từ 15:00. Khách ghi nhận combo nướng 2 người kèm cơm khoảng 580.000 VND; ngồi ngoài trời buổi tối lạnh và ẩm sương."),
  ("Lời Của Gió", "Hoàng hôn", "Quán nhiều tầng, view hơn 180° nhìn thành phố và thung lũng, rất nhiều góc chụp ảnh. Khách ghi nhận vé vào khoảng 80.000 VND kèm đồ uống; thường đông."),
  ("Vì Yêu Mà Đến", "Tối", "Nhiều tầng sân nhìn ra núi và nhà kính, cạnh vườn hồng; Google Maps ghi mở 24 giờ. Khách ghi nhận cà phê sữa khoảng 55.000 VND, nhân viên chu đáo, có chăn cho khách khi lạnh."),
  ("Làng Vũ Thị", "Tối", "Không gian đèn vàng lãng mạn, nhiều tối có nhạc sống (theo đánh giá của khách); đồ uống từ khoảng 70.000 VND. Cuối tuần đông, không nhận giữ chỗ — nên đến sớm."),
  ("Tiệm cà phê bánh Nhà Mây Cây", "Hoàng hôn – tối", "Quán nhỏ yên tĩnh trong hẻm 31 Sào Nam, bánh ngon, buổi tối có bếp lửa; ít đông hơn các quán lớn.")])
T["en"] = _mk("Da Lat Night-View Cafés: Map of 6 Greenhouse-View Cafés | Van Phu", "Da Lat Night-View Café Map",
 "Map of 6 Da Lat cafés with a night view over the glowing greenhouses: Chenh Venh, Chang Vang, Loi Cua Gio, Vi Yeu Ma Den, Lang Vu Thi, Nha May Cay — opening hours, prices guests report, directions and a free PDF.",
 "6 cafés on the hills east of town (Xuan Truong – Trai Mat), looking down on the greenhouse valley. Arrive for sunset and stay until the greenhouse lights come on across the valley. They are close together, about 5–6 km from our shop.",
 "Cafés (1–6)", "Good to know",
 [("Best time", "from sunset (around 17:30) into the evening, when the greenhouse lights in the valley come on"), ("Cold", "the hills are very cold and windy at night — bring a warm jacket"), ("Weekends", "very busy — arrive before sunset for a good seat"), ("Rainy season", "rain is common in the late afternoon and fog can hide the view")],
 "Tips",
 ["All 6 cafés are about 5–6 km from our shop — an easy round trip on an electric scooter.",
  "The roads up are steep, dark and often foggy — use your lights and ride slowly.",
  "Don't drink and ride.",
  "A 1-day rental runs until 21:00 — to stay out late, rent for 2 days or more and keep the bike overnight.",
  "Prices under each café are what guests report on Google Maps and can change."],
 [("Chenh Venh Coffee Chill", "Sunset – evening", "A big grassy hilltop looking over the greenhouse fields; campfires in the evening and food on the menu (according to visitor reviews)."),
  ("Chang Vang (BBQ)", "Sunset – evening", "BBQ spot on the slope of Huynh Tan Phat Street — watch the sunset, then the greenhouse lights; opens at 15:00. Guests report a BBQ combo for 2 with rice at about 580,000 VND; the outdoor seats get cold and damp with fog at night."),
  ("Loi Cua Gio", "Sunset", "Multi-level café with a view of more than 180° over the city and valley, with lots of photo corners. Guests report entry of about 80,000 VND including a drink; often busy."),
  ("Vi Yeu Ma Den", "Evening", "Several terraces facing the mountains and greenhouses, next to a rose garden; Google Maps lists it as open 24 hours. Guests report milk coffee at about 55,000 VND, kind staff and blankets when it gets cold."),
  ("Lang Vu Thi", "Evening", "Romantic warm lighting and live music on many evenings (according to visitor reviews); drinks from about 70,000 VND. Busy at weekends and no reservations — come early."),
  ("Nha May Cay Café & Bakery", "Sunset – evening", "A small, quiet café down lane 31 Sao Nam with good cakes and a fire pit in the evening; less crowded than the big cafés.")])

from content.nightcafemap_tr import TR as _TR
for _l, _v in _TR.items():
    T[_l] = _mk(*_v)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"chenhvenh": "Chênh Vênh Coffee Chill Đà Lạt", "changvang": "Chạng Vạng Đà Lạt Huỳnh Tấn Phát", "loicuagio": "Lời Của Gió cafe Đà Lạt",
      "viyeu": "Vì Yêu Mà Đến Đà Lạt", "vuthi": "Làng Vũ Thị Đà Lạt", "maycay": "Nhà Mây Cây Đà Lạt"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
