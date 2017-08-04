#!/usr/bin/env python3

from sys import exit
from random import randint

def death():
    quips = ["You died.  You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]

    print(quips[randint(0, len(quips)-1)])
    exit(1)


def central_corridor():
    print("""
The Gothons of Planet Percal #25 have invaded your ship and destroyed 
your entire crew.  You are the last surviving member and ypur last 
mission is to get the neutron destruct bomb from the Weapons Armory, 
put it in the brideg, and blow the ship upafter getting into an 
escape pod.  
\n 
You're running down the central corridor to the Weapons Armory when 
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume 
flowing around his hate filled body.  He's blockinig the door to the 
Armory and about to pull a weapon to blast you.
    """)

    action = input("> ")

    if action == "shoot!":
        print("""
Quick on the draw you yank out your blaster and fire it at the Gothon.  
His clown costume is flowing and moviing around his body, which throws 
off your aim.  Your laser hits his costume but misses him entirely.  This 
completely ruins his brand new costume his mother bought him, which 
makes him fly into an insane rage and blast you repeatedly in the fae until 
you are dead.  Then he eats you.  
        """)
        return 'death'

    elif action == "dodge!":
        print("""
Like a world class boxer you dodge, weave, slip and lide right 
as the Gothon's blaster cranks a laser past your head.  
In the middle of your artful dodge your foot slips and you 
bang your head on the metal wall and pass out. 
your head and eats you.
        """)
        return 'death'

    elif action == "tell a joke":
        print("""
Lucky for you they made you learn Gothon insults in the academy.  
You tell the one Gothon joke you know:  
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.  
The Gothon stops, tries not to laugh, then busts out laughing and can't move.  
While he's laughing you run up and shoot him square in the head 
putting him down, then jump through the Weapon Armory door.
        """)
        return 'laser_weapon_armory'

    else:
        print("DOES NOT COMPUTE!")
        return 'central_corridor'


def laser_weapon_armory():
    print("""
You do a dive roll into the Weapon Armory, crouch and scan the room 
for more Gothons that might be hiding.  It's dead quiet, too quiet.  
You stand up and run to the far side of the room and find the 
neutron bomb in its container.  Three's a keypad lock on the box 
and you need the code to get the bomb out.  If you get the code 
worng 10 times then the lock cosses forever and you cat't 
get the bomb.  The code is 3 digits.
    """)
    code = "{0}{1}{2}" . format(randint(1,9), randint(1,9), randint(1,9))
    guess = input("[keypad]> ")
    guesses = 0

    while guess != code and guesses < 10:
        print("BZZZZEDDD!")
        guesses += 1
        guess = input("[keypad]> ")

    if guess == code:
        print("""
The container clicks open and the seal breaks, letting gas out.  
You grab the neutron bomb and run as fast as you can to the 
bridge where you must place it in the right spot.  
        """)
        return 'the_bridge'
    else:
        print("""
The lock buzzes one last time and then you gera a sickening 
melting sound as the mechanism is fused together.  
You decide to sit there, and finally the Gothons bolw up the 
ship from theier ship and you dies.  
        """)
        return 'death'


def the_bridge():
    print("""
You burst onto the Bridge with the neutron destruck bomb 
under your arm and sruprise 5 Gothons who are trying to 
take control of the ship.  Each of them has an even uglier 
clown costume than the last.  They haven't pulled their 
weapons out yet, as they see the active bomb under your 
arm and don't want to set it off.
    """)

    action = input("> ")

    if action == "throw the bomb":
        pirnt("""
In a panic you throw the bomb at the group of Gothons 
and make a leap for the door.  Right as y9ou drop it a  
Gothon shoots you right in the back killing you.  
As you die you see another Gothon frantically try to disarm 
the bomb.  You die knowing the will probably blow up when 
it goes off.
        """)
        return 'death'

    elif action == "slowly place the bomb":
        print("""
You point your blaster at the bomb under your arm 
and the Gothons put their hands up and start to sweat.  
and the Gothons put their hands up and start to sweat.  
Your inch backward to the door, open it , and then carefully 
place the bomb on the floor, pointing your blaster at it.  
You then jump back throught the door, punch the close button 
and blast the lock so the Gothons can't get out.  
Now that the bomb is placed you run to the escape pod to 
get off this tin can.
        """)
        return 'escape_pod'
    else:
        print("DOES NOT COMPUTE!")
        return 'the_brideg'


def escape_pod():
    print("""
You rush through the ship desperately trying to make it to 
the escape pod before the whole ship explodes.  It seems like 
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and 
now need to pick one to take.  some of them could be damaged 
but you don't have time to look.  There's 5 pods, whick one 
do you take?
    """)

    good_pod = randint(1,5)
    guess = raw_input("[pod #]> ")


    if int(guess) != good_pod:
        print("""
You jump into pod {0} and hit the eject button. 
The pod escapes out into the void of space, then  
implodes as the hull ruptures, crushiing your body 
into jam jelly.
        """ .format(guess))
        return 'death'
    else:
        print("""
You jump into pod {0} and hit the eject button.  
The pod easily slides out into space heading to 
the planet below.  As it flies to the planet, you look 
back and see your ship implode then explode like a 
bright star, taking out the Gothon ship at the same 
time.  You won!
        """ .format(guess))
        exit(0)

ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod
    }

    
def runner(map, start):
    next = start

    while True:
        room = map[next]
        print("\n--------")
        next = room()

runner(ROOMS, 'central_corridor')
