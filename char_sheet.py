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
    dict_list.insert(-1, dict_char)


mage_stats = dict_list[0] 
cleric_stats = dict_list[1]
monk_stats = dict_list[2]
rogue_stats = dict_list[3]
builder_stats = dict_list[4]
barb_stats = dict_list[5]
cowboy_stats = dict_list[6]
paladin_stats = dict_list[7]
