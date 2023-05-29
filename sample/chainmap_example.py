from collections import ChainMap

# dictionaries can be created using curly bracket or dict() function

bedroom_furnitures = { 
    "bedframe": 500,
    "mattress": 1000,
    "nightstand": 500,
    "light": 150 
    }

livingroom_furnitures = {
    "tv" : 2000,
    "sofa": 2000,
    "coffetable": 200,
    "light": 100
    }

diningroom_furnitures = {
    "diningtable": 2000,
    "diningchairs": 2000,
    "light": 200
    }

# hold all maps as one chainmap object
all_funitures = ChainMap(bedroom_furnitures, livingroom_furnitures, diningroom_furnitures)
print(all_funitures["diningtable"])

# return first occurrence of any duplicate keys
print(all_funitures["light"]) # 150

print(all_funitures) # all duplicates still exist in chainmap
# ChainMap({'bedframe': 500, 'mattress': 1000, 'nightstand': 500, 'light': 150}, {'tv': 2000, 'sofa': 2000, 'coffetable': 200, 'light': 100}, {'diningtable': 2000, 'diningchairs': 2000, 'light': 200})