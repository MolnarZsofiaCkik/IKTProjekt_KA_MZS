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

#Molnár Zsófia
#10/B
#Python első beadandó
print("a) feladat")
t=[185, 158, 159, 160, 167, 174, 172, 185]
n=len(t)
talalat = -1 
for i in range(1, n - 1):  
    if t[i] <= t[i - 1] and t[i] <= t[i + 1]:
        talalat = i + 1  


if talalat != -1:
    print("A(z)", talalat, ". diák az, akit ha elnéz jobbra vagy balra, nem látja csak a mellette levőt.")
else:
    print("Nincs olyan diák, aki csak a mellette levőt látja.")