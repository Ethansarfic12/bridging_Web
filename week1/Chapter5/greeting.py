usernames = ['james', 'john', 'admin', 'eric', 'tom']
for username in usernames: 
    if username == 'admin':
        print ('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')
print('') # print a blank line
# Compare this snippet from python/bridging_Web/week1/Chapter5/ex.5.9.py: