import os
os.system('cls')

print(50*'-')
print("Nilai Mata Kuliah Algoritma & Pemrograman 2")
print(50*'-')

dataMhs = []

while True:
    nim = input("Masukkan NIM \t: ")
    name = input("Masukkan Nama \t: ")
    nilaiAkhir = float(input("Masukkan Nilai Akhir : "))
    isiData = input("Masukkan data lagi? [Y/N]: ").lower()
    print(50*'-')
    if isiData == "n":
        break
    dataMhs.append((nim, name, nilaiAkhir))


def dataTerendah():
    print(50*'-')
    nilaiTerendah = sorted(dataMhs, key=lambda x: x[2])
    print("Nilai Mahasiswa Terendah -> Tertinggi")
    for nim, name, nilaiAkhir in nilaiTerendah:
        print(f"""
          NIM \t\t: {nim}
          Nama \t\t: {name}
          Nilai Akhir : {nilaiAkhir}
          """)
    print(50*'-')


def dataTertinggi():
    print(50*'-')
    nilaiTertinggi = sorted(dataMhs, key=lambda x: x[2], reverse=True)
    print("Nilai Mahasiswa Tertinggi -> Terendah")
    for nim, name, nilaiAkhir in nilaiTertinggi:
        print(f"""    
          NIM \t\t: {nim}
          Nama \t\t: {name}
          Nilai Akhir : {nilaiAkhir}
          """)
    print(50*'-')


dataTertinggi()
dataTerendah()
