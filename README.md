Tugas 2: 
1. Cara saya mengimplementasikan checklist di atas tentu saja kebanyakan dengan bantuan tutorial yang ada. Seperti yang sudah ada dalam tutorial 0, saya membuat projek baru django. awalnya saya tidak langsung membuat new repo di git, melainkan saya membuat di local terlebih dahulu. pada permulaan saya mengaktifkan env terlebih dahulu dalam direktori lokal saya kemudian membuat requirements dan instalasi dependencies dan terbuat lah projek django baru sesuai keinginan saya. lalu saya konfigurasi proyek dan run server dan menambahkan file .gitignore . kemudian saya membuat aplikasi main dalam proyek lalu membuat template dan mengisi direktori template dengan file html yang berisi nama app, nama diri, dan nama kelas. lalu membuat function dalam views.py yang berisi nama app, nama diri, dan nama kelas yang sudah diassign sesuai keinginan saya untuk nantinya ditampilkan pada html. lalu membuat urls.py pada main untuk memetakan function yang telah dibuat pada views.py. lalu saya deploy ke pws, tetapi masih terjadi failed. kemudian saya baru membuat sebuah repo baru dalam git saya yang berisi file ecommerce saya tadi dan membuat readme yang berisi pertanyaan pertanyaan dalam tugas
   
