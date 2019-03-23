from sys import exit
import random
import os
import string
import json

#load names list
names = json.loads(open('/Users/Sam/Documents/Programming/Python/Python_Shaw/text-based-adventure/names.json').read())
#load animals list
animals = json.loads(open('/Users/Sam/Documents/Programming/Python/Python_Shaw/text-based-adventure/animals.json').read())
#load weapons list
weapons = json.loads(open('/Users/Sam/Documents/Programming/Python/Python_Shaw/text-based-adventure/weapons.json').read())
#load colors list

#decide random player name from list
f_name = random.choice(names)
l_name = random.choice(names)
full_name= f_name + " " + l_name

def room_desc(color, animal, weapon):
    print("...")
    print(f"You entered a {color} room with a {color} {animal}. ")
    print(f"You find a {weapon}. ")

def action_loop():
    resp = input("What do you do now? ")
    x="start"
    #print(str.lower(resp))
    while x=="start":
        #use list comprehension to see if response has one of these terms
        if any(st in str.lower(resp)for st in ["kill","murder","fight","stab","shoot", "eat", "fire"] ):
            x="end"
            dead("It proves to be too strong. It lunges at you and bites you. You die shortly thereafter.")
        elif any(st in str.lower(resp) for st in ["pet", "love"]):
            print("The animal likes that. He looks at you passionately.")
            action_loop()
        elif any(st in str.lower(resp) for st in ["kiss"]):
            print("Woah! Let's not get carried away.")
            action_loop()
        elif any(st in str.lower(resp) for st in ["hug","cuddle"]):
            x="end"
            win("Congrats, your new pet likes you. You mount your new best friend and burst out of the room like the Koolaid man. You both live happily ever.")
        elif any(st in str.lower(resp) for st in ["run"]):
            x="end"
            dead("You trip over a pebble and crack your head on a big rock. It proves to be fatal.")
        elif any(st in str.lower(resp) for st in ["pickup", "pick up"]):
            print("You pickup the weapon you found.")
            action_loop()
        elif any(st in str.lower(resp) for st in ["lick"]):
            print("That's wierd. The animal is not impressed.")
            action_loop()
        elif any(st in str.lower(resp) for st in ["leave", "go back", "go out","back","exit"]):
            print("You can't do that. Gotta face your problems in life. ")
            action_loop()
        else:
            print("Don't understand what you mean. Try again. ")
            action_loop()
def red_room():
    color="red"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} throws poop at you.")
    print("...")
    action_loop()
def orange_room():
    color="orange"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} gobbles up your bag.")
    print("...")
    action_loop()
def yellow_room():
    color="yellow"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} sneezes on you.")
    print("...")
    action_loop()
def green_room():
    color="green"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} licks you.")
    print("...")
    action_loop()
def blue_room():
    color="blue"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} sniffs you.")
    print("...")
    action_loop()
def indigo_room():
    color="indigo"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} humps your leg.")
    print("...")
    action_loop()
def violet_room():
    color="violet"
    a=random.choice(animals)
    b=random.choice(weapons)
    room_desc(color,a,b)
    print(f"The {a} burps.")
    print("...")
    action_loop()

def dead(why):
    print(why, "\n...")
    end_choice = input("Type yes  or y if you want to play again: ")
    if str.lower(end_choice)=='yes' or str.lower(end_choice)=='y':
        start()
    else:
        exit(0)
def win(why):
    print(why, "\n...")
    end_choice = input("Type yes or y if want to play again: ")
    if str.lower(end_choice)=='yes' or str.lower(end_choice)=='y':
        start()
    else:
        exit(0)
def start():
    #print intro description
    ani=random.choice(animals);
    print("...")
    print("NOTE: This is a text-based game. You must type out your actions.")
    print("Hello Adventurer, ")
    print(f"Your name is {full_name}.")
    print("...")
    print("Today you decide to go to the park with your pet {}.".format(ani)),
    print("You manage to get her in your car and drive to the park. ")
    print("Suddenly, you're both magically transported to a dark cave.")
    print(f"Your pet {str.lower(ani)} hands you a flashlight from her fabulous backpack.")
    print("...")
    print("There is a route to your right and left.")
    print("...")
    print("Which path do you take?")
    #create list of functions
    ls_func = [red_room, orange_room,yellow_room, green_room,
    blue_room, indigo_room, violet_room]
    #initialize items
    flashlight_on=True
    #first user prompt
    choice = input("> ")
    if choice == "left":
        random.choice(ls_func)()
    elif choice == "right":
        dead("You enter the wrong room fall to your death. Try the other room next time.")
    else:
        end_choice = input("The room collapse and you fell to your death. Type yes or y if you want to try again: ")
        if str.lower(end_choice)=='yes' or str.lower(end_choice)=='y':
            print("\n")
            start()
        else:
            exit(0)
start()
