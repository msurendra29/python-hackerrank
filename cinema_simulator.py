films = {
    "Finding Dory":{"age_limit":5,"seats_available":5},
    "World Warz":{"age_limit":10,"seats_available":5},
    "Passengers":{"age_limit":12,"seats_available":5},
    "Rogue One":{"age_limit":12,"seats_available":5},
    "Befikre":{"age_limit":15,"seats_available":5}
    }
while True:
    choice = input("Which movie do you want to see?: ").strip().title()
    if(choice in films):
        age = int(input("Please enter your age: "))
        if (age > films[choice]["age_limit"]):
            if(films[choice]["seats_available"] > 0):
               print("Enjoy the film!")
               films[choice]["seats_available"] = films[choice]["seats_available"] - 1
            else:
               print("Sorry!, sold out!")
        else:
               print("you are not young enough to watch the film.")
    else:
               print("We don't have the film")
    
