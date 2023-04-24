
# LANGKAH NSTALASI
-------------------------------------------------------
buka aplikasi visual studio code
buka terminal dengan : ctrl + j
turun folder terlebih dahulu dengan : cd ..
aktivkan env dengan : .\env\Scripts\activate (pastikan sudah membuat env terlebih dahulu)
masuk folder project dengan: cd .\PENGADILAN\PEGAWAI>
install kebutuhan dengan: pip -r requirement.txt
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

## Inventasi
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
=======
# PJ_PENGADILAN
1. pastika python sudah terinstall
2. download/clone project dengan git
3. masuk ke folder project dengan : cd pj_pengadilan/sidang
4. buat virtual env dengan : python -m venv env
5. aktifkan env dengan : env\scripts\activate
6. install django dengan : pip install django 
7. install jazzmin dengan : pip install -U django-jazzmin
8. jalankan server dengan: python manage.py runserver

- untuk login sebagai admin gunakan akun username = admin dan password = admin123
- untuk melihat data user sementara gunakan user1 | pengguna1
