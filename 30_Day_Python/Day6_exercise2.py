#Day6_exercise2
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('apple','mango','kiwi')
print(fruits)
veggie=('onion','chilly','beans')
print(veggie)
animal_prod=('milk','beef','cheese')
print(animal_prod)
food_stuff_tp=fruits+veggie+animal_prod
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
length = len(food_stuff_tp)
mid = length // 2

# Slice out the middle item(s)
if length % 2 == 0:  # Even length
    middle_items = food_stuff_tp[mid - 1: mid + 1]
else:  # Odd length
    middle_items = (food_stuff_tp[mid],)

print("Middle item(s):", middle_items)

#Slice out the first three items and the last three items from food_staff_lt list
first_three_lt=food_stuff_tp[0:3]
print(first_three_lt)
last_three_lt=food_stuff_tp[-3:]
print(last_three_lt)

#delete food_stuff_tp tuple completely
del food_stuff_tp
print(food_stuff_tp)


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)