#Day14_exercise

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use map to create a new list by changing each country to uppercase in the countries list
def uppercase_countires(countries):
    return countries.upper()

updated_countries=map(uppercase_countires,countries)
print(list(updated_countries))

#Use map to create a new list by changing each number to its square in the numbers list
def num_squares(num):
    return num**2

squares= map(num_squares,numbers)
print(list(squares))

#Use map to change each name to uppercase in the names list
def uppercase_name(name):
    return name.upper()

upper_names= map(uppercase_name,names)
print(list(upper_names))

#Use filter to filter out countries containing 'land'.
def countries_filter(countries):
    if 'land' in countries:
        return countries
    
land_countries=filter(countries_filter,countries)
print(list(land_countries))

#Use filter to filter out countries having exactly six characters.
def countries_len(countries):
    if len(countries)==6:
        return countries
    
land_countries=filter(countries_len,countries)
print(list(land_countries))

#Use filter to filter out countries containing six letters and more in the country list.
def countries_len(countries):
    if len(countries)>=6:
        return countries
    
len_countries=filter(countries_len,countries)
print(list(len_countries))

#Use filter to filter out countries starting with an 'E'
def countries_withE(countries):
    if countries.startswith('E'):
        return countries

countriestartswithE=filter(countries_withE,countries)
print(list(countriestartswithE))

#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
def squares(num):
    return num**2
    
def square_filter(num):
    if num>5:
        return num
squares=map(squares,numbers)
gtfive=filter(square_filter,numbers)

def reduce_num(x,y):
    return int(x)+int(y)
total_of_num=reduce(reduce_num,numbers)
print(list(squares))
print(list(gtfive))
print(total_of_num)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
lst=[1,'two','three',4,5,'six',7,8,'nine','ten']

def get_string_lists(lst):
    string_list=[]
    for x in lst:
        if type(x)==str:
            string_list.append(x)
    return string_list
        
print(list(get_string_lists(lst)))

#Use reduce to sum all the numbers in the numbers list.
numbers=[2,4,6,8,10,12,14,16,18,20]

def add_nums(x,y):
    return int(x)+int(y)

total=reduce(add_nums,numbers)
print(total)

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda acc, cur: acc + ', ' + cur, countries[:-1])
sentence += f', and {countries[-1]} are north European countries.'
print(sentence)

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    return [country for country in countries if pattern.lower() in country.lower()]

print(categorize_countries('land'))
print(categorize_countries('ia'))

#Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def country_name_stats(countries):
    stats = {}
    for country in countries:
        first_letter = country[0].upper()  # Get the first letter and convert to uppercase
        stats[first_letter] = stats.get(first_letter, 0) + 1  # Update the count
    return stats

result=country_name_stats(countries)
print(result)

