import random, string

story = """
Once upon a time in a {place}, there was a {adjective} {animal}. 
This {animal} loved to {verb} all day long. One day, while {verb_ing}, 
the {animal} found a {adjective_2} {object}. The {animal} took the {object} 
and decided to {verb_2}. It was a {adjective_3} day for the {animal}.
"""

places = ["forest", "castle", "village", "city", "desert", "mountain"]
adjectives = ["happy", "sad", "angry", "excited", "nervous", "brave"]
animals = ["cat", "dog", "rabbit", "dragon", "unicorn", "fox"]
verbs = ["run", "jump", "swim", "fly", "dance", "sing"]
verb_ing = ["running", "jumping", "swimming", "flying", "dancing", "singing"]
adjectives_2 = ["shiny", "old", "new", "mysterious", "magical", "ancient"]
objects = ["key", "sword", "book", "map", "box", "gem"]
verbs_2 = ["explore", "hide", "share", "keep", "discover", "bury"]
adjectives_3 = ["wonderful", "terrible", "fantastic", "strange", "amazing", "weird"]

def random_choice(lst):
    return random.choice(lst)

plce = random_choice(places)
adjctve = random_choice(adjectives)
anmial = random_choice(animals)
vrb = random_choice(verbs)
vrb_ing = random_choice(verb_ing)
adjctve_2 = random_choice(adjectives_2)
obect = random_choice(objects)
vrb_2 = random_choice(verbs_2)
adjctve_3 = random_choice(adjectives_3)

mad_lib = story.format(
    place=plce, adjective=adjctve, animal=anmial, 
    verb=vrb, verb_ing=vrb_ing, adjective_2=adjctve_2, 
    object=obect, verb_2=vrb_2, adjective_3=adjctve_3)

print(mad_lib)

def get_user_input(prompt):
    return input(prompt).strip()

while True:
    user_place = get_user_input("Enter a place: ")
    user_adjective = get_user_input("Enter an adjective: ")
    user_animal = get_user_input("Enter an animal: ")
    user_verb = get_user_input("Enter a verb: ")
    user_verb_ing = get_user_input("Enter a verb ending in -ing: ")
    user_adjective_2 = get_user_input("Enter another adjective: ")
    user_object = get_user_input("Enter an object: ")
    user_verb_2 = get_user_input("Enter another verb: ")
    user_adjective_3 = get_user_input("Enter one last adjective: ")
    
    user_mad_lib = story.format(
        place=user_place, adjective=user_adjective, animal=user_animal, 
        verb=user_verb, verb_ing=user_verb_ing, adjective_2=user_adjective_2, 
        object=user_object, verb_2=user_verb_2, adjective_3=user_adjective_3)

    print(user_mad_lib)
    
    another = get_user_input("Do you want to create another Mad Lib? (yes/no): ")
    if another.lower() != 'yes':
        break

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

for _ in range(5):
    print(random_string(10))
