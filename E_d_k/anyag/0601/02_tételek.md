
# **1. Alap tételek**

## **Megszámlálás tétel alkalmazása**

**Miről szól a megszámlálás tétel?**

A megszámlálás tétel olyan algoritmikus eljárás, amely során megszámoljuk, hogy egy adott feltételnek hány elem felel meg egy sorozatban, listában vagy adathalmazban. A tétel célja tehát nem az elemek módosítása, hanem azok számának meghatározása egy adott szempont alapján.

**Mikor alkalmazzuk?**

A megszámlálás tételt akkor alkalmazzuk, amikor kíváncsiak vagyunk arra, hogy egy adott adathalmazban hány olyan elem található, amely megfelel egy meghatározott logikai feltételnek. Például: hány páros szám van egy listában, hány név kezdődik „A” betűvel, hány tanuló ért el legalább elégséges osztályzatot stb.

**Hogyan lehet felismerni?**

A megszámlálás tétel jellemző felismerhető elemei:

* Az algoritmus egy számlálót (pl. `db`, `számláló`, `count`) használ, amelyet kezdetben nullára állítunk.
* Bejárjuk az adathalmaz elemeit (pl. ciklus segítségével).
* Minden egyes elemre ellenőrizzük, hogy teljesül-e a kívánt feltétel.
* Ha teljesül, a számlálót eggyel növeljük.
* A ciklus végén a számláló tartalmazza a feltételnek megfelelő elemek számát.



## **Összegzés tétel alkalmazása**


**Miről szól az összegzés tétel?**

Az összegzés tétel célja, hogy egy sorozat, lista vagy adathalmaz elemei közül meghatározott szempont szerint kiválasztott értékeket összeadjuk. Az algoritmus eredményeként egyetlen számot kapunk: a részhalmaz vagy az összes elem összegét.

**Mikor alkalmazzuk?**

Az összegzés tételt akkor alkalmazzuk, amikor meg akarjuk határozni:

* egy lista elemeinek összegét,
* egy részhalmazba tartozó elemek (például csak a páros számok, vagy csak a pozitív értékek) összegét,
* például egy osztály tanulói pontszámainak vagy jegyeinek összegét.

**Hogyan lehet felismerni?**

Az összegzés tétel algoritmusában a következő jellemző lépések találhatók:

* Egy változót (pl. `osszeg`, `sum`) kezdetben nullára állítunk.
* Ciklussal végigmegyünk az adathalmazon.
* Minden lépésben vagy minden feltételnek megfelelő elemnél az aktuális értéket hozzáadjuk az összegváltozóhoz.
* A ciklus végére az összegváltozó tartalmazza a kívánt értékek összegét.



## **Eldöntés tétel alkalmazása**


**Miről szól az eldöntés tétel?**

Az eldöntés tétel célja annak megállapítása, hogy egy adott feltétel teljesül-e legalább egy elemre egy sorozatban, listában vagy más adathalmazban. A tétel végén egy logikai (igaz/hamis) értéket kapunk válaszként.

**Mikor alkalmazzuk?**

Az eldöntés tételt akkor használjuk, ha arra vagyunk kíváncsiak, hogy:

* van-e olyan elem, amely megfelel egy adott feltételnek,
* előfordul-e bizonyos tulajdonságú adat az adathalmazban.

Példák:

* Van-e az osztályban elégtelen osztályzat?
* Szerepel-e negatív szám egy listában?
* Található-e páros szám egy tömbben?

**Hogyan lehet felismerni?**

Az eldöntés tétel algoritmusának jellemzői:

* Egy logikai változót (pl. `van`, `talalt`, `letezik`) kezdetben hamisra (`False`) állítunk.
* Ciklussal végigmegyünk az adathalmazon.
* Minden lépésben ellenőrizzük a feltételt.
* Ha valamelyik elemre teljesül a feltétel, a logikai változót igazra (`True`) állítjuk, és az esetek többségében a ciklus megszakítható (nem kötelező, de hatékonyabb).



## **Kiválasztás tétel alkalmazása**



**Miről szól a kiválasztás tétel?**

A kiválasztás tétel célja, hogy **megtaláljunk egy olyan elemet egy adathalmazban, amely megfelel egy adott feltételnek**, és amelyről előzetesen **biztosan tudjuk, hogy létezik**. A tétel eredménye maga az elem, vagy annak helye (például indexe).

