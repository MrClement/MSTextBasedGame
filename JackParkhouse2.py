question = raw_input("You walk into a room were a man takes control of your mind and says, 'you must play this game and win to live'. You black out. When you wake up you are a general in Germany in world war II. You decide to Attack the St. Petersburg in the Soviet Union. You have no idea what kind of military the Soviet Unuion has stationed in St. Petersburg. You have two choices. a. Take an army of three tanks, two fighter jets, and one missile. b. You dicide to send a spy and reinforce your army.")
if question == "a":
    question = raw_input("The enemy had five tanks, one heavy tank, three fighter jets, two planes with bombs, two scouts, and a destroyer they easily deafeat you in battle and you run away to fight another day. You have two choices. a. Create a navy. b. create an army")
    if question == "a":
        question = raw_input("Would you like to create a. a destroyer or b. a scout?")
        if question == "a":
            print("You create a destroyer but in the prosses the French capture you and you are never seen again. The End")
        elif question == "b":
             print("After you create the scout you are sewed for stealing money. You go to court and spend the rest of your life in jail. The End.")
    elif question == "b":
        question = raw_input("would you like to create a. a missile or b. a machine gun")
        if question == "a":
            print("As you created the missile you were  attacked by two American jets. You were shot and died. The end.")
        elif question == "b":
            print("A Russian assasin saw that you where a threat and killed you. The end.")


elif question == "b":
    question = raw_input("your spy discovers that while you where waiting they sent three fourths of their army to fight your ally Japan. You take your army and fight in St. Petersburg. You obtain all the supplies and leave. You have two chosses. a. use the supplies to create two heavy tanks. b. use the supplies to create three fighter jets. ")

    if question == "a":
        question = raw_input("after you create your heavy tank news comes in that China is fighting Germany in Lhasa. Japan is sending air support. They want you to bring in reinforcments. You have two choses. a. send reinforcments. If you send reinforcments you could gain mony as well as troops. b. Do not send reinforcments. If you do not send reinforcements you can live to fight another day.")
        if question == "a":
            question = raw_input("You win the battle and are awarded with five tanks and one fighter jet. You now have two choices. a. battle at nice, France. b. create a scientist.")
            if question=="a":
                print("Even with your huge army you loose the battle because France was gathering troops at Nice. The End.")
            elif question=="b":
                print("Hitler runs into you at a camp you are stationed at. You agree to hand over your army to him in return for some money. You live the rest of your life in a mansion. The End.")

        elif question == "b":
            question = raw_input ("A German general is planing a huge naval attack on an area near you. He wants you to send a spy to survey the area. If your spy gives accurate information then you would be given money. If he doesn't you will loose everything. You have two choices. a. send a spy. b. don't send a spy.")
            if question == "a":
                print("Your spy sends inacurate information and you loose your army. You spend the rest of your life known as someone who didn't help the war. The End")
            elif question=="b":
                print("You are stationed in japan. Unfortunetly you are in the area where the Nucler bomb was dropped. You die. The End.")



elif question == "b":
        question = raw_input("A military general near you dies. Because of your recent victory at St. Petersburg, the German government decides to put you in charge of his military. Now you have a surpreme navy, army, and air force. with your new troops you dicide to Arlon, a city in Belgium. Send a spy to survey the area. b. attach now. ")
        if question == "a":
            print("You wait but are attacked by a combined force of America, China, and Britain. Your army is crushed and you fall  with them. The end")
        elif question == "b":
            question = raw_input("You attack at night. Your enemy is sleeping. You enter unseen. There is no fighting. You steel all the money you can grab and leave. You have two choices. a. create a laboratory with 7 scientists. create 10 scientists without a laboratory.")
            if question=="a":
                print("your army is angry at you that you use your money for science and not war. They stab you in your sleep. The end")
            elif question=="b":
                print("You start to become parinoid over your survival and end up commiting suiside. The End")
