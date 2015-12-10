def roomSelection():
    print "There are three doors. One to you left, forward, and right. Which door do you want to go through: "
    input = raw_input()
    if input == "left":
        print "You were engulfed by flames. Game over"

    if input == "forward":
        print "The door is locked. You can not enter. There are three doors. One to you left, forward, and right. Which door do you want to go through: "
        print "LOL YOU DIED!"
    if input == "right":
        print "You have fallen down a cliff and into a lake. There is a cave 15 feet up the cliff. The lake also empties into a calm river."
        if input == "climb cliff":
            print "You are at the entrace of the cave. The rest of the cliff is unclimable. What would you like to do from here? "
            if input ==  "enter cave":
                print "You have entered the cave. There is a lamp, a supply of food for a week, keys, and a bow and arrow. What would you like to do from here? "
