**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {17, 22, 39, 8, 41, 36, 25}`
Írjunk programot, amely:

1. **Megkeresi a legnagyobb számot** a listában.
2. Ezután módosítjuk a programot úgy, hogy **a legnagyobb szám indexét is meghatározza**.

---

### 1. Melyik algoritmikus tétel?

**Maximum kiválasztás tétel**

---

### 2. Miért a **maximum kiválasztás tétel**?

Az algoritmus célja: **megtalálni a legnagyobb értékű elemet egy sorozatban**.
Ez megfelel a maximum tétel definíciójának: egy változóban tároljuk az aktuális legnagyobb értéket, és folyamatosan frissítjük, ha találunk nagyobbat.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* van egy **aktuális maximum változó** (pl. `max`)
* **végigiterálunk** a listán
* **összehasonlítunk** minden elemet a jelenlegi maximummal
* ha nagyobbat találunk, **frissítjük** a maximum értékét

---

### 4. Pszeudó kód – legnagyobb érték meghatározása

```
max := A[0]
ciklus i := 1-től lista hossza - 1-ig
    ha A[i] > max akkor
        max := A[i]
ciklus vége
kiír max
```

---

### 5. Python kód – legnagyobb érték meghatározása

```python
A = [17, 22, 39, 8, 41, 36, 25]

max = A[0]
for i in range(1, len(A)):
    if A[i] > max:
        max = A[i]

print("A legnagyobb szám:", max)
```

---

### 6. A feladat módosítása – legnagyobb érték és index meghatározása

Két változót kell használnunk:

* **érték** tárolására: `max`
* **index** tárolására: `max_index`

---

### 7. Pszeudó kód – legnagyobb érték és index meghatározása

```
max := A[0]
max_index := 0
ciklus i := 1-től lista hossza - 1-ig
    ha A[i] > max akkor
        max := A[i]
        max_index := i
ciklus vége
kiír max, max_index
```

---

### 8. Python kód – legnagyobb érték és index meghatározása

```python
A = [17, 22, 39, 8, 41, 36, 25]

max = A[0]
max_index = 0
for i in range(1, len(A)):
    if A[i] > max:
        max = A[i]
        max_index = i

print("A legnagyobb szám:", max)
print("Indexe:", max_index)
```
