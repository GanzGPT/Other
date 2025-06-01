**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {4, 7, 9, 11, 12, 14, 18, 20}`
Írjunk programot, amely:

1. **A számokat három csoportba osztja**, attól függően, hogy **3-mal osztva a maradékuk 0, 1 vagy 2**.
2. Ezután módosítjuk a programot úgy, hogy **a számjegyek összege szerint csoportosítsa** a számokat (pl. 5, 6, 7…).

---

### 1. Melyik algoritmikus tétel?

**Csoportosítás tétel**

---

### 2. Miért a **csoportosítás tétel**?

A csoportosítás célja, hogy **egy adathalmazt több csoportra bontsunk**, ahol a **csoportok egyértelműen meghatározhatók egy adott szempont (feltétel) alapján**.
Ebben az esetben:

* 3-mal oszthatóság maradéka szerint, vagy
* számjegyek összege szerint.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **több listát/dictionary-t használunk**
* **minden elem egy szabály alapján** egy konkrét csoportba kerül
* **nem kizárás vagy szelekció történik**, hanem besorolás a megfelelő csoportba

---

### 4. Pszeudó kód – maradék szerinti csoportosítás (mod 3)

```
maradek0 := üres lista
maradek1 := üres lista
maradek2 := üres lista

ciklus minden x elemre A-ban
    ha x mod 3 = 0 akkor
        maradek0 listához hozzáad x
    különben ha x mod 3 = 1 akkor
        maradek1 listához hozzáad x
    különben
        maradek2 listához hozzáad x
ciklus vége

kiír maradek0
kiír maradek1
kiír maradek2
```

---

### 5. Python kód – maradék szerinti csoportosítás (mod 3)

```python
A = [4, 7, 9, 11, 12, 14, 18, 20]

maradek0 = []
maradek1 = []
maradek2 = []

for x in A:
    if x % 3 == 0:
        maradek0.append(x)
    elif x % 3 == 1:
        maradek1.append(x)
    else:
        maradek2.append(x)

print("Maradék 0:", maradek0)
print("Maradék 1:", maradek1)
print("Maradék 2:", maradek2)
```

---

### 6. A feladat módosítása – számjegyek összege szerinti csoportosítás

A feltételt módosítani kell: **számjegyek összegét kell kiszámolni**, és annak alapján kell csoportosítani.
Ebben az esetben **nem fix számú csoport** van, hanem annyi, ahányféle számjegyösszeg előfordul.

---

### 7. Pszeudó kód – számjegyösszeg szerinti csoportosítás

```
csoportok := üres szótár

ciklus minden x elemre A-ban
    szamjegyosszeg := számjegyek összege x-ben
    ha szamjegyosszeg nincs a csoportok kulcsai között akkor
        hozzunk létre új üres listát ezzel a kulccsal
    csoportok[szamjegyosszeg]-hez hozzáad x
ciklus vége

kiír csoportok
```

(Segédfüggvény: számjegyek összege)

---

### 8. Python kód – számjegyösszeg szerinti csoportosítás

```python
A = [4, 7, 9, 11, 12, 14, 18, 20]

def szamjegyosszeg(n):
    return sum(int(c) for c in str(n))

csoportok = {}

for x in A:
    osszeg = szamjegyosszeg(x)
    if osszeg not in csoportok:
        csoportok[osszeg] = []
    csoportok[osszeg].append(x)

for osszeg, lista in csoportok.items():
    print(f"Számjegyösszeg = {osszeg}: {lista}")
```

