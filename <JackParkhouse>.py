def attacking_animals():
        import random
        being_attacked = 1
        dragon = 1
        living = 1
        bear_health = 40
        eagle_health = 50
        moose_health = 70
        tiger_health = 60
        tyranisourous_rex_health = 100
        snake_health = 30
        life = 50
        while being_attacked == 1 and dragon > 0 and living == 1:
            animals = ["bear", "eagle", "moose", "tiger", "tyranisourous rex", "snake"]
            print ("Before the bear attacks you quick reflexes draw your sword and slash the bear. You take 10 life from the bear. Other animals ready to strike are an eagle, moose, tiger, tyranisourous rex, and a snake.")
            print ("bear health = " + str(bear_health))
            print ("eagle health = " + str(eagle_health))
            print ("moose health = ") + str(moose_health)
            print ("tiger health = ") + str(tiger_health)
            print ("tyranisourous rex health = ") + str(tyranisourous_rex_health)
            print ("snake health = ") + str(snake_health)
            print ("Your life = ") + str(life)
            info = raw_input("What would you like to attack?")
            while len(animals) > 0:
                if life < 0:
                    living = 1
                if info == "snake" or info == "attack snake" or info == "kill snake":
                    damage = random.randint(0, snake_health)
                    snake_health = snake_health - damage
                    givin = random.randint(0, 10)
                    life = life - givin
                    if snake_health == 0:
                        info = raw_input("you killed the snake. Press enter")
                        animals.remove("snake")
                    info = raw_input("you attack the snake and deal " + str(damage) + " damage but were dealt " + str(givin) + " damage. Press enter")
                if info == "bear" or info == "attack bear" or info == "kill bear":
                    damage = random.randint(0, bear_health)
                    bear_health = snake_health - damage
                    givin = random.randint(0, 15)
                    life = life - givin
                    if bear_health == 0:
                        info = raw_input("you killed the bear.")
                        animals.remove("bear")
                    info = raw_input("you attack the bear and deal " + str(damage) + " but were dealt" + str(givin) + (" damage. Press enter."))
                if info == "eagle" or info == "attack eagle" or info == "kill eagle":
                    damage = random.randint(0, eagle_health)
                    eagle_health = snake_health - damage
                    givin = random.randint(0, 15)
                    life = life - givin
                    if eagle_health == 0:
                        info = raw_input("you killed the eagle.")
                        animals.remove("eagle")
                    info = raw_input("you attack the eagle and deal " + str(damage) + " but were dealt " + str(givin) + " damage ")
                if info == "moose" or info == "attack moose" or info == "kill moose":
                    damage = random.randint(0, moose_health)
                    moose_health = snake_health - damage
                    givin = random.randint(0, 20)
                    life = life - givin
                    if moose_health == 0:
                        info = raw_input("you killed the moose.")
                        animals.remove("moose")
                    print ("you attack the moose and deal " + str(damage) + " but were dealt " + str(givin))
                if info == "tiger" or info == "attack tiger" or info == "kill tiger":
                    damage = random.randint(0, tiger_health)
                    tiger_health = snake_health - damage
                    givin = random.randint(0, 18)
                    life = life - givin
                    if tiger_health == 0:
                        info = raw_input("you killed the tiger.")
                        animals.remove("tiger")
                    print ("you attack the tiger and deal " + str(damage) + " but were dealt " + str(givin))
                if info == "tyranisourous rex" or info == "attack tyranisourous rex" or info == "kill tyranisourous rex":
                    damage = random.randint(0, tyranisourous_rex_health)
                    tyranisourous_rex_health = snake_health - damage
                    givin = random.randint(0, 30)
                    life = life - givin
                    if tyranisourous_rex_health == 0:
                        info = raw_input("you killed the tyranisourous rex.")
                        animals.remove("tyranisourous rex")
                    print ("you attack the tyranisourous rex and deal " + str(damage) + " but were dealt " + str(givin))


