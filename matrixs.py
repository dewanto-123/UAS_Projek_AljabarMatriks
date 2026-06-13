import dewa025


A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

B = [
    [2, 1, 0],
    [3, 4, 1],
    [5, 2, 2]
]


print("Matriks A:")
dewa025.tampilkan_matriks(A)

print("\nMatriks B:")
dewa025.tampilkan_matriks(B)

print("\nHasil Penjumlahan A + B:")
dewa025.tampilkan_matriks(dewa025.tambah_matriks(A, B))

print("\nHasil Pengurangan A - B:")
dewa025.tampilkan_matriks(dewa025.kurang_matriks(A, B))

print("\nHasil Perkalian A x B:")
dewa025.tampilkan_matriks(dewa025.kali_matriks(A, B))

print("\nTranspose Matriks A:")
dewa025.tampilkan_matriks(dewa025.transpose(A))

print("\nDeterminan Matriks A:")
print(dewa025.determinan(A))

print("\nKofaktor Matriks A:")
dewa025.tampilkan_matriks(dewa025.kofaktor_matriks(A))

print("\nAdjoin Matriks A:")
dewa025.tampilkan_matriks(dewa025.adjoin_matriks(A))

print("\nInvers Matriks A:")
dewa025.tampilkan_matriks(dewa025.invers_matriks(A))
