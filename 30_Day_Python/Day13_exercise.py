# Day13_exercise
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers=[i for i in numbers if i<=0]
print(negative_numbers)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]

print(flattened)

#Using list comprehension create the following list of tuples
list_of_tuples = [(n, n**0, n**1, n**2, n**3, n**4, n**5) for n in range(11)]
print(list_of_tuples)

#Flatten below list to new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(),capital.upper()] 
            for [[country,capital]] in countries]

print(output)

# Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dicts = [{'country': country, 'city': city} 
                for [[country, city]] in countries]
print(country_dicts)

#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{first} {last}" for [[first, last]] in names]
print(full_names)

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
m = slope(1, 2, 3, 6)
print("Slope:", m)