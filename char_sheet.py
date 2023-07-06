line_list = []
list_type = ["class_name", "atk",
             "dfns", "dod", "hp",
             "intel", "fth", "stgh", "dex"]
class_list = []

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
    class_dict.insert(-1, dict_char)


mage_stats = class_dict[0]
cleric_stats = class_dict[1]
monk_stats = class_dict[2]
rogue_stats = class_dict[3]
builder_stats = class_dict[4]
barb_stats = class_dict[5]
cowboy_stats = class_dict[6]
paladin_stats = class_dict[7]
