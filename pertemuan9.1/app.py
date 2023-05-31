import os
os.system('cls')


class courseList():
    matKul = {
        'Pemrograman': {
            'pemrograman': 0,
            'berhitung': 0,
            'menggambar': 0,
            'teknologi': 0,
            'praktis': 0,
            'teori': 0,
            'minatKhusus': 0
        },
        'Matematika': {
            'pemrograman': 0,
            'berhitung': 0,
            'menggambar': 0,
            'teknologi': 0,
            'praktis': 0,
            'teori': 0,
            'minatKhusus': 0
        },
        'Seni Rupa': {
            'pemrograman': 0,
            'berhitung': 0,
            'menggambar': 0,
            'teknologi': 0,
            'praktis': 0,
            'teori': 0,
            'minatKhusus': 0
        }
    }

    pemrograman = int(
        input("Apakah anda suka mata kuliah pemrograman? [1:YES/0:NO]: "))
    berhitung = int(
        input("Apakah anda suka mata kuliah tentang berhitung? [1:YES/0:NO]: "))
    menggambar = int(
        input("Apakah anda suka mata kuliah menggambar? [1:YES/0:NO]: "))
    teknologi = int(
        input("Apakah anda suka mata kuliah tentang teknologi? [1:YES/0:NO]: "))
    praktis = int(
        input("Apakah anda suka mata kuliah yang praktis? [1:YES/0:NO]: "))
    teori = int(
        input("Apakah anda suka mata kuliah yang banyak teori? [1:YES/0:NO]: "))
    minatKhusus = int(
        input("Apakah anda memiliki minat khusus dalam suatu mata kuliah? [1:YES/0:NO]: "))
    scores = {}
    for x, att in matKul.items():
        score = 0
        if att['pemrograman'] == pemrograman:
            score += 1
        if att['berhitung'] == berhitung:
            score += 1
        if att['menggambar'] == menggambar:
            score += 1
        if att['teknologi'] == teknologi:
            score += 1
        if att['praktis'] == praktis:
            score += 1
        if att['teori'] == teori:
            score += 1
        if att['minatKhusus'] == minatKhusus:
            score += 1
        scores[x] = score

    sortedCourses = sorted(scores, key=scores.get, reverse=True)
    print("--------------------------")
    print("List Rekomendasi Mata Kuliah berdasarkan preferensi anda: ")
    for x in range(len(sortedCourses)):
        print(f"{x+1}.{sortedCourses[x]}")
