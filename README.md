Nama = Alena Aura Deviyana
NPM = 2506656394
Kelas = PBP

### Tugas 1

1. **Penggunaan Elemen Semantik HTML5**
   Ya, dalam merancang struktur halaman web portofolio ini, saya menggunakan elemen semantik HTML5 seperti `<section>` untuk memisahkan bagian utama (seperti *Hero*, *Education*, *Skills*, *Experience*, *Interests*, dan *Tools*), serta `<article>` untuk membungkus kartu-kartu konten individual (seperti kartu riwayat pendidikan dan kartu minat). Penggunaan elemen semantik ini sangat membantu membuat *static web* menjadi lebih terstruktur, mudah dibaca oleh mesin pencari (*SEO-friendly*), serta memudahkan pengelolaan *styling* CSS pada masing-masing bagian secara spesifik dan modular.

2. **Tantangan Tata Letak Responsif & Evaluasi Prioritas Elemen**
   Tantangan terbesar dalam merespons ukuran layar adalah menjaga agar konten tidak terpotong atau terlalu padat pada layar perangkat seluler (seperti bagian kartu pengalaman kerja dan galeri minat). Saat berpindah dari tampilan *desktop* ke *mobile*, saya mengevaluasi elemen dengan melihat fungsionalitas utamanya: elemen dekoratif atau tata letak grid berlapis (seperti *flex-row* yang memanjang ke samping) diprioritaskan untuk diubah menjadi *stacked* (tersusun vertikal ke bawah) atau diaktifkan fitur *horizontal scrolling* agar tetap nyaman diakses menggunakan gestur sentuh tanpa merusak estetika antarmuka.

3. **Batasan Web Statis & Rencana Fungsionalitas Dinamis**
   Sebagai sebuah *static web* murni, batasan utama yang dirasakan adalah ketidakmampuan website untuk mengelola data secara interaktif secara langsung dari pengguna—misalnya formulir kontak (*contact form*) yang tidak bisa mengirim pesan secara nyata, atau ketidakmampuan memperbarui portofolio tanpa mengubah kode sumber secara manual. Pada iterasi proyek selanjutnya, fungsionalitas dinamis yang paling ingin saya tambahkan adalah integrasi backend (seperti Django REST Framework atau sistem basis data) untuk pengelolaan data portofolio secara dinamis, serta fitur interaktif seperti mode gelap/terang (*dark/light mode switch*) yang tersimpan secara lokal.

- AI Disclosure & Strategy Analysis

Dalam pengerjaan dan pengembangan fitur portofolio ini, saya memanfaatkan AI (Gemini) sebagai kolaborator teknis. 
- Tools yang Digunakan: Gemini AI sebagai asisten pengkodean (coding assistant), pemecah masalah layout CSS, dan menyusun ulang dengan bahasa yang lebih formal teks refleksi.

- Strategi Prompting: 
- Iterative Refinement: Memasukkan potongan kode aktual (style.css dan index.html) beserta tangkapan layar (screenshot) error atau tampilan visual yang kurang pas untuk mendapatkan solusi spesifik.
- Context-Driven Prompting: Meminta bantuan penulisan salinan teks profesional (copywriting) berbahasa Inggris untuk bagian deskripsi pengalaman kerja di COMPFEST 18 agar selaras dengan standar industri.


Bagian Spesifik yang Dibantu oleh AI:
- Penulisan variasi kalimat profesional untuk deskripsi pengalaman (exp-bio) pada section Experience.
- Penyusunan ulang kode CSS untuk transisi tata letak horizontal scrolling pada bagian Interests beserta penambahan gradient overlay agar teks tetap kontras dan terbaca di atas latar belakang gambar.
- Membantu memformat dan merumuskan jawaban analitis untuk pertanyaan refleksi mingguan.

- Analisis Kritis & Batasan AI: Meskipun AI sangat membantu mempercepat proses debugging CSS dan penyusunan struktur HTML, AI terkadang memberikan solusi generik yang tidak memperhitungkan struktur hierarki kelas CSS yang sudah ada sebelumnya. Oleh karena itu, saya melakukan peninjauan manual (code review), penyesuaian selektor kelas secara presisi, serta pengujian tampilan secara langsung di browser lokal (trial and error) untuk memastikan tata letak akhir benar-benar rapi, responsif, dan sesuai dengan estetika desain yang saya inginkan.

- Ringkasan Interaksi:
- Permintaan Konten Portfolio: "Ganti deskripsi COMPFEST 18 agar menyesuaikan dengan landing page hero section...", AI memberikan opsi kalimat profesional dalam bahasa Inggris.
- Perbaikan Layout & CSS: "Gap di bawah skill masih sedikit dan tdk sama dhn atasnya, lalu AI menganalisis kode CSS dan memberikan snippet kode.  

### Tugas 2

