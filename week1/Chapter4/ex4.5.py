"""4-5. Summing a Million: Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers."""

one_million = list(range(1,100001))
print(f"minium of list {min(one_million)}")
print(f"maximum of list {max(one_million)}")
print(f"sum of list {sum(one_million)}")
# print(one_million)