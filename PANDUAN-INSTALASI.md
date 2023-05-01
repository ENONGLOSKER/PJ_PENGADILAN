LINK DOC PROGRAM : https://github.com/ENONGLOSKER/PJ_PENGADILAN/

# LANGKAH INSTALASI
-------------------------------------------------------
1. pastika python sudah terinstall
2. download/clone project dengan git
3. buat virtual env dengan : python -m venv env
4. aktifkan env dengan : env\scripts\activate
5. install django dengan : pip install django 
6. install jazzmin dengan : pip install -U django-jazzmin atau 
7. untuk menginstall semua kebutuhan bisa dengan: pip install -r requirements.txt
8. masuk ke folder project dengan : cd pj_pengadilan/sidang(sesuai nama projrct)
9. jalankan server dengan: python manage.py runserver

- menjalankan program

buka aplikasi visual studio code
buka terminal dengan : ctrl + j
turun folder terlebih dahulu dengan : cd ..
aktivkan env dengan : .\env\Scripts\activate (pastikan sudah membuat env terlebih dahulu)
masuk folder project dengan: cd .\PENGADILAN\PEGAWAI>
jalankan server dengan : python manage.py runserver

# TESTING
-------------------------------------------------------
## Kepegawaian
<!-- sebagai admin -->
username = admin
password = admin123

<!-- sebagai non admin -->
username = pegawai
password = pengguna2023

## Inventaris
<!-- super admin -->
user : admin
password : admin123

<!-- admin biasa -->
user : operator
password : operator123

## Absensi
<!-- sebagai admin -->
username = admin
password = admin123

<!-- sebagai non admin -->
username = pegawai
password = pegawai123

## Jadwal
<!-- sebagai admin -->
username = admin
password = admin123

<!-- sebagai non admin -->
username = pegawai
password = pegawai123

## Surat
<!-- sebagai admin -->
username = admin
password = admin123

<!-- sebagai non admin -->
username = pegawai
password = pegawai123

----------------------------------------------
