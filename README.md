# 👩‍💻Tugas Bahasa Pemrograman2 Perkalian Matriks 5x5
Program ini dibuat untuk menyelesaikan tugas dari mata kuliah Bahasa Pemrograman 2. Program ini berisi logika untuk mengalikan dua buah matriks 5x5 dan menampilkan hasilnya.
## ⚒ Membuat Matriks 5x5 ⚒
    ``python
    A = []
    for i in range(5):
    baris = []
    for j in range(5):
    baris.append(nilai)
    A.append(baris)
    
Penjelasan :
-Membuat list kosong A
-Mengisi A dengan 5 baris
-Setiap baris diisi dengan 5 kolom mengguanakan append
## 🔗Perkalian Matriks
    for i in range(5):
    baris = []
    for j in range(5):
    total = 0
    for k in range(5):
    total += A[i][k] * B[k][j]
    baris.append(total)
    hasil.append(baris)
    
Penjelasan :
-Mengambil baris ke-i dari A dan kolom ke-j dari B
-Mengalikan elemen yang bersesuaian dan  menjumlahkan
-Hasil disimpan di matriks hasil pada posisi [i][j]
    
## 🔗Menampilkan Hasil
    print("Hasil perkalian matriks A dan B adalah:")
    for row in hasil:
    print(row)

Penjelasan :
Menampilkan output hasil perkalian matriks ke layar
## 🪄Output💫
    [13, 13, 13, 13, 13]
    [4, 15, 4, 15, 4]
    [12, 18, 12, 18, 12]
    [10, 15, 10, 15, 10]
    [8, 11, 8, 11, 8]
    
## 💗Author
Siti Aulia Rachmah
Nim : 3337240002
