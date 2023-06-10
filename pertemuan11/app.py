# Membuat list kosong untuk menyimpan data mahasiswa
data_mahasiswa = []

# Mendapatkan input data mahasiswa dan nilai
while True:
    nim = input("Masukkan NIM mahasiswa (0 untuk menghentikan input): ")
    if nim == '0':
        break
    mahasiswa = input("Masukkan Nama Mahasiswa: ")
    nilai_akhir = float(input("Masukkan Nilai Akhir: "))

    # Menambahkan data mahasiswa ke dalam list
    data_mahasiswa.append((nim, mahasiswa, nilai_akhir))

# Mengurutkan data mahasiswa berdasarkan nilai tertinggi
data_mahasiswa_tertinggi = sorted(
    data_mahasiswa, key=lambda x: x[2], reverse=True)

# Mengurutkan data mahasiswa berdasarkan nilai terendah
data_mahasiswa_terendah = sorted(data_mahasiswa, key=lambda x: x[2])

# Menampilkan data mahasiswa yang telah diurutkan
print("Data Mahasiswa (Nilai Tertinggi):")
for nim, mahasiswa, nilai_akhir in data_mahasiswa_tertinggi:
    print(f"NIM: {nim}, Mahasiswa: {mahasiswa}, Nilai Akhir: {nilai_akhir}")

print("\nData Mahasiswa (Nilai Terendah):")
for nim, mahasiswa, nilai_akhir in data_mahasiswa_terendah:
    print(f"NIM: {nim}, Mahasiswa: {mahasiswa}, Nilai Akhir: {nilai_akhir}")
