users = [
    {'username' : 'aeinstein',
        'first' : 'albert',
        'last' : 'einstein',
        'location':'princeton'
    },
    { 'username' : 'mcurie',
        'first' : 'marie',
        'last' : 'curie',
        'location': 'princeton',
    },
    { 'username' : 'elonmusk',
        'first' : 'elon',
        'last' : 'musk',
        'location' : 'washintonD.C'
    },
    { 'username' : 'dtrump',
        'first' : 'donald',
        'last' : 'trump',
        'location' : 'washintonD.C'
    },
    { 'username' : 'jbiden',
        'first' : 'Joe',
        'last' : 'biden',
        'location' : 'Pennsylvania'
    },
]
for user in users : #iterable
    for key,value in user.items():
        print(f"{key} {value.title()}")
    print()