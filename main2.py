import random

tabMiasta = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Radom", "Lublin", "Szczecin", "Białystok", "Gniezno", "Sopot", "Paryż"]
wynik = []
for x in range(10):
    random1 = random.randint(0, len(tabMiasta) - 1)
    wynik.append(tabMiasta[random1])
    tabMiasta.remove(tabMiasta[random1])
wynik.sort()

for x in wynik:
    print(x)
