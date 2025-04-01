pet_0 = {'name' : 'boobby',
         'type' : 'dog',
         'owner_name' : 'U Kyaw Min'}
pet_1 = {'name' : 'bunny',
         'type' : 'rabbit',
         'owner_name' : 'Daw Pan Nu'}
pet_2 = {'name' : 'kitty',
         'type' : 'cat',
         'owner_name' : 'U Tun Tun'}
pets = [pet_0, pet_1,pet_2]
for pet in pets :
    for k, v in pet.items():
        print(f"\t{k} : {v}")
    print() 