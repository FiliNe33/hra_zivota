# Technická dokumentace
Program se skládá z jednoho souboru, který obsahuje dvě funkce. Funkce jsou níže lehce popsány. Parametry a proměnné jsou vetšinou jasně pochopitelné z kódu, případně dovysvětlé komentáři v kódu nebo během popisu funkcí.
### Funkce *akt*
Funkce *akt* dostane dvojrozměrné pole jedniček a nul a vytvoří nové pole s aktualizovnými stavy buněk po vývoji dle pravidel. Funkce také přiřadí buňkám barvy a to v zálislosti na parametru *progres*. 
- Je-li tento parametr *True*, přiřadí živým buňkám zlatou, mrtvým stříbrnou, ale navíc i buňkám ožívajícím zlatou a buňkám umírajicím žlutou (to se děje za standartních okolností, když je hra nepozastavená, aby byl lépe viditelný a znázorněný vývoj).
- Je-li tento parametr *False* přiřadí pouze mrtvým buňkám stříbrnou a živým zlatou (to se děje při spuštění nebo zastavení hry, případně během oživování buněk).
### Funkce *main*
Funkce *main* nám zobrazí výchozí obrazovku a poté obsahuje nekonečnou smyčku, která řídí ovládání hry (popsané v uživatelské dokumentaci) a také během spuštěné (nepozastavené) hry aktualizuje obrazovku s buňkami. Po každé iteraci má smyčka 10 milisekund pauzu pro lepší pozorování vývoje a taky aby se příliš nezatížil procesor.
