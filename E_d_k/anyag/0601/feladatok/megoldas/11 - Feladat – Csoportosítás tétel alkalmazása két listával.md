**Feladat:**
Adott két egész számokat tartalmazó lista:
`A = {3, 6, 9, 12, 15, 18}`
`B = {6, 10, 12, 14, 18, 20}`
Írjunk programot, amely:

1. A számokat **három csoportba rendezi**:

   * csak az **A** listában szereplők,
   * csak a **B** listában szereplők,
   * **mindkét listában** szereplők.
2. Ezután módosítjuk az algoritmust úgy, hogy a számokat **páros vagy páratlan csoportba** rendezzük, **függetlenül attól, melyik listából származnak**.

---

### 1. Melyik algoritmikus tétel?

**Csoportosítás tétel**

---

### 2. Miért a **csoportosítás tétel**?

Az algoritmus célja: az adatok **több, kizárólagos csoportba való sorolása** egy feltétel vagy szempont alapján (pl. hol szerepel az elem, milyen tulajdonsága van).
Ez megfelel a csoportosítás tétel definíciójának.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **több lista vagy szótár** keletkezik
* **egy logikai feltétel** alapján minden elem pontosan egy csoportba kerül
* a **feltétel kizáró jellegű** (pl. csak A-ban, csak B-ben, mindkettőben)

---

### 4. Pszeudó kód – csak A-ban, csak B-ben, mindkettőben

```
csak_A := üres lista
csak_B := üres lista
mindketto := üres lista

ciklus minden x elemre A-ban
    ha x benne van B-ben akkor
        mindketto listához hozzáad x
    különben
        csak_A listához hozzáad x
ciklus vége

ciklus minden y elemre B-ben
    ha y nincs benne A-ban és nincs benne mindketto listában akkor
        csak_B listához hozzáad y
ciklus vége

kiír csak_A
kiír csak_B
kiír mindketto
```

---

### 5. Python kód – csak A-ban, csak B-ben, mindkettőben

```python
A = [3, 6, 9, 12, 15, 18]
B = [6, 10, 12, 14, 18, 20]

csak_A = []
csak_B = []
mindketto = []

for x in A:
    if x in B:
        mindketto.append(x)
    else:
        csak_A.append(x)

for y in B:
    if y not in A and y not in mindketto:
        csak_B.append(y)

print("Csak A listában:", csak_A)
print("Csak B listában:", csak_B)
print("Mindkét listában:", mindketto)
```

---

### 6. A feladat módosítása – páros és páratlan számok csoportosítása

Itt az összes elemet egyesíteni kell, és **az oszthatóság paritása alapján** kell két csoportra bontani.

---

### 7. Pszeudó kód – páros és páratlan számok

```
paros := üres lista
paratlan := üres lista

egyesitett := A és B elemeinek uniója

ciklus minden x elemre egyesitett-ben
    ha x mod 2 = 0 akkor
        paros listához hozzáad x
    különben
        paratlan listához hozzáad x
ciklus vége

kiír paros
kiír paratlan
```

---

### 8. Python kód – páros és páratlan számok

```python
A = [3, 6, 9, 12, 15, 18]
B = [6, 10, 12, 14, 18, 20]

egyesitett = list(set(A + B))

paros = []
paratlan = []

for x in egyesitett:
    if x % 2 == 0:
        paros.append(x)
    else:
        paratlan.append(x)

print("Páros számok:", paros)
print("Páratlan számok:", paratlan)
```
