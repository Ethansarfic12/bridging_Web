dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimension[0] = 250
# TypeError: 'tuple' object does not support item assignment

my_t = (500) #
print(type (my_t)) # 500
my_t = (500,) # tuple
print(type (my_t)) # <class 'tuple'>

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)    