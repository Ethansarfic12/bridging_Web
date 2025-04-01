favourite_number = {'TLM': 7, 'TLM2': 8, 'TLM3': 9, 'TLM4': 10, 'TLM5': 11}
for name, number in favourite_number.items():
    print(f"{name}'s favourite number is {number}")

print("items view")
for item in favourite_number.items():
    print("keys view ")
    print(favourite_number.keys())
    
    print("values view")
    print(favourite_number.values())

    