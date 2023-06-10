import os
os.system('cls')


# sort Tertinggi
def bubbleSort_tertinggi(float(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


dataMhs = []
while True:
    nim = input("Masukkan NIM: ")
    if nim == "0":
        break
    nama = input("Masukkan Nama: ").upper()
    nilaiAkhir = float(input("Masukkan Nilai Akhir: "))
    # isiData = input("Isi data lagi? [Y/N]: ").lower()
    # print(50*'-')
    # if isiData == "n":
    #     break
    dataMhs.append([nim, nama, nilaiAkhir])

for nim, nama, nilaiAkhir in dataMhs:
    print(f"NIM: {nim}, NAMA: {nama}, NILAI AKHIR: {nilaiAkhir}")
