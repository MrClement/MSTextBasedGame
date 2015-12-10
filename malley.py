powerlevel = 0

def torture_chamber():
    print "you find yourself on a table and a legendary sword is on the floor"
    hs = raw_input("take sword y/n")

    if hs == "y":
        print "you slay the Laser Sxorpion in a way so brutal it is instantly posed on heavyr"
        powerlevel = powerlevel + 100
    else:
        print "The sword dissapears and you are trapped in room forever"
def Act1():
    act1 = raw_input("The Laser_Sxorpion appears! fight or run")



    if act1 == "fight":
        print "the Laser_Sxorpion shoots you and you black out"
        print "you wake up in a torture chamber"
        torture_chamber()

    else:
        print "you trip and the sxorpion readies his stinger Prepare for the precision incision"

def Laser_Sxorpion():

    Act1()


Laser_Sxorpion()
