from operator import attrgetter


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country("India", 1200, 100),
             Country("China", 1400, 200),
             Country("USA", 120, 300)]
print("----------------------------- list -----------------------------")
print(countries)
print(countries[0])
print(countries[0:2])
countries.append(Country("Russia", 100, 500))
print(countries)
print("----------------------------- sorting -----------------------------")
# Below line will give error -
# TypeError: '<' not supported between instances of 'Country' and 'Country'
# countries.sort()

# To sort using the instance's specific key we have to import attrgetter
# from operator package
countries.sort(key=attrgetter('population'))
print(countries)
print("----------------------------- max population -----------------------------")
print(max(countries, key=attrgetter('population')))
print("----------------------------- min population -----------------------------")
print(min(countries, key=attrgetter('population')))
print("----------------------------- max area -----------------------------")
print(max(countries, key=attrgetter('area')))
print("----------------------------- min area -----------------------------")
print(min(countries, key=attrgetter('area')))