**Mikor alkalmazzuk?**

A kiválasztás tételt akkor alkalmazzuk, ha:

* a feldolgozandó adathalmazban garantáltan van olyan elem, amely kielégíti a keresett feltételt,
* és konkrétan szükség van **egy** ilyen elem megtalálására, nem pusztán annak eldöntésére, hogy létezik-e.

Példák:

* Egy osztály jegyei között ki kell választani az első jeles osztályzatot.
* Egy tömbből ki kell választani egy olyan számot, amely osztható 4-gyel.
* Egy szöveges listából meg kell adni egy „B” betűvel kezdődő nevet, ha tudjuk, hogy van ilyen.

**Hogyan lehet felismerni?**

A kiválasztás tétel algoritmusának jellemző elemei:

* Ciklus segítségével bejárjuk az elemeket.
* Minden elemre megvizsgáljuk, hogy teljesíti-e az adott feltételt.
* Amint ilyet találunk, az elem értékét vagy indexét eltároljuk.
* A ciklus gyakran megszakítható, de nem kötelező.


## **Keresés tétel alkalmazása**


**Miről szól a keresés tétel?**

A keresés tétel célja, hogy **megtaláljunk egy olyan elemet egy sorozatban vagy adathalmazban, amely megfelel egy megadott feltételnek**. A keresés során **nem biztos, hogy létezik ilyen elem**, ezért a tétel végeredménye lehet egy sikeres találat (az elem vagy annak helye), vagy az, hogy nem található ilyen.

**Mikor alkalmazzuk?**

A keresés tételt akkor alkalmazzuk, ha:

* szeretnénk megtalálni egy feltételnek megfelelő elemet,
* **nem tudjuk előre**, hogy létezik-e ilyen elem,
* a keresés eredménye fontos a további feldolgozás szempontjából.

Példák:

* Egy számsorozatban keressük az első negatív számot.
* Egy névsorban keressük, hogy van-e "Anna" nevű személy.
* Egy dolgozatjegyek listájában keressük, van-e 1-es.

**Hogyan lehet felismerni?**

A keresés tétel algoritmusának jellegzetes lépései:

* Egy logikai változót (pl. `talalt`) induláskor hamisra állítunk.
* Egy ciklus segítségével bejárjuk az adatokat.
* Minden elemnél ellenőrizzük, hogy teljesíti-e a feltételt.
* Ha igen:

  * eltároljuk az elem értékét vagy indexét,
  * a logikai változót igazra állítjuk,
  * a ciklust gyakran megszakítjuk.
* A feldolgozás végén a logikai változó értéke jelzi, hogy sikeres volt-e a keresés.


## **Maximum tétel alkalmazása**

**Miről szól a maximum tétel?**

A maximum tétel célja, hogy **meghatározzuk egy adathalmaz legnagyobb elemét**. Az algoritmus során végigvizsgáljuk a sorozat minden elemét, és megkeressük azt, amelyiknél nincs nagyobb. A tétel eredményeként vagy a legnagyobb értéket kapjuk meg, vagy annak helyét (indexét), attól függően, hogy milyen célból alkalmazzuk.

**Mikor alkalmazzuk?**

A maximum tételt akkor használjuk, ha:

* egy adatsorozatban a legnagyobb értéket keressük,
* szükség van a legnagyobb elem konkrét értékére vagy annak pozíciójára,
* például statisztikai elemzéseknél, rangsorolásoknál, értékeléseknél.

Példák:

* Egy dolgozatpontszám-listában meg kell határozni a legmagasabb pontszámot.
* Egy napi hőmérsékleti adatsorban meg kell keresni a legmelegebb nap értékét.
* Egy árlistából meg kell találni a legdrágább termék árát vagy annak indexét.

**Hogyan lehet felismerni?**

A maximum tétel algoritmusa az alábbi jellemző lépésekből áll:

1. A sorozat első elemét kiindulási maximumként eltároljuk (pl. `max = lista[0]`).
2. Végiglépkedünk a többi elemen egy ciklus segítségével.
3. Minden egyes lépésnél összehasonlítjuk az aktuális elemet a jelenlegi maximumértékkel.
4. Ha találunk nagyobb értéket, akkor azt eltároljuk új maximumként.
5. A ciklus végére a változó tartalmazza a legnagyobb értéket.

