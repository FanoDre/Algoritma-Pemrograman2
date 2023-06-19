import os
os.system('cls')

def tambah(a,b):
  return a + b

def kurang(a,b):
  return a - b

def kali(a,b):
  return a * b

def bagi(a,b):
  return a / b

while True:
  try:
    print(50*'-')
    operator = input("Masukkan operator [+][-][*][/]: ")
    if operator.isdigit() == True:
      raise TypeError(f"Masukkan operator bukan angka ({operator})")
    elif operator.isalpha() == True:
      raise TypeError(f"Masukkan operator bukan huruf ({operator})")
    else:   
      angka1 = float(int(input("Masukkan angka pertama: ")))
      angka2 = float(int(input("Masukkan angka kedua: "))) 
      if operator == "+":
        total = tambah(angka1,angka2)
        print(f"Hasil: {int(angka1)} {operator} {int(angka2)} = {int(total)}")
      elif operator == "-":
        total = kurang(angka1,angka2)
        print(f"Hasil: {int(angka1)} {operator} {int(angka2)} = {int(total)}")
      elif operator == "*":
        total = kali(angka1,angka2)
        print(f"Hasil: {int(angka1)} {operator} {int(angka2)} = {int(total)}")
      elif operator == "/":
        total = bagi(angka1,angka2)
        print(f"Hasil: {float(angka1)} {operator} {float(angka2)} = {float(total)}")
  except ValueError:
    print(50*'-')
    print("Input harus bilangan!")
    continue
