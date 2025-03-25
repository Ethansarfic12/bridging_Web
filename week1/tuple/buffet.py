buffet_foods = ('rice', 'beans', 'chicken', 'beef', 'fish')
print("Favorite foods:")
for food in buffet_foods:
    print(food)

#buffet_foods[0] = 'pasta'
#TypeError: 'tuple' object does not support item assignment
buffet_foods = ('pasta', 'beans', 'chicken', 'beef', 'fish','noodle', 'soup')
print("\nModified favorite foods:")
for ind, food in enumerate(buffet_foods):
    print(f"{ind+1} {food}")
