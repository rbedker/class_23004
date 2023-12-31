character_1 = {'name': 'rock-umm', 
               'character_class': paladin_stats, 
               'desc': '2 feet tall, buff', 
               'age': '40', 
               'gender': 'male', 
               'start_item': 'rock', 
               'ability': '??'}
character_2 = {'name': 'glassina cannonina',
               'character_class': mage_stats,
               'desc': '',
               'age': '99',
               'gender': 'female',
               'start_item': 'cane staff',
               'ability': ''}
character_3 = {'name': 'ned flanders',
               'character_class': cleric_stats,
               'desc': 'friendly neighbor',
               'age': '45',
               'gender': 'male',
               'start_item': 'bible',
               'ability': ''}
character_4 = {'name': 'billy',
               'character_class': monk_stats
               'desc': 'vanilla ice haircut',
               'age': '27, thinks he is 19',
               'gender': 'male',
               'start_item': 'skateboard',
               'ability': ''}
character_5 = {'name': 'baldwin',
               'character_class': rogue_stats,
               'desc': 'steals',
               'age': '7',
               'gender': 'female',
               'start_item': 'your wallet',
               'ability': ''}
character_6 = {'name': 'steve',
               'character_class': builder_stats,
               'desc': 'geometric, hella based',
               'age': '12',
               'gender': 'male',
               'start_item': 'bare hands',
               'ability': ''}
character_7 = {'name': 'barbie',
               'character_class': barb_stats,
               'desc': 'thiccc and 210 cm tall',
               'age': '77',
               'gender': 'male',
               'start_item': 'doll with matching dress',
               'ability': ''}
character_8 = {'name': 'herbert bernard',
               'character_class': cowboy_stats,
               'desc': 'canadian',
               'age': 'redacted',
               'gender': 'redacted',
               'start_item': 'colt 1845',
               'ability': ''}

def return_name(char):
    return(char['name'])

def return_char_class(char):
    return(char['character_class'])

def return_desc(char):
    return(char['desc'])

def return_age(char):
    return(char['age'])

def return_gender(char):
    return(char['gender'])

def return_start_item(char):
    return(char['start_item'])

def return_ability(char):
    return(char['ability'])

def print_character(char):
    print("Name: " + return_name(char))
    print("Class: " + return_char_class(char))
    print("Description: " + return_desc(char))
    print("Age: " + return_age(char))
    print("Gender: " + return_gender(char))
    print("Starter item: " + return_start_item(char))
    print("Ability: " + return_ability(char))
