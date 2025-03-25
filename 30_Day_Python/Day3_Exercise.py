#Day3_Exercise
import math
Age=int(input("please enter your age: "))
print("My age is", Age, 'years!')
Height=float(input("please enter a value as height: "))
print("Given height is", Height)
comp_num=complex(input('Enter a complex number'))
print("Complex number is", comp_num)

A#rea of a triangle
base=float(input("Please a value for base of a triangle: "))
print("Please confirm that value for base of a triangle is ",base)
height=float(input("Please a value for height of a triangle: "))
print("Please confirm that value for height of a triangle is ",height)
Area_of_triangle= 0.5*base*height
print("Area of a triangle is ",Area_of_triangle)

#Calculate Perimeter of a triangle
a=float(input("Enter value for side a: "))
b=float(input("Enter value for side b: "))
c=float(input("Enter value for side c: "))
Perimeter_of_triangle=a+b+c
print("Perimeter of a triangle is ",Perimeter_of_triangle)

#Calculate Perimeter of a rectangle
length=float(input("Enter value of rectangle length: "))
width=float(input("Enter value for rectangle width: "))
Perimeter_of_rectangle=2*(length+width)
print("Perimeter of a rectangle is ",Perimeter_of_rectangle)

#Calculate the slope
x=float(input("Please enter a value for x-intercept: "))
print("x-intercept is ", x)
y=2*x-2
print("Value of slope is: ", y)

#Calculate slope and Euclidean distance
import math
print("Please enter four cordinates: ")
p1=float(input("Enter value of p1: "))
p2=float(input("Enter value of p2: "))
q1=float(input("Enter value of q1: "))
q2=float(input("Enter value of q2: "))

slope= (q2-q1)/(p2-p1)
print("Calculated slope value is ",slope)

euc_dist=math.sqrt(pow((p2-p1),2)+pow((q2-q1),2))
print("Calculated value for euclidean distance is ",euc_dist)

# Comparing two slopes with variable y and slope calculated above
if y==slope:
    print("Both slopes are equal")
else:
    print("Both slopes are not equal")

#Evaluate an equation
x=float(input("Please enter a value of x to evaluate an equation:"))
y=x**2+6*x+9
print("Result of an evaluated equation x^2+6x+9 is",y)

str1= 'Python'
str2= 'Dragon'
str1=input("Enter string1: ")
str2=input("Enter string2: ")
if len(str1)==len(str2):
    print("Lengths of two strings are equal")
else:
    print("Lengths of two strings are not equal")

print('on' in 'Python' and 'on' in 'Dragon' ) # to check if 'on' is present in Python and Dragon

dialogue= 'I hope this course is not full of jargon.'
print('jargon' in dialogue)

str1_len=len(str1)
print(str1_len)
str1_flt=float(str1_len)
print(str1_flt)
str1_strng= str(str1_len)
print(str1_strng)

#even/odd number
num=int(input("Please enter a number to check if its even or odd:"))
if (num%2)==0:
   print(num,"is an even number")
else:
   print(num,"is an odd number")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_div=math.floor(7/3)
print(floor_div)
int_conv=int(2.7)
if floor_div == int_conv:
    print('Results of floor_div and int converted are same')
else:
    print('Results of floor_div and int converted are not same')

#Check if type of '10' is equal to type of 10
ten= '10'
ten1= 10
if type(ten) == type(ten1):
    print("Datatypes of both the variables are same")
else:
    print("Datatypes of both the variables are different")

#Calculate weekly pay of the person
hours=float(input('Enter number of hours an employee worked for: '))
rate_per_hour=float(input('Enter per hour wage of an employee: '))
Weekly_earnings_of_employee= hours*rate_per_hour
print("This employee earns weekly $",Weekly_earnings_of_employee)

#Calculate the number of seconds a person have lived.
year=float(input("Please enter your age in years: "))
lived_years=year*365*24*60*60
print("Wow! So far you've lived for ", lived_years, 'seconds!')

# Function to print the table
'''1   1   1   1   1
2   1   2   4   8
3   1   3   9  27
4   1   4  16  64
5   1   5  25 125'''
def print_table():
    for i in range(1, 6):
        row = [i ** j for j in range(4)]
        print(i," ".join(f'{num:3}' for num in row))

print_table()
