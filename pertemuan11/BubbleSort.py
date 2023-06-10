import os
os.system('cls')


# sort Tertinggi
def bubbleSort_tertinggi(listTertinggi):
    n = len(listTertinggi)  # jumlah list Tertinggi
    for i in range(n):  # perulangan pertama
        for j in range(n - i - 1):  # perulangan kedua
            if listTertinggi[j][2] < listTertinggi[j + 1][2]:  # jika lebih besar, tukar
                listTertinggi[j], listTertinggi[j +
                                                1] = listTertinggi[j + 1], listTertinggi[j]
    return listTertinggi


# sort Terendah
def bubbleSort_terendah(listTerendah):
    n = len(listTerendah)  # jumlah list Terendah
    for i in range(n):  # perulangan pertama
        for j in range(n - i - 1):  # perulangan kedua
            if listTerendah[j][2] > listTerendah[j + 1][2]:  # jika lebih kecil, tukar
                listTerendah[j], listTerendah[j +
                                              1] = listTerendah[j + 1], listTerendah[j]
    return listTerendah


dataMhs = []  # list data mahasiswa
dataMhsTertinggi = []
dataMhsTerendah = []
print(50*'-')
print("Nama : Alfanoel Audrey")
print("NIM  : 411221162")
print(50*'-')
print("\t  SORT [ASC/DESC] NILAI MAHASISWA")
print(50*'-')
while True:
    nim = input("Masukkan NIM \t\t: ")
    nama = input("Masukkan Nama \t\t: ").upper()
    nilaiAkhir = float(input("Masukkan Nilai Akhir \t: "))
    isiData = input("Isi data lagi? [Y/N] \t: ").lower()
    print(50*'-')
    dataMhsTertinggi.append([nim, nama, nilaiAkhir])
    dataMhsTerendah.append([nim, nama, nilaiAkhir])
    if isiData == "n":
        break


os.system('cls')

nTertinggi = bubbleSort_tertinggi(dataMhsTertinggi)
nTerendah = bubbleSort_terendah(dataMhsTerendah)

while True:
    pilih = input("Pilih [1:TERBESAR/2:TERKECIL]: ")
    print(50*'-')
    if pilih == "1":
        print("Data Mahasiswa (Nilai Tertinggi)")
        for data in nTertinggi:
            print(50*'-')
            print(f"NIM \t\t: {data[0]}")
            print(f"NAMA \t\t: {data[1]}")
            print(f"NILAI AKHIR \t: {data[2]}")
            print(50*'-')

    elif pilih == "2":
        print("Data Mahasiswa (Nilai Terendah)")
        for data in nTerendah:
            print(50*'-')
            print(f"NIM \t\t: {data[0]}")
            print(f"NAMA \t\t: {data[1]}")
            print(f"NILAI AKHIR \t: {data[2]}")
            print(50*'-')
    else:
        break
