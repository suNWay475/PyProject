capitals = {
    "USA": "Washington",
    "Ukraine": "Kiyiv",
    "Germany": "Berlin",
    "France": "Paris"
    }

print(capitals.keys())

def seeCountry(somecapitals):
    for key in somecapitals.keys():
        print(key)

seeCountry(capitals)

capitals.update({'Poland': 'Warsaw'})

seeCountry(capitals)

values = capitals.values()

def valueCountry():
    for value in values:
        print(value)

valueCountry()