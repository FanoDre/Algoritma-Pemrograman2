import random
import os
os.system('cls')

listRandom = []


def tambahData(data):
    print(55*'-')
    panjangData = int(input("Masukkan Panjang data: "))
    for i in range(panjangData):
        listRandom.append(random.randint(-25, 100))
    return data


def sortTertinggi(data):
    max = data[0]
    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]
    return max


def sortTerendah(data):
    max = data[0]
    for i in range(1, len(data)):
        if data[i] < max:
            max = data[i]
    return max


dataRandom = tambahData(listRandom)
lRandomTertinggi = sortTertinggi(dataRandom)
lRandomTerendah = sortTerendah(dataRandom)

print(55*'-')
print(f"Nilai Random : {dataRandom}")
print(f"Nilai terbesar: {lRandomTertinggi}")
print(f"Nilai terkecil: {lRandomTerendah}")
print(55*'-')
