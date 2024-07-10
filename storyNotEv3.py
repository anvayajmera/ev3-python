import time
import random

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def introduction():
    slow_print("welcome to the adventure game.")
    slow_print("you find yourself in a dark forest with two paths in front of you.")
    slow_print("do you want to take the left path or the right path?")

def left_path():
    slow_print("you take the left path and come across a small, abandoned cabin.")
    slow_print("do you want to go inside the cabin or keep walking?")

def cabin_inside():
    slow_print("you decide to go inside the cabin. it's dark and dusty.")
    slow_print("you see a strange box in the corner and a staircase leading down.")
    slow_print("do you want to open the box or go down the stairs?")

def cabin_box():
    slow_print("you open the box and find an old, magical book. it starts to glow.")
    slow_print("suddenly, you're transported to a mystical land filled with strange creatures.")
    slow_print("congratulations, you found a hidden world. your adventure continues!")

def cabin_stairs():
    slow_print("you go down the stairs and find a hidden underground tunnel.")
    slow_print("you follow the tunnel and discover a secret treasure room filled with gold.")
    slow_print("you've struck it rich! your adventure has brought you great fortune.")

def keep_walking():
    slow_print("you decide to keep walking and come across a wild animal.")
    slow_print("do you want to try to befriend the animal or run away?")

def befriend_animal():
    slow_print("you try to befriend the animal and it surprisingly becomes your companion.")
    slow_print("together, you explore the forest and find many hidden secrets.")
    slow_print("you and your new friend live many exciting adventures together.")

def run_away():
    slow_print("you run away from the animal and eventually find your way out of the forest.")
    slow_print("you feel relieved but can't help but wonder what adventures you missed out on.")
    slow_print("your journey ends here, but the forest will always be there for another adventure.")

def right_path():
    slow_print("you take the right path and stumble upon a river with a rickety bridge.")
    slow_print("do you want to cross the bridge or follow the river downstream?")

def cross_bridge():
    slow_print("you carefully cross the bridge and reach a mysterious castle on the other side.")
    slow_print("do you want to enter the castle or explore the grounds?")

def enter_castle():
    slow_print("you enter the castle and find it filled with ancient artifacts and magical items.")
    slow_print("you've discovered a place of great power. your adventure is just beginning.")

def explore_grounds():
    slow_print("you explore the castle grounds and find a hidden garden with magical plants.")
    slow_print("you've found a place of peace and wonder. your adventure continues in tranquility.")

def follow_river():
    slow_print("you follow the river downstream and find a small village.")
    slow_print("the villagers welcome you and share their stories and secrets with you.")
    slow_print("you become part of their community and live a life full of stories and adventures.")

def random_event():
    events = [
        "you find a hidden treasure chest with gold coins.",
        "you encounter a friendly elf who gives you a magic potion.",
        "you find an ancient map leading to a secret location.",
        "you meet a wise old man who shares a valuable piece of advice.",
        "you come across a beautiful meadow filled with rare flowers."
    ]
    event = random.choice(events)
    slow_print(event)

def main():
    introduction()
    choice1 = input("type 'left' to take the left path or 'right' to take the right path: ").lower()
    
    if choice1 == 'left':
        left_path()
        choice2 = input("type 'inside' to go inside the cabin or 'walk' to keep walking: ").lower()
        if choice2 == 'inside':
            cabin_inside()
            choice3 = input("type 'box' to open the box or 'stairs' to go down the stairs: ").lower()
            if choice3 == 'box':
                cabin_box()
            elif choice3 == 'stairs':
                cabin_stairs()
        elif choice2 == 'walk':
            keep_walking()
            random_event()
            choice3 = input("type 'befriend' to befriend the animal or 'run' to run away: ").lower()
            if choice3 == 'befriend':
                befriend_animal()
            elif choice3 == 'run':
                run_away()
    
    elif choice1 == 'right':
        right_path()
        choice2 = input("type 'cross' to cross the bridge or 'follow' to follow the river: ").lower()
        if choice2 == 'cross':
            cross_bridge()
            random_event()
            choice3 = input("type 'enter' to enter the castle or 'explore' to explore the grounds: ").lower()
            if choice3 == 'enter':
                enter_castle()
            elif choice3 == 'explore':
                explore_grounds()
        elif choice2 == 'follow':
            follow_river()

if __name__ == "__main__":
    main()
