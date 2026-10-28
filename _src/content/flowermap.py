"""Da Lat flower gardens page — website page per language, slug per language.
9 places from a Klook travel article (updated 30 Oct 2025). Each place checked against Google Maps on 2026-10-28:
coordinates, Google Maps place link and opening hours come from Google Maps; ticket prices are reference prices from
recent visitor reviews. Left out: Tu Tra sunflower fields near Cau Dat (no Google Maps listing found)."""
from content import photomap as _PM
from content.flowermap_tr import TR as _TR

# id, lat, lng, Google Maps cid or place_id, ok on electric scooter, hours
SPOTS = [
    ("dalatflower", 11.9502479, 108.4498289, "ChIJZ0qug8wTcTER0m4S0SZkp2I", True, "6:30–18:00"),
    ("flowerplateau", 11.9266145, 108.3712692, "ChIJy0IMmMttcTERFDhXzzS1jB4", True, "7:00–16:30"),
    ("freshgarden", 11.9476933, 108.4090729, "ChIJzXuSUrZtcTERMCq6MmWKNTg", True, "7:30–17:30"),
    ("euro", 11.8807965, 108.5628551, "ChIJyTfYLD4XcTER9AmV8KOxlDc", False, "8:00–17:00"),
    ("florest", 11.9039342, 108.3674764, "ChIJEVcdXbATcTERrZHMhl3cKbM", False, "5:30–18:30"),
    ("fairytale", 11.9484697, 108.4029385, "ChIJCcTm2xdtcTERLlbemsPGwVI", True, "7:30–17:00"),
    ("godsvalley", 11.9084210, 108.3302057, "ChIJG53eZgBpcTERsaTfCuvGzIA", False, "8:00–17:00"),
    ("hydrangea", 11.9459911, 108.5130737, "ChIJ50x58zMScTERbfECwVkKQqI", True, "7:00–17:30"),
    ("lavender", 11.8964620, 108.4200723, "ChIJfTzy2FFrcTERgAWgJRroyQM", True, "7:30–22:00"),
]
CENTER = _PM.CENTER
SLUG = {"en": "flower-gardens-da-lat", "vi": "vuon-hoa-da-lat", "de": "blumengaerten-da-lat", "es": "jardines-de-flores-da-lat",
        "fr": "jardins-de-fleurs-da-lat", "it": "giardini-di-fiori-da-lat", "nl": "bloementuinen-da-lat", "id": "taman-bunga-dalat",
        "ms": "taman-bunga-da-lat", "ru": "sady-cvetov-dalat", "zh": "dalat-hua-yuan", "ko": "dalat-kkot-jeongwon",
        "ja": "dalat-hanazono", "th": "suan-dok-mai-dalat", "he": "ganot-prachim-dalat", "km": "suan-pka-dalat",
        "lo": "suan-dokmai-dalat", "my": "pan-khrai-dalat"}
PDF = None  # no printable PDF — the PDF button is hidden when this is None
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
T["vi"] = _mk("Vườn hoa Đà Lạt: 9 vườn và cánh đồng hoa đẹp, giờ mở cửa và cách đi | Văn Phú",
 "Vườn hoa và cánh đồng hoa Đà Lạt",
 "9 vườn hoa và cánh đồng hoa ở Đà Lạt: vườn hoa thành phố, cẩm tú cầu, lavender, vườn Châu Âu — giờ mở cửa theo Google Maps, giá vé tham khảo và cách đi từng điểm.",
 "9 vườn và cánh đồng hoa khách hay ghi trong lịch Đà Lạt: từ vườn hoa ngay bên hồ Xuân Hương đến cánh đồng cẩm tú cầu và lavender. Vườn hoa thành phố và Fresh Garden gần trung tâm; Vườn Châu Âu, The Florest và Dalat Gods' Valley xa hơn, nên đi xe số.",
 "Vườn hoa (1–9)", "Thời gian đẹp",
 [("Tháng 4–8", "cẩm tú cầu và lavender nở đẹp nhất"), ("Sáng sớm (6:30–9:00)", "sương và ánh sáng đẹp nhất để chụp ảnh"), ("Chiều (15:00–17:00)", "nắng dịu, ít khách hơn"), ("Cuối tuần", "các vườn hoa đông, dễ kẹt xe")],
 "Lưu ý",
 ["Giá vé là giá tham khảo từ đánh giá khách gần đây — kiểm tra tại cổng.",
  "Vườn Châu Âu Cầu Đất và The Florest khá xa, đường có đoạn đá dăm — nên đi xe máy số hoặc thuê xe.",
  "Dalat Gods' Valley và Lavender Dalat nên gọi xe ôm hoặc Grab chờ về vì ít xe quay đầu.",
  "Vườn hoa thành phố nên đến sáng sớm; buổi trưa nắng gắt và đông khách."],
 [("Vườn hoa thành phố Đà Lạt", "Sáng sớm", "Vườn hoa hàng trăm loài bên hồ Xuân Hương, có nhà kính hoa hồng và vườn bonsai phía sau; vé khoảng 100.000 VND."),
  ("Cao nguyên Hoa Đà Lạt", "Sáng", "Khu vườn trong rừng thông với vườn hồng, cây đa cổ thụ và đồi cẩm tú cầu; có xích đu cao ngắm đèo Tà Nung."),
  ("Fresh Garden", "Sáng", "Vườn hoa lavender, cúc và trầu bà ở làng hoa Vạn Thành, có cối xay gió và sở thú nhỏ; vé có một đồ uống."),
  ("Vườn Châu Âu Cầu Đất", "Sáng", "Vườn kiểu châu Âu với cối xay gió và quán cà phê trong toa tàu; vé khoảng 90.000 VND kèm đồ uống theo đánh giá."),
  ("The Florest – Hoa Trong Rừng", "Sáng", "Khu hoa 60 ha giữa rừng thông ở Cam Ly, có đồi hoa, suối và cánh đồng sậy; vé khoảng 210.000 VND theo đánh giá."),
  ("Dalat Fairytale Land", "Sáng", "Làng kiểu Hobbit giữa vườn hoa, nhà gỗ nhỏ; vé gồm cả hầm rượu Vĩnh Tiến."),
  ("Thung lũng Các Vị Thần (GOD Valley)", "Sáng", "Thung lũng theo thần thoại với mô hình lớn chuyển động; khách cho biết vé khoảng 150.000–220.000 VND tùy gói ăn uống."),
  ("Cánh đồng cẩm tú cầu Trại Mát", "Sáng sớm hoặc chiều", "Cánh đồng cẩm tú cầu cách trung tâm khoảng 8 km, có cầu gỗ giữa đồi hoa; vé khoảng 80.000 VND kèm nước."),
  ("Cánh đồng lavender Hồ Tuyền Lâm", "Sáng hoặc chiều", "Cánh đồng lavender bên hồ Tuyền Lâm, có trò trượt xuống đồi; vé khoảng 80.000 VND, có thêm gói kèm đồ uống.")])
