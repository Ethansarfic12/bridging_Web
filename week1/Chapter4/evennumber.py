even_number = list(range(2,11,2))#start,stop,step
#list function use [] operator to creat list of numbers
#range function use to generate sequence of numbers
print(even_number)

num_list = [4,5,6,7,8]
num_list2= list(range(4,9))
a_tuple = ()
#tuple is immutable 
b_tuple = tuple([4,5,6])

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(f"square list\n {squares}")
print(f"min value in square list {min(squares)}")
print(f"max value in square list {max(squares)}")

#list comprehension - generate the same list in one line of code 
square_list = [value ** 2 for value in range(1,11)]
print(square_list)