#### 1. Alur Permintaan dan Pemrosesan Halaman Baru (MVT Architecture)
Ketika pengguna mengakses URL halaman baru (misalnya `/interest/`):
1. **HTTP Request:** Browser mengirimkan *request* HTTP GET ke server Django.
2. **Root `urls.py` (Proyek):** Django menerima permintaan dan memeriksa `portofolio/urls.py` untuk mengarahkan rute awal. Karena terdapat konfigurasi `path("", include("main.urls"))`, permintaan diteruskan ke konfigurasi routing milik aplikasi `main`.
3. **App `urls.py` (Aplikasi):** Berkas `main/urls.py` mencocokkan *path* `'interest/'` dengan fungsi pengendali `show_interest` yang diimpor dari `main/views.py`.
4. **View (`views.py`):** Fungsi `show_interest(request)` dipanggil. View bertugas meminta data dari *database* dengan memanggil `Interest.objects.all()`.
5. **Model (`models.py`):** Object-Relational Mapper (ORM) Django pada model `Interest` menerjemahkan perintah Python menjadi *query* SQL untuk mengambil seluruh baris data dari tabel `main_interest` di *database*.
6. **Context & Render:** View menerima data dari model, mengemasnya ke dalam *dictionary* `context`, lalu memanggil `render(request, 'interest.html', context)`.
7. **Template (`interest.html`):** Django Template Engine memproses berkas HTML. Tag DTL seperti `{% for interest in interests %}` mengiterasi data dan mengisi struktur HTML secara dinamis.
8. **HTTP Response:** Hasil render HTML utuh dikembalikan ke browser pengguna untuk ditampilkan di layar.

#### 2. Alasan Menggunakan Model Dibandingkan Hardcoding pada Template
Menyimpan data pada model *database* sangat disarankan dibanding menulisnya langsung (*hardcoding*) di dalam berkas template HTML karena beberapa alasan:
* **Kemudahan Pemeliharaan (*Maintainability*):** Jika ada perubahan data (seperti menambah minat baru, mengubah deskripsi, atau memperbarui gambar), perubahan cukup dilakukan pada *database* (misalnya via Django Admin atau Shell) tanpa perlu menyentuh berkas kode HTML aplikasi.
* **Pemisahan Tanggung Jawab (*Separation of Concerns*):** Mengisolasi data (Model) dari tampilan visual (Template) menjaga struktur kode tetap rapi dan terhindar dari keterikatan data statis.
* **Skalabilitas dan Reusabilitas:** Data pada model dapat dipanggil kembali di berbagai halaman lain atau disajikan dalam bentuk API jika aplikasi berkembang di masa mendatang.

#### 3. Perbedaan `makemigrations` dan `migrate`
* **`makemigrations`:** Berfungsi untuk mendeteksi perubahan skema pada berkas `models.py` dan mendokumentasikannya ke dalam berkas "cetak biru" migrasi di dalam folder `migrations/`. Perintah ini **belum** mengubah struktur *database* fisik.
* **`migrate`:** Berfungsi untuk mengeksekusi berkas-berkas migrasi yang telah dibuat oleh `makemigrations` dan menerapkannya secara nyata ke *database* (seperti membuat tabel baru atau menambah kolom).
* **Contoh Kasus:** Ketika membuat model `Interest` baru di `models.py` dengan *field* `title`, `description`, dan `image_name`:
  1. Perintah `python manage.py makemigrations` akan menghasilkan berkas migrasi baru (misal `0002_interest.py`).
  2. Perintah `python manage.py migrate` wajib dijalankan setelahnya agar tabel `main_interest` benar-benar terbuat di *database* SQLite. Jika langkah kedua terlewat, aplikasi akan mengalami error `OperationalError: no such table`.

---

### AI Disclosure
Dalam penyelesaian Tugas 2, saya menggunakan alat bantu AI (**Gemini**) sebagai rekan diskusi teknis dengan rincian sebagai berikut:
* **Alat yang Digunakan:** Gemini AI.
* **Strategi Prompting:** Menggunakan *prompting* bertahap (*step-by-step guidance*) berdasarkan rubrik tugas, mulai dari perancangan model `Interest`, perbaikan error migrasi/routing, penyusunan *unit test*, hingga pengecekan konsistensi navbar.
* **Bagian yang Dibantu AI:**
  * Pembuatan struktur pengujian (*unit tests*) pada `main/tests.py` untuk menguji aksesibilitas URL, pemuatan data dinamis dari model, dan kondisi *empty state*.
  * *Troubleshooting* error `OperationalError: no such table` dan `NameError` pada pendaftaran routing/views.
  * Penyusunan penjelasan alur MVT dan refleksi teknis untuk dokumentasi `README.md`.
* **Evaluasi & Pengoperasian:** Seluruh kode hasil saran AI telah saya uji secara independen menggunakan perintah `python manage.py test` dan dipastikan lulus 100% tanpa error sebelum di-commit.