import os
os.system('cls')
# -----------------------------------------------
print(54*"-")
print(f"{'TUGAS PERTEMUAN 7':>35}")
print(54*"-")
# -----------------------------------------------

# Array ------------------------
menuList = [
    'Pandan Latte',
    'Matcha',
    'Espresso',
    'Cuppocino',
    'Kopi Kenangan Mantan',
    'Kopi Kangen',
    'Kopi Enak'
]

priceList = [
    28000,
    29000,
    25000,
    25000,
    31000,
    26000,
    18000
]

isi = []
# -------------------------------
restartApp = "y"
while restartApp == "y":
    # printIn -------------------------------------------
    print()
    print(54*'=')
    print(f"{'WARUNG KOPI KITA':>35}")
    print(54*'-')
    print("Selamat Datang di Warung Kopi Kita😊")
    print("Silahkan isi data dibawah ini dulu yaaaa...")
    print(54*'-')
    name = input("[?]Masukan Nama: ").upper()
    print(54*'-')
    # ---------------------------------------------------

    # Lihat Menu -------------------------------------------------------------
    seeMenu = input(f"[?]Hallo {name}, Mau lihat menu kita? [Y/N] : ").lower()
    pesanLagi = "y"
    if seeMenu == "y":
        while pesanLagi == "y":
            # --------------------------------------------------
            print(54*'-')
            print("### DAFTAR MENU")
            print(54*'-')
            print(f"| {'#'} | {'MINUMAN':<22}|  {'HARGA':<22}|")
            print(54*'-')
            # --------------------------------------------------

            # for Lihat Menu -------------------------------------------------
            for x in range(len(menuList)):
                print(f"| {x+1} | {menuList[x]:<22}| Rp. {priceList[x]:<19}|")
            print(54*'-')
            # ----------------------------------------------------------------

            # Kode Menu ------------------------------------------
            menuCode = int(input("[+]Masukan Kode Menunya ya: "))
            if menuCode < 1 or menuCode > len(menuList):
                print("Maaf kode menu yang kamu masukan salah😢")
                break
            # ----------------------------------------------------

            # Mengumpulkan Item -----------------------
            items = {'menu': menuList[menuCode - 1],
                     'price': priceList[menuCode - 1]}
            isi.append(items)
            # -----------------------------------------

            pesanLagi = input("[+]Pesan Lagi? [Y/N] : ").lower()
            print()

            # show DAFTAR PESANAN --------------------------
            print(32*'-')
            print("### DAFTAR Pesanan")
            print(32*'-')
            print(f"| {'QTY'} | {'PESANAN':<22} |")
            print(32*'-')
            for x, items in enumerate(isi):
                print(f"|  {x+1}  | {items['menu']:<22} |")
            print(32*'-')
            # ----------------------------------------------

    # show Invoice ---------------------------------------------------
    if seeMenu == "n":
        print(54*'-')
        print("\tTERIMA KASIH :)")
        print(54*'-')

    if pesanLagi == "n":
        print(54*'-')
        print("\t\t    INVOICE BELANJA")
        print(54*'-')
        total = 0
        for x, items in enumerate(isi):
            print(f"{x+1}. {items['menu']:<22} Rp.{items['price']}")
            total += items['price']
        print(54*'-')
        print("Total: Rp. {:,.2f}".format(total))
        print(54*'-')
        cash = int(input("Masukan Uang: "))
        print(54*'-')
        change = cash - total
        print("Uang anda sebesar: Rp. {:,.2f}".format(cash))
        print("Kembalian: Rp. {:,.2f}".format(change))
        print(54*'-')
# ----------------------------------------------------------------
    break
restartApp = input("Lanjut? [Y/N]: ").lower()

if restartApp == "n":
    print(54*'-')
    print("\tTERIMA KASIH :)")
    print(54*'-')
    quit()
