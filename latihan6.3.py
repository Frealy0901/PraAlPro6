# Mendefinisikan
def deret(tinggi, lebar):
    a = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(a, end=" ")
            a += 1
        print()

# Meminta Input Pengguna
tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

# Menampilkan deret sesuai dengan input pengguna
deret(tinggi, lebar)
