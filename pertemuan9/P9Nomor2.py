print(60*"-")
print("Nama : Alfanoel Audrey")
print("NIM  : 411221162")
print(60*"-")


class penentuanMK:

    def aplikasiPenentu():
        mataKuliah = {
            'Pemrograman': {
                'perhitungan': 0,
                'menggambar': 0,
                'pemrograman': 1,
                'teknologi': 1,
                'praktek': 1,
                'teori': 0,
                'minat_khusus': 0
            },
            'Matematika': {
                'perhitungan': 1,
                'menggambar': 0,
                'pemrograman': 0,
                'teknologi': 0,
                'praktek': 1,
                'teori': 1,
                'minat_khusus': 0
            },
            'Seni Rupa': {
                'perhitungan': 0,
                'menggambar': 1,
                'pemrograman': 0,
                'teknologi': 0,
                'praktek': 1,
                'teori': 1,
                'minat_khusus': 1
            }
        }

        nilai1 = {}

        print(60*"=")
        print(60*"-")
        print("\t   Aplikasi Penentu Minat Mata Kuliah")
        print(60*"-")
        print("Jawablah Survey dibawah ini:")
        print(60*"-")

        perhitungan = input("[?]Apakah anda suka berhitungan? [Y/N]: ")
        menggambar = input("[?]Apakah anda suka menggambar? [Y/N]: ")
        pemrograman = input(
            "[?]Apakah anda suka sesuatu yang berhubungan dengan pemrograman? [Y/N]: ")
        teknologi = input(
            "[?]Apakah anda suka sesuatu yang berhubungan dengan teknologi? [Y/N]: ")
        praktek = input(
            "[?]Apakah anda suka mata kuliah yang sering praktek? [Y/N]: ")
        teori = input(
            "[?]Apakah anda suka mata kuliah yang punya banyak teori? [Y/N]: ")
        minat_khusus = input(
            "[?]Apakah anda memiliki minat khusus pada bidang tertentu? [Y/N]: ")

        if (perhitungan, menggambar, pemrograman, teknologi, praktek, teori, minat_khusus == "y"):
            perhitungan = 1
            menggambar = 1
            pemrograman = 1
            teknologi = 1
            praktek = 1
            teori = 1
            minat_khusus = 1

        elif (perhitungan, menggambar, pemrograman, teknologi, praktek, teori, minat_khusus == "n"):
            perhitungan = 0
            menggambar = 0
            pemrograman = 0
            teknologi = 0
            praktek = 0
            teori = 0
            minat_khusus = 0

        else:
            print("Kode Tidak Ditemukan!`")

        for x, attributes in mataKuliah.items():
            nilai2 = 0
            if attributes['perhitungan'] == perhitungan:
                nilai2 += 1
            if attributes['menggambar'] == menggambar:
                nilai2 += 1
            if attributes['pemrograman'] == pemrograman:
                nilai2 += 1
            if attributes['teknologi'] == teknologi:
                nilai2 += 1
            if attributes['praktek'] == praktek:
                nilai2 += 1
            if attributes['teori'] == teori:
                nilai2 += 1
            if attributes['minat_khusus'] == minat_khusus:
                nilai2 += 1
            nilai1[x] = nilai2

        nilai_sort = sorted(nilai1, key=nilai1.get, reverse=True)
        print(60*"-")
        print("Rekomendasi Mata Kuliah untuk anda :")
        for x in nilai_sort:
            print(f"\t[>]{x}")

    aplikasiPenentu()
    print(60*"-")
    print(60*"=")
