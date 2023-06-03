import os
os.system('cls')

# ---------------------------------------------------
print(30*'-')
print("Nama \t: Alfanoel Audrey")
print("NIM \t: 411221162")
print(30*'-')

# Global --------------------------------------------
pecahan = [5000, 100]
# ---------------------------------------------------

# Fungsi dengan Argumen -----------------------------
def cekPecahan(totalUang):
    # Lokal -----------------------------------------
    totalUang = int(totalUang)
    count1 = 1
    for x in pecahan:
        count2 = 0
        while totalUang >= x:
            count2 += 1
            totalUang -= x
            
    print(f"{'{'}{pecahan[0]}: {count1}, {pecahan[1]}: {count2}{'}'}")
    # -----------------------------------------------
    # Mengembalikan nilai totalUang
    return totalUang

# Argumen totalUang dalam fungsi berubah jadi inputUser
inputUser = int(input("Masukkan Jumlah Uang: "))
cekPecahan(inputUser)
# --------------------------------------------------
print(30*'-')
print()
        