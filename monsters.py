list_of_monsters = []

monster_stat_types = ["atk",
             "dfns", "dod", "hp",
             "intel", "fth", "stgh", "dex", "mon_lvl"]
#mon_lvl will be used later to sum to some number generated based off ave party lvl
with open("monster_stats.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        line = line.replace(" ", ",")
        line = line.split(",")
        for item in line:
            if item.isdigit() == True or item.isdecimal() == True:
                line[line.index(item)] = float(item)
        list_of_monsters.append(line)
print(list_of_monsters)
