**Feladat:**
Adott két **rendezett (növekvő sorrendű)** egész számokat tartalmazó lista:
`A = {2, 5, 9, 14, 27}`
`B = {1, 6, 10, 13, 30}`
Írjunk programot, amely:

1. **Egy új listába összefuttatja** a két sorozat elemeit úgy, hogy a **végeredmény is rendezett legyen**.
2. Ezután módosítjuk az algoritmust úgy, hogy **kiszűrje az ismétlődő elemeket** az összefuttatott listából (még akkor is, ha a két bemeneti listában volt közös elem).

---

### 1. Melyik algoritmikus tétel?

**Összefuttatás tétel**

---

### 2. Miért az **összefuttatás tétel**?

Az algoritmus célja: két **rendezett sorozat egyesítése** egy új sorozatba úgy, hogy az eredmény is **rendezett maradjon**.
Ez az összefuttatás tétel definíciója.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **két bemeneti lista rendezett**
* **egy új rendezett listát** szeretnénk kapni
* **két indexet** használunk (pl. `i`, `j`) a két listában való lépkedéshez

---

### 4. Pszeudó kód – összefuttatás ismétlődésekkel

```
i := 0
j := 0
C := üres lista

amíg i < A hossza és j < B hossza
    ha A[i] < B[j] akkor
        C-hez hozzáad A[i]
        i := i + 1
    különben
        C-hez hozzáad B[j]
        j := j + 1

ciklus vége

amíg i < A hossza
    C-hez hozzáad A[i]
    i := i + 1

amíg j < B hossza
    C-hez hozzáad B[j]
    j := j + 1

kiír C
```

---

### 5. Python kód – összefuttatás ismétlődésekkel

```python
A = [2, 5, 9, 14, 27]
B = [1, 6, 10, 13, 30]

i = 0
j = 0
C = []

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

while i < len(A):
    C.append(A[i])
    i += 1

while j < len(B):
    C.append(B[j])
    j += 1

print("Összefuttatott lista:", C)
```

---

### 6. A feladat módosítása – ismétlődések kiszűrése

A feltételt módosítani kell:

* **Csak akkor adjuk hozzá az elemet, ha az előző nem azonos vele.**
  Ehhez figyelni kell, hogy **ne tegyünk két egyforma számot egymás után** a listába.

---

### 7. Pszeudó kód – összefuttatás ismétlődések nélkül

```
i := 0
j := 0
C := üres lista

amíg i < A hossza és j < B hossza
    ha A[i] < B[j] akkor
        ha C üres vagy A[i] ≠ C utolsó eleme akkor
            C-hez hozzáad A[i]
        i := i + 1
    különben ha A[i] > B[j] akkor
        ha C üres vagy B[j] ≠ C utolsó eleme akkor
            C-hez hozzáad B[j]
        j := j + 1
    különben  // A[i] == B[j]
        ha C üres vagy A[i] ≠ C utolsó eleme akkor
            C-hez hozzáad A[i]
        i := i + 1
        j := j + 1

amíg i < A hossza
    ha A[i] ≠ C utolsó eleme akkor
        C-hez hozzáad A[i]
    i := i + 1

amíg j < B hossza
    ha B[j] ≠ C utolsó eleme akkor
        C-hez hozzáad B[j]
    j := j + 1

kiír C
```

---

### 8. Python kód – összefuttatás ismétlődések nélkül

```python
A = [2, 5, 9, 14, 27]
B = [1, 6, 10, 13, 30]

i = 0
j = 0
C = []

def hozzad_ha_nem_egyezik(x):
    if len(C) == 0 or C[-1] != x:
        C.append(x)

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        hozzad_ha_nem_egyezik(A[i])
        i += 1
    elif A[i] > B[j]:
        hozzad_ha_nem_egyezik(B[j])
        j += 1
    else:
        hozzad_ha_nem_egyezik(A[i])
        i += 1
        j += 1

while i < len(A):
    hozzad_ha_nem_egyezik(A[i])
    i += 1

while j < len(B):
    hozzad_ha_nem_egyezik(B[j])
    j += 1

print("Összefuttatott, ismétlésmentes lista:", C)
```