def dragon_room():
    dragon = 1
    attack = 0
    location = 1
    being_attacked = 0
    import random
    info = raw_input("You have entered a room with a dragon sleeping on a pile of treasure to the north. he is surrounded by statues of other creatures. A sword,  bow and arrow, and axe are also on the floor. The dragon could wake up at the slightest movement. you will have to sneak to move. press enter")
    while dragon == 1 and being_attacked == 0:
        info = raw_input("what will you do?")
        if info == "talk":
            info = raw_input("You start to talk to the dragon and he wakes up. He looks at you and says 'you dare awake me?' His eye's turn puple and the statues come to life. A bear attacks from the left  ")
            being_attacked = 1
        elif info == ("take bow"):
            print ("type 'take all' this will allow you to pick up the sword, axe, and bow.")
        elif info == ("take axe"):
            print ("type 'take all' this will allow you to pick up the sword, axe, and bow.")
        elif info == ("take sword"):
            print ("type 'take all' this will allow you to pick up the sword, axe, and bow.")
        elif info == ("pick up bow"):
            print ("type 'take all' this will allow you to pick up the sword, axe, and bow.")
        elif info == ("pick up sword"):
            print ("type 'take all' this will allow you to pick up the sword, axe, and bow.")
        elif info == ("pick up pick up axe"):
            print ("type 'pick up all' this will allow you to pick up the sword, axe, and bow.")
        elif info == "pick up all" or info == "take all":
            if attack == 0 and location == 1:
                print ("you picked up all three weapons")
                attack = 3
            elif location == 2:
                print("You try picking up as much as you can but the dragon awakes and while you are occupied brings to life the statues around him. You are killed in a bloodbath of claws, talons, and scaled you die")
                dragon = 1
            else:
                print ("there is nothing to pick up.")
        elif info == "sneak":
            if location == 1:
                print ("You sneak and are able to get to the treasure.")
                location = 2
            else:
                print ("you sneaked back to the first location")
                location = 1
        elif info == "south":
            if location == 2:
                print ("you try to move south but the dragon awaks an before you know what happens you are killed.")
            else:
                ("you can't move that way")
        elif info == "attack":
            if attack == 3 and location == 2:
                print ("say what you would like to attack with")
            elif attack == 3 and location == 1:
                print ("you can only attack with the bow and arrow. say 'attack with bow'")
            else:
                print ("There is nothing to attack with")
        elif info == "north":
            if location == 1:
                print ("You try moving towads the dragon but he awakes and using his purple eyes summons the statues to life. A bear attacks you.")
                being_attacked = 1
            else:
                print ("you can't move that way.")
        elif info == "attack with bow":
            if attack == 3:
                print ("You shoot a bow and arrow. You have incredible aim and hit the dragon in the eye. The dragon is injured but brings to life every statue around. A bear attacks from the left.")
                if location == 1:
                    dragon = .5
                    being_attacked = 1
                else:
                    dragon = .45
                    being_attacked = 1
            else:
                print ("you do not have a bow")
        elif info == "attack with sword":
            if location == 1 and attack == 3:
                print ("you are to far away to attack with a sword")
            if location == 1 and attack == 0:
                print ("you do not have a sword")
            if location == 2 and attack == 0:
                print ("you do not have a sword")
            if location == 2 and attack == 3:
                print ("you attack with your sword. The dragon cries in anguish and brings to life every statue. A bear attacks from you left.")
                being_attacked = 1
                dragon = .25
        elif info == "attack with axe":
            if location == 1 and attack == 3:
                print ("you are to far away to attack with an axe")
            if location == 1 and attack == 0:
                print ("you do not have an axe")
            if location == 2 and attack == 0:
                print ("you do not have an axe")
            if location == 2 and attack == 3:
                print ("you attack with your axe. The dragon cries in anguish and brings to life every statue. A bear attacks from you left.")
                being_attacked = 1
                dragon = .25
        elif info == "kill dragon":
            print ("type 'kill with' and what you would like to use")
        elif info == "kill":
            print (" what would you like to kill with?")
        elif info == "kill with bow" or info == "attack with bow" or info == "use bow":
            if attack == 3:
                print ("You shoot a bow and arrow. You have incredible aim and hit the dragon in the eye. The dragon is injured but brings to life every statue around. A bear attacks from the left.")
                if location == 1:
                    dragon = .5
                    being_attacked = 1
                else:
                    dragon = .45
                    being_attacked = 1
            else:
                print ("you do not have a bow")
        elif info == "kill with axe" or info == "attack with axe" or info == "use axe":
            if location == 1 and attack == 3:
                print ("you are to far away to attack with an axe")
            if location == 1 and attack == 0:
                print ("you do not have an axe")
            if location == 2 and attack == 0:
                print ("you do not have an axe")
            if location == 2 and attack == 3:
                print ("you attack with your axe. The dragon cries in anguish and brings to life every statue. A bear attacks from you left.")
                being_attacked = 1
                dragon = .25
        elif info == "kill with sword" or info == "attack with sword" or info == "use sword":
            if location == 1 and attack == 3:
                print ("you are to far away to attack with a sword")
            if location == 1 and attack == 0:
                print ("you do not have a sword")
            if location == 2 and attack == 0:
                print ("you do not have a sword")
            if location == 2 and attack == 3:
                print ("you attack with your sword. The dragon cries in anguish and brings to life every statue. A bear attacks from you left.")
                being_attacked = 1
                dragon = .25
        else:
            print ("I can't do that.")

    while being_attacked == 1 and dragon > 0:
        attacking_animals()
        dragon = 0
    if dragon == 0:
        print ("you killed the dragon.")
    else:
        ("you died")
dragon_room()
