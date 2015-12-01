
import random

hp = 10
fistdmg = 1
stickdmg = 2
rockdmg = 4
sgoblin = 4

def rooms():
    hp = 10
    fistdmg = 1
    stickdmg = 2
    rockdmg = 4
    sgoblindmg = 2

    print "You are trapped in a damp, old, cobblestone room with a iron door looking as if it is locked."
room1 = (raw_input("You are trapped in a damp, old, cobblestone room with a iron door looking as if it is locked. Type 1 to give the door a push, type 2 to look for a key, and type 3 to sit there and do nothing."))

if room1 == "1":

    room2 = (raw_input("The door flies open and there is a stick and a rock. Do you take either?"))

    if room2 == "take stick":
        print "Stick taken"
    stick = 1

    if room2 == "take rock":
        print "Rock taken"
    rock = 1
    if room2 == "take stick" or "take rock":
        room21 = (raw_input("There is a sign that says, 4 path crossway. There is a door to the east, north, and west."))

        if room21 == "east":
            print "You are at the foot of a mountain with a path heading upward."
            cliffs = (raw_input("Do you head up the path, or do you go back to the 4 path crossway. (path) or (crossway) "))
            if cliffs == "path":
                cliffse1 = (raw_input("You head up the path to find a small goblin. Do you attack it? (Hint type attack with rock/stick for more damage) "))
            if cliffse1 == "attack":
                    sgoblin = sgoblin - fistdmg
                    hp = hp - sgoblindmg
                    print "You hit the goblin for 1 damage!"
                    print "You lost 2 hp points from the goblin.."
                    if sgoblin in range(1, 4):
                        rekill1 = (raw_input("The goblin is still alive, attack again!!"))
                        print "You hit the goblin for 1 damage!"
                        print "You lost 2 hp points from the goblin.."
                    sgoblin = sgoblin - fistdmg
                    hp = hp - sgoblindmg
                    if sgoblin in range(1, 4):
                            rekill1 = (raw_input("The goblin is still alive, attack again!!"))
                            print "You hit the goblin for 1 damage!"
                            print "You lost 2 hp points from the goblin.."
                    sgoblin = sgoblin - fistdmg
                    hp = hp - sgoblindmg
                    if sgoblin in range(1, 4):
                                rekill1 = (raw_input("The goblin is still alive, attack again!!"))
                                print "You hit the goblin for 1 damage!"
                                print "You lost 2 hp points from the goblin.."
                    sgoblin = sgoblin - fistdmg
                    hp = hp - sgoblindmg
                    if sgoblin == 0:
                        print "You have slain the goblin!(You have 2 hp left)"
                        love = (raw_input("You suddenly are struck with a vicious headache, do you love minions? Your options are yes, no, or maybe"))
                        if love == "yes":
                            print "You are teleported home, your family is there waiting for you."
                        if love == "no":
                            print "You will witness endless years of pain and torture in the end"
                        if love == "maybe":
                            print "Ehhh, good enough I suppose, you are teleported home."
            if cliffse1 == "attack with stick":
                sgoblin = sgoblin - stickdmg
                hp = hp - sgoblindmg
                print "You hit the goblin for 2 damage!"
                print "You lost 2 hp points from the goblin.."
                if sgoblin in range(1, 4):
                    rekill2 = (raw_input("The goblin is still alive, attack again!!"))
                    print "You hit the goblin for 2 damage!"
                    print "You lost 2 hp points from the goblin.."
                    print "You have slain the goblin!(You have 6 hp left)"
                    love = (raw_input("You suddenly are struck with a vicious headache, do you love minions? Your options are yes, no, or maybe"))
                    if love == "yes":
                        print "You are teleported home, your family is there waiting for you."
                    if love == "no":
                        print "You will witness endless years of pain and torture in the end"
                    if love == "maybe":
                        print "Ehhh, good enough I suppose, you are teleported home."
            if cliffse1 == "attack with rock":
                sgoblin = sgoblin - rockdmg
                print "You hit the goblin for 4 damage!"
                print "You lost 0 hp points from the goblin"
                print "You have slain the goblin without taking a single point of damage!!(You have 10 hp left)"
                love = (raw_input("You suddenly are struck with a vicious headache, do you love minions? Your options are yes, no, or maybe"))
                if love == "yes":
                    print "You are teleported home, your family is there waiting for you."
                if love == "no":
                    print "You will witness endless years of pain and torture in the end"
                if love == "maybe":
                    print "Ehhh, good enough I suppose, you are teleported home."

        if room21 == "north":
            print "You enter the room and you suddenly feel a sharp pain in your side."
            print "You black out..."
        if room21 == "west":
            print "You see a troll, it is the last thing you see..."
if room1 == "2":
    print "You look around for a key, but to no prevail."
    return rooms
if room1 == "3":
    print "You sit there starving, hopeless and lazy."
    return rooms
