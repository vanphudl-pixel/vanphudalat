"""Indonesian-only page: halal restaurants in Da Lat for Muslim travellers from Indonesia/Malaysia (/id/sewa-motor-dalat/restoran-halal-dalat/).
Places were picked from Google Maps search results (2026-10-27) and kept only when the listing says halal or guests describe halal food.
Ratings and hours are Google Maps values on that date. Văn Phú holds no halal certificate for these restaurants: guests must ask."""

UPDATED = "2026-10-27"
H1 = "Restoran Halal di Đà Lạt"
TITLE = "Restoran Halal di Đà Lạt: Peta untuk Wisatawan Muslim | Van Phu"
DESC = "Peta restoran halal di Đà Lạt untuk wisatawan Muslim: 5 tempat dengan jam buka, rating Google, arah ke setiap tempat dan tips sebelum makan. Gratis."
LEAD = "Daftar dan peta restoran halal di Đà Lạt untuk wisatawan Muslim: jam buka, rating Google dan arah ke tiap tempat. Dari tiệm Văn Phú, semua tempat ini bisa dicapai dengan motor."

# name, rating, rating count, lat, lng, Google Maps place_id, hours, what it is, tip
SPOTS = [
    ("Sarah Halal Food", 4.3, 385, 11.9393156, 108.4344752, "ChIJNR7IagATcTERBdYNpK36fEQ", "06:30–22:30 setiap hari",
     "Restoran halal di pusat kota, di jalan utama, sekitar 350 m dari pasar malam. Menu Vietnam halal seperti gỏi cuốn, nasi ayam claypot dan hot pot. Ulasan menyebut staf bisa berbahasa Melayu.",
     "Cocok untuk makan malam setelah dari pasar malam."),
    ("Sagar Indian Cuisine – Halal Food", 4.9, 2827, 11.944323, 108.4348131, "ChIJzZTRb2ITcTERWlGidA6B1Dg", "10:00–22:00 (Selasa 14:30–22:00)",
     "Masakan India halal: biryani, kari, tandoori, samosa dan naan. Rating tertinggi dari antara tempat di daftar ini, dengan lebih dari 2.800 ulasan.",
     "Porsi besar dan cocok untuk makan berdua atau berkelompok."),
    ("Halal Food Dalat Hajah Hawa", 4.4, 220, 11.9382808, 108.439614, "ChIJ6a96xABtcTERFN7c10FhZGc", "07:00–22:00 setiap hari",
     "Hot pot seafood ala Vietnam dan pho daging sapi, dengan ruang makan dua lantai untuk rombongan. Ulasan menyebut ada tempat sholat dan pengunjung bisa mengisi daya ponsel.",
     "Tanyakan tempat sholat saat datang; staf biasanya melayani dalam bahasa Inggris."),
    ("Halal food ISMAEL", 4.3, 110, 11.9408137, 108.418481, "ChIJuXjkyt8TcTERmhAy1h6PfDY", "07:00–20:00 setiap hari",
     "Restoran di Cam Ly dengan bánh mì daging sapi, phở dan nasi goreng, sarapan sampai makan malam. Ulasan menyebut ada ruang sholat untuk Muslim dan parkir motor di depan.",
     "Agak jauh dari pusat, jadi pakai motor atau taksi. Minta cili potong jika suka pedas."),
    ("Halal Restaurant Kampung Melayu", 4.2, 184, 11.9435021, 108.4513805, "ChIJ0yjMS7UTcTERnq3m_tvAhHY", "06:00–21:30 setiap hari",
     "Restoran bergaya Melayu-Malaysia di Yersin, dengan pemilik yang bisa berbahasa Melayu. Ulasan pengunjung terbagi: ada yang puas, ada yang mengeluhkan rasa dan pelayanan.",
     "Baca ulasan terbaru dan coba dulu menu sederhana."),
]

TIPS = [
    "Tanyakan langsung kepada restoran tentang sertifikat halal, bahan dan cara memasak sebelum memesan. Văn Phú tidak memiliki sertifikat halal untuk tempat-tempat ini.",
    "Jika butuh tempat sholat, tanyakan dulu. Ulasan Google menyebut ISMAEL dan Hajah Hawa menyediakannya.",
    "Sarah Halal Food dan Sagar berada di pusat kota dan bisa dijangkau dengan jalan kaki atau motor singkat.",
    "ISMAEL dan Kampung Melayu agak jauh dari pusat, jadi sebaiknya naik motor atau taksi.",
    "Jam buka bisa berubah saat hari raya atau libur. Cek Google Maps sebelum datang.",
]

FAQ = [
    ("Apakah restoran di Đà Lạt ini bersertifikat halal?",
     "Văn Phú tidak memiliki sertifikat halal resmi untuk tempat-tempat ini. Daftar ini dibuat dari Google Maps dan ulasan pengunjung, jadi tanyakan langsung kepada restoran sebelum memesan."),
    ("Restoran halal mana yang paling dekat pusat kota?",
     "Sarah Halal Food dan Sagar Indian Cuisine berada di pusat kota dan sekitar Xuân Hương. ISMAEL dan Kampung Melayu sedikit lebih jauh."),
    ("Bagaimana sampai ke restoran-restoran ini?",
     "Sewa motor di tiệm Văn Phú di 1/15/5 Thông Thiên Học, buka mulai 4:30 pagi. Dari tiệm, semua tempat di daftar ini bisa dicapai dengan motor dalam waktu singkat."),
    ("Apakah ada tempat sholat di dekat restoran?",
     "Ulasan Google menyebut ISMAEL dan Hajah Hawa menyediakan tempat sholat. Tanyakan saat datang karena ini tidak selalu tercantum di Google Maps."),
]
