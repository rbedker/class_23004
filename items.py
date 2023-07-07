list_of_items = []

item_stat_types = ["atk",
             "dfns", "dod", "hp",
             "intel", "fth", "stgh", "dex"]

with open("items.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        line = line.replace(" ", ",")
        line = line.split(",")
        for item in line:
            if item.isdigit() == True or item.isdecimal() == True:
                line[line.index(item)] = float(item)
        list_of_items.append(line)
print(list_of_items)
