**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {5, 12, -3, 8, 0, 17}`
Írjunk programot, amely:

1. Eldönti, hogy **van-e a listában negatív szám**.
2. Ezután módosítjuk a programot úgy, hogy eldöntse, **minden szám páros-e**.

---

### 1. Melyik algoritmikus tétel?

**Eldöntés tétel**

---

### 2. Miért az **eldöntés tétel**?

Az algoritmus célja: **megállapítani, hogy teljesül-e egy adott feltétel legalább egy elemre**.
Ez megfelel az eldöntés tétel definíciójának: egy logikai változót (pl. `van`) használunk, amit igazra állítunk, ha a feltétel teljesül, és ekkor a ciklus akár meg is szakítható.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **logikai változót** használunk (pl. `van = False`)
* **végigiterálunk** az adatokon (pl. `for x in A`)
* **vizsgálunk egy feltételt** (pl. `ha x < 0`)
* **ha a feltétel igaz**, akkor megjegyezzük és kilépünk a ciklusból

---

### 4. Pszeudó kód – van-e negatív szám

```
van := hamis
ciklus minden x elemre A-ban
    ha x < 0 akkor
        van := igaz
        kilépés a ciklusból
ciklus vége
kiír van
```

---

### 5. Python kód – van-e negatív szám

```python
A = [5, 12, -3, 8, 0, 17]

van = False
for x in A:
    if x < 0:
        van = True
        break

print("Van negatív szám:", van)
```

---

### 6. A feladat módosítása – minden szám páros-e

Az algoritmust módosítani kell úgy, hogy **akkor állítsa hamisra**, ha **bármelyik szám nem páros**.
Ez a **mindig igaz vizsgálata** → **nem-páros szám keresése**.

---

### 7. Pszeudó kód – minden szám páros-e

```
mind := igaz
ciklus minden x elemre A-ban
    ha x mod 2 ≠ 0 akkor
        mind := hamis
        kilépés a ciklusból
ciklus vége
kiír mind
```

---

### 8. Python kód – minden szám páros-e

```python
A = [5, 12, -3, 8, 0, 17]

mind = True
for x in A:
    if x % 2 != 0:
        mind = False
        break

print("Minden szám páros:", mind)
```
