from security_regex import validate_phone
from ai_scheduler import check_day_capacity


while True:
    print("1. Prendre un rendez-vous\n2. Sortir du systeme")
    choice = input("Please ecrire votre choix : ").strip()
    if choice == "2":
        break
    elif choice == "1":
        name = input("Please ecrire votre nom : ").capitalize().strip()
        kniya = input("Et votre prenoms : ").capitalize().strip()
        age = int(input("Votre Age : ").strip())
        num = input("Votre numero de telephone : ").strip()
        jour = input("Et finalement le jour de votre choix du rendez-vous : ").capitalize().strip()
        if not validate_phone(num):
            print("Votre numero est incorrecte utilise un numero du maroc")
            continue
        final_day = check_day_capacity(jour)
        if final_day is None:
            continue
        datadoc = open(r"C:\Users\__uness\Documents\python\DocNotifyAI\appointments.txt", "a")
        datadoc.write(f"Name : {name} | Prenoms : {kniya} | Age : {age} | Numero : {num} | Day : {final_day}\n")
        datadoc.close()
        
