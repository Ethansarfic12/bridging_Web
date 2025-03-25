age = int (input ("Enter your age >> "))
if age < 4 :
    #print("Your admission cost is 0.")
    price=0
elif age <18:
    #print("Your admission cost is $25.")
    price = 25
else:
    #print("Your admission cost is $50.")
    price = 40
print(f"Your admission cost is $50.")