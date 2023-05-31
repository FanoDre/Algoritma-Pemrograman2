import os
os.system('cls')
# -----------------------------------------------
print(54*"-")
print(f"{'TUGAS PERTEMUAN 7':>36}")
print(54*"-")
# -----------------------------------------------
print(f"{'APLIKASI CEK PLAT NOMOR GANJIL/GENAP':>46}")
print(54*"-")


def cekTgl():
    while True:
        tanggal = input("Masukan Tanggal: ")
        if tanggal.isdigit():
            tanggal = int(tanggal)
        else:
            print("Tolong Masukan Tanggal.")
            cekTgl()
            break

        if tanggal % 2 != 0:
            print(f"Tanggal {tanggal} adalah Ganjil")
        else:
            print(f"Tanggal {tanggal} adalah Genap")

    return tanggal


cekTgl()
