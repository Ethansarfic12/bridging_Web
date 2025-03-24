cars = ['bmw', 'audi', 'toyota', 'subaru']#car_list
print(f"Here is the original list:\n{cars}\n")
print(f"Here is the sorted list:\n{sorted(cars)}\n")
print(f"Here is the original list again:\n{cars}\n")
print(f"Here is the reverse sorted list:\n{sorted(cars,reverse=True)}\n")

cars.reverse()
print(f"reverse list\n {cars}")
print (f"car length {len(cars)}")