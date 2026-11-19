work_days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

def check_day_capacity(chosen_day):
    data = open(r"C:\Users\__uness\Documents\python\DocNotifyAI\appointments.txt", "r").read()
    count_clients = data.count(chosen_day)
    limit = 20 if chosen_day == "Friday" else 40

    if count_clients >= limit:
        print("Ce jour est plein")
        for day in work_days:
            day_limit = 20 if day == "Friday" else 40
            if data.count(day) < day_limit:
                print(f"Votre rendez-vous est déplacé automatiquement vers {day}")
                return day
        print("Tous les jours sont pleins")
        return None
    else:
        return chosen_day
    