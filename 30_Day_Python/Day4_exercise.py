# #Day4_Exercise
# #Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Con_strng=['Thirty', 'Days', 'Of', 'Python']
# con_res_strng=' '.join(Con_strng)
# print(con_res_strng)

# #Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Con_strng=['Coding', 'For' , 'All']
# con_res_strng=' '.join(Con_strng)
# print(con_res_strng)

# #Declare a variable named company and assign it to an initial value "Coding For All". Print the variable company using print().
# #Print the length of the company string using len() method and print().
company="Coding For All"
print(company)
print("Length of the string in variable company is ",len(company))
print("String in uppercase is:",company.upper()) #convert all characters of string to upper case
print("String in lowercase is:",company.lower()) #convert all characters of string to lower case
print("Capitalized String is:",company.capitalize()) #convert all characters of string to capitalize format
print("String using title format function is:",company.title()) #convert string using title format function
print("String after using swapcase function is:",company.swapcase()) #convert string using swapcase format function
print(company[7:]) #Cut(slice) out the first word of Coding For All string.

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

#Replace the word coding in the string 'Coding For All' to Python.
company_repl=company.replace('Coding','Python')
print(company_repl)

#Change Python for All to Python for Everyone using the replace method or other methods.
company_repl1=company_repl.replace('All','Everyone')
print(company_repl1)

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_name= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_name.split(','))

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
substring= 'All'
print(company.rindex(substring))
print(company.index(substring))

#What character is at index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acr= company_repl1.split(' ')
acronym= ''.join(a[0] for a in acr )
print(acronym)

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C')) #find or index both can be used

#Use rfind to determine the position of the last occurrence of l in Coding For All.
print(company.rfind('l'))

#find the position of the first occurrence of the word 'because' in the following sentence: 
sent='You cannot end a sentence with because because because is a conjunction'
print(sent.index('because'))

#find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.replace('because because because','').strip())

#Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
company1= '   Coding For All      '
print(company1.strip(' '))

#Which one of the following variables return True when we use the method isidentifier():
is_iden1='30DaysOfPython'
is_iden2='thirty_days_of_python'
print(is_iden1.isidentifier())
print(is_iden2.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
python_libraries_repl= '# '.join(python_libraries)
print(python_libraries_repl)

#Use the new line escape sequence to separate the following sentences.
strng= ("I am enjoying this challenge.\nI just wonder what is next.")
print(strng)

#String formatting
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)


#Formatting
a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#Display in following format
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print('Name\t\Age\tCountry\tCity')
print('John\t25\tUSA\tNew York')