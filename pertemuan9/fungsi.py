

def fakultasUndira():
    fakultasList = ['Fakultas Bisnis & Ilmu Sosial',
                    'Fakultas Teknik & Informatika']
    pilihFakultas(fakultasList)


def pilihFakultas(fakultas):
    for x in range(len(fakultas)):
        print(f"{x+1}. {fakultas[x]}")


# print("Daftar Fakultas :")
# for x in range(len(fakultasUndira)):
#     print(f"\t{x+1}. {fakultas[x]}")
# print(60*"-")
# pilihFakultas = int(input("Pilih Fakultas : "))
# print(60*"-")
