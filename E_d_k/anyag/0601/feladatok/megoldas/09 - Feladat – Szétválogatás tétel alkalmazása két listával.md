**Feladat:**
Adott két egész számokat tartalmazó lista:
`A = {3, 7, 10, 15, 22}`
`B = {5, 7, 10, 18, 22, 30}`
Írjunk programot, amely:

1. **Szétválogatja azokat az elemeket, amelyek csak az egyik listában szerepelnek**, két külön listába.
2. Ezután módosítjuk a programot úgy, hogy **azokat az elemeket gyűjtse külön listába, amelyek mindkét listában megtalálhatók**.

---

### 1. Melyik algoritmikus tétel?

**Szétválogatás tétel**

---

### 2. Miért a **szétválogatás tétel**?

Az algoritmus célja: **egy vagy több feltétel alapján külön csoportba sorolni az adatokat**.
Jelen esetben két listában szereplő elemek közötti viszony alapján választjuk szét az értékeket.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **több új lista** jön létre
* **végigiterálunk** az egyik vagy mindkét listán
* **vizsgáljuk, hogy egy elem szerepel-e a másik listában**
* és ennek alapján az egyik új listába kerül

---

### 4. Pszeudó kód – csak egyik listában szereplő elemek

```
csak_A := üres lista
csak_B := üres lista

ciklus minden x elemre A-ban
    ha x nincs benne B-ben akkor
        csak_A listához hozzáad x
ciklus vége

ciklus minden y elemre B-ben
    ha y nincs benne A-ban akkor
        csak_B listához hozzáad y
ciklus vége

kiír csak_A
kiír csak_B
```

---

### 5. Python kód – csak egyik listában szereplő elemek

```python
A = [3, 7, 10, 15, 22]
B = [5, 7, 10, 18, 22, 30]

csak_A = []
csak_B = []

for x in A:
    if x not in B:
        csak_A.append(x)

for y in B:
    if y not in A:
        csak_B.append(y)

print("Csak A listában szereplők:", csak_A)
print("Csak B listában szereplők:", csak_B)
```

---

### 6. A feladat módosítása – közös elemek listázása

A feltételt módosítani kell: csak azokat az elemeket válogassuk ki, amelyek **mindkét listában szerepelnek**.

---

### 7. Pszeudó kód – mindkét listában szereplő elemek

```
kozos := üres lista

ciklus minden x elemre A-ban
    ha x benne van B-ben és nincs még benne kozos-ban akkor
        kozos listához hozzáad x
ciklus vége

kiír kozos
```

---

### 8. Python kód – mindkét listában szereplő elemek

```python
A = [3, 7, 10, 15, 22]
B = [5, 7, 10, 18, 22, 30]

kozos = []

for x in A:
    if x in B and x not in kozos:
        kozos.append(x)

print("Mindkét listában szereplő elemek:", kozos)
```
