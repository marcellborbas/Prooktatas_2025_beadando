Projekt leírása:
Ez a projekt egy egyszerű adatkezelő rendszer, amely a PostgreSQL adatbázisba tölt be adatokat egy CSV fájlból, és különböző táblák létrehozását és kezelését végzi.

Fájlok magyarázata:
database.py: Az adatbázis kapcsolati információkat tartalmazó konfigurációs fájl.
models: Az adatbázis táblák modelljei. Minden modell egy-egy táblát reprezentál az adatbázisban.
db_service.py: Az adatbázissal való kommunikációt kezelő szolgáltatás, amely az SQL lekérdezések végrehajtását végzi.
data_loader.py: Az adatbetöltésért felelős szolgáltatás, amely betölti az adatokat a CSV fájlból és elvégzi az adatok beszúrását.
main.py: Az alkalmazás belépési pontja. Itt történik a táblák létrehozása és az adatok betöltése.
select.sql: Tartalmazza az a feladatban megadott lekérdezéseket. Ezeket a lekérdezéseket manuálisan kell végrehajtani az adatbázisban.


Telepítés és futtatás:

Előfeltételek:
Telepítve kell legyen a Python 3.10 + verzió , PostgreSQL és az adatbázis elérhetősége szükséges.

Telepítési lépések:
Klónozd a repository-t: git clone https://github.com/marcellborbas/Prooktatas_2025_beadando.git
Telepítsd a szükséges Python csomagokat: pip install -r requirements.txt

Állítsd be az adatbázis konfigurációját a database.py fájlban. A következő beállítások elérhetők:
dbname: Az adatbázis neve.
user: Az adatbázis felhasználó neve.
password: Az adatbázis felhasználó jelszava.
host: Az adatbázis kiszolgáló címe.
port: Az adatbázis portja (alapértelmezetten: 5432)

Futás során elérhető funkciók:
Táblák létrehozása: A táblák automatikusan létrejönnek a megfelelő SQL parancsok végrehajtásával.
Adatok betöltése: A Denormaliz_lt_HR_adatok.csv fájlban található adatokat betölti a rendszer az adatbázisba.