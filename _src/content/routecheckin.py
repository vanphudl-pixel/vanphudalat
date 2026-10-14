"""Self-drive day route 'Hot check-in spots' (east then south): Lac Hu Co Tran, Memory Station (Tram Ky Uc), Suoi Binh Yen,
Happy Hill at Tuyen Lam Lake. Same idea as the popular 1-day group tours, ridden by motorbike. Coordinates, cid and hours
from Google Maps (2026-10-15). Prices are not stated (paid at each gate). vi + en for now."""
from content import photomap as _PM
from content._route import total as _total

SPOTS = [
    ("lachu",     11.9377633, 108.4933161, "15130344301866232807", True, "—"),
    ("memory",    11.9568290, 108.4876487, "5757446961785011590",  True, "7:00–22:00"),
    ("binhyen",   11.9018417, 108.4396697, "14318154768793841277", True, "7:00–18:00"),
    ("happyhill", 11.8838550, 108.4183732, "17209697497579551074", True, "7:00–17:30"),
]
ROUTE = True
CENTER = _PM.CENTER
SLUG = "route-check-in"
PDF = "VanPhu-Dalat-Route-Check-In"
GUIDES = {}
LANGS = ["vi", "en"]
NCENTER = 4
LEGW = 250
MAPH = 460
H1PT = 21
MAXKM = 9.0
RINGS = (2, 4, 7)
SIDE = {}
JITTER = {}
TOTAL = _total(SPOTS)
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]
T = {
"vi": {
 "title": "Đà Lạt 1 ngày tự túc: lộ trình check-in điểm hot bằng xe máy | Văn Phú",
 "h1": "Đà Lạt 1 ngày tự túc: lộ trình check-in điểm hot",
 "desc": "Tự chạy xe máy 4 điểm check-in hot ở Đà Lạt: Lạc Hư Cổ Trấn, Trạm Ký Ức (Memory Station), Suối Bình Yên và Happy Hill hồ Tuyền Lâm — thứ tự, giờ gợi ý, khoảng cách, chỉ đường và PDF miễn phí.",
 "lead": "Lộ trình giống các tour check-in 1 ngày, nhưng bạn tự chạy xe máy: buổi sáng 2 điểm phía Đông (hướng Trại Mát), buổi chiều 2 điểm phía Nam quanh hồ Tuyền Lâm. Trưa đi ngang trung tâm — tiện ăn trưa và ghé tiệm đổi pin nếu đi xe máy điện.",
 "center": "Thứ tự đi (1–4)",
 "season_h": "Lịch trình gợi ý",
 "season": [("8:00", "Lạc Hư Cổ Trấn — phố cổ kiểu Á Đông, hồ và cầu"), ("9:30", "Trạm Ký Ức (Memory Station) — đường ray, hồ nhỏ, nhiều hoa"), ("12:00", "ăn trưa ở trung tâm; xe máy điện ghé tiệm đổi pin (20.000 VND)"), ("13:30", "Suối Bình Yên — suối, rừng thông, có quán ăn"), ("15:30", "Happy Hill — đồi hoa nhìn hồ Tuyền Lâm; trả xe trước 21:00")],
 "tips_h": "Lưu ý",
 "tips": [f"Cả vòng khoảng {TOTAL} km đường chim bay, đường thực tế dài hơn — xe máy điện cần đổi pin buổi trưa (một pin khoảng 35–40 km), hoặc đi Honda Air Blade 125cc cho thoải mái.",
          "Giá vé ghi ở mỗi điểm là giá tham khảo (tổng hợp tháng 10/2026), thường đã kèm đồ uống — có thể thay đổi, kiểm tra tại cổng.",
          "Happy Hill rất đông cuối tuần — đi ngày thường hoặc đến sớm.",
          "Đường vào Suối Bình Yên và Happy Hill có đoạn hẹp, dốc — chạy chậm, nhất là khi mưa."],
 "price_l": "Giá vé tham khảo", "leg": "từ điểm trước", "total": "Cả vòng (tiệm → các điểm → tiệm): khoảng {km} km đường chim bay",
 "s": {
  "lachu": ("Lạc Hư Cổ Trấn", "Buổi sáng", "Phố cổ phong cách Á Đông với hồ và cầu ở phía Đông thành phố; buổi tối lên đèn đẹp (theo đánh giá của khách)."),
  "memory": ("Trạm Ký Ức (Memory Station)", "Buổi sáng", "Không gian mở trên đồi với đường ray, hồ nhỏ và nhiều hoa, nhìn xuống thung lũng; đẹp cả lúc hoàng hôn."),
  "binhyen": ("Suối Bình Yên", "Buổi chiều", "Suối và vườn hoa trong rừng thông gần Thiền viện Trúc Lâm; có quán ăn, nhiều góc chụp; tránh giờ trưa đông khách."),
  "happyhill": ("Happy Hill (đảo trái tim hồ Tuyền Lâm)", "Buổi chiều", "Đồi hoa nhìn ra hồ Tuyền Lâm; rất đông cuối tuần."),
 }},
"en": {
 "title": "Da Lat Day Trip by Motorbike: Hot Check-in Spots Route | Van Phu",
 "h1": "Da Lat Self-Guided Day Trip: Hot Check-in Spots",
 "desc": "Ride Da Lat's 4 hottest photo spots yourself: Lac Hu Co Tran, Memory Station (Tram Ky Uc), Suoi Binh Yen and Happy Hill at Tuyen Lam Lake — stop order, suggested times, distances, directions and a free PDF.",
 "lead": "The same day out as the popular check-in group tours, but on your own motorbike: two stops east of town (towards Trai Mat) in the morning, two around Tuyen Lam Lake in the afternoon. At lunchtime you pass the centre — handy for food and a battery swap at our shop if you ride electric.",
 "center": "Stop order (1–4)",
 "season_h": "Suggested plan",
 "season": [("8:00", "Lac Hu Co Tran — Asian-style old town with a lake and bridges"), ("9:30", "Memory Station (Tram Ky Uc) — rail track, small lake, lots of flowers"), ("12:00", "lunch in the centre; electric scooters can swap the battery at our shop (20,000 VND)"), ("13:30", "Suoi Binh Yen — stream and pine forest, food on site"), ("15:30", "Happy Hill — flower hill over Tuyen Lam Lake; return the bike before 21:00")],
 "tips_h": "Good to know",
 "tips": [f"The loop is about {TOTAL} km in a straight line, longer by road — on an electric scooter swap the battery at lunch (one battery is about 35–40 km), or take a Honda Air Blade 125cc for comfort.",
          "Ticket prices shown for each stop are for reference (collected October 2026), usually with a drink — they can change, check at the gate.",
          "Happy Hill is very busy at weekends — go on a weekday or arrive early.",
          "The access roads to Suoi Binh Yen and Happy Hill are narrow and steep in places — ride slowly, especially in the rain."],
 "price_l": "Reference price", "leg": "from the previous stop", "total": "Whole loop (shop → stops → shop): about {km} km in a straight line",
 "s": {
  "lachu": ("Lac Hu Co Tran", "Morning", "Asian-style old town with a lake and bridges east of the city; pretty when lit up in the evening (according to visitor reviews)."),
  "memory": ("Memory Station (Tram Ky Uc)", "Morning", "Open-air hilltop spot with a rail track, a small lake and lots of flowers over the valley; lovely at sunset too."),
  "binhyen": ("Suoi Binh Yen", "Afternoon", "Stream and flower gardens in pine forest near Truc Lam Monastery; food on site and many photo spots; avoid the lunchtime crowd."),
  "happyhill": ("Happy Hill (heart island, Tuyen Lam Lake)", "Afternoon", "Flower hill overlooking Tuyen Lam Lake; very busy at weekends."),
 }},
}
PRICE = {
 "vi": {"lachu": "khoảng 120.000–130.000 VND, kèm đồ uống và món ăn nhẹ",
        "memory": "khoảng 90.000–140.000 VND tùy gói, phổ biến 120.000 VND kèm 1 đồ uống hoặc bánh",
        "binhyen": "120.000 VND kèm 1 đồ uống; combo cùng Vườn Địa Đàng 150.000 VND (đồ uống + 1 xiên nướng)",
        "happyhill": "khoảng 110.000–120.000 VND kèm 1 đồ uống"},
 "en": {"lachu": "about 120,000–130,000 VND with a drink and a light snack",
        "memory": "about 90,000–140,000 VND depending on the option, usually 120,000 VND with a drink or cake",
        "binhyen": "120,000 VND with a drink; combo with Vuon Dia Dang 150,000 VND (drink + a grilled skewer)",
        "happyhill": "about 110,000–120,000 VND with a drink"},
}
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l
_Q = {"lachu": "Lạc Hư Cổ Trấn Đà Lạt", "memory": "Memory Station Trạm Ký Ức Đà Lạt", "binhyen": "Suối Bình Yên Đà Lạt", "happyhill": "Happy Hill hồ Tuyền Lâm"}
def img_link(sid):
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
