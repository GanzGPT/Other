**Feladat:**
Adott egy egész számokat tartalmazó lista:
`A = {12, 4, 19, 7, 3, 15, 10}`
Írjunk programot, amely:

1. **Sorba rendezi a lista elemeit növekvő sorrendbe.**
2. Ezután módosítjuk az algoritmust úgy, hogy **csökkenő sorrendbe rendezze** a lista elemeit.

---

### 1. Melyik algoritmikus tétel?

**Rendezés tétel**

---

### 2. Miért a **rendezés tétel**?

Az algoritmus célja: **egy rendezetlen adatsor elemeinek meghatározott sorrendbe állítása** (növekvő vagy csökkenő).
Ez megfelel a rendezés tétel definíciójának.

---

### 3. Honnan lehet felismerni?

A feladat jellemzője, hogy:

* **egy adott adatsort** módosítunk
* az elemeket **összehasonlítás alapján** cseréljük
* a cél a **teljes rendezés** növekvő vagy csökkenő logika szerint

---

### 4. Pszeudó kód – növekvő sorrendű rendezés (pl. egyszerű buborék rendezés)

```
ciklus i := 0-tól lista hossza - 2-ig
    ciklus j := 0-tól lista hossza - i - 2-ig
        ha A[j] > A[j + 1] akkor
            csere A[j] és A[j + 1]
ciklus vége

kiír A
```

---

### 5. Python kód – növekvő sorrendű rendezés

```python
A = [12, 4, 19, 7, 3, 15, 10]

for i in range(len(A) - 1):
    for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

print("Növekvő sorrend:", A)
```

---

### 6. A feladat módosítása – csökkenő sorrend

A logikai feltételt meg kell fordítani: `A[j] < A[j + 1]`

---

### 7. Pszeudó kód – csökkenő sorrendű rendezés

```
ciklus i := 0-tól lista hossza - 2-ig
    ciklus j := 0-tól lista hossza - i - 2-ig
        ha A[j] < A[j + 1] akkor
            csere A[j] és A[j + 1]
ciklus vége

kiír A
```

---

### 8. Python kód – csökkenő sorrendű rendezés

```python
A = [12, 4, 19, 7, 3, 15, 10]

for i in range(len(A) - 1):
    for j in range(len(A) - i - 1):
        if A[j] < A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

print("Csökkenő sorrend:", A)
```
