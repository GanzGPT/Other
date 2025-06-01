**Feladat:**
Adott egy egész számokat tartalmazó rendezett lista:
`A = {3, 6, 11, 25, 32, 45}`
Írjunk programot, amely:

1. Kiszámítja az **összegét az összes számnak** a listában.
2. Ezután módosítjuk a programot úgy, hogy csak a **hárommal osztható számok összegét** számolja ki.

---

### 1. Melyik algoritmikus tétel?

**Összegzés tétel**

---

### 2. Miért az **összegzés tétel**?

Az algoritmus célja: **kiszámolni az adatsor adott elemeinek az összegét**.
Ez megfelel az összegzés tétel definíciójának: egy változóban (pl. `osszeg`) folyamatosan gyűjtjük össze az értékeket, akár az összes elemet, akár csak bizonyos feltételnek megfelelőeket.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **összeg változót** használunk (pl. `osszeg = 0`)
* **végigiterálunk** az adatokon (pl. `for x in A`)
* **összeadunk valamit** minden körben (pl. `osszeg += x`)
* esetleg **feltétel** is van, ha nem minden elem kerül az összegbe

---

### 4. Pszeudó kód – összes szám összege

```
osszeg := 0
ciklus minden x elemre A-ban
    osszeg := osszeg + x
ciklus vége
kiír osszeg
```

---

### 5. Python kód – összes szám összege

```python
A = [3, 6, 11, 25, 32, 45]

osszeg = 0
for x in A:
    osszeg += x

print("Az elemek összege:", osszeg)
```

---

### 6. A feladat módosítása – csak hárommal osztható számok összege

A feltételt módosítani kell: `x % 3 == 0`

---

### 7. Pszeudó kód – hárommal osztható számok összege

```
osszeg := 0
ciklus minden x elemre A-ban
    ha x mod 3 = 0 akkor
        osszeg := osszeg + x
ciklus vége
kiír osszeg
```

---

### 8. Python kód – hárommal osztható számok összege

```python
A = [3, 6, 11, 25, 32, 45]

osszeg = 0
for x in A:
    if x % 3 == 0:
        osszeg += x

print("A hárommal osztható számok összege:", osszeg)
```
