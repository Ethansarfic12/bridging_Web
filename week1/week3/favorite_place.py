favourite_places = {
    'yati' : ['POL','MDY','Saging'],
    'kevin' : ['YAY','Maungmakan','Ngapali'],
    'andrew' : ['Taungyi' , 'Innlay', 'Pintaya']
}

for name, places in favourite_places.items():
    print(f"Name : {name}")
    print("Favourite places")
    for place in places:
        print("\t",place)
    print()
    