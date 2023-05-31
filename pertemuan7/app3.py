import os
os.system('cls')
# -----------------------------------------------
print(54*"-")
print(f"{'TUGAS PERTEMUAN 4':>35}")
print(54*"-")
# -----------------------------------------------


def tambah_kurang_bagi_kali():
    angka1 = input("Masukan Angka ke-1: ")
    math = input("[ + | - | / | x ]: ")
    angka2 = input("Masukan Angka ke-2: ")
    total = 0
    if angka1.isdigit() and angka2.isdigit():
        angka1 = int(angka1)
        angka2 = int(angka2)
    else:
        print("Please enter a number.")
        tambah_kurang_bagi_kali()

    if math.isdigit():
        print("Masukan [ + | - | / | x ] bukan angka.")
        tambah_kurang_bagi_kali()
    elif math == "+":
        total = angka1 + angka2
    elif math == "-":
        total = angka1 - angka2
    elif math == "/":
        total = angka1 / angka2
    elif math == "x":
        total = angka1 * angka2
    else:
        print("Masukan [ + | - | / | x ] bukan string/character.")
        tambah_kurang_bagi_kali()

    print(f"{angka1} {math} {angka2} = {total}")

    return angka1, angka2, math, total


tambah_kurang_bagi_kali()


def lanjut():
    lanjut = input("Lanjut? [Y/N]: ").lower()
    if lanjut == "y":
        tambah_kurang_bagi_kali()
    elif lanjut == "n":
        print("Terima Kasih")
    else:
        print("Perintah Tidak Ditemukan.")
        lanjut()


lanjut()