Amennyiben a maximum érték **helyére (indexére)** is szükség van, akkor az algoritmus során külön változóban tároljuk az aktuális maximum **indexét is**, és azt is frissítjük, ha új maximumot találunk.

Fontos: a maximum tétel csak akkor használható biztonságosan, ha az adathalmaz **nem üres**. Üres lista esetén hibakezelést kell alkalmazni.


## **Minimum tétel alkalmazása**



**Miről szól a minimum tétel?**

A minimum tétel célja, hogy **megtaláljuk egy adatsorozat legkisebb elemét**. Az algoritmus során végigvizsgáljuk az összes elemet, és kiválasztjuk azt, amelyiknél nincs kisebb. A végeredmény lehet maga a legkisebb érték, vagy az adott érték helye (például az indexe) az adathalmazon belül.

**Mikor alkalmazzuk?**

A minimum tételt akkor használjuk, ha:

* egy lista vagy sorozat legkisebb értékét keressük,
* az elem értéke vagy annak pozíciója fontos a további feldolgozás során.

Példák:

* Egy tanulói jegyek listájából meg kell határozni a legalacsonyabb osztályzatot.
* Egy árlistából ki kell választani a legolcsóbb termék árát.
* Egy sportversenyen rögzített idők közül meg kell keresni a leggyorsabb versenyző eredményét.

**Hogyan lehet felismerni?**

A minimum tétel algoritmusa nagyon hasonló a maximum tételhez, csak a legkisebb értékre koncentrál:

1. A sorozat első elemét tekintjük kezdeti minimumnak (pl. `min = lista[0]`).
2. Végigmegyünk a többi elemen ciklus segítségével.
3. Minden lépésben összehasonlítjuk az aktuális elemet az eddigi minimumértékkel.
4. Ha kisebb értéket találunk, frissítjük a minimum változót.
5. A ciklus végén a minimum változó tartalmazza a legkisebb értéket.

Ha az érték **helyét is** szeretnénk megtudni (például hogy hányadik elem a legkisebb), akkor külön változóban tároljuk az aktuális minimum indexét is, és azt is frissítjük, ha új kisebb értéket találunk.

A minimum tétel alkalmazásának előfeltétele, hogy az adatsor **legalább egy elemet tartalmazzon**. Üres adathalmaz esetén nem lehet minimumot meghatározni – ilyenkor külön hibakezelést kell beépíteni.

A minimum tétel a maximum tétel párjaként is gyakran előfordul, például amikor az adathalmaz szélső értékeit keressük (minimum és maximum egyaránt).


# **2. Haladóbb lineáris tételek**

## **Szétválogatás tétel alkalmazása**


**Miről szól a szétválogatás tétel?**

A szétválogatás tétel célja, hogy **egy adathalmaz elemeit több csoportra bontsuk egy adott feltétel alapján**. Az algoritmus minden elemet megvizsgál, és a feltétel teljesülésétől függően más-más halmazba (pl. listába) helyez. A tétel során tehát nem elég csak megvizsgálni az elemeket, hanem **szervezetten különválasztjuk őket**.

**Mikor alkalmazzuk?**

A szétválogatás tételt akkor alkalmazzuk, ha:

* az adathalmaz elemeit szeretnénk több csoportba sorolni,
* például két (vagy több) új listát szeretnénk létrehozni, attól függően, hogy az egyes elemek megfelelnek-e egy adott tulajdonságnak.

Példák:

* Egy egész számokat tartalmazó listából különválogatjuk a páros és páratlan számokat.
* Egy névsorban szétválogatjuk a fiú- és lányneveket.
* Egy osztály tanulói közül külön listába tesszük a legalább elégséges és az elégtelen jegyet szerzett tanulókat.

**Hogyan lehet felismerni?**

A szétválogatás tétel algoritmusa az alábbi lépésekből épül fel:

