Nama : Nadya Alyssa Azzahra

NPM : 2506599270

Kelas : PBP A

### Tugas 1

1. Dalam merancang struktur HTML yang digunakan, saya menggunakan elemen section. Elemen ini berguna dalam memisahkan bagian-bagian dalam page myportofolio menjadi beberapa section berbeda, sehingga kode jadi lebih rapi, terstruktur, dan mudah dipahami.

2. Tantangan tata letak yang saya temui adalah ukuran teks yang terlalu besar dan memenuhi layar. Untuk mengatasinya, saya mengecilkan ukuran font ke ukuran yang sesuai agar lebih enak dipandang tapi tetap terbaca dengan jelas.

3. Karena website HTML ini merupakan static web murni, semua kontennya bersifat hard-coded sehingga setiap perubahan harus diedit langsung di source filenya. Hal ini terasa kurang efisien, seperti jika saya ingin memperbarui informasi (misalnya menambahkan experience baru) saya harus kembali ke source file dan menambahkannya secara manual. Ke depannya, saya tertarik untuk menambahkan fitur dimana perubahan (seperti penambahan data) bisa dilakukan langsung di website.

Disclosure AI: saya tidak menggunakan bantuan AI dalam mengerjakan tugas ini.

### Tugas 2

1. Pengguna mengakses URL webpage Education melalui browser -> Browser mengirim HTTP request ke server Django -> Request tersebut ditangkap oleh urls.py proyek yang berperan sebagai gerbang utama untuk memetakan request ke aplikasi yang tepat -> Request diteruskan ke main/urls.py (urls.py aplikasi) yang bertugas memetakan URL spesifik ke view yang sesuai -> View menerima request lalu memanggil model (Education.objects.all()) untuk mengambil data -> Model yang bertugas mengatur dan mengelola data pada aplikasi mengambil data dari database dan mengembalikannya ke view -> View yang berfungsi menangani logika yang akan ditampilkan ke pengguna mengirim data ke template -> Template sebagai berkas HTML yang menentukan bagaimana aplikasi ditampilkan menerima data dari view -> Django me-render template education.html dengan context yang tertera di view -> HTML yang sudah di-render dikirim balik ke browser sebagai HTTP response -> Browser menampilkan webpage Education

2. Dengan menyimpan data dalam model, data bisa diubah tanpa harus setiap kali mengedit file HTML secara manual dan melakukan deploy ulang. Selain itu, data juga bisa dipakai di banyak tempat tanpa harus menulis ulang sehingga mengurangi redundansi. Memisahkan fungsi data dan tampilan membuat kode jadi lebih terstruktur dan mudah dikelola.

3. makemigrations membaca perubahan pada model lalu membuat file migrasi yang berisi perubahan model yang belum diaplikasikan ke database, sedangkan migrate mengaplikasikan perubahan model dalam file migrasi tersebut ke database. Contoh perubahan model yang mengharuskan kedua perintah tersebut dijalankan adalah menambah model baru di Models.py atau menambah field baru di model yang sudah ada.

Disclosure AI: saya tidak menggunakan bantuan AI dalam mengerjakan tugas ini.