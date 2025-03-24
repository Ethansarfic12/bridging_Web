#3-8. Seeing the World

locations = ['Yangon','Mandalay','Bagan','Inle','PyinOoLwin']
print(locations)

#using temporary sorted function without affecting original list
print(sorted(locations))

print(f"original list \n {locations}")

locations.reverse()# it verses the original order of list
print(f"reverse order of list {locations}")

locations.reverse()#it verses the original order of list again
print(f"second time reverse call and order of list {locations}")

locations.sort()#smllest to largest
print(f"after sorting in alphabetical order {locations}")

locations.sort(reverse=True)#largest to smallest
print(f" after sorting with decreasing order {locations}")

print(f"number of places that I like to travel {len(locations)} locations")#number of elements in list

#print(locations[-6])