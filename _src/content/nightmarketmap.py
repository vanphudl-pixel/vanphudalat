"""Da Lat night market & evening food map — website page (/night-market-food-map/) and printable PDF.
The night market plus 5 well-known evening food / hot-drink spots in the centre. Coordinates, place_id and hours from
Google Maps (2026-10-24); prices only as "guests report" from Google reviews."""
from content import photomap as _PM

# id, lat, lng, Google Maps cid or place_id, ok on electric scooter, hours
SPOTS = [
    ("chodem",  11.9414015, 108.4372912, "ChIJw-dBTv8TcTERPCSnIa35zyE", True, "17:30–24:00"),
    ("hoasua",  11.9436816, 108.4353550, "ChIJv1VaSSkTcTERp6ulBpKkaLk", True, "7:00–23:30"),
    ("chehe",   11.9427897, 108.4351573, "ChIJe4zlRXQTcTER9GLiNOvVM80", True, "16:30–23:00"),
    ("didinh",  11.9428701, 108.4287827, "ChIJOXrSxiwTcTERUC5y-ke7Tc8", True, "13:00–20:30"),
    ("dungbeo", 11.9393009, 108.4344909, "ChIJs36GrNUTcTERKlg3Gh_YL1E", True, "12:00–01:00"),
    ("taongo",  11.9391984, 108.4480242, "ChIJ14MTlwqRNDERKh9SbNSC2TE", True, "8:00–22:00"),
]
CENTER = _PM.CENTER
PROJ_CENTER = (11.9412, 108.4380)
SLUG = "night-market-food-map"
PDF = "VanPhu-Dalat-Night-Market-Food-Map"
GUIDES = {}
LANGS = list(_PM.LANGS)
NCENTER = 6
LEGW = 220
MAPH = 470
H1PT = 22
MAXKM = 2.5
RINGS = ()
SIDE = {}
JITTER = {"hoasua": (8, -8), "chehe": (-10, 8)}
SHARED = ["pdf", "dir", "hours", "best", "km", "photo", "ev", "gas", "h", "check", "map_note", "cta_h", "cta", "addr", "qr", "shop"]

def _mk(title, h1, desc, lead, center, season_h, season, tips_h, tips, s):
    return {"title": title, "h1": h1, "desc": desc, "lead": lead, "center": center, "season_h": season_h, "season": season,
            "tips_h": tips_h, "tips": tips, "s": dict(zip([x[0] for x in SPOTS], s))}

T = {}
T["en"] = _mk("Da Lat Night Market & Street Food Map: What to Eat at Night | Van Phu", "Da Lat Night Market & Food Map",
 "Map of the Da Lat night market and 5 local evening food spots: grilled rice paper (banh trang nuong), hot soy milk, che dessert and chicken hot pot with lemon basil — opening hours, prices guests report, directions and a free PDF.",
 "The night market comes alive every evening below Da Lat Market, and the best local snacks are a few minutes away: grilled rice paper, hot soy milk, warm che dessert and chicken hot pot with lemon basil (lau ga la e). All spots are within about 2 km of Xuan Huong Lake — easy on foot or by scooter.",
 "Night market & food (1–6)", "Good to know",
 [("Best time", "from about 18:00, when the market stalls are set up; weekends are very busy"), ("Cold nights", "Da Lat evenings are cool — hot soy milk and hot pot are the local way to warm up"), ("Prices", "street snacks are cheap; ask the price before you order at market stalls"), ("Rain", "afternoon and evening rain is common in the rainy season — the market is quieter then")],
 "Tips",
 ["Agree on the price before you order at night market stalls, and check the change.", "Keep your phone and wallet in front of you in the crowd.", "Parking: use the paid bike parking near the market and keep the ticket.", "Prices under each place are what guests report on Google Maps and can change."],
 [("Da Lat Night Market", "Evening", "Street food, hot drinks, grilled snacks, strawberries and warm clothes on Nguyen Thi Minh Khai Street below Da Lat Market; the steps above it are a popular place to sit and eat."),
  ("Hoa Sua soy milk shop", "Evening", "Long-running local shop for hot soy milk, peanut, black sesame and corn milk with small pastries; very busy in the evening, served fast (according to visitor reviews)."),
  ("Che He dessert shop", "Evening", "Small shop for warm Vietnamese che dessert, always busy with locals; guests report about 8,000–15,000 VND a cup."),
  ("Banh trang nuong Di Dinh", "Afternoon – early evening", "Famous grilled rice paper (\"Vietnamese pizza\") on Hoang Dieu Street; guests report about 17,000–24,000 VND each and a short queue. Closes at 20:30."),
  ("Dung Beo soy milk & bakery", "Late evening", "Soy milk and bakery open until about 1:00 — good for a late hot drink with bread or cream puffs."),
  ("Tao Ngo chicken hot pot (lau ga la e)", "Dinner", "Da Lat's well-known chicken hot pot with lemon basil and mushrooms; guests report about 200,000–300,000 VND for a pot for 2–3 people. Snacks put on the table are charged if you eat them.")])
