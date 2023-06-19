import os
os.system('cls')

def cariKata(kata, teks):
  kataX = []
  kataSplit = teks.split()
  
  for kataTeks in kataSplit:
    if kata.lower() in kataTeks.lower():
      kataX.append(kataTeks)
  return kataX

while True:
  print(50*'-')
  teks = input("Masukkan teks: ")
  kata = input("Masukkan kata atau huruf yang ingin dicari: ")
  dataCek = teks + kata
  if teks.isdigit() == True or kata.isdigit() == True:
    print(50*'-')
    print("Teks dan Kata bukan huruf")
    continue
  else:
    print(50*'-')
    print(f"Teks : {teks}")
    print(f"Kata : {kata}")

    hasil = cariKata(kata, teks)

    if hasil:
      for kataX in hasil:
        print(50*'-')
        print(f"Kata yang ditemukan : {kataX}")
        continue
    else:
      print(50*'-')
      print("Kata tidak ditemukan.")
      print(50*'-')
      lanjut = input("Lanjut? [Y/N]: ")
      if lanjut == "y":
        continue
      elif lanjut == "n":
        break