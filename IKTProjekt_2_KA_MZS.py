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
t = [185, 175, 182, 159, 167, 174, 172, 185]

maxhossz = 1  
jelenlegihossz = 1  
kezdoindex = 0  
jelenlegiindex = 0  

for i in range(1, n):
    if t[i] > t[i - 1]: 
        jelenlegihossz += 1  
    else:
        if jelenlegihossz > maxhossz:  
            maxhossz = jelenlegihossz  
            kezdoindex = jelenlegiindex  
        jelenlegihossz = 1  
        jelenlegiindex = i  


if jelenlegihossz > maxhossz:
    maxhossz = jelenlegihossz
    kezdoindex = jelenlegiindex


print(maxhossz)  
print(f"a {kezdoindex + 1}. gyerektől.") 

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