import os
os.system("cls")



with open("1.txt", "r") as fayl:
    sonlar = fayl.read().split()

matn = ""

for son in sonlar:
    matn = matn + chr(int(son))

print(matn)