#clist = [45, 67, 56, 78] list, list()
#ctuple = (45, 67, 56, 78) tuple, tuple()
#creating a dictionary
#item represent the key and value
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0['points'])
print("type",type(alien_0))
print("len",len(alien_0))

new_point = alien_0['points']
print(f"You just earned {new_point} points!")

#adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25

#viewing the whole raw dictionary
print(alien_0)
alien_0['x_position']= 10

#after setting value 10 to x_position
print(alien_0)