T["en"] = _mk("Da Lat Flower Gardens: 9 Gardens and Flower Fields, Hours and Directions | Van Phu",
 "Flower Gardens and Flower Fields in Da Lat",
 "9 flower gardens and flower fields in Da Lat: city flower garden, hydrangea and lavender fields, a European-style garden — opening hours from Google Maps, reference ticket prices and directions for each stop.",
 "9 gardens and flower fields visitors add to their Da Lat plans, from the city flower garden by Xuân Hương Lake to hydrangea and lavender fields. The city garden and Fresh Garden are close to the centre; the European Garden, The Florest and Dalat Gods' Valley are farther, so ride a manual motorbike.",
 "Gardens (1–9)", "Best time to go",
 [("April–August", "hydrangeas and lavender bloom best"), ("Early morning (6:30–9:00)", "mist and soft light for photos"), ("Afternoon (15:00–17:00)", "gentler sun and fewer visitors"), ("Weekends", "gardens are busy and traffic builds up")],
 "Good to know",
 ["Ticket prices are reference prices from recent visitor reviews — check at the gate.",
  "The European Garden at Cau Dat and The Florest are farther out, with some gravel roads — ride a manual motorbike or hire a car.",
  "At Dalat Gods' Valley and Lavender Dalat, ask your driver to wait, as taxis are scarce there.",
  "Visit the city flower garden in the morning; by midday the sun is strong and it is crowded."],
 [("Dalat City Flower Garden", "Early morning", "Hundreds of flower species by Xuân Hương Lake, with a rose greenhouse and a bonsai garden at the back; entry about 100,000 VND."),
  ("Dalat Flower Plateau", "Morning", "Garden in a pine forest with rose beds, an old banyan tree and hydrangea hills; a high swing with a view over Tà Nung pass."),
  ("Fresh Garden", "Morning", "Lavender, chrysanthemum and monstera gardens in Vạn Thành flower village, with a windmill and a small zoo; entry includes one drink."),
  ("Euro Garden Cầu Đất", "Morning", "European-style garden with a windmill and a café inside a train carriage; reviews put entry around 90,000 VND with a drink."),
  ("The Florest – Hoa Trong Rừng", "Morning", "A 60-hectare flower garden among pines in Cam Ly, with flower hills, streams and reed fields; reviews put entry around 210,000 VND."),
  ("Dalat Fairytale Land", "Morning", "Hobbit-themed village among flower gardens with wooden houses; the ticket includes the Vĩnh Tiến wine cellar."),
  ("Dalat Gods' Valley", "Morning", "Mythology-themed valley with large moving models; reviews put tickets around 150,000–220,000 VND depending on food included."),
  ("Trại Mát Hydrangea Fields", "Early morning or afternoon", "Hydrangea fields about 8 km from the centre, with a wooden bridge over a flower hill; entry about 80,000 VND with a drink."),
  ("Tuyền Lâm Lake Lavender Fields", "Morning or afternoon", "Lavender fields beside Tuyền Lâm Lake, with a coaster ride down the hill; about 80,000 VND entry, with a drink package at 150,000 VND.")])

from content.flowermap_tr import TR as _TR
for _l, _v in _TR.items():
    T[_l] = _mk(*_v)
for _l in LANGS:
    for _k in SHARED:
        T[_l][_k] = _PM.T[_l][_k]
    assert set(T[_l]["s"]) == {x[0] for x in SPOTS}, _l

_Q = {"dalatflower": "Vườn hoa thành phố Đà Lạt", "flowerplateau": "Cao nguyên Hoa Đà Lạt", "freshgarden": "Fresh Garden Đà Lạt",
      "euro": "Euro Garden Cầu Đất Đà Lạt", "florest": "The Florest Hoa trong rừng Đà Lạt", "fairytale": "Fairytale Land Đà Lạt",
      "godsvalley": "Dalat Gods Valley Đà Lạt", "hydrangea": "Cánh đồng cẩm tú cầu Trại Mát", "lavender": "Lavender Đà Lạt Hồ Tuyền Lâm"}
def img_link(sid):
    """Temporary photo link: Google Images search for the place name."""
    from urllib.parse import quote
    return "https://www.google.com/search?tbm=isch&q=" + quote(_Q[sid])
