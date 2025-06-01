**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {12, 5, 23, 7, 18, 3, 14}`
Írjunk programot, amely:

1. **Megkeresi a legkisebb számot** a listában.
2. Ezután módosítjuk a programot úgy, hogy **meghatározza, hányszor fordul elő a legkisebb szám** a listában.

---

### 1. Melyik algoritmikus tétel?

**Minimum kiválasztás tétel**

---

### 2. Miért a **minimum kiválasztás tétel**?

Az algoritmus célja: **megtalálni a legkisebb értékű elemet** a sorozatban.
Ez megfelel a minimum tétel definíciójának: egy változóban tároljuk az aktuális legkisebb értéket, és minden új, kisebb értéknél frissítjük azt.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* van egy **aktuális minimum változó** (pl. `min`)
* **végigiterálunk** az adatokon
* **összehasonlítunk** minden elemet az aktuális minimummal
* ha kisebbet találunk, **frissítjük** az értéket

---

### 4. Pszeudó kód – legkisebb érték meghatározása

```
min := A[0]
ciklus i := 1-től lista hossza - 1-ig
    ha A[i] < min akkor
        min := A[i]
ciklus vége
kiír min
```

---

### 5. Python kód – legkisebb érték meghatározása

```python
A = [12, 5, 23, 7, 18, 3, 14]

min = A[0]
for i in range(1, len(A)):
    if A[i] < min:
        min = A[i]

print("A legkisebb szám:", min)
```

---

### 6. A feladat módosítása – legkisebb szám előfordulásainak száma

A legkisebb érték meghatározása után **végig kell menni újra a listán**, és **megszámlálni**, hányszor fordul elő ez az érték.

---

### 7. Melyik algoritmikus tétel?

**Összegzés tétel** (megszámlálásként használva)

---

### 8. Pszeudó kód – legkisebb érték és előfordulások száma

```
min := A[0]
ciklus i := 1-től lista hossza - 1-ig
    ha A[i] < min akkor
        min := A[i]
ciklus vége

db := 0
ciklus minden x elemre A-ban
    ha x = min akkor
        db := db + 1
ciklus vége

kiír min, db
```

---

### 9. Python kód – legkisebb érték és előfordulások száma

```python
A = [12, 5, 23, 7, 18, 3, 14]

min = A[0]
for i in range(1, len(A)):
    if A[i] < min:
        min = A[i]

db = 0
for x in A:
    if x == min:
        db += 1

print("A legkisebb szám:", min)
print("Előfordulások száma:", db)
```
