def first_room():
    user_input = raw_input().lower()

    if user_input.find('1') >= 0:
        print "You enter a chamber with spikes on all the walls and ceiling, there is a lever near the door"
        user_input = raw_input().lower()
        if user_input.find('lever') >=0:
            print "You barely touch the lever and the spikes come rushing toward you. Game over."
        else:
            print "You are in a large room with dozens of doors leading off in different directions. What do you do?"



def second_room():
    user_input = raw_input(). lower()

    if user_input.find('door1') >=0:
        print "You go into the first door. The door closes and locks behind you. It is dark. The floor slides away and you fall into a helicopter and ride into the sunset and are safe. YOU WIN."
    elif user_input.find('door2') >=0:
        print "You go into the second door. You go into a helicopter and fly into the sunset and are safe. YOU WIN!"
    elif user_input.find('door3') >=0:
        print "You go into the third door and see an airplane and you get in to find a hot tub. You get in and the plane takes off into the sunset safe. YOU WIN."
    else:
        print "You oppened the door and saw a hot tub. You get in and the water drains and the floor opens to a pit of lava. Game over. "
