## 🔹 1. **Pozitív vagy negatív szám**


szam = int(input("Adj meg egy számot: "))

if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám nulla.")




## 🔹 2. **Nagyobb szám két érték közül**


a = int(input("Add meg az első számot: "))
b = int(input("Add meg a második számot: "))

if a > b:
    print("Az első szám a nagyobb.")
elif a < b:
    print("A második szám a nagyobb.")
else:
    print("A két szám egyenlő.")




## 🔹 3. **Osztható-e 3-mal**


szam = int(input("Adj meg egy számot: "))

if szam % 3 == 0:
    print("A szám osztható hárommal.")
else:
    print("A szám nem osztható hárommal.")




## 🔹 4. **Szökőév vizsgálat**


ev = int(input("Add meg az évet: "))

if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0):
    print("Az év szökőév.")
else:
    print("Az év nem szökőév.")



## 🔹 5. **Négyzet kiszámítása, ha nem negatív**


szam = float(input("Adj meg egy számot: "))

if szam >= 0:
    negyzet = szam * szam
    print("A szám négyzete:", negyzet)
else:
    print("A szám negatív, nem számolható a négyzete valós számként.")

