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
    tanggal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
               17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    tglGenap = []
    tglGanjil = []
    for x in tanggal:
        if x % 2 != 0:
            tglGanjil.append(x)
        else:
            tglGenap.append(x)
    sortedTglGenap = sorted(tglGenap)
    sortedTglGanjil = sorted(tglGanjil)
    while True:
        tanggal = input("Masukan Tanggal: ")
        if tanggal.isdigit():
            tanggal = int(tanggal)
            if tanggal <= 0:
                print("Masukan angka yang lebih besar dari 0.")
                cekTgl()
        else:
            print("Tolong Masukan Tanggal.")
            cekTgl()

        if tanggal % 2 != 0:
            print(f"Tanggal {tanggal} adalah Ganjil")
            print(f"List Tanggal Ganjil ({sortedTglGanjil})")
        else:
            print(f"Tanggal {tanggal} adalah Genap")
            print(f"List Tanggal Ganjil ({sortedTglGenap})")
            break
        #
        return tanggal, sortedTglGenap, sortedTglGanjil


def cekPlat():
    while True:
        plat = input("Masukan Nopol anda? [4330/4331/4332/4333/4334]: ")

        if plat.isdigit():
            plat_akhir = int(plat[-1])
            if plat_akhir % 2 != 0:
                print(
                    f"Nopol anda ({plat}), Angka terakhir pada Nopol anda adalah ({plat_akhir}) Ganjil")
            else:
                print(
                    f"Nopol anda ({plat}), Angka terakhir pada Nopol anda adalah ({plat_akhir}) Genap")
        else:
            print("Tolong masukan angka.")
            cekPlat()
            break
        return plat, plat_akhir


cekPlat()


print(54*'-')
seeTgl = input(
    "Apakah anda ingin melihat pada tanggal berapa saja anda bisa lewat? [Y/N]: ").lower()

if seeTgl == "y":
    cekTgl()
elif seeTgl == "n":
    print("Terima Kasih")
    quit()
else:
    print("Bukan Pilihan.")


def nextOp():
    next = input("Lanjut? [Y/N]: ").lower()
    if next == "y":
        cekPlat()
        cekTgl()
        nextOp()
    elif next == "n":
        print("Terima Kasih")
        quit()
    else:
        print("Bukan Pilihan.")


nextOp()
