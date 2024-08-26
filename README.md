# Conwayova hra života
Conwayova hra života je jeden z nejslavnějších buňečných automatů, který vytvořil britský matematik John Horton Conway (1937 - 2020) v roce 1970. Jde o simulaci, kdy máme síť buněk, která se vyvíjí v čase. Buňka se může nacházet ve dvou stavech, živá nebo mrtvá, tento stav se pak mění na základě pravidel níže, kde za sousední buňky považujeme osm okolních buněk.
### Pravidla vývoje
- každá živá buňka s méně než dvěma živými sousedy umírá
- každá živá buňka s dvěma nebo třema živými sousedy zůstává žít
- každá živá buňka s více než třema živými sousedy umírá
- každá mrtvá buňka s třema živými sousedy ožívá

# Uživatelská dokumentace
### Spuštění
Pro spuštění je třeba mít nainstalovaný Python, ve kterém po stažení a otevření souboru **hra_zivota.py** musíme ještě nainstalovat knihovny NumPy a Pygame (pomocí příkazů "*pip install numpy*" a "*pip install pygame*"). Poté se nám hra spustí v novém okně po zadání příkazu "*python hra_zivota.py*".
### Ovládání
- buňky můžeme oživovat kliknutím levým tlačítkem myši
- mezerníkem simulaci spouštíme a pozastavujeme
- simulaci ukončíme uzavřením okna
