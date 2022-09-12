
"""
Sets = {"Element1","Element2", "Element3", "Element4"}
print(Sets)

if "Element1" in Sets:
    print("Yes")
"""



CountryList  = []

for i in range(5):
    Country = input("Please Enter Your Country: ")
    CountryList.append(Country)

"""
CountrySet = set(CountryList)

print(CountryList)
print(CountrySet)

if "Brazil" in CountrySet:
    print("Attended")

"""

#Dictionary = {"Key":"Value", "Key2":"Value2"}

CountryDictionary = {}
for Country in CountryList:
    if Country in CountryDictionary:
        CountryDictionary[Country] += 1
    else:
        CountryDictionary[Country] = 1

print(CountryDictionary)
