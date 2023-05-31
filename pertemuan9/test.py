# Cara Mengeluarkan Array Dari def/fungsi
def jurusanFbis():
    jurusan = ['Akuntansi', 'Ilmu Komunikasi',
               'Manajemen', 'Sastra Inggris']
    # Mata Kuliah
    matkulAkt = ['Pengantar Akuntansi', 'Pengantar Manajemen & Bisnis',
                 'Matematika Ekonomi Bisnis', 'Lembaga Keuangan', 'Hukum Bisnis & Lingkungan',]
    matkulIlkom = ['Pengantar Ilmu Komunikasi',
                   'Pengantar Public Relations', 'Komunikasi Organisasi', 'Teori Komunikasi Communication',
                   'Dasar-Dasar Manajemen & Kepemimpinan Principles Of Management And Leadership',]
    matkulMj = ['Pengatar Ekonomi Bisnis', 'Pengantar Ekonomi Mikro',
                'Pengantar Akuntansi', 'Matematika Bisnis', 'Pengantar Manajemen']
    matkulSs = ['Reading & Writing', 'Listening & Speaking', 'Grammar',
                'English Pronunciation', 'Cross Cultural Communication']
    return jurusan, matkulAkt, matkulIlkom, matkulMj, matkulSs


jurusan, matkulAkt, matkulIlkom, matkulMj, matkulSs = jurusanFbis()
for x in range(len(jurusan)):
    print(f"{x+1}. {jurusan[x]}")
