def return_name(char):
    return char['name']


def return_char_class(char):
    return char['character_class']['class_name']

def return_desc(char):
    return char['desc']


def return_age(char):
    return char['age']


def return_gender(char):
    return char['gender']


def return_start_item(char):
    return char['start_item']


def return_ability(char):
    return char['ability']


def return_char(name, char_list):
    for x in char_list:
        if x['name'] == name.lower():
            return x
    else:
        raise ValueError('Char doesn\'t exist!')
        
def player_attack(char):
    return char['character_class']['atk']

def monster_attack(char):
    return char['atk']

def monster_name(char):
    return char['monster_name']


def print_character(char):
    print(f'Name: {return_name(char).title()}')
    print(f'Class: {return_char_class(char).title()}')
    print(f'Description: {return_desc(char).title()}')
    print(f'Age: {return_age(char).title()}')
    print(f'Gender: {return_gender(char).title()}')
    print(f'Starter item: {return_start_item(char).title()}')
    print(f'Ability: {return_ability(char).title()}')
