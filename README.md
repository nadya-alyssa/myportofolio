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

### Tugas 3

1. ModelForm pada Django membuat form berdasarkan model yang sudah dibuat, sehingga setiap definisi field untuk diinput tidak perlu dibuat ulang. Selain itu, ModelForm juga memvalidasi data secara otomatis dan memudahkan proses penyimpanan data ke database. {% csrf_token %} wajib ditambahkan untuk melindungi form dari serangan yang mengubah request ke server Django menjadi request ke API lain yang berpotensi berbahaya.

2. JSON lebih disukai dibanding XML karena lebih sederhana, ukurannya lebih kecil, mudah diproses, proses parsing lebih cepat, serta mudah terintegrasi dengan JavaScript dan API modern.

3. Proses mengembalikan data (misal: data pendidikan) dalam bentuk JSON dilakukan melalui fungsi get_education_json() -> school_query berfungsi mengambil query yang ditulis pada parameter, dalam hal ini school -> Django mengambil seluruh data Education dari database -> data difilter berdasarkan nama sekolah (school) -> data yang didapatkan masih berbentuk object (belum JSON) -> serialization dilakukan untuk mengubah data menjadi format JSON -> data JSON dikembalikan kepada client melalui HttpResponse

Disclosure AI: saya tidak menggunakan bantuan AI dalam mengerjakan tugas ini.

### Tugas 4

Disclosure AI: saya tidak menggunakan bantuan AI dalam mengerjakan tugas ini.

### Tugas 5

1. Debouncing merupakan teknik menunda suatu fungsi hingga user berhenti memicu sebuah event selama jeda waktu tertentu. Setiap event baru akan mereset timer, sehingga fungsi hanya berjalan setelah user selesai. Debouncing penting diterapkan dalam fitur pencarian dengan AJAX karena bisa menghemat beban server dan database, mengurangi request ke server, serta membuat UI jadi lebih stabil.

2. fetch() merupakan fungsi async dan selalu mengembalikan sebuah Promise. await menjeda eksekusi fungsi async sampai Promise itu selesai diproses sebelum lanjut ke kode berikutnya. Tanpa await, kode berikutnya akan langsung berjalan tanpa menunggu hasil Promise selesai sehingga bisa terjadi error/hasil salah karena kode belum mendapat data yang dibutuhkan.

3. XSS adalah serangan dimana penyerang menyisipkan kode JavaScript miliknya ke halaman web yang kemudian dijalankan di browser korban. Data yang ditampilkan melalui AJAX/JavaScript lebih rentan terkena serangan ini dibanding yang langsung pakai template Django. Hal ini karena Django melalukan escaping secara otomatis, sedangkan AJAX ataupun JavaScript tidak memiliki perlindungan tersebut secara otomatis sehingga harus diaplikasikan secara manual.

Disclosure AI: saya menggunakan Claude untuk membantu dalam penerapan JavaScript untuk mengubah format tampilan DateField() di experience.html dan menerapkan fitur edit di experience.html yang kemudian saya aplikasikan juga di project.html

### Tugas 6

1. REST (Representational State Transfer) adalah gaya arsitektur untuk merancang web API, bukan library maupun format data. Mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena JSON hanyalah format data, sedangkan REST adalah cara API diatur. Endpoint seperti /api/get-projects/, /api/delete-project/5/, atau /projects/add-ajax/ bisa saja mengembalikan JSON, tetapi tetap tidak RESTful karena tindakan ditulis di URL, method HTTP tidak dimanfaatkan sesuai maknanya, dan resource tidak terstruktur.

Perbedaan PUT dan PATCH adalah PUT mengirim representasi pengganti sehingga seluruh field wajib dikirim, sedangkan PATCH hanya mengirim field yang ingin diubah dan field lain tetap memakai nilai sebelumnya. Selain itu, PUT cocok dipakai saat form edit mengirim seluruh data sekaligus, sedangkan PATCH cocok untuk mengubah satu atau beberapa field saja, misalnya hanya mengganti judul experience.

2. Serializer pada DRF berperan sebagai penerjemah dua arah antara objek model dan data yang dikirim ke klien. Pada GET, serializer mengubah objek model menjadi tipe data Python yang kemudian dirender menjadi JSON (serialization), sedangkan pada POST/PUT/PATCH, serializer memeriksa input dan mengubahnya menjadi data tervalidasi yang siap disimpan (deserialization). Serializer lebih menguntungkan dibanding merakit dictionary manual karena tidak perlu ditulis berulang, langsung bisa validasi, field hasil perhitungan seperti star_count tidak bisa dipalsukan klien, serta bentuk data lebih sederhana dan konsisten.

3. Perbedaan autentikasi dan otorisasi pada Django REST Framework adalah autentikasi menjawab pertanyaan "siapa kamu", sedangkan otorisasi menjawab "apa yang boleh kamu lakukan". Pada DRF, authentication class mengenali session login lalu mengisi request.user, kemudian permission class (IsPortfolioOwnerOrEditorOrReadOnly dan IsAuthenticated) memutuskan apakah request boleh diteruskan ke isi view.

Hak akses harus diperiksa dengan permission class di server karena menyembunyikan tombol di template hanya mengatur tampilan, bukan membatasi eksekusi perintah di server. Siapa pun bisa mengirim request langsung lewat DevTools Console, Browsable API, atau tools seperti curl tanpa melewati tombol di halaman. Oleh karena itu, permission class di sisi server (seperti IsPortfolioOwnerOrEditorOrReadOnly) merupakan pertahanan utama untuk memvalidasi dan memblokir request tidak sah dengan status 403 Forbidden.

4. SessionAuthentication mengandalkan cookie sessionid, dan browser mengirim cookie domain secara otomatis pada setiap request ke domain tersebut, termasuk yang dipicu situs penyerang. Tanpa perlindungan, halaman jahat bisa membuat browser korban yang sedang login mengirim POST/DELETE ke API kita dan server mengira itu tindakan sah (serangan CSRF).

Test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan karena force_authenticate pada APITestCase hanya melakukan bypass/penetapan langsung identitas request.user untuk mempermudah pengujian otorisasi (permission) tanpa melalui proses login sesi yang sebenarnya. Jadi test dengan force_authenticate hanya berguna untuk menguji permission (siapa boleh apa), bukan login dan CSRF. Test seperti itu akan tetap hijau walaupun perlindungan CSRF rusak atau dimatikan.

Disclosure AI: saya menggunakan Claude untuk membantu dalam menyesuaikan main/tests.py yang sebelumnya belum diubah.
                                                                                