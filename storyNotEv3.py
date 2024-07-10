def introduction():
    print("welcome to the adventure game.")
    print("you find yourself in a dark forest with two paths in front of you.")
    print("do you want to take the left path or the right path?")

def left_path():
    print("you take the left path and come across a small, abandoned cabin.")
    print("do you want to go inside the cabin or keep walking?")

def cabin_inside():
    print("you decide to go inside the cabin. it's dark and dusty.")
    print("you see a strange box in the corner and a staircase leading down.")
    print("do you want to open the box or go down the stairs?")

def cabin_box():
    print("you open the box and find an old, magical book. it starts to glow.")
    print("suddenly, you're transported to a mystical land filled with strange creatures.")
    print("congratulations, you found a hidden world. your adventure continues!")

def cabin_stairs():
    print("you go down the stairs and find a hidden underground tunnel.")
    print("you follow the tunnel and discover a secret treasure room filled with gold.")
    print("you've struck it rich! your adventure has brought you great fortune.")

def keep_walking():
    print("you decide to keep walking and come across a wild animal.")
    print("do you want to try to befriend the animal or run away?")

def befriend_animal():
    print("you try to befriend the animal and it surprisingly becomes your companion.")
    print("together, you explore the forest and find many hidden secrets.")
    print("you and your new friend live many exciting adventures together.")

def run_away():
    print("you run away from the animal and eventually find your way out of the forest.")
    print("you feel relieved but can't help but wonder what adventures you missed out on.")
    print("your journey ends here, but the forest will always be there for another adventure.")

def right_path():
    print("you take the right path and stumble upon a river with a rickety bridge.")
    print("do you want to cross the bridge or follow the river downstream?")

def cross_bridge():
    print("you carefully cross the bridge and reach a mysterious castle on the other side.")
    print("do you want to enter the castle or explore the grounds?")

def enter_castle():
    print("you enter the castle and find it filled with ancient artifacts and magical items.")
    print("you've discovered a place of great power. your adventure is just beginning.")

def explore_grounds():
    print("you explore the castle grounds and find a hidden garden with magical plants.")
    print("you've found a place of peace and wonder. your adventure continues in tranquility.")

def follow_river():
    print("you follow the river downstream and find a small village.")
    print("the villagers welcome you and share their stories and secrets with you.")
    print("you become part of their community and live a life full of stories and adventures.")

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
            choice3 = input("type 'enter' to enter the castle or 'explore' to explore the grounds: ").lower()
            if choice3 == 'enter':
                enter_castle()
            elif choice3 == 'explore':
                explore_grounds()
        elif choice2 == 'follow':
            follow_river()

if __name__ == "__main__":
    main()
