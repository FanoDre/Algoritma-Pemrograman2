import os
import csv
os.system("cls")

# start
users = open("Semester_2/pertemuan9/users.csv", "r")

usersCsv = csv.reader(users, delimiter="|")

print(usersCsv)

users.close()