2. ![chart](https://github.com/user-attachments/assets/8bc4677d-52ca-443c-b417-09c020db4db0)

3. git dapat membantu dalam tracking pengembangan perangkat lunak yang biasanya dikerjakan oleh beberapa anggota dalam satu tim. git dapat memudahkan pengerjaan secara terpisah melalui device masing - masing melalui beberapa branch yang nantinya hasil akhir nya dapat dimerge sesuai kemauan dan kesepakatan. git juga dapat menyimpan kode secara online sehingga mudah diakses oleh tim

4. django dapat memudahkan user dengan banyak fitur bawaan nya sehingga user tidak perlu lagi menginstall dan mengonfigurasi banyak hal tambahan, lalu django memiliki arsitektur mvt yang memudahkan pemula memahami konsep dasar pengembangan perangkat lunak 

5. model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menyediakan cara untuk memetakan objek dalam kode Python ke tabel di database relasional

Tugas 3 : 
1. Data delivery penting dalam pengimplementasian platform karena dapat memastikan bahwa data yang relevan sampai ke user dengan data yang akurat dan tepat waktu
2. JSON lebih ringan dan readable dibandingkan XML karena sintaksnya lebih simpel, selain itu JSON punya struktur struktur data yang lebih sesuai dengan objek dalam programming language modern
3. Ini memeriksa apakah data yang dikirimkan melalui form valid atau tidak, kalo dipanggil method ini bakal validasi data input nya udah sesuai kaya aturan yang ada di model or form nya atau belom, kalo semua data nya udah tervalidasi, method ini bakalan balikin True, kalo ada data yang ga valid, dia bakalan balikin False dan isi attribute error dengan message yang dimauin
4. CSRF (Cross-Site Request Forgery) token digunakan untuk mencegah serangan CSRF, di mana penyerang mencoba memanipulasi pengguna yang terautentikasi agar melakukan aksi yang tidak diinginkan tanpa sepengetahuan mereka.
Jika kita tidak menambahkan csrf_token pada form, form tersebut rentan terhadap serangan CSRF, di mana penyerang bisa eksekusi request jahat dsb
5. pertama saya buat base.html dan isi dengan isi kontennya
   lalu saya buat form input data yang bakal nampilin data product entry pada html
   trus saya tambahin beberapa kode pada views.py buat return data dalam bentuk xml dan json dalam bentuk semua data dan beberapa id nya aja
   kemudian saya copass link ke postman dan lihat data dari json dan xml yang tersedia
   lalu saya lakukan add commit dan push ke github dan push ke pws

6.![WhatsApp Image 2024-09-18 at 08 51 33_412fc302](https://github.com/user-attachments/assets/f603af0d-8199-47af-b18f-75ab7845c4c3)
![WhatsApp Image 2024-09-18 at 08 50 44_ee453bd6](https://github.com/user-attachments/assets/d9aa4a96-ef88-4582-a4ac-6cc64b1d099d)
   ![WhatsApp Image 2024-09-18 at 08 52 06_89c09b4b](https://github.com/user-attachments/assets/b9c63137-5dd2-47a6-88f2-c1edcf80c57e)
   ![WhatsApp Image 2024-09-18 at 08 51 06_ae253954](https://github.com/user-attachments/assets/93c08305-7980-4899-b1ae-31a015d13e96)

Tugas 4 : 

1. HttpResponseRedirect(): adalah objek Django yang mengembalikan respons HTTP dengan kode status 302 (Redirect). Kode ini memberitahu browser untuk melakukan permintaan baru (GET) ke URL yang diberikan. Biasanya kita harus nyebutin URL nya secara manual, misal kayak HttpResponseRedirect('/some-url/').

redirect(): Fungsi utilitas yang lebih praktis dari Django. Ini membuat kode lebih sederhana karena bisa memasukkan URL, URL pattern name, atau bahkan instance model, dan Django akan secara otomatis melakukan mapping ke URL yang benar. Contoh: redirect('main:show_main') akan mengarahkan pengguna ke view show_main.

2. Penghubungan model Product dengan User biasanya dilakukan pake ForeignKey. Kalo di Django, misal model Product punya field user sebagai ForeignKey ke model User, ini berarti bahwa setiap produk dihubungkan dengan satu pengguna, dan setiap pengguna dapat memiliki banyak produk.

3. Authentication: Proses memverifikasi identitas pengguna, memastikan bahwa pengguna adalah siapa yang mereka klaim. Misalnya, pengguna harus memasukkan username dan password yang sesuai untuk mengakses sistem.

Authorization: Setelah pengguna berhasil di-autentikasi, authorization menentukan hak akses mereka, yaitu apa yang dapat mereka lakukan atau lihat dalam sistem. Sebagai contoh, satu pengguna bisa memiliki hak akses admin untuk membuat atau menghapus data, sementara yang lain mungkin hanya bisa melihat data.

4. Django mengingat pengguna yang telah login dengan menggunakan sessions dan cookies. Saat pengguna berhasil login:

Django menciptakan session untuk pengguna tersebut, dan session ID disimpan dalam cookie.
Pada setiap request berikutnya, cookie session dikirim oleh browser, sehingga Django bisa mengetahui siapa pengguna yang sedang melakukan request berdasarkan session ID tersebut.

5. step - step : 
- pertama saya tambahkan from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
pada views.py yang saya punya lalu saya tambahkan function register 
- kemudian membuat file register.html dan mengisi dengan beberapa kode 
- lalu menambahkan beberapa import dan path dalam urls.py
- kemudian menambahkan beberapa import dalam views.py dan menambahkan function login dan logout
- lalu buat login.html pada templates dan mengisi dengan beberapa kode
- kemudian menambahkan sedikit perubahan pada function login dan logout
- lalu menghubungkan productentry dengan user dengan migrate
Tugas 5 :

1. Urutan prioritas (specificity) dalam CSS menentukan selector mana yang diterapkan jika ada beberapa selector yang mengacu pada elemen yang sama. Urutan prioritas didasarkan pada tingkat spesifikasinya:

Inline Styles: CSS yang diterapkan langsung di atribut elemen HTML, seperti <div style="color: red;">. Ini memiliki prioritas tertinggi.

ID Selectors: Selector dengan #id memiliki prioritas lebih tinggi dibandingkan class atau element selector. Misal: #myID.

Class, Pseudo-Class, Attribute Selectors: Selector yang menggunakan class (.class), pseudo-class (:hover), atau atribut ([type="text"]). Misal: .myClass.

Type (Tag) Selectors: Selector berbasis elemen HTML, seperti h1, p, atau div.

Universal Selectors and Inherited Styles: Selektor yang bersifat umum, seperti * atau style yang diwariskan dari elemen induk.

Jika ada konflik, aturan dengan prioritas lebih tinggi diterapkan. Jika dua selector memiliki specificity yang sama, maka yang ditulis terakhir dalam CSS yang akan diambil.

2. Responsive design adalah pendekatan dalam pengembangan web di mana tampilan aplikasi menyesuaikan diri dengan berbagai ukuran layar atau perangkat, seperti smartphone, tablet, dan desktop. Ini penting karena pengguna mengakses aplikasi dari perangkat yang berbeda-beda
Contoh:
Sudah Menerapkan Responsive Design:
   Twitter: Tampilan feed menyesuaikan ukuran layar, dengan elemen-elemen seperti menu atau kolom samping menghilang atau berpindah.
Belum Menerapkan Responsive Design
    Arngren.net: Ini adalah contoh situs web e-commerce yang terkenal karena tampilannya yang berantakan, dengan banyak gambar, teks, dan tautan yang bertumpuk dan tidak teratur di layar kecil.

3. Perbedaan antara Margin, Border, dan Padding

Margin: Jarak antara elemen dan elemen lainnya. Digunakan untuk memberi ruang di luar batas elemen.css 

Border: Garis di sekitar elemen yang memisahkan padding dan margin.css Copy code 

Padding: Jarak antara konten di dalam elemen dan batas elemen.css Copy code 

Margin dan padding mempengaruhi tata letak elemen, tetapi margin berinteraksi dengan elemen luar, sedangkan padding berinteraksi dengan elemen di dalamnya.

4. Flexbox dan Grid Layout

Flexbox: Digunakan untuk mengatur elemen dalam satu dimensi (baris atau kolom). Cocok untuk tata letak yang lebih sederhana atau dinamis, seperti menyejajarkan elemen atau membagi ruang di antara elemen.

Grid Layout: Digunakan untuk mengatur elemen dalam dua dimensi (baris dan kolom). Berguna untuk tata letak yang lebih kompleks, seperti membangun grid di seluruh halaman.

5. Cara saya menyelesaikan checklist checklist 
- Pertama saya membuat fungsi edit product yang dapat mengedit nama, harga, dan deskripsi dari produk yang sudah dimasukkan
- Lalu saya membuat navigation bar yang responsive dan menyesuaikan dengan perangkat yang digunakan untuk mengakses web saya
- Lalu, saya mendesign login page dan register page
- Lalu, saya mendesign home dan card berisi product berdasarkan yang sudah diajarkan
Tugas 6 :

1. Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web:
* Interaktivitas: JavaScript memungkinkan pengguna untuk berinteraksi langsung dengan halaman web tanpa harus merefresh atau memuat ulang halaman. Misalnya, pengguna dapat menekan tombol untuk memunculkan popup atau menjalankan animasi.
* Pengelolaan DOM: JavaScript memungkinkan manipulasi langsung elemen HTML (DOM) untuk mengubah konten, struktur, atau gaya halaman secara dinamis.
* Asynchronous Processing: Dengan JavaScript, kita dapat melakukan operasi asinkron seperti mengambil data dari server menggunakan AJAX, sehingga tidak mengganggu interaksi pengguna di halaman web.
* Validasi Form: JavaScript bisa digunakan untuk memvalidasi input pengguna di sisi frontend sebelum dikirim ke server, menghemat waktu dan sumber daya.
* Pengalaman Pengguna yang Lebih Baik: Penggunaan JavaScript dapat meningkatkan pengalaman pengguna dengan memberikan feedback yang cepat dan responsif (misalnya melalui loading indikator saat mengambil data).

2. Fungsi await pada Fetch: await digunakan untuk menunggu penyelesaian (resolved) dari Promise yang dihasilkan oleh fetch() sebelum melanjutkan eksekusi kode berikutnya. fetch() adalah operasi asinkron yang mengembalikan Promise, yang berarti hasilnya mungkin belum tersedia langsung setelah pemanggilan.

3. Alasan Penggunaan csrf_exempt pada View AJAX POST: csrf_exempt digunakan untuk menonaktifkan proteksi CSRF (Cross-Site Request Forgery) pada view tertentu, seperti view yang menerima request AJAX POST. Secara default, Django memproteksi view dari serangan CSRF dengan memerlukan token CSRF untuk setiap request POST. Namun, dalam kasus AJAX, terutama ketika request dilakukan dari klien yang tidak menyediakan token CSRF, kita perlu menonaktifkan validasi tersebut. Penggunaan yang hati-hati: Menggunakan csrf_exempt bisa mengurangi keamanan aplikasi, jadi penggunaannya harus dibatasi hanya pada view yang sangat diperlukan, dan pastikan metode lain diterapkan untuk mengamankan aplikasi.
  
4. Alasan Pembersihan Data Input di Backend: Pembersihan data di backend tetap diperlukan karena:
* Keamanan: Validasi di frontend dapat dengan mudah diabaikan oleh pengguna yang mengakses API secara langsung, atau yang memanipulasi data menggunakan alat seperti Postman atau DevTools browser. Validasi di backend melindungi sistem dari data yang berbahaya seperti input yang mengandung script (XSS) atau SQL injection.
* Konsistensi: Validasi dan pembersihan di backend memastikan data yang masuk ke dalam sistem selalu berada dalam format yang benar, terlepas dari apakah pengguna mematuhi validasi di frontend atau tidak.
* Kontrol yang lebih mendalam: Backend memiliki kontrol penuh terhadap bagaimana data diproses dan disimpan. Pembersihan data di backend memungkinkan pengembang untuk melakukan validasi yang lebih kompleks, yang mungkin sulit atau tidak aman dilakukan di frontend. Jadi, meskipun validasi di frontend berguna untuk memberikan umpan balik cepat kepada pengguna, backend tetap menjadi lapisan perlindungan terakhir.

5. Yang pertama saya menambahkan function untuk menambahkan product dengan AJAX yang diletakkan di views.py, lalu saya tambahkan routing di urls.py agar add product by ajax dapat terakses, kemudian buat beberapa kode di bagian script di main.html agar page dapat refresh secara asinkronus, dan membuat form untuk menambahkan product by ajax


   
