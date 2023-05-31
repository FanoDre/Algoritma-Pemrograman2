import os

os.system('cls')

# -----------------------------------------------
print(50*"-")
print(f"{'TUGAS PERTEMUAN 4':>33}")
print(50*"-")
# -----------------------------------------------
print(f"{'PT. DINGIN DAMAI':>33}")
print(50*"-")
gapok = 300000
name = input("Masukan Nama Lengkap: ").upper()
nrp = input("Masukan NRP: ")
golongan = input("Masukan Golongan [1/2/3]: ")
pendidikan = input("Masukan Pendidikan [SMA/D1/D3/S1]: ").upper()
# ----------------------------------------------
gol1 = 0.5*gapok
gol2 = 0.10*gapok
gol3 = 0.15*gapok
sma = 0.025*gapok
d1 = 0.5*gapok
d3 = 0.20*gapok
s1 = 0.30*gapok
# ----------------------------------------------
if golongan == "1":
    gajiGol = gol1
elif golongan == "2":
    gajiGol = gol2
elif golongan == "3":
    gajiGol = gol3
else:
    print("Data Tidak Ditemukan.")

if pendidikan == "SMA":
    gajiPend = sma
elif pendidikan == "D1":
    gajiPend = d1
elif pendidikan == "D3":
    gajiPend = d3
elif pendidikan == "S1":
    gajiPend = s1
else:
    print("Data Tidak Ditemukan.")

totalGaji = gajiGol + gajiPend + gapok
# pOut
print(50*'-')
print(f"{'SLIP GAJI':>30}")
print(50*'-')
print(f"NAMA LENGKAP \t\t: {name}")
print(f"NRP \t\t\t: {nrp}")
print(f"GOLONGAN \t\t: {golongan}")
print(f"PENDIDIKAN \t\t: {pendidikan}")
print("TUNJANGAN GOLONGAN \t:", "Rp.{:,.2f}".format(gajiGol))
print("TUNJANGAN PENDIDIKAN \t:", "Rp.{:,.2f}".format(gajiPend))
print("TOTAL GAJI \t\t:", "Rp.{:,.2f}".format(totalGaji))
print(50*'-')
print()
# --------------------------------------------------------------
