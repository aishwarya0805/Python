#Day9_exercise
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
#If below 18 give feedback to wait for the missing amount of years. 

age=int(input("Enter your age:"))
if age > 18:
    print("You are old enough to drive.")
else:
    print("Please wait for the missing amount of years")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
my_age= 30
your_age=int(input("Please enter your age: "))
age_diff=abs(my_age-your_age)
if your_age>my_age:
    print("you are ", age_diff, "older than me!")
elif your_age<my_age:
    print("you are ", age_diff, "younger than me!")
if abs(your_age-my_age)==1:
    print("We have only 1 year age difference")
else:
    print("We both are of same age!!")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. 
a=int(input("Please enter a number: "))
b=int(input("Please enter another number: "))

if a>b:
    print("a is greater than b")
elif a<b:
    print("a is smaller than b")
else:
    print("a is equal to b")

#Write a code which gives grade to students according to theirs scores:

score=float(input("Please enter your score to know your grades: "))

if (score >= 80 and score <= 100):
    print("You've received grade A")
elif (score >= 70 and score <= 79):
    print("You've received grade B")
elif (score >= 60 and score <= 69):
    print("You've received grade C")
elif (score >= 50 and score <= 59):
    print("You've received grade D")
else:
    print("You've received grade F")

#Check if the season is Autumn, Winter, Spring or Summer. 
month= input("Please enter a month to check the season: ")

if month in ('December', 'January','February'):
    print(month,"is winter season")
elif month in ('March', 'April','May'):
    print(month,"is spring season")
elif month in ('June', 'July','August'):
    print(month,"is summer season")
else:
    print(month,"is autumn season")

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruit_name=input("Please enter fruit name of your choice: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit_name in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit_name)
    print(fruit_name,"was added to the list and modified list is: ",fruits)

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#If the person is married and if he lives in Finland, print the information in the following format:
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print(person)

if 'skills' in person:
    skill_list=person['skills']
    middle_element= len(skill_list)//2
    mid_skill= skill_list[middle_element]
    print("Middle skill in the list is:  ",mid_skill)
else:
    print("Skills key doesn't exist in the dictionary")

if 'Python' in person['skills']:
    print("Yes Python is one of the skill in the list")
else:
    print("Python doesn't exist")

if ['JavaScript', 'React'] in person['skills']:
    print('He is a front end developer')
elif ['Node', 'Python', 'MongoDB'] in person['skills']:
    print('He is a backend developer')
elif ['React', 'Node','MongoDB'] in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['country']=='Finland' and person['is_marred']==True:
    print("Asabeneh lives in ",person['country'],"and he is married")