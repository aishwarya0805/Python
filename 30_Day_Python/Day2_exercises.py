#Day2_exercise1
# Write a python comment saying 'Day 2: 30 Days of python programming'
#Day 2: 30 Days of python programming
# Declare a first name variable and assign a value to it
#first_name= 'John'
first_name= input("Please enter your first name: ")
print("My first name is",first_name)
print(type(first_name))
fname_len=print('Length of my first name is: ',len(first_name))
s
# Declare a last name variable and assign a value to it
#last_name= 'Smith'
last_name= input("Please enter your last name: ")
print("My last name is",last_name)
print(type(last_name))
lname_len=print('Length of my last name is: ',len(last_name))

if fname_len==lname_len:
    print("Lengths of first name and last name are same")
else:
    print("Lengths of first name and last name are not same")

# Declare a full name variable and assign a value to it
full_name= (first_name,last_name)
print("My full name is ",full_name)
print(type(full_name))
# Declare a country variable and assign a value to it
country= input("Please enter the country name where you stay: ")
print('I stay in',country)
print(type(country))
# Declare a city variable and assign a value to it
city= input("Please enter your city: ")
print('I stay in',city)
print(type(city))
# Declare an age variable and assign a value to it
age= input("Please enter your age: ")
print('My age is',age, 'years old')
print(type(age))
# Declare a variable is_married and assign a value to it
married= input("Please let us know if your marital status: ")
print('I am', married)
print(type(married))
# Declare a variable is_true and assign a value to it
is_true= input("Is your marital status true?")
print(is_true)
print(type(is_true))
# Declare multiple variable on one line
a=b=c=d='letters'
print(type(b))

#Day2_exercise2
import math
 #num_one=5
 #num_two=4
num_one=int(input("Please enter first number: "))
num_two=int(input("Please enter second number: "))
total= num_one+num_two
print("Total of two numbers is",total)
diff=num_one-num_two
print("Difference of two numbers is",diff)
mul=num_one*num_two
print("Product of two numbers is",mul)
div=num_one/num_two
print("Division of two numbers is",div)
remainder=num_two%num_one
print("Remainder of two numbers is",remainder)
exp=num_one**num_two
print("Exponential value of two numbers is",exp)
pow_exp=pow(num_one,num_two)
print("Exponential value of two numbers using power function is",pow_exp)
floor_div=int(num_one/num_two) # using simple int approach
print("Floor value post division of two numbers is",floor_div)
math_floor_div=math.floor(num_one/num_two) # by importing math library to use floor function
print("Floor value post division of two numbers is",math_floor_div)

#To calculate area and circumference of a circle
radius= int(input("Please enter a value for radius of a circle: "))
area=3.14*pow(radius,2)
print("Area of a circle is: ",area)
circumference= 2*3.14*radius
print("Circumference of a circle is: ",circumference)