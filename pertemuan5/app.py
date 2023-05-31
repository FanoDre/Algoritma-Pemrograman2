import os

os.system('cls')

# -----------------------------------------------
print(50*"-")
print(f"{'TUGAS PERTEMUAN 4':>33}")
print(50*"-")
# -----------------------------------------------
print("Nomor 1")
x = 1
if x > 0:
    print("Nilai %x adalah besar dari 0" % x)
print(50*"-")
# -----------------------------------------------
print("Nomor 2")
nilai = 3
if (nilai > 7):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")
print(50*"-")
# -----------------------------------------------
print("Nomor 3")
number = 5
if number < 0:
    print("Negative")
else:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
print(50*"-")
# -----------------------------------------------
print("Nomor 4")
a = 5
if (a > 2) and ((a == 3) or (a < 7)):
    print("Hallo")
print(50*"-")
# -----------------------------------------------
print("Nomor 5")
n = eval(input("Enter a number: "))
if n / 2 == 0:
    print("The Number is an even number.")
else:
    print("The Number is an odd number.")
print(50*"-")
# -----------------------------------------------
print("Nomor 6")
major = "Business Statistics"
if major == "Business Statistics" or "Computer Science":
    print("Yes")
print(50*"-")
# -----------------------------------------------
print("Nomor 7")
numbers = 6
if numbers > 5 and numbers < 9:
    print("Yes")
else:
    print("No")
print(50*"-")
# -----------------------------------------------
print("Nomor 8")
angka = int(input("Enter a number: "))
if (angka != 7):
    print("Bukan Tujuh")
else:
    print("Tujuh")
print(50*"-")
# -----------------------------------------------
print("Nomor 9")
age = int(input("Enter your age: "))
if age >= 25:
    print("Anda Sudah Dewasa")
elif age >= 17 and age <= 25:
    print("Anda masih Remaja")
print(50*"-")
# -----------------------------------------------
print("Nomor 10")
standar_gaji = 3500000
gaji = int(input("Masukan Gaji anda: "))
status = input("Masukan Status anda? [Lajang/Berkeluarga]: ").lower()
status_rumah = input(
    "Masukan Status Rumah anda? [Kontrak/Pribadi]: ").lower()
if gaji >= standar_gaji and status == "berkeluarga" and status_rumah == "pribadi":
    print("Anda Harus Membayar Pajak")
else:
    print("Anda Tidak Harus Membayar Pajak")
print(50*"-")
# -----------------------------------------------
