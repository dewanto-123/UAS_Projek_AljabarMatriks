def cek_matriks_3x3(M):
    if len(M) != 3:
        raise ValueError("Matriks harus memiliki 3 baris.")

    for baris in M:
        if len(baris) != 3:
            raise ValueError("Setiap baris harus memiliki 3 kolom.")

    return True


def tampilkan_matriks(M):
    cek_matriks_3x3(M)

    for baris in M:
        print(baris)


def tambah_matriks(A, B):
    cek_matriks_3x3(A)
    cek_matriks_3x3(B)

    hasil = []

    for i in range(3):
        baris_hasil = []
        for j in range(3):
            baris_hasil.append(A[i][j] + B[i][j])
        hasil.append(baris_hasil)

    return hasil


def kurang_matriks(A, B):
    cek_matriks_3x3(A)
    cek_matriks_3x3(B)

    hasil = []

    for i in range(3):
        baris_hasil = []
        for j in range(3):
            baris_hasil.append(A[i][j] - B[i][j])
        hasil.append(baris_hasil)

    return hasil


def kali_matriks(A, B):
    cek_matriks_3x3(A)
    cek_matriks_3x3(B)

    hasil = []

    for i in range(3):
        baris_hasil = []
        for j in range(3):
            total = 0
            for k in range(3):
                total = total + (A[i][k] * B[k][j])
            baris_hasil.append(total)
        hasil.append(baris_hasil)

    return hasil


def transpose(M):
    cek_matriks_3x3(M)

    hasil = []

    for i in range(3):
        baris_hasil = []
        for j in range(3):
            baris_hasil.append(M[j][i])
        hasil.append(baris_hasil)

    return hasil


def determinan(M):
    cek_matriks_3x3(M)

    a = M[0][0]
    b = M[0][1]
    c = M[0][2]

    d = M[1][0]
    e = M[1][1]
    f = M[1][2]

    g = M[2][0]
    h = M[2][1]
    i = M[2][2]

    det = (
        a * ((e * i) - (f * h))
        - b * ((d * i) - (f * g))
        + c * ((d * h) - (e * g))
    )

    return det


def kofaktor_matriks(M):
    cek_matriks_3x3(M)

    a = M[0][0]
    b = M[0][1]
    c = M[0][2]

    d = M[1][0]
    e = M[1][1]
    f = M[1][2]

    g = M[2][0]
    h = M[2][1]
    i = M[2][2]

    kofaktor = [
        [
            (e * i) - (f * h),
            -((d * i) - (f * g)),
            (d * h) - (e * g)
        ],
        [
            -((b * i) - (c * h)),
            (a * i) - (c * g),
            -((a * h) - (b * g))
        ],
        [
            (b * f) - (c * e),
            -((a * f) - (c * d)),
            (a * e) - (b * d)
        ]
    ]

    return kofaktor


def adjoin_matriks(M):
    cek_matriks_3x3(M)

    kofaktor = kofaktor_matriks(M)
    adjoin = transpose(kofaktor)

    return adjoin


def invers_matriks(M):
    cek_matriks_3x3(M)

    det = determinan(M)

    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinannya 0.")

    adj = adjoin_matriks(M)

    hasil = []

    for i in range(3):
        baris_hasil = []
        for j in range(3):
            baris_hasil.append(adj[i][j] / det)
        hasil.append(baris_hasil)

    return hasil


