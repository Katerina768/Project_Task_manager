ukoly = []

# def hlavni_menu()
def hlavni_menu():
    menu = ["1. Přidat nový úkol", 
         "2. Zobrazit všechny úkoly", 
         "3. Odstranit úkol", 
         "4. Konec programu"]

    print("Správce úkolů - Hlavní menu")
    for ukol in menu:
     print(ukol)

    user_input = int(input("Vyberte možnost (1-4): "))          
    
    if user_input == 1:
             print("")
             pridat_ukol()

    elif user_input == 2:
             print("")
             zobrazit_ukoly()

    elif user_input == 3:
             print("")
             odstranit_ukol()

    elif user_input == 4:
             print("")
             konec_programu()

    else: 
        print("Zadaná volba je neplatná. Prosím vyplňte znovu.")
        print("")
        hlavni_menu()
            
# def pridat_ukol()
def pridat_ukol():
      
        user_task_1 = str(input("Zadejte název úkolu: "))
        user_task_2 = str(input("Zadejte popis úkolu: "))
       
           
        if user_task_1 == "" or user_task_2 == "": 
            print("Zadaný název nebo popis je prázdný. Prosím vyplňte.")
            print("")
            pridat_ukol()
        else:
            print(f"Úkol '{user_task_1}' byl přidán.")
            ukoly.append((user_task_1, user_task_2))
                                      
            print("")
            
            hlavni_menu()

 # def zobrazit_ukoly()             
def zobrazit_ukoly():
    global ukoly
    print("Seznam úkolů:")
    for i, (user_task_1, user_task_2) in enumerate(ukoly, start=1):
        print(f"{i}. {user_task_1} - {user_task_2}")

    print("")
    hlavni_menu()

# def odstranit_ukol()
def odstranit_ukol():
    
    cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
     
    if 1 <= cislo <= len(ukoly):
            odstraneno=ukoly.pop(cislo -1)
            print(f"Úkol '{odstraneno[0]}' byl odstraněn.")
            print("")
    else: 
            print("Neexistující úkol. Vyberte prosím znovu. ")
            odstranit_ukol()

    hlavni_menu()

# def konec_programu()
def konec_programu():
      print("Konec programu.")
      print("")


# volání funkce hlavni_menu()
      
hlavni_menu()




