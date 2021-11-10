import sys

dlugosc_cyklu = int(sys.stdin.readline().rstrip())
wagi_słoni = list(map(int, sys.stdin.readline().rstrip().split()))
oryginalna_kolejnosc = list(map(int, sys.stdin.readline().rstrip().split()))
pozadana_kolejnosc = list(map(int, sys.stdin.readline().rstrip().split()))

suma_mas_sloni = sum(wagi_słoni)
masa_najlzejszego_slonia = min(wagi_słoni)

sprawdzenie_bolonskie =  [False for n in range(dlugosc_cyklu)]

permutacje = list(range(0, dlugosc_cyklu))
for i in range(dlugosc_cyklu):
    permutacje[pozadana_kolejnosc[i]-1] = oryginalna_kolejnosc[i]-1
wynik = int(0)

for i in range(dlugosc_cyklu):
    if sprawdzenie_bolonskie[i] == False:
        aktualnie_sprawdzany_slon = int(i)
        suma_wag_cyklu = int(0)
        minimalna_waga_cyklu = 9999
        dlugosc_cyklu = int(0)
    
        while True:
            minimalna_waga_cyklu = min(minimalna_waga_cyklu, wagi_słoni[aktualnie_sprawdzany_slon])
            
            suma_wag_cyklu += wagi_słoni[aktualnie_sprawdzany_slon]
            
            aktualnie_sprawdzany_slon = permutacje[aktualnie_sprawdzany_slon]
            
            sprawdzenie_bolonskie[aktualnie_sprawdzany_slon] = True
            
            dlugosc_cyklu += 1
            
            if aktualnie_sprawdzany_slon == i:
                break
    else:
        continue
          
    wynik += min((suma_wag_cyklu + (dlugosc_cyklu-2) * minimalna_waga_cyklu), (suma_wag_cyklu + minimalna_waga_cyklu + (dlugosc_cyklu + 1)*masa_najlzejszego_slonia))

print(wynik)