1. Létrehozunk legalább két új, üres listát (pl. `A` és `B`), amelyekbe az elemek kerülni fognak.
2. Egy ciklus segítségével végigmegyünk az eredeti adathalmazon.
3. Minden egyes elemre megvizsgáljuk, hogy teljesíti-e a feltételt.
4. A feltétel teljesülése szerint az elemet az egyik vagy a másik listába helyezzük.
5. A ciklus végén az új listák tartalmazzák az eredeti adatok különválogatott részeit.

A szétválogatás során **minden elem** szerepel valamelyik új listában – egy elem **egy listába kerül**, és nem veszhet el.

A szétválogatás tétel különösen hasznos adatok csoportosítására, előfeldolgozására, illetve strukturáltabb feldolgozáshoz (pl. statisztikai számításokhoz, további elemzésekhez). Több feltétel alkalmazása esetén bővíthető három vagy több részhalmazra is.



## **Csoportosítás tétel alkalmazása**


**Miről szól a csoportosítás tétel?**

A csoportosítás tétel célja, hogy **egy adathalmaz elemeit több, egymástól jól elkülöníthető csoportba rendezzük**, egy meghatározott szempont vagy kategória szerint. Ellentétben a szétválogatás tétellel, ahol általában két részhalmazba soroljuk az elemeket, a csoportosítás során **több különálló kategóriát** is kezelünk – például évfolyamok, jegyek, kezdőbetűk vagy típusok szerint.

**Mikor alkalmazzuk?**

A csoportosítás tételt akkor használjuk, ha:

* az adatok között **többféle osztályozási kategória** van jelen,
* szeretnénk egy listán belül az elemeket logikailag elkülönített csoportokba sorolni,
* a csoportosított adatokra külön feldolgozást, statisztikát vagy megjelenítést tervezünk.

Példák:

* Egy tanulói jegylistában az osztályzatokat csoportosítjuk jegyenként (pl. hány 1-es, 2-es, stb.).
* Egy terméklistát kategóriák (pl. élelmiszer, elektronika, ruházat) szerint csoportosítunk.
* Egy névsorban az embereket a nevük kezdőbetűje alapján csoportosítjuk (A–B–C…).

**Hogyan lehet felismerni?**

A csoportosítás tétel algoritmusa általában a következő lépésekből áll:

1. Létrehozunk több csoportot képviselő adatszerkezetet (pl. több lista vagy egy szótár, amely kulcsként a csoport nevét, értékként a hozzá tartozó elemek listáját tartalmazza).
2. Ciklussal végigmegyünk az eredeti adathalmazon.
3. Minden elemnél meghatározzuk, melyik csoportba tartozik (pl. egy jellemző érték alapján).
4. A megfelelő csoporthoz hozzáadjuk az elemet.
5. A ciklus végére minden csoport listája tartalmazza a neki megfelelő elemeket.

A csoportosítás tétel tehát **nemcsak kettéoszt**, mint a szétválogatás, hanem **tetszőleges számú csoportba sorol**. A gyakorlatban sokszor használunk hozzá **kulcs–érték párokat** (pl. Python szótár, JavaScript objektum, adatbázis táblák), mivel ezekkel hatékonyan kezelhetők a dinamikusan kialakuló kategóriák.

Ez a tétel fontos alapja például adatelemzésnek, statisztikai feldolgozásnak, vizualizációk előkészítésének vagy éppen riportkészítésnek.


## **Összefuttatás tétel alkalmazása**

**Miről szól az összefuttatás tétel?**

Az összefuttatás tétel célja, hogy **két rendezett (általában növekvő vagy csökkenő sorrendű) sorozatból egy harmadik, szintén rendezett sorozatot hozzunk létre**, amely tartalmazza az eredeti listák összes elemét. Az algoritmus **kihasználja az eredeti sorozatok rendezettségét**, így hatékonyabb, mint ha az összefűzött listát újra rendeznénk.

**Mikor alkalmazzuk?**

Az összefuttatás tételt akkor használjuk, ha:

* két **rendezett** listát szeretnénk egyetlen **szintén rendezett** listába egyesíteni,
* fontos a hatékony működés, például nagy adathalmazok összeolvasztásánál,
* nem akarjuk külön újrarendezni az összeillesztett listát.

Példák:

* Két rendezett tanulói névsort összevonunk egy közös névsorrá, úgy hogy az új lista is ábécérendben legyen.
* Két napon rögzített, időrendbe tett eseménylistát egyetlen időrendi sorrendbe illesztünk.
* Rendezett pontszámlistákból készítünk egy közös rangsort.

