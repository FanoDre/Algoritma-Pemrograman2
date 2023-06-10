import random
import os
os.system('cls')

listRandom = []
listRandomx = []


def tambahData(data):
    for i in range(panjangData):
        listRandom.append(random.randint(0, 100))
    return data


def kaliData(data):
    for i in range(len(listRandom)):
        listRandomx.append(listRandom[i] * kali)
    return data


print(55*'-')
panjangData = int(input("Masukkan Panjang data: "))
print(55*'-')
kali = int(input("Mau dikalikan berapa?: "))

dataRandom = tambahData(listRandom)
dataRandomx = kaliData(listRandomx)

print(55*'-')
print(f"Panjang Data \t\t: [{panjangData}]")
print(f"Nilai Random before \t: {dataRandom}")
print(f"Dikalikan \t\t: [{kali}]")
print(f"Nilai Random after \t: {dataRandomx}")
print(55*'-')
