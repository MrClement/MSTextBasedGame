def reptilians():
    x = 0
    y = True
    while y:

        while x == 0:
            print " "
            reproom = raw_input("You find yourself in dark room. You feel a sharp sting in the back of your neck. Slowly, your vision starts to come back and before you stands a magnificent statue. ")
            if reproom == "forward" or "f":
                print " "

                statue = raw_input("You walk towards the statue and there is a word scratched into the base in an unreadable script. The letters begin to jumble themselves together and you can finally read what it says, 'To our lord and savior Leafy'. Suddenly, you hear hisses all around you. 'Hiss' 'hiss' 'hiss'. What do you do? ")
                if statue == "attack":
                    print " "
                    death = raw_input("Since you're a scrub, you get 360 noscoped and called a n00b before you can do anything. Retry?: Yes No ")
                    if death == "no":
                        print " "
                        x = 1
                        y = False
                        break
                    else: " pri"
                if statue == "run":
                    print " "
                    ro = raw_input("You start to run but you hear someone slithering up behind you. An unmanned voice shouting 'watch out, Watch Out, WATCH OUT!' and an arm wraps around head slamming you forward into the ground. *Press Enter*")
                    print " "
                    x = 1
                    y = False


                    x = 0
                    y = True
                    inventory = []
                    while y:

                        jc = raw_input("You awake to the sound of cheers and airhorns. A commentators frantic cries are blasting all around you, talking about some men fighting to the death. Get up? ")
                        if jc == "yes" or jc == "up":
                            x = 1
                            y = False

                            x = 0
                            y = True
                            while y:
                                print " "
                                jcr = raw_input("The room around you looks like its made out of stone. There is a steel door and a pickaxe laying next to it. What do you do? ")
                                if jcr == "take pickaxe" or jcr == "pick up pickaxe" or jcr == "take" or jcr == "pickaxe":
                                    inventory.append("pickaxe")
                                    print " "
                                    inv = raw_input("You now have: " + str(inventory) + "*Press Enter*")
                                elif jcr == "door" or jcr == "go to door" or jcr == "use door":
                                    print " "
                                    d = raw_input("You move to the door and can't believe your eyes: John Cena and Randy Orton are in a wrestling match for the death! ")
                                elif jcr == "wall" or jcr == "break wall":
                                    if len(inventory) == 1:
                                        print " "
                                        print "That worked"
                                        x + 1
                                        y = False

                                        x = 0
                                        y = True
                                        while y:
                                            print " "
                                            print "You break out of the room and see Cthulu"
                                            return
                                    else:
                                        print " "
                                        print "No son."
                                else:
                                    print " "
                                    jcr = raw_input("'10 out of 10 would not do that again' -IGN")


                    else:
                        jc = raw_input("Boi. No. You're in prison. Just...stop. ")

                else:
                    print " "
                    reproom = raw_input("Son you just fell into a hole you can't do that. ")
