import time
import random

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def introduction():
    slow_print("welcome to the oregon trail.")
    slow_print("you're leading a group of pioneers across the country.")
    slow_print("your journey starts in missouri and ends in oregon.")
    slow_print("are you ready to start your adventure?")

def start_journey():
    slow_print("you gather your supplies and set out on your journey.")
    slow_print("the first leg of your trip takes you to the great plains.")
    slow_print("do you want to hunt for food or continue traveling?")

def hunt_food():
    slow_print("you decide to hunt for food.")
    outcome = random.choice(["you successfully hunt a deer and gather plenty of food.", 
                             "you spend hours hunting but find nothing.", 
                             "you encounter a wild bear and have to defend yourself."])
    slow_print(outcome)
    if "deer" in outcome:
        slow_print("your journey continues with enough food for now.")
    elif "nothing" in outcome:
        slow_print("you continue your journey, but food is scarce.")
    elif "bear" in outcome:
        slow_print("you manage to scare the bear away, but it's a close call.")

def continue_travel():
    slow_print("you decide to keep traveling.")
    slow_print("the weather is getting rough. do you want to find shelter or push through?")

def find_shelter():
    slow_print("you find a small cave to take shelter in.")
    slow_print("a storm passes through, but you and your group stay safe.")
    slow_print("after the storm, you continue your journey.")

def push_through():
    slow_print("you decide to push through the rough weather.")
    outcome = random.choice(["you make it through the storm, but everyone is exhausted.", 
                             "the storm takes a toll on your group, and some supplies are lost.", 
                             "you get caught in the storm and suffer injuries."])
    slow_print(outcome)
    if "exhausted" in outcome:
        slow_print("you rest for a while before continuing.")
    elif "supplies" in outcome:
        slow_print("you have to ration your remaining supplies carefully.")
    elif "injuries" in outcome:
        slow_print("you take time to tend to the injuries before moving on.")

def reach_rockies():
    slow_print("you reach the rocky mountains.")
    slow_print("the terrain is tough. do you want to find a safer route or take the direct path?")

def safer_route():
    slow_print("you decide to find a safer route.")
    slow_print("it takes longer, but you avoid many dangers and make steady progress.")

def direct_path():
    slow_print("you take the direct path through the mountains.")
    outcome = random.choice(["you make it through quickly but face several challenges.", 
                             "you encounter dangerous wildlife and have to fend them off.", 
                             "you get lost and spend extra days finding your way."])
    slow_print(outcome)
    if "quickly" in outcome:
        slow_print("your group is tired but you've saved time.")
    elif "wildlife" in outcome:
        slow_print("you successfully fend off the wildlife but it's a close call.")
    elif "lost" in outcome:
        slow_print("you eventually find your way and continue on.")

def reach_oregon():
    slow_print("after many hardships, you finally reach oregon.")
    slow_print("you've successfully led your group to their new home.")
    slow_print("congratulations, you've completed the oregon trail!")

def main():
    introduction()
    start_journey()
    choice1 = input("type 'hunt' to hunt for food or 'travel' to continue traveling: ").lower()
    
    if choice1 == 'hunt':
        hunt_food()
    elif choice1 == 'travel':
        continue_travel()
        choice2 = input("type 'shelter' to find shelter or 'push' to push through the weather: ").lower()
        if choice2 == 'shelter':
            find_shelter()
        elif choice2 == 'push':
            push_through()
    
    reach_rockies()
    choice3 = input("type 'safer' to find a safer route or 'direct' to take the direct path: ").lower()
    if choice3 == 'safer':
        safer_route()
    elif choice3 == 'direct':
        direct_path()
    
    reach_oregon()

if __name__ == "__main__":
    main()
