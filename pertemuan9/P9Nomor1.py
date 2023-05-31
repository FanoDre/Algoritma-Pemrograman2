# luas = sisi * sisi
# volume = panjang * lebar * tinggi
print()
print(60*"=")
print("Nama : Alfanoel Audrey")
print("NIM  : 411221162")
print(60*"-")


class luasPersegi:

    panjang = 5
    lebar = 10
    tinggi = 10

    def hitungLuas(panjang, lebar):
        luas = panjang * lebar
        print("Hitung Luas :")
        print(f"Luasnya adalah {luas}cm")

    def hitungVolume(panjang, lebar, tinggi):
        volume = panjang * lebar * tinggi
        print(60*"-")
        print("Hitung Volume :")
        print(f"Volumenya adalah {volume}cm3")
        print(60*"=")

    hitungLuas(panjang, lebar)
    hitungVolume(panjang, lebar, tinggi)
    print()
