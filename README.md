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