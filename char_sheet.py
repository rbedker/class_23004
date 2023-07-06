line_list = []
list_type = ["class_name", "atk",
             "dfns", "dod", "hp",
             "intel", "fth", "stgh", "dex"]
dict_list = []

with open("char_stats.txt", 'r') as f:
    for line in f:
        line = line.replace("\n", "")
        line = line.split()
        for item in line:
            if item.isdigit() == True:
                line[line.index(item)] = int(item)
        line_list.append(line)

for characters in line_list:
    dict_char = dict(zip(list_type, characters))
    char_dict.insert(-1, dict_char)


mage_stats = char_dict[0]
cleric_stats = char_dict[1]
monk_stats = char_dict[2]
rogue_stats = char_dict[3]
builder_stats = char_dict[4]
barb_stats = char_dict[5]
cowboy_stats = char_dict[6]
paladin_stats = char_dict[7]
