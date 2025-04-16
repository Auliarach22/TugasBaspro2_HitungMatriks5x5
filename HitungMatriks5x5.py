# Matriks A (5x5)
A = [
    [4, 8, 2, 5, 7],
    [6, 1, 9, 3, 0],
    [2, 4, 6, 8, 10],
    [5, 3, 1, 7, 9],
    [7, 2, 0, 6, 4]
]

# Matriks B (5x5)
B = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

# Inisialisasi matriks hasil
hasil = []

# Perkalian matriks A x B
for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

# Menampilkan hasil
print("Hasil perkalian matriks A dan B adalah:")
for row in hasil:
    print(row)