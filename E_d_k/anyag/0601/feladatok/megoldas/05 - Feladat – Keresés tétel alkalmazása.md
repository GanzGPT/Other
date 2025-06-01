**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {8, 14, 27, 33, 42, 56, 71}`
Írjunk programot, amely:

1. **Megkeresi, hogy szerepel-e a listában a 42-es szám**, és ha igen, **melyik indexen található meg**.
2. Ezután módosítjuk a programot úgy, hogy **meghatározza, hányadik utáni elem a 42**, ha szerepel a listában.

---

### 1. Melyik algoritmikus tétel?

**Keresés tétel**

---

### 2. Miért a **keresés tétel**?

A keresés tétel célja: **megtalálni egy adott értéket a sorozatban**.
Az algoritmus a keresett érték előfordulását vizsgálja, és ha megtalálja, megjegyzi annak helyét, majd befejezi a keresést.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **keresünk egy konkrét értéket** (pl. `42`)
* **végigiterálunk** a listán, amíg meg nem találjuk
* **megjegyezzük az indexet**, ha sikeres a keresés

---

### 4. Pszeudó kód – 42-es szám keresése index alapján

```
i := 0
amíg i < lista hossza és A[i] ≠ 42
    i := i + 1
ha i < lista hossza akkor
    kiír "42 megtalálva", i. indexen
különben
    kiír "42 nem szerepel a listában"
```

---

### 5. Python kód – 42-es szám keresése index alapján

```python
A = [8, 14, 27, 33, 42, 56, 71]

i = 0
while i < len(A) and A[i] != 42:
    i += 1

if i < len(A):
    print("A 42-es szám indexe:", i)
else:
    print("A 42-es szám nem szerepel a listában.")
```

---

### 6. A feladat módosítása – hányadik utáni elem a 42

Itt az a kérdés, hogy **a 42-es szám hányadik után szerepel** → tehát az **indexe - 1**
Például: ha a 42 az `i = 4`-edik indexen van, akkor **a 4. elem után van** → **az 5. után következik**.

---

### 7. Pszeudó kód – hányadik utáni elem a 42

```
i := 0
amíg i < lista hossza és A[i] ≠ 42
    i := i + 1
ha i < lista hossza akkor
    kiír "A 42 az", i, "edik elem után szerepel"
különben
    kiír "42 nem szerepel a listában"
```

---

### 8. Python kód – hányadik utáni elem a 42

```python
A = [8, 14, 27, 33, 42, 56, 71]

i = 0
while i < len(A) and A[i] != 42:
    i += 1

if i < len(A):
    print("A 42-es szám a(z)", i, ". elem után szerepel.")
else:
    print("A 42-es szám nem szerepel a listában.")
```
