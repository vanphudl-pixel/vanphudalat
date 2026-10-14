"""Reference ticket prices for the places hub (collected October 2026). Where sources disagree, a range is given.
Sources: lamdongtours.com/ve (2026), intour.com.vn price list (updated 01/07/2026), cungphuot.info (updated 17/09/2026),
Google Maps visitor reviews (2025–2026). Places with no reliable price are left out (no line shown).
Religious sites and public spaces: free. Add a language by adding a dict keyed by spot id."""
_FREE_VI = "Miễn phí"
_FREE_REL_VI = "Miễn phí (có hòm công đức)"
_FREE_EN = "Free"
_FREE_REL_EN = "Free (donation box)"
PRICE = {
"vi": {
 "lake": _FREE_VI, "square": _FREE_VI, "market": "Miễn phí vào chợ",
 "cathedral": _FREE_REL_VI, "pink": _FREE_REL_VI, "thanhtam": _FREE_REL_VI, "camly": _FREE_REL_VI, "dusinh": _FREE_REL_VI, "thanhmau": _FREE_REL_VI,
 "linhson": _FREE_REL_VI, "linhquang": _FREE_REL_VI, "tau": _FREE_REL_VI, "vanhanh": _FREE_REL_VI, "linhan": _FREE_REL_VI, "linhphuoc": _FREE_REL_VI,
 "truclam": "Vào thiền viện miễn phí; cáp treo từ đồi Robin khoảng 120.000 VND một chiều, 150.000 VND khứ hồi",
 "tuyenlam": "Miễn phí; thuyền, kayak tính riêng",
 "crazy": "Khoảng 50.000–60.000 VND người lớn, trẻ em khoảng 20.000 VND",
 "station": "Vé vào ga khoảng 50.000 VND; tàu Đà Lạt – Trại Mát khứ hồi khoảng 85.000–124.000 VND",
 "palace": "Khoảng 30.000–40.000 VND người lớn",
 "vanthanh": "Một số vườn hoa thu phí chụp ảnh, bảng giá tham khảo ghi khoảng 40.000 VND",
 "valley": "250.000 VND người lớn (gồm xe điện trong khu), trẻ em khoảng 110.000–125.000 VND; cầu kính, máng trượt tính thêm",
 "datanla": "Vé vào cổng khoảng 30.000–50.000 VND; máng trượt (alpine coaster), zipline tính thêm",
 "clay": "Khoảng 120.000 VND người lớn, trẻ em khoảng 30.000–50.000 VND",
 "langbiang": "Vé vào khoảng 50.000 VND; xe jeep lên đỉnh Radar tính thêm",
 "radar": "Gồm trong vé khu Langbiang (khoảng 50.000 VND); xe jeep lên đỉnh tính thêm",
 "caudat": "Đồi chè vào miễn phí; cà phê, dịch vụ tính riêng",
 "caudatsky": "Khoảng 120.000 VND, kèm đồ uống và bữa sáng",
 "prenn": "Bảng giá tham khảo ghi khoảng 50.000 VND; có khách ghi nhận 110.000 VND",
 "voi": "Khoảng 30.000–60.000 VND",
 "pongour": "Khoảng 20.000–50.000 VND; xe điện xuống thác khoảng 15.000 VND mỗi chiều",
},
"en": {
 "lake": _FREE_EN, "square": _FREE_EN, "market": "Free to enter",
 "cathedral": _FREE_REL_EN, "pink": _FREE_REL_EN, "thanhtam": _FREE_REL_EN, "camly": _FREE_REL_EN, "dusinh": _FREE_REL_EN, "thanhmau": _FREE_REL_EN,
 "linhson": _FREE_REL_EN, "linhquang": _FREE_REL_EN, "tau": _FREE_REL_EN, "vanhanh": _FREE_REL_EN, "linhan": _FREE_REL_EN, "linhphuoc": _FREE_REL_EN,
 "truclam": "Monastery free; cable car from Robin Hill about 120,000 VND one way, 150,000 VND return",
 "tuyenlam": "Free; boats and kayaks extra",
 "crazy": "About 50,000–60,000 VND per adult, children about 20,000 VND",
 "station": "Station entry about 50,000 VND; Da Lat – Trai Mat train return about 85,000–124,000 VND",
 "palace": "About 30,000–40,000 VND per adult",
 "vanthanh": "Some flower gardens charge for photos; reference price lists show about 40,000 VND",
 "valley": "250,000 VND per adult (shuttle inside included), children about 110,000–125,000 VND; glass bridge and slides extra",
 "datanla": "Entry about 30,000–50,000 VND; alpine coaster and zipline extra",
 "clay": "About 120,000 VND per adult, children about 30,000–50,000 VND",
 "langbiang": "Entry about 50,000 VND; jeep to Radar Peak extra",
 "radar": "Included in the Lang Biang ticket (about 50,000 VND); jeep to the top extra",
 "caudat": "Tea hills free; café and services extra",
 "caudatsky": "About 120,000 VND with a drink and breakfast",
 "prenn": "Reference price lists show about 50,000 VND; some visitors report 110,000 VND",
 "voi": "About 30,000–60,000 VND",
 "pongour": "About 20,000–50,000 VND; buggy down to the falls about 15,000 VND each way",
},
}
LABEL = {"vi": "Giá vé tham khảo", "en": "Reference price"}
NOTE = {"vi": "Giá vé là giá tham khảo tổng hợp tháng 10/2026 từ các bảng giá du lịch và đánh giá của khách — có thể thay đổi, kiểm tra tại cổng.",
        "en": "Ticket prices are for reference, collected in October 2026 from travel price lists and visitor reviews — they can change, check at the gate."}
