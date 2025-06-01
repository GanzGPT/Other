**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {4, 7, 12, 19, 22, 35, 40}`
Írjunk programot, amely:

1. Megszámolja, hány darab **páros szám** van a listában.
2. Ezután módosítjuk a programot úgy, hogy azt számolja meg, hány szám **van 10 és 30 között (beleértve)**.

---

### 1. Melyik algoritmikus tétel?

**Megszámlálás tétel**

---

### 2. Miért a **megszámlálás tétel**?

Az algoritmus célja: **megszámolni, hány olyan elem van a sorozatban**, amely kielégít egy adott feltételt.
Ez pontosan megfelel a megszámlálás tétel definíciójának: végigmegyünk az adatokon, és minden feltételnek megfelelő elemnél egy számlálót növelünk.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **egy számláló változót** használunk (pl. `db = 0`)
* **végigiterálunk** az adatsoron (pl. `for x in A`)
* **feltételt vizsgálunk** (pl. `ha x páros`)
* és **növeljük a számlálót**, ha a feltétel teljesül

---

### 4. Pszeudó kód – páros számok megszámlálása

```
db := 0
ciklus minden x elemre A-ban
    ha x mod 2 = 0 akkor
        db := db + 1
ciklus vége
kiír db
```

---

### 5. Python kód – páros számok megszámlálása

```python
A = [4, 7, 12, 19, 22, 35, 40]

db = 0
for x in A:
    if x % 2 == 0:
        db += 1

print("A páros számok száma:", db)
```

---

### 6. A feladat módosítása – számok 10 és 30 között (beleértve)

A feltételt módosítani kell: `10 <= x <= 30`

---

### 7. Pszeudó kód – 10 és 30 közötti számok megszámlálása

```
db := 0
ciklus minden x elemre A-ban
    ha x ≥ 10 és x ≤ 30 akkor
        db := db + 1
ciklus vége
kiír db
```

---

### 8. Python kód – 10 és 30 közötti számok megszámlálása

```python
A = [4, 7, 12, 19, 22, 35, 40]

db = 0
for x in A:
    if 10 <= x <= 30:
        db += 1

print("A 10 és 30 közötti számok száma:", db)
```
