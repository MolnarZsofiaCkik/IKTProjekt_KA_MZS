#Kőmíves Albert
#10/B
#Python első beadandó
# Kérjük be a diákok számát

print("c) feladat")
# Kérjük be a diákok magasságait
magassagok = [185, 158, 159, 160, 167, 174, 111, 111, 123, 189]
n=len(magassagok)
# for i in range(n):
#     magassag = float(input(f"Adja meg a {i+1}. diák magasságát (cm): "))
#     magassagok.append(magassag)
    
# Átlag kiszámítása
osszeg = 0
for magassag in magassagok:
    osszeg += magassag

atlag = osszeg / n
    
# Alacsonyabb és magasabb diákok számlálása
alacsonyabb = 0
magasabb = 0

for magassag in magassagok:
    if magassag < atlag:
        alacsonyabb += 1
    elif magassag > atlag:
        magasabb += 1
    
# Eredmény kiírása
print("Átlag:",atlag,"Alacsonyabb:",alacsonyabb,"Magasabb",magasabb)
if alacsonyabb > magasabb:
    print("Alacsonyabb")
elif magasabb > alacsonyabb:
    print("Magasabb")
else:
    print("Egyenlő")

