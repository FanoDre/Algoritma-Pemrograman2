import os
os.system('cls')

# ---------------------------------------------------
print(30*'-')
print("Nama \t: Alfanoel Audrey")
print("NIM \t: 411221162")
print(30*'-')

# Global --------------------------------------------
pecahan = [50000, 20000, 10000, 5000, 2000, 1000]
# ---------------------------------------------------

# Fungsi dengan Argumen -----------------------------
def cekPecahan(totalUang):
    # Lokal -----------------------------------------
    totalUang = int(totalUang)
    for x in pecahan:
        count = 0
        while totalUang >= x:
            count += 1
            totalUang -= x
        print(f"{'Jumlah Pecahan'} {x}: {count}")
    # -----------------------------------------------
    # Mengembalikan nilai totalUang
    return totalUang, x, count

# Argumen totalUang dalam fungsi berubah jadi inputUser
inputUser = int(input("Masukkan Jumlah Uang: "))
cekPecahan(inputUser)
# --------------------------------------------------
print(30*'-')
print()


        