T["vi"] = _mk("Chợ đêm Đà Lạt & ăn vặt buổi tối: bản đồ quán ngon | Văn Phú", "Bản đồ chợ đêm và quán ăn tối Đà Lạt",
 "Đà Lạt có món gì ngon buổi tối? Bản đồ chợ đêm Đà Lạt và 5 quán quen: bánh tráng nướng Dì Đinh, sữa đậu nành Hoa Sữa, Dung Béo, chè Hé, lẩu gà lá é Tao Ngộ — giờ mở cửa, giá khách ghi nhận, chỉ đường và PDF miễn phí.",
 "Chợ đêm họp mỗi tối ngay dưới chợ Đà Lạt, và các món ăn vặt ngon nhất chỉ cách vài phút: bánh tráng nướng, sữa đậu nành nóng, chè nóng và lẩu gà lá é. Tất cả nằm trong khoảng 2 km quanh hồ Xuân Hương — đi bộ hoặc chạy xe máy đều tiện.",
 "Chợ đêm và quán ăn (1–6)", "Nên biết",
 [("Giờ đẹp", "từ khoảng 18:00, khi các sạp đã dọn xong; cuối tuần rất đông"), ("Tối lạnh", "buổi tối Đà Lạt se lạnh — sữa đậu nành nóng và lẩu là cách người địa phương làm ấm"), ("Giá", "đồ ăn vặt rẻ; ở các sạp chợ đêm nên hỏi giá trước khi gọi"), ("Mưa", "mùa mưa chiều tối hay mưa — khi đó chợ vắng hơn")],
 "Lưu ý",
 ["Ở sạp chợ đêm nên hỏi giá trước khi gọi món và kiểm tra tiền thối.", "Chỗ đông người, để điện thoại và ví phía trước.", "Gửi xe ở bãi giữ xe gần chợ và giữ vé.", "Giá ghi trong từng quán là khách ghi nhận trên Google Maps, có thể thay đổi."],
 [("Chợ đêm Đà Lạt", "Buổi tối", "Đồ ăn đường phố, đồ uống nóng, đồ nướng, dâu tây và áo ấm trên đường Nguyễn Thị Minh Khai dưới chợ Đà Lạt; bậc thang phía trên là chỗ ngồi ăn quen thuộc."),
  ("Sữa đậu nành Hoa Sữa", "Buổi tối", "Quán lâu năm với sữa đậu nành nóng, sữa đậu phộng, mè đen, bắp, kèm bánh ngọt; buổi tối rất đông nhưng phục vụ nhanh (theo đánh giá của khách)."),
  ("Quán chè Hé", "Buổi tối", "Quán chè nóng nhỏ, lúc nào cũng đông người địa phương; khách ghi nhận khoảng 8.000–15.000 VND một ly."),
  ("Bánh tráng nướng Dì Đinh", "Chiều – chập tối", "Bánh tráng nướng nổi tiếng trên đường Hoàng Diệu; khách ghi nhận khoảng 17.000–24.000 VND một cái, có lúc phải xếp hàng. Đóng cửa 20:30."),
  ("Sữa đậu nành Dung Béo", "Tối muộn", "Sữa đậu nành và tiệm bánh mở tới khoảng 1:00 sáng — hợp uống nóng khuya với bánh mì, bánh su."),
  ("Lẩu gà lá é Tao Ngộ", "Bữa tối", "Lẩu gà lá é nổi tiếng Đà Lạt, có nấm và măng; khách ghi nhận nồi cho 2–3 người khoảng 200.000–300.000 VND. Đồ ăn kèm để sẵn trên bàn, ăn mới tính tiền.")])

from content.nightmarketmap_tr import TR as _TR
for _l, _v in _TR.items():
    T[_l] = _mk(*_v)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"chodem": "Chợ đêm Đà Lạt", "hoasua": "Sữa đậu nành Hoa Sữa Đà Lạt", "chehe": "Chè Hé Đà Lạt",
      "didinh": "Bánh tráng nướng Dì Đinh Đà Lạt", "dungbeo": "Sữa đậu nành Dung Béo Đà Lạt", "taongo": "Lẩu gà lá é Tao Ngộ Đà Lạt"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
