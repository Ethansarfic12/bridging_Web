"""4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube."""
cubes = []
for value in range(1,11):
    cubes.append(value **3)
    print ("First ten cubes")
    print (cubes)
    
"""4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
10 cubes."""
cube_list = [value **3 for value in range(1,11) ]
print(cube_list)
# Output: