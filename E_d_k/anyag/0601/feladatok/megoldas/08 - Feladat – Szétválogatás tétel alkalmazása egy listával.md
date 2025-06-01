**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {4, 9, 12, 15, 22, 33, 40, 41}`
Írjunk programot, amely:

1. **Szétválogatja a páros és páratlan számokat** két külön listába.
2. Ezután módosítjuk a programot úgy, hogy **pozitív és negatív számokra válogassa szét** az elemeket.

---

### 1. Melyik algoritmikus tétel?

**Szétválogatás tétel**

---

### 2. Miért a **szétválogatás tétel**?

Az algoritmus célja: **egy listából két (vagy több) külön csoportba rendezni az elemeket egy feltétel alapján**.
Ez megfelel a szétválogatás tétel definíciójának: minden elemről eldöntjük, hogy melyik csoportba tartozik, és a megfelelő listába helyezzük.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **több új lista** jön létre (pl. `paros`, `paratlan`)
* **végigiterálunk** az adatokon
* **vizsgálunk egy feltételt**, majd a megfelelő listába **besoroljuk az elemet**

---

### 4. Pszeudó kód – páros és páratlan számok szétválogatása

```
paros := üres lista
paratlan := üres lista

ciklus minden x elemre A-ban
    ha x mod 2 = 0 akkor
        paros listához hozzáad x
    különben
        paratlan listához hozzáad x
ciklus vége

kiír paros
kiír paratlan
```

---

### 5. Python kód – páros és páratlan számok szétválogatása

```python
A = [4, 9, 12, 15, 22, 33, 40, 41]

paros = []
paratlan = []

for x in A:
    if x % 2 == 0:
        paros.append(x)
    else:
        paratlan.append(x)

print("Páros számok:", paros)
print("Páratlan számok:", paratlan)
```

---

### 6. A feladat módosítása – pozitív és negatív számokra szétválogatás

A feltételt módosítani kell: `x >= 0` vagy `x < 0`

---

### 7. Pszeudó kód – pozitív és negatív számok szétválogatása

```
pozitiv := üres lista
negativ := üres lista

ciklus minden x elemre A-ban
    ha x ≥ 0 akkor
        pozitiv listához hozzáad x
    különben
        negativ listához hozzáad x
ciklus vége

kiír pozitiv
kiír negativ
```

---

### 8. Python kód – pozitív és negatív számok szétválogatása

```python
A = [4, 9, 12, 15, 22, 33, 40, 41]

pozitiv = []
negativ = []

for x in A:
    if x >= 0:
        pozitiv.append(x)
    else:
        negativ.append(x)

print("Pozitív számok:", pozitiv)
print("Negatív számok:", negativ)
```
