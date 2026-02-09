#Day10_exercise
#Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(0,11):
    print(i)
print("Printed values of 'i' using 'for' loop")

count=0
while count<11:
    print(count)
    count=count+1
print("Printed values of 'i' using 'while' loop")

#Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)
print("Printed values of 'i' using 'for' loop")

count=10
while count>=0:
    print(count)
    count=count-1
print("Printed values of 'i' using 'while' loop")

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("# triangle in incremental order")
for i in range(1,8):
    print('#'*i)

print("# triangle in inverted order")
for i in range(7,0,-1):
    print('#'*i)

  #inverted triangle
print("complete # triangle")
for i in range(7,-1,-1):
    print('#'*i)

#Use nested loops to create the following:
i=1
j=1
for i in range(11):
    for j in range(11):
        print("#",end=' ')
    print()

#Print the following pattern:
i=0
for i in range(11):
    print(i,'*',i,'=',i*i)
print()

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
tech_list= ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in tech_list:
    print(i)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,101):
    if i%2==0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,100):
    if i%2!=0:
        print(i)

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum=0
for i in range(0,101):
    sum=sum+i
print("Sum of 100 numbers",sum)

#print the sum of all numbers from 0 to 100 without using loop.
n=100
sum=n*(n+1)//2
print("Sum of 100 numbers",sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even=0
sum_odd=0
for i in range(101):
    if (i%2)==0:
        sum_even=sum_even+i
    elif (i%2)!=0:
        sum_odd=sum_odd+i
print("Sum of even numbers from 0 to 100 is: ",sum_even)
print("Sum of odd numbers from 0 to 100 is: ",sum_odd)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits= ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = [] 
for i in range(len(fruits) - 1, -1, -1): \
    reversed_fruits.append(fruits[i]) 

print(reversed_fruits)

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data.countries import countries

countries_land= [country for country in countries if 'land' in country]
print(countries_land)
