cities = {'yangon': {
        'Country' : 'Myanmar',
        'Population' : 5.1,
        'fact': "Yangon, formerly romanized as Rangoon, is the capital of the Yangon Region and the largest city of Myanmar."
    },
          'bangkok':{
              'country':'thailand',
              'population': 11.23,
              'fact' : "It's capital of Thailand"},
          
          'tokyo':{
              'country' :'japan',
              'population' : 37.1,
              'fact' : "It's the capital of Japan"},
          'aukland':{
              'country' :'new zealand',
              'population' : 1.7,
              'fact' : "It's the capital of Newzeland"},
          'toranto':{
              'country' :'japan',
              'population' : 2.8,
              'fact' : "It's the capital of Canada."
          }}
for city, info in cities.items():
    print(f"c{city}'s Information")
    for k, v in info.items():
        print(f"\t{k} : {v}")
    print()