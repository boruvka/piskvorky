import random

def vypis_pole(pole_k_vypsani):
    print ''.join(pole_k_vypsani)

def zpracuj_tah_hrac(pole, pozice):
    pole[pozice] = 'X'
    vypis_pole(pole)
    #jestli jsou vedle sebe 3X
    for i in range(len(pole)-2):
        if (pole[i] == 'X' and pole[i+1]=='X' and pole[i+2]=='X'):
            print 'Vyhral hrac'
	    return True

def zpracuj_tah_pc(pole, pozice):
    pole[pozice] = 'O'
    vypis_pole(pole)
    #jestli jsou vedle sebe 3O
    for i in range(len(pole)-2):
        if (pole[i] == 'O' and pole[i+1]=='O' and pole[i+2]=='O'):
            print 'Vyhral pocitac'
	    return True

# inicializce
# - vztvorit hraci pole
#vypsat hraci pole
delka_pole = 42
pole = []
for i in range(delka_pole):
    pole.append(".")
vypis_pole(pole)

#pta se kam chce tahnout  a v pripade tecky pokracje dal tzn. fce zpracuj_tah
#jinak se znovu zepta a jede smycka porad dokola
while True:
	while True:
	    pozice = input('hraci kam chces tahnout? ')
	    if pole[pozice] == ".":
	       break
	if zpracuj_tah_hrac(pole, pozice):
		break
	 
	while True:
	    pozice = random.randint(0, delka_pole-1)
	    if pole[pozice] == ".":
		break
	        if pole[pozice-1] == "X"  pole[pozice+1]=="X":
		    break
	if zpracuj_tah_pc(pole, pozice):
		break
