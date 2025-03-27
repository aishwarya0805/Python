# #Day5_exercise
# #Declare an empty list
# lst=[] #empty list
# print(lst)

# #Declare a list with more than 5 items
# lst=[1,2,3,4,5,6,7,8,9]
# print(lst)

# #Find the length of your list
# print(len(lst))

# #Get the first item, the middle item and the last item of the list
# print("First element of the list is",lst[0],"\nMiddle element is",lst[(len(lst)//2)],"\nlast ement of the list is",lst[-1])

# #Declare a list with mixed data types
# mixed_list=['Ash','25','5.7','Unmarried','USA']
# print(mixed_list)

# it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(it_companies)
# print(len(it_companies)) #gives length of the list and number of items in the list

# print("First company of the list is",it_companies[0],"\nMiddle company is",it_companies[(len(it_companies)//2)],"\nlast company of the list is",it_companies[-1])

# #Modify anyone company and print the list
# it_companies[4]='Walmart'
# print(it_companies)
# it_companies.insert(7,'Nvidia')
# print(it_companies)

# #Change one of the it_companies names to uppercase 
# it_companies[3]=it_companies[3].upper()
# print(it_companies)

# #Join the it_companies with a string '#;  '
# it_companies_change= '#;'.join(it_companies)
# print(it_companies_change)

# #Check if a certain company exists in the it_companies list.
# print('Walmart' in it_companies)

# #Sort the list using sort() method
# it_companies.sort()
# print(it_companies)

# it_companies.reverse()
# print(it_companies)

# it_companies.sort(reverse=False)
# print(it_companies)

# #Slice out the first  and last 3 companies from the list
# #first three companies
# print(it_companies[0:3])

# #last three
# print(it_companies[-3:])

# #middle company
# print(it_companies[len(it_companies)//2])

# #Remove the first IT company from the list
# it_companies.remove('APPLE')
# print(it_companies)

# #Remove the middle IT company or companies from the list
# it_companies.pop(len(it_companies)//2)
# print(it_companies)

# #Remove the last IT company from the list
# del it_companies[-1]
# print(it_companies)

# #Remove all IT companies from the list
# it_companies.clear()
# print(it_companies)

# #destroy list
# del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#After joining the lists above. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=front_end.copy()
print(full_stack)

full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
