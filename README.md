#Documentasi Tugas Django Auth
##HAK AKSES
###1. Yang bisa di akses oleh admin yang is_superuser:
  - localhost:8000/dashboard            -> untuk Dashboard admin
  - localhost:8000/about_admin          -> untuk melihat konten about pada dashboard admin
  - localhost:8000/about_edit           -> untuk mengedit konten about yang taggal postnya akan menyesuaikan hari itu
  - localhost:8000/upload_gambar        -> untuk mengupload gambar pada page portfolio
  - localhost:8000/about_detail         -> untuk melihat frontpage about detail  
  - localhost:8000/about_komentar       -> untuk memberi komentar di kolom komentar pada page about_detail
  - localhost:8000/about_create         -> untuk Mengisi konten pada about, apabila konten masih kosong dan ini hanya bisa untuk 1 konten saja

###2. Yang bisa di akses member yang sudah login namun bukan is_superuser:
  - localhost:8000/about_komentar       -> untuk memberi komentar di kolom komentar pada page about_detail
  - localhost:8000/logout               -> untuk Logout
  - localhost:8000/about_detail         -> untuk melihat frontpage about detail  

###3. Yang bisa di akses semua user tanpa login :
  - localhost:8000/register             -> Untuk mendaftar bisa sebagai member biasa atau admin, apabila admin kolom checkbox harus di check, dan memiliki hak akses seperti pada point2 di nomor 1
  - localhost:8000/login                -> Untuk login user
  - localhost:8000/portfolio            -> melihat portfolio
  - localhost:8000/about                -> melihat about
  - localhost:8000/about_detail         -> melihat detail about

##MYSQL CONFIGURATION:
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'django_auth',
  'HOST': '127.0.0.1',
  'USER': 'root',
  'PASSWORD': '',

##EXPORT DATABASE
Jika export data dari databse saya di file 'django_auth.sql', maka sudah ada 2 user:

1. User sebagai admin yang bisa mengakses fitur2 admin
  - username : admin
  - password : password123

2. User sebagai Member yang bisa mengakses fitur2 Member
  - username : member
  - password : password123
