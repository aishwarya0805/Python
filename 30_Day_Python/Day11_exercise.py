# #Day11_exercise
# #Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add(a,b):
#     add=a+b
#     return add
# print("The sum of two numbers is: ",add(3,4))

# #Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle(r):
#     area_of_circle=3.14*r*r
#     return area_of_circle
# print("Area of circle is: ",area_of_circle(5))

# #Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*args):
#     if (float(i) for i in args):
#         return sum(args)

# print(add_all_nums(1,4,2))
# print(add_all_nums(1,'hi',8)) #throws error

# #Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# def temp_CtoF(Celsius):
#     Farenheit=Celsius*(9/5)+32
#     return Farenheit
# print("Farenheit equivalent to Celsius is: ",temp_CtoF(32))

# #Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def season(month):
#     if month in ('December', 'January','February'):
#         return print(month,"is winter season")
#     elif month in ('March', 'April','May'):
#         return print(month,"is spring season")
#     elif month in ('June', 'July','August'):
#         return print(month,"is summer season")
#     else:
#         return print(month,"is autumn season")
# print(season('January'))

# #Write a function called calculate_slope which return the slope of a linear equation
# def slope(x1,x2,y1,y2):
#     return (y2-y1)/(x2-x1)

# print(slope(2,1,3,4))

# #Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# def linear_equation(a,b,c):
#     return print(a,"x^2 +",b,"x +",c,"= 0")
# print(linear_equation(2,3,4))

# #Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(my_list):
#     for i in my_list:
#         print(i)

# my_list=[1,1,3,2,4]
# print_list(my_list)

# #Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# def reverse_list(my_array):
#     reverse_list=[]
#     for i in range(len(my_array)-1,-1,-1):
#         reverse_list.append(my_array[i])
#     return reverse_list
# my_array= ['one','two','three','four','five']
# print(reverse_list(my_array))

# #Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(my_list):
#     return [i.capitalize() for i in my_list]

# my_list=['dog','cat','hen','frog']
# print(capitalize_list_items(my_list))

# #Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# def add_item(my_list,item):
#     my_list.append(item)
#     return my_list

# my_list=[1,2,3,4]
# print(add_item(my_list,5))

# #Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# def remove_item(my_list,item):
#     my_list.pop(item) #use index to remove item
#     return my_list
# my_list=[1,2,3,4]
# print(remove_item(my_list,3))

# def remove_item(my_list,item):
#     my_list.remove(item) #give item value to remove it
#     return my_list
# my_list=[1,2,3,4]
# print(remove_item(my_list,3))

# #Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# def sum_of_numbers(num):
#     sum=0
#     for i in range(1,num):
#         sum = sum + i
#     return sum
# print(sum_of_numbers(5))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(num):
#     sum_odd=0
#     for i in range(1,num+1):
#         if i%2!=0:
#             sum_odd+=i
#     return sum_odd

# print(sum_of_odds(5))

# #Alternative method
# def sum_of_odds(num):
#     sum_odd=0
#     for i in range(1,num+1,2):
#             sum_odd+=i
#     return sum_odd

# print(sum_of_odds(5))

# #Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(num):
#     sum_even=0
#     for i in range(0,num+1,2):
#             sum_even+=i
#     return sum_even

# print(sum_of_even(5))

# #Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# def evens_and_odds(n):
#     cnt_even=0
#     cnt_odd=0
#     for i in str(n):
#         if int(i)%2==0:
#             cnt_even+=1
#             #print("Count of even numbers in given range is:",cnt_even)
#         else:
#             cnt_odd+=1
#             #print("Count of even numbers in given range is:",cnt_odd)
       
    
#     print("Number of evens: ",cnt_even)
#     print("Number of odds: ",cnt_odd)

# evens_and_odds(123456789)

# #Call your function is_empty, it takes a parameter and it checks if it is empty or not
# def is_empty(my_list):
#     if len(my_list)==0:
#         print("List is an empty list")
#     else:
#         print("List has",len(my_list),"items")

# my_list=[1,2,3,4,5]
# my_list=[]
# is_empty(my_list)

#Create different functions to calculate mean,median,mode,variance,standard_deviation,range
import math
def calculate_mean(data):
    data_mean=sum(data)/len(data)
    return data_mean

def calculate_median(data):
    sorted_data=sorted(data)
    n=len(data)
    if n%2==1:
        return sorted_data[n//2]
    else:
        return (sorted_data[n//2-1] + sorted_data[n//2])/2     

def calculate_mode:

def calculate_range(data):
    data_range=max(data)-min(data)
    return data_range

def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)

def calculate_std_deviation(data):
    std_dev=math.sqrt(calculate_variance(data))
    return std_dev

data=[1,2,3,4,5]
print("Calculated mean of data is: ",calculate_mean(data))
print("Calculated median of data is: ",calculate_median(data))
print("Calculated range of data is: ",calculate_range(data))
print("Calculated variance of data is: ",calculate_variance(data))
print("Calculated standard deviation of data is: ",calculate_std_deviation(data))