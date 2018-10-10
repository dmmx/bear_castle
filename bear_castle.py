
# Dead
def dead(tale_of_woe):
    print()
    print(tale_of_woe)
    print("Good Job! You're Dead.")
    exit(0)

def riddle():
    print("""
    The four bears huddle together whispering then turn to you and ask:
    
    "Fuzzy Wuzzy was a bear
     Fuzzy Wuzzy had no hair
     Fuzzy Wuzzy was no bear
     Was he?"
     
    What is your answer?
    1. Yes.
    2. No.
    """)
    answer = input("> ")

    if answer == "1":
        print("The four bears look slightly amused by your answer as if they know")
        print("something that you don't, but they seem satisfied and leave.")
        print()
        return True # Red Room is cleared
    elif answer == "2":
        print("For no reason you can discern you're answer angers the four bears mightly")
        dead("It looks like your discerning days are over. CHOMP CHOMP CHOMP CHOMP.")
    else:
        dead("Not even close ... but the bear's find you soft fatty flesh delicious")

def joke():
    print("""

    Without further adu, you tell your joke:

    "What did the Bear with a toothache eat after seeing the dentist?"
    
    ... after a brief pause ...
    
    "The dentist."

    The bears look at each other, then at you, then back at each other.
    Pretty soon they all start laughing and laughing.
    
    Theu're still laughing when they get up and leave the room all in a jumble.

    What would you like to do?
    1. Grab a chest of gold and the key.
    2. Grab both chests of gold.
    """)
    action = input("> ")

    if action == "1":
        return 1
    elif action == "2":
        return 2
    else:
        dead("Try to do that with two chests of gold turns out to be too much for your puny muscles.")

    
# Green Room
def green_room(cleared, chests):
    print("You are in the Green Room")

    print("""
    
    There is a Ghost Bear gliding around the room.
    
    There is door to North and a door to the South.

    What would you like to do?
    1. Go through the North Door.
    2. Go through the South Door.
    3. Leave through the Front Door.
    """)
    action = input("> ")

    if action == "1":
        return "BLACK", cleared
    elif action == "2" :
        return "WHITE", cleared
    elif action == "3":
        if chests == 1:
            return "OUT_SIDE", cleared
        elif chests == 2:
            dead("The door is locked and the key is lost for ever. You are left to play with the Ghost Bear until you starve")
        else:
            print("The door is locked")
            return "GREEN", cleared
    else:
        dead("You're stumbling around alerts the Ghost Bear\nwho immediately attacks and eats you face off with his immense ghost teeth")


# Black Room
def black_room(cleared):
    print("You are in the Black Room")

    if cleared:
        print("""

        There is a mirror on the East wall. Otherwise the room is empty.
    
        On the West end of the room there is a door leading South.
        On the East end of the room there is another door leading South.

        What would you like to do?
        1. Go through the door on the West end.
        2. Go through the door on the East end.
        """)
        action = input("> ")

        if action == "1":
            return "GREEN", cleared
        elif action == "2":
            return "RED", cleared
        else:
            dead("Oopsy, you trip and fall backwards into mirror and find the two bears with Lazers.")
    else:
        print("""
    
        There is a mirror on the East wall.
        And Two bears with freakin' Lazers on there heads.
    
        On the West end of the room there is a door leading South.
        On the East end of the room there is another door leading South.

        What would you like to do?
        1. Go through the door on the West end.
        2. Go through the door on the East end.
        3. Yell at the bears to go away!
        4. Stand in front of the mirror and wave your hands to get the
           bears' attention!
        """)
        action = input("> ")

        if action == "4" and not cleared:
            print("The bears shoot their lazers at you, but you leap ")
            print("out of the way at the last second!")
            print("The bears angrily charge at the mirror and disappear into it!")
            print()
            return "BLACK", True
        else:
            dead("The bears shoot their lazer and you end up looking like a flaming marshmallow.")

# Red Room
def red_room(cleared):
    print(f"You are in the Red Room")
    
    if cleared:
        print("""
        The room is empty.
        
        You didn't notice it the first time when the bears were here
        but there is a door open to the East.

        There are also doors to the North, and South.
        
        What would you like to do?
        1. Go North.
        2. Go East.
        3. Go South.
        """)
        action = input("> ")

        if action == "1":
            return "BLACK", cleared
        elif action == "2":
            return "GOLD", cleared
        elif action == "3":
            return "WHITE", cleared
        else:
            dead("The four bears return. No riddle this time. Just teeth, claws, and your blood.")
    else:
        print("""
    
        There are four bears sitting in a half-circle facing you.
        They want to ask you a riddle.

        There is a door to the North and a door to the South.

        What would you like to do?
        1. Go through the door to the North.
        2. Go through the door to the South.
        3. Answer the riddle of the bears.
        """)
        action = input("> ")

        if action == "1":
            return "BLACK", False
        elif action == "2":
            return "WHITE", False
        elif action == "3":
            return "RED", riddle()
        else:
            dead("Each bear picks a limb to gnaw off")

