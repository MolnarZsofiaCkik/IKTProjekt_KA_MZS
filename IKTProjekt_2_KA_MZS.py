#Molnár Zsófia
#10/B
#Python első beadandó

print("a) feladat")
t = [160, 185, 159, 185, 167, 174, 172, 185]
n = len(t)
alacsonyabb = []

for i in range(1, n - 1):  
    if t[i] < t[i - 1] and t[i] < t[i + 1]:
        alacsonyabb.append(i + 1)  

print("A(z)", alacsonyabb, "diák csak a mellette levőket látja")


print("b) feladat")
t = [185, 158, 159, 160, 167, 174, 172, 185]
n = len(t)
rossz_helyen = []


for i in range(1, n - 1):
    if t[i - 1] > t[i] and t[i + 1] > t[i]:
        rossz_helyen.append(i + 1)  

print("A(z)", rossz_helyen, "diák van rossz helyen")



#Kőmíves Albert
#10/B
#Python első beadandó

print("c) feladat")

magassagok = [185, 158, 159, 160, 167, 174, 111, 111, 123, 189]
n=len(magassagok)
# for i in range(n):
#     magassag = float(input(f"Adja meg a {i+1}. diák magasságát (cm): "))
#     magassagok.append(magassag)
    
osszeg = 0
for magassag in magassagok:
    osszeg += magassag

atlag = osszeg / n
    
alacsonyabb = 0
magasabb = 0

for magassag in magassagok:
    if magassag < atlag:
        alacsonyabb += 1
    elif magassag > atlag:
        magasabb += 1
    
print("Átlag:",atlag,"Alacsonyabb:",alacsonyabb,"Magasabb",magasabb)
if alacsonyabb > magasabb:
    print("Alacsonyabb")
elif magasabb > alacsonyabb:
    print("Magasabb")
else:
    print("Egyenlő")


print("d) feladat")

n = 8
tomeg = [185, 175, 182, 159, 167, 174, 172, 185]

maxhossz = 1
aktualishossz = 1
maxstart = 0  
aktualisstart = 0  

for i in range(1, n):
    if tomeg[i] > tomeg[i - 1]:
        aktualishossz += 1
    else:
        if aktualishossz > maxhossz:
            maxhossz = aktualishossz
            maxstart = aktualisstart 
        aktualishossz = 1
        aktualisstart = i 

if aktualishossz > maxhossz:
    maxhossz = aktualishossz
    maxstart = aktualisstart

print(maxhossz, "a", maxstart + 1, ". gyerektől")