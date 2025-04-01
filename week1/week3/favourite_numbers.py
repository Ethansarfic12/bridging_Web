favourite_numbers = {
    'marie' : [1,4,5,3,2],
    'bob' : [2,1,4,6,4,1],
    'theingi' : [4,5,6]
}
for user in favourite_numbers.keys():
    print(f"{user}'s favourite numbers")
    for number in favourite_numbers[user]:
        print(number, end = " ")
    print()

print(favourite_numbers['marie'])

