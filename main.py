liczby = input("podaj liczby (oddziel je przecinkiem): ")
tab = liczby.split(',')
min = int(tab[0])
max = int(tab[0])
for tab in tab:
    if(int(tab)<min): min = int(tab)
    if(int(tab)>max): max = int(tab)
print("Najmniejsza: " + str(min) + "\nNajwieszka: " + str(max))