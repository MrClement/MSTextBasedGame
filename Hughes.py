def street():
    print "There are two buildings. One has an address of 1, and the other, 2. Which building do you want to enter?"
    x = raw_input()
    if x == "1":
        print "You have chosen the correct building."
        return
    else:
        print "You did not choose wisely. You fell into a pit of lava. GAME OVER"
        return
