import os
os.system('cls')

# List
nilai = [56,32,67,88,22,33,45,87]
nilaiX = [i for i in nilai]
print(68*'=')
print(f"Nilai \t\t\t\t: {nilaiX}")

nilai.sort()
print(f"Nilai terkecil adalah \t\t: {nilai[0]}")
print(f"Nilai terbesar adalah \t\t: {nilai[-1]}")
print(f"Urutan dari yang terkecil adalah: {nilai}")

nilai.sort(reverse=True)
print(f"Urutan dari yang terbesar adalah: {nilai}")
print(68*'=')