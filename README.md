
**Nama : Febryvia Deya Nur Havidtar Murti Aqsa**

**NIM : 312510194**

**Kelas : TI.25.A.2**

**Mata Kuliah : Pengantar Pemrograman**

**TUGAS UAS**

**MODULAR DAN OOP**

#*Tujuan*
Program ini merupakan program sederhana pendataan pengunjung yang dibuat untuk memenuhi tugas UAS mata kuliah Pengantar Pemrograman. Program menerapkan konsep pemrograman modular dan _Object Oriented Programming_ atau OOP, program memungkinkan pengguna untuk :

-	Menginput data pengunjung

-	Melakukan validasi input menggunakan exception (ValueError)

-	Menyimpan data pengunjung

-	Menampilkan data pengunjung dalam bentuk tabel

Program ini digunakan untuk mencatat data pengunjung berupa nama, umur, jenis  kelamin, dan tujuan pengunjung.

#Konsep yang digunakan adalah

1.	Pemrograman Modular

Program yang dibagi menjadi beberapa bagian (class) sesuai dengan fungsi masing-masing agar kode lebih terstruktur, mudah dibaca, dan mudah dikembangkan.

2.	Object Oriented Programming (OOP)

Konsep OOP menerapkan dengan menggunakan class dan object, setiap class memiliki tanggung jawab yang berbeda.

#Class yang digunakan:

1.	Class Data

2.	Class Process

3.	Class View

4.	Program utama / main

#Fungsi Class :

1.	Class Data
Class ini berfungsi sebagai penyimpanan data pengunjung, didalam class terdapat data yang disimpan berupa:

_Nama, umur, jenis  kelamin, tujuan_

-	Pada class ini terdapat method (__init__) berfungsi untuk menyimpan data awal saat object dibuat

-	Penggunaan keyword self bertujuan agar setiap data yang dimasukkan tersimpan didalam object masing-masing

Class ini tidak melakukan proses logika dan validasi hanya menyimpan data

Hasil : <img width="1434" height="743" alt="Screenshot 2026-01-09 200750" src="https://github.com/user-attachments/assets/0d1f6c09-02c9-4048-b856-87613205bddf" />


2.	Class Process

Class ini berfungsi untuk melakukan validasi terhadap data input dari pengguna sebelum data disimpan.

Validasi yang dilakukan meliputi:

-	Nama tidak boleh kosong

-	Umur harus berupa angka dan bernilai positif

-	Jenis kelamin harus sesuai ketentuan

-	Tujuan kunjungan tidak boleh kosong

Contohnya, umur harus berupa angka dan tidak boleh bernilai nol atau negative

Claass ini menggunakan exception (ValueError) untuk menangani kesalahan input sehingga program dapat tetap berjalan meskipun kesalahan input dari pengguna

Hasil : <img width="1494" height="906" alt="Screenshot 2026-01-09 172052" src="https://github.com/user-attachments/assets/91847005-baa8-4e49-b5af-7e0c3452469b" />


3.	Class View
Class ini berfungsi untuk menangani interaksi dengan pengguna yaitu :

-	Menerima input data pengunjung

-	Menampilkan data pengunjung dalam bentuk tabel

Class view tidak melakukan proses logika atau validasi agar pemisahan tugas antar class tetap jelas

Hasil : <img width="1471" height="864" alt="Screenshot 2026-01-09 173937" src="https://github.com/user-attachments/assets/01a61ea1-7c59-4828-87d8-99f71e94d409" />

4.	Program Utama (main)

Program utama berfungsi untuk menghubungkan seluruh class yang telah dibuat. Pada bagian ini, object dari setiap class dibuat dan digunakan untuk menjalankan alur program secara menyeluruh

Program akan:

-	Meminta pengguna memasukkan data pengunjung

-	Melakukan validasi data melalui process

-	Menyimpan data pengunjung ke dalam list

-	Menanyakan apakah pengguna ingin menambahkan data lagi

-	Menampilkan seluruh data pengunjung dalam bentuk tabel

Hasil : <img width="1530" height="624" alt="Screenshot 2026-01-09 203743" src="https://github.com/user-attachments/assets/208e73fc-c367-452c-97c3-96ffab117fd3" />

**Alur Program**

1.	Program dimulai

2.	Pengguna mengimput data pengunjung

3.	Data validasi oleh class process

4.	Jika data valid, data disimpan ke dalam list

5.	Jika data tidak valid, program menampilkan pesan error

6.	Pengguna dapat menginputkan data kembali

7.	 Data pengunjung ditampilkan dalalm bentuk tabel

8.	Program selesai

Flowchartnya

```
       +----------------+
       |      Start      |
       +----------------+
               |
               v
   +----------------------+
   | Inisialisasi variabel|
   | daftar_pengunjung    |
   | process & view       |
   +----------------------+
               |
               v
       +----------------+
       |  Input Data    |
       | nama, umur,    |
       | jk, tujuan     |
       +----------------+
               |
               v
       +----------------+
       | Validasi Data  |
       +----------------+
         |          |
      Error?       Ok
       |           |
       v           v
   +--------+   +----------------+
   |Tampil  |   | Buat Object    |
   |Pesan   |   | Pengunjung     |
   |Error   |   | & simpan ke    |
   +--------+   | daftar         |
                +----------------+
                        |
                        v
                +----------------+
                | Lanjut Input?  |
                | (l/p)          |
                +----------------+
                  |         |
                 l|         |p
                  v         v
            +-----------+   +------+
            | Kembali ke|   |Tampil|
            | Input     |   |Tabel |
            +-----------+   +------+
                                |
                                v
                           +--------+
                           |  End   |
                           +--------+
```

**Kesimpulan:**

Dengan penerapan konsep pemrograman modular dan Object Oriented Programming (OOP), program pendataan pengunjung ini menjadi lebih terstruktur, mudah dipahami, dan mudah dikembangkan. Pemisahan antara class data, process, view, dan program utama membuat setiap bagian program memiliki tanggung jawab yang jelas.

Program ini telah memenuhi seluruh ketentuan tugas UAS yaitu menggunakan konsep OOP dan modular, meminta input dari pengguna, melakukan validasi input menggunakan exception (Value Error) serta menampilkan output dalam tabel.

**Link Youtubbe** = https://youtu.be/KBIDbEcQR-w?si=bQqw0znckYPWliK_
