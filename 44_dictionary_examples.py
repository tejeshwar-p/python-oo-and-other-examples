occurrences = dict(a=5, b=6, c=8)
print(occurrences)
print(type(occurrences))
occurrences['d'] = 15
print(occurrences)
occurrences['d'] = 10
print(occurrences)
print(occurrences.get('d'))
print(occurrences.get('e', 20))  # just prints the value since not present in dictionary
print(occurrences)
print(occurrences.keys())
print(occurrences.values())
print(occurrences.items())

for key, value in occurrences.items():
    print(f"{key} {value}")

occurrences['a'] = 0
print(occurrences)
del occurrences['a']
print(occurrences)

