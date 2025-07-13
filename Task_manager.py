
# Seznam úkolů – každý úkol je slovník s klíči 'nazev' a 'popis'
ukoly = []


# Funkce zobrazí hlavní menu a zpracuje volbu uživatele.
# Nabízí možnosti pro přidání, zobrazení, odstranění úkolu nebo ukončení programu.
def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        menu = [
            "1. Přidat nový úkol", 
            "2. Zobrazit všechny úkoly", 
            "3. Odstranit úkol", 
            "4. Konec programu"
        ]
        for polozka in menu:
            print(polozka)

       # získání volby uživatele 
        volba = input("Vyberte možnost (1-4): ").strip()
        print("")

        # kontrola platnosti vstupu
        if volba not in ("1", "2", "3", "4"):
            print("Zadaná volba je neplatná. Prosím zkuste to znovu.")
            print("")
            continue

        # zpracování volby
        if volba == "1":
            print("")
            pridat_ukol()

        elif volba == "2":
            print("")
            zobrazit_ukoly()

        elif volba == "3":
            print("")
            odstranit_ukol()

        elif volba == "4":
            print("")
            konec_programu()
            break  # ukončení hlavní smyčky a programu
        
        print("")

# Funkce pro přidání nového úkolu do seznamu `ukoly`.
# Uživatel zadá název a popis. Pokud nejsou prázdné, úkol se uloží jako slovník do seznamu `ukoly`.

def pridat_ukol():
    while True:
        # vstup k získání návzvu a popisu od uživatele
        nazev_ukolu = input("Zadejte název úkolu: ").strip()
        popis_ukolu = input("Zadejte popis úkolu: ").strip()

        # kontrola platnosti vstupu a pokud nejsou prázdné, uloží se jako slovník do seznamu `ukoly`.
        if nazev_ukolu == "" or popis_ukolu == "":
            print("Zadaný název nebo popis je prázdný. Prosím vyplňte.")
            print("")
        else:
            novy_ukol = {
                "nazev": nazev_ukolu,
                "popis": popis_ukolu
            }
            ukoly.append(novy_ukol)     # přidání nového úkolu ve formě slovníku do seznamu `ukoly`.
            print(f"Úkol '{nazev_ukolu}' byl přidán.\n")
            break

# Funkce pro zobrazení všech úkolů v seznamu `ukoly`.
# Každý úkol je očíslován a zobrazen s názvem a popisem.

def zobrazit_ukoly():
    if not ukoly:  # pokud je seznam prázdný, zobrazí se pouze oznámení
         print("Seznam úkolů:")
    else:
        print("Seznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):  # zobrazí očíslovaný Seznam  úkolů, který se začíná číslovat od čísla 1 s nazvem a popisem
            print(f"{index}. {ukol['nazev']} - {ukol['popis']}")
    print("")

# Funkce pro odstranění úkolu na základě jeho čísla ze seznamu.
# Pokud seznam úkolů není prázdný, uživatel zadá číslo úkolu ke smazání.
# Funkce ověřuje správnost vstupu a upozorní na chyby.

def odstranit_ukol():
# Pokud je seznam úkolů prázdný, zobrazí zprávu a ukončí funkci,
# protože není žádný úkol, který by bylo možné odstranit.
    if not ukoly:
            print("Seznam úkolů je prázdný. Není co odstranit.\n")
            return
        
    
    zobrazit_ukoly()  # pokud není prázdný seznam `ukoly`, zobrazí se seznam s výpisem úkolů
    
    # Nekonečná smyčka pro zajištění opakovaného dotazování uživatele,
    # dokud nezadá platné číslo úkolu k odstranění.
    while True:
        try:
            # Převedení vstupu od uživatele na celé číslo
            cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo_ukolu <= len(ukoly):  # Kontrola, zda číslo odpovídá existujícímu úkolu v seznamu
                odstraneny_ukol = ukoly.pop(cislo_ukolu - 1)
                print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.\n")
                break # Ukončení smyčky po úspěšném odstranění
            else:
                print("Neexistující číslo úkolu. Zkuste to znovu.\n")  # Upozornění na neexistující číslo úkolu
        except ValueError:
            print("Zadejte platné číslo.\n")  # Ošetření případu, kdy uživatel nezadá číslo (např. zadá text)
    print("")

# Funkce pro ukončení programu s oznámením
def konec_programu():
    print("Konec programu.\n")

# Spuštění hlavního menu při startu aplikace
hlavni_menu()