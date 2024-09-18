![WhatsApp Image 2024-09-18 at 08 51 33_412fc302](https://github.com/user-attachments/assets/f603af0d-8199-47af-b18f-75ab7845c4c3)![WhatsApp Image 2024-09-18 at 08 52 06_89c09b4b](https://github.com/user-attachments/assets/1e74e857-a491-4bc5-a455-1a1670236f32)![WhatsApp Image 2024-09-18 at 08 50 44_c6da6957](https://github.com/user-attachments/assets/2fbbc854-edad-468d-a634-50ab2a0a979a)1. Cara saya mengimplementasikan checklist di atas tentu saja kebanyakan dengan bantuan tutorial yang ada. Seperti yang sudah ada dalam tutorial 0, saya membuat projek baru django. awalnya saya tidak langsung membuat new repo di git, melainkan saya membuat di local terlebih dahulu. pada permulaan saya mengaktifkan env terlebih dahulu dalam direktori lokal saya kemudian membuat requirements dan instalasi dependencies dan terbuat lah projek django baru sesuai keinginan saya. lalu saya konfigurasi proyek dan run server dan menambahkan file .gitignore . kemudian saya membuat aplikasi main dalam proyek lalu membuat template dan mengisi direktori template dengan file html yang berisi nama app, nama diri, dan nama kelas. lalu membuat function dalam views.py yang berisi nama app, nama diri, dan nama kelas yang sudah diassign sesuai keinginan saya untuk nantinya ditampilkan pada html. lalu membuat urls.py pada main untuk memetakan function yang telah dibuat pada views.py. lalu saya deploy ke pws, tetapi masih terjadi failed. kemudian saya baru membuat sebuah repo baru dalam git saya yang berisi file ecommerce saya tadi dan membuat readme yang berisi pertanyaan pertanyaan dalam tugas
   
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

6. ![WhatsApp Image 2024-09-18 at 08 50 44_ee453bd6](https://github.com/user-attachments/assets/d9aa4a96-ef88-4582-a4ac-6cc64b1d099d)
   ![Uploading WhatsApp Im![WhatsApp Image 2024-09-18 at 08 51 33_412fc302](https://github.com/user-attachments/assets/34ad863e-a1fe-4a1b-b77c-7dc6d8f08b4e)
![WhatsApp Image 2024-09-18 at 08 52 06_89c09b4b](https://github.com/user-attachments/assets/b9c63137-5dd2-47a6-88f2-c1edcf80c57e)
![WhatsApp Image 2024-09-18 at 08 51 06_ae253954](https://github.com/user-attachments/assets/93c08305-7980-4899-b1ae-31a015d13e96)
![WhatsApp Image 2024-09-18 at 08 51 06_ae253954](https://github.com/user-attachments/assets/d4ddfa9b-4f97-4d8b-9efe-0cfa6bfbe751)
age 2024-09-18 at 08.51.33_412fc302.jpg…]()


   
