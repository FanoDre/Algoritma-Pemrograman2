import os
import csv
os.system('cls')

with open("/pertemuan11/DataMahasiswa.csv", "r") as dataMhs:
    csvdata = csv.reader(dataMhs)
    for x in csvdata:
        print(x)
