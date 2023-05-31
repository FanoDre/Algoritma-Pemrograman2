import os
os.system('cls')
# -----------------------------------------------
print(54*"-")
print(f"{'TUGAS PERTEMUAN 7':>35}")
print(54*"-")
# -----------------------------------------------
print(54*"-")
print(f"{'CALCULATOR PYTHON':>35}")
print(54*"-")


def calc():
    num11 = input("Enter a number \t\t: ")
    op = input("Enter a sign [+|-|/|x] \t: ")
    num22 = input("Enter a number \t\t: ")
    print(54*"-")
    if num11.isdigit() and num22.isdigit():
        num11 = int(num11)
        num22 = int(num22)

        if op == "+":
            isTotal = num11 + num22
            print(f"Result \t\t\t: {num11} {op} {num22} = {int(isTotal)}")
        elif op == "-":
            isTotal = num11 - num22
            print(
                f"Result \t\t\t: {num11} {op} {num22} = {int(isTotal)}")
        elif op == "/":
            isTotal = num11 / num22
            print(
                f"Result \t\t\t: {num11} {op} {num22} = {isTotal}")
        elif op == "x":
            isTotal = num11 * num22
            print(
                f"Result \t\t\t: {num11} {op} {num22} = {int(isTotal)}")
        else:
            print("Please enter this sign [ + | - | / | x ] only.")
            print(54*"-")
            calc()
    else:
        print("Please type a number.")
        calc()

    return


calc()

print(54*"-")


def nextOp():
    next = input("Try Again? [Y/N]: ").lower()
    if next == "y":
        print(54*"-")
        calc()
        print(54*"-")
        nextOp()
    elif next == "n":
        print(54*"-")
        print("Thank You.")
        print(54*"-")
        quit()


nextOp()