# White Room
def white_room(cleared):
    print("You are in the White Room")

    if cleared:
        print("""
        There are two bears rolled over on the backs sound asleep.

        What would you like to do?
        1. Go through the door on the West end.
        2. Go through the door on the East end.
        """)
        action = input("> ")

        if action == "1":
            return "GREEN", cleared
        elif action == "2":
            return "RED", cleared
        else:
            dead("You accidently wake the bears who are really hungry.")

    else:
        print("""
    
        There are two sleeping bears laying on the floor.
    
        On the West end of the room there is a door leading North.
        On the East end of the room there is another door leading North.

        What would you like to do?
        1. Try to sneak past the bears to the door on the West end.
        2. Try to sneak past the bears to the door on the East end.
        3. Sing to the bears.
        4. Now is your chance while they're sleep. ATTACK the bears.
        """)
        action = input("> ")

        if action == "3":
            print("You sing the bears a lullaby so sweet and soft")
            print("that the bears roll over on their backs and fall into an even deeper sleep.")
            print()
            return "WHITE", True
        elif action == "4":
            print("With a warriors yell to charge the bears!")
            print("The first bears squints one eye at you")
            print("and then swats you away.")
            dead("Your body flies across the room and goes splat against the wall.")
        else:
            dead("You trip and fall waking the bears who hungerly eat your legs off.")

# Gold Room
def gold_room(cleared, chests):

    print("You are in the Gold Room")

    if cleared:
        print("""
        The room is empty. No bears. No chests. No Key. Nothing. Weird.

        What would you like to do:
        1. Leave
        """)
        action = input("> ")

        if action == "1":
            return "RED", cleared, chests
        else:
            dead("Oh wait, that's how you sommon eight hungry bears!")
    else:
        print("""

        The room contains two huge chests of gold and a key.
        You can carry both chests or one chest and the key.
        
        There are also eight bears loitering around looking bored.
        
        There is a door to the East.

        What would you like to do?
        1. Go through the East door.
        2. Try to grab a chest of gold and run.
        3. Sing to the bears.
        4. Tell the bears a joke.
        5. There are only eight of them. ATTACK!

        """)
        action = input("> ")

        if action == "1":
            print("You can't. There is a bear in your way.")
            print()
            return "GOLD", cleared, chests
        elif action == "2":
            dead("You dive for a chest but end up landing in a bear's mouth who\nproceeds to shake you like a polaroid picture.")
        elif action == "3":
            print('You sing "I Gave My Love a Cherry".\nTurn\'s out bears really don\'t like folk music.')
            dead("Ironically they eat you vital organs while listening to Joan Baez.")
        elif action == "4":
            return "GOLD", True, joke()
        elif action == "5":
            dead("You make like you know karate\nThen yell that your hands are registered as leathal weapons.\nThe bears pause. Then smile. Then eat your entrails for lunch.")
        else:
            print("You're lucky the bears are bored.")
            return "GOLD", cleared, chests

def start():
    green_room_cleared = False
    black_room_cleared = False
    red_room_cleared = False
    white_room_cleared = False
    gold_room_cleared = False
    stuck_inside = True
    chests = 0

    next_room = "GREEN"
    while stuck_inside:
        if next_room == "GREEN":
            next_room, green_room_cleared = green_room(green_room_cleared, chests)
        elif next_room == "BLACK":
            next_room, black_room_cleared = black_room(black_room_cleared)
        elif next_room == "RED":
            next_room, red_room_cleared = red_room(red_room_cleared)
        elif next_room == "WHITE":
            next_room, white_room_cleared = white_room(white_room_cleared)
        elif next_room == "GOLD":
            next_room, gold_room_cleared, chests = gold_room(gold_room_cleared, chests)
        elif next_room == "OUT_SIDE":
            print("Good Job! You have escaped Bear Castle")
            stuck_inside = False
        else:
            print(f"NO SUCH ROOM: {next_room}")
            exit(0)
            



start()