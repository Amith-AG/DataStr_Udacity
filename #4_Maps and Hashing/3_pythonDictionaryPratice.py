"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""
locations = {'North America': {'USA': ['Altanta','Mountain View']},
    'Asia':{'India':'Bangalore','China':'Shanghai'},
    'Africa':{'Egypt':['Cairo']},
}
"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
for i in locations.keys():
    if i =='North America':
        for idx,val in locations[i].items():
            if idx=='USA':
                for a in val:
                    print a
                break
for i in locations.keys():
    if i =='Asia':
        for idx,val in locations[i].items():
            print val," - ",idx
