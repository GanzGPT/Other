**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {3, 11, 18, 25, 36, 40, 52}`
Írjunk programot, amely:

1. **Kiválasztja az első 5-tel osztható számot** a listából.
2. Ezután módosítjuk a programot úgy, hogy **a legkisebb páros számot** válassza ki a listából.

---

### 1. Melyik algoritmikus tétel?

**Kiválasztás tétel**

---

### 2. Miért a **kiválasztás tétel**?

A kiválasztás tétel célja: **megtalálni egy olyan elemet, amely megfelel egy adott feltételnek**, és **visszaadni az első ilyet**.
A ciklus az első megfelelő elem megtalálásakor leáll.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **végigiterálunk** a listán
* **feltételt vizsgálunk** (pl. osztható-e 5-tel)
* ha a feltétel **először teljesül**, az **értéket elmentjük** és kilépünk

---

### 4. Pszeudó kód – első 5-tel osztható szám kiválasztása

```
i := 0
amíg i < lista hossza és A[i] mod 5 ≠ 0
    i := i + 1
ha i < lista hossza akkor
    eredmeny := A[i]
    kiír eredmeny
különben
    kiír "Nincs 5-tel osztható szám"
```

---

### 5. Python kód – első 5-tel osztható szám kiválasztása

```python
A = [3, 11, 18, 25, 36, 40, 52]

i = 0
while i < len(A) and A[i] % 5 != 0:
    i += 1

if i < len(A):
    print("Első 5-tel osztható szám:", A[i])
else:
    print("Nincs 5-tel osztható szám a listában.")
```

---

### 6. A feladat módosítása – legkisebb páros szám kiválasztása

Ez már **maximum (minimum) kiválasztás tétel**, nem egyszerű kiválasztás.
Meg kell keresni a **legkisebb olyan elemet**, amely **páros**.

---

### 7. Melyik algoritmikus tétel?

**Minimum kiválasztás tétel (feltételes)**

---

### 8. Pszeudó kód – legkisebb páros szám kiválasztása

```
min := végtelen
ciklus minden x elemre A-ban
    ha x mod 2 = 0 akkor
        ha x < min akkor
            min := x
ciklus vége
ha min ≠ végtelen akkor
    kiír min
különben
    kiír "Nincs páros szám"
```

---

### 9. Python kód – legkisebb páros szám kiválasztása

```python
A = [3, 11, 18, 25, 36, 40, 52]

min_páros = None
for x in A:
    if x % 2 == 0:
        if min_páros is None or x < min_páros:
            min_páros = x

if min_páros is not None:
    print("Legkisebb páros szám:", min_páros)
else:
    print("Nincs páros szám a listában.")
```