**Hogyan lehet felismerni?**

Az összefuttatás tétel algoritmusa jellemzően így néz ki:

1. Két külön rendezett listával dolgozunk (pl. `A` és `B`).
2. Létrehozunk egy üres listát (`C`), ahová az eredményt építjük.
3. Két indexet használunk (`i` és `j`), amelyek az `A` és `B` listák aktuális pozícióját jelzik.
4. Egy ciklus segítségével addig hasonlítjuk össze a `A[i]` és `B[j]` elemeket, amíg az egyik lista végére nem érünk.

   * A kisebbik elemet hozzáadjuk `C`-hez, és az adott listában léptetjük az indexet.
5. Ha az egyik lista elfogyott, a másik listából a fennmaradó elemeket **változtatás nélkül** hozzáfűzzük `C`-hez.
6. A végén `C` tartalmazza a teljes, rendezett sorozatot.

**Megjegyzés:** Ha a két lista **ismétlődő elemeket** is tartalmazhat, de a végeredményben **nem szeretnénk duplikációt**, akkor a ciklus során külön ellenőrzést építünk be, amely kiszűri az ismétlődő elemeket.

Az összefuttatás tétel az alapja a **merge sort** nevű hatékony rendezési algoritmusnak is. Fontos előfeltétel, hogy az eredeti két lista **rendezett legyen** – ha nem az, akkor előbb külön rendezésre van szükség.


## **Rendezés tétel alkalmazása**


**Miről szól a rendezés tétel?**

A rendezés tétel célja, hogy **egy adathalmaz elemeit meghatározott sorrendbe állítsuk**, általában növekvő vagy csökkenő sorrend szerint. Az algoritmus során az elemeket egymással összehasonlítjuk, és helyet cserélünk, ha szükséges, hogy a kívánt sorrend kialakuljon. A rendezés eredménye egy új vagy módosított lista, amelyben az elemek rendezetten követik egymást.

**Mikor alkalmazzuk?**

A rendezés tételt akkor alkalmazzuk, ha:

* egy adatsorozatot áttekinthetőbbé vagy feldolgozhatóbbá szeretnénk tenni,
* szükség van a legkisebb, legnagyobb vagy középső elemek gyors megtalálására,
* az adatokat rendezetten kell megjeleníteni (pl. névsor, árlista, pontszámok szerint).

Példák:

* Egy osztály tanulóinak pontszámait növekvő sorrendbe rendezzük.
* Egy terméklistát ár szerint sorba állítunk.
* Egy névsort ábécérendbe helyezünk.

**Hogyan lehet felismerni?**
A rendezés tétel felismerhető, ha:

* az algoritmus **több összehasonlítást** és **helycserét** hajt végre az elemek között,
* a cél a teljes adathalmaz sorrendbe állítása, nem csak egy elem megtalálása,
* az eredmény: **ugyanazok az elemek, de más sorrendben**.

**Algoritmikus jellemzők:**

1. Egy külső és belső ciklus segítségével az elemeket egymáshoz viszonyítva vizsgáljuk.
2. Ha az elemek nem a megfelelő sorrendben vannak, akkor **helyet cserélünk**.
3. Ezt a folyamatot addig ismételjük, amíg az egész lista a kívánt sorrendben nem lesz.

**Példák rendezési módszerekre:**

* Buborékrendezés (Bubble sort): egymás melletti elemeket hasonlít össze, és szükség esetén cserél.
* Minimumkiválasztásos rendezés (Selection sort): minden körben kiválasztja a legkisebbet, és a megfelelő helyre teszi.
* Beillesztéses rendezés (Insertion sort): elemenként építi fel a rendezett részt.
* Beépített nyelvi rendezők (pl. Python `sorted()`, JavaScript `array.sort()`).

**Fontos megjegyzés:**

A rendezés tétel gyakran más algoritmusok előkészítő lépéseként jelenik meg. Például ha egy összefuttatást vagy bináris keresést szeretnénk alkalmazni, előbb rendezni kell az adatokat. A választott rendezési módszer függ az adathalmaz méretétől, típusától, és a program nyelvi környezetétől.
