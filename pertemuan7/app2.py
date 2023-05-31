import os
os.system('cls')
# -----------------------------------------------
print(54*"-")
print(f"{'TUGAS PERTEMUAN 4':>35}")
print(54*"-")
# -----------------------------------------------

# Array
fakultas = ['Fakultas Teknik',
            'Fakultas Bisnis dan Ilmu Sosial']

jurusanTeknik = ['Teknik Informatika',
                 'Teknik Elektro',
                 'Teknik Sipil',
                 'Teknik Mesin']

jurusanFbis = ['Manajemen',
               'Akuntansi',
               'Bahasa Inggris',
               'Ilmu Komunikasi']

daftarKelas = ['Reguler 1',
               'Reguler 2']

priceJurusanteknik = [4900000,
                      4600000,
                      4800000,
                      4700000]

priceJurusanfbis = [4200000,
                    4150000,
                    4100000,
                    4250000]

priceKelas = [0,
              700000]

lstFakul = []
lstJurusan = []
lstKelas = []
# ---------------------------

print(f"{'FORMULIR PENDAFTARAN MAHASISWA BARU':>45}")
print(f"{'UNIVERSITAS BEYEGE':>36}")
print(54*'-')

print("[+]Silahkan Lengkapi Data dibawah ini: ")
nisn = input("Masukan NISN \t\t: ")
name = input("Masukan Nama Lengkap \t: ")
noHp = input("Masukan No. Hp \t\t: ")
alamat = input("Masukan Alamat Lengkap \t: ")

print(54*'-')
print("[+]Daftar Fakultas di Universitas BEYEGE:")
print(54*'-')

for x in range(len(fakultas)):
    print(f"\t{x+1}. {fakultas[x]}")
pilihFakul = int(input("Pilih Fakultas \t: "))
itemFakul = {'fakul': fakultas[pilihFakul - 1]}

print(54*'-')
print(f"[+]Daftar Jurusan di {itemFakul['fakul']}")
print(54*'-')

if pilihFakul == 1:
    for x in range(len(jurusanTeknik)):
        print(f"\t{x+1}. {jurusanTeknik[x]} {priceJurusanteknik[x]}")
    pilihJurusan = int(input("Pilih Jurusan : "))
    print(54*'-')
    itemJurusan = {'jurusan': jurusanTeknik[pilihJurusan - 1],
                   'price': priceJurusanteknik[pilihJurusan - 1]}
elif pilihFakul == 2:
    for x in range(len(jurusanFbis)):
        print(f"\t{x+1}. {jurusanFbis[x]} {priceJurusanfbis[x]}")
    pilihJurusan = int(input("Pilih Jurusan : "))
    itemJurusan = {
        'jurusan': jurusanFbis[pilihJurusan - 1], 'price': priceJurusanfbis[pilihJurusan - 1]}
else:
    print("Pilihan Tidak Ada!")

priceJurusan = itemJurusan['price']

print("[+]Daftar Kelas")
print(54*'-')

for x in range(len(daftarKelas)):
    print(f"\t{x+1}. {daftarKelas[x]} {priceKelas[x]}")
kelas = int(input("Pilih Kelas : "))
itemKelas = {'kelas': daftarKelas[kelas - 1], 'price': priceKelas[kelas - 1]}
hargaKelas = itemKelas['price']

totalBiaya = priceJurusan + hargaKelas
print(54*'-')

os.system('cls')

print(54*'-')
print(f"{'DATA FORMULIR PENDAFTARAN MAHASISWA BARU':>48}")
print(54*'-')
print(f"Nomor Induk Siswa Nasional \t: {nisn}".upper())
print(f"Nama Lengkap \t\t\t: {name}".upper())
print(f"Nomor Handphone \t\t: {noHp}".upper())
print(f"Alamat Lengkap \t\t\t: {alamat}".upper())
print(f"Fakultas \t\t\t: {itemFakul['fakul']}".upper())
print(f"Jurusan \t\t\t: {itemJurusan['jurusan']}".upper())
print(f"Kelas \t\t\t\t: {itemKelas['kelas']} ".upper())
print(54*'-')
print("\tInvoice")
print(54*'-')
print(f"\tBiaya Jurusan \t: " "Rp.{:,.2f}".format(priceJurusan))
print(f"\tBiaya Kelas \t: " "Rp.{:,.2f}".format(hargaKelas))
print(f"\tTotal Biaya \t: " "Rp.{:,.2f}".format(totalBiaya))
print(54*'-')
