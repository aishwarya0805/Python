#Day8_exercise

#Create an empty dictionary called dog
dog={}
print(type(dog))

#add name, color, breed, legs, age to the dog dictionary
dog['key1']='name'
dog['key2']='color'
dog['key3']='breed'
dog['key4']='legs'
dog['key5']='age'
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={}
student['first_name']='John'
student['last_name']='Smith'
student['gender']='Male'
student['age']='29'
student['marital status']='Unmarried'
student['skills']=['Python','Java','SQl','Excel']
student['country']='ABC'
student['city']='XYZ'
student['address']='Suite 1001'
print(student)

#Get the length of the student dictionary
print("Length dictionary 'student' is: ",len(student))

#Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

#Modify the skills values by adding one or two skills
student['skills'].append('PowerBI')
print(student)

#Get the dictionary keys as a list
print("Here are the keys of the dictionary in list format: ",list(student))

#Get the dictionary values as a list
student_val_list=list(student.values())
print(student_val_list)

#Change the dictionary to a list of tuples using items() method
list_of_tuples=list(student.items())
print(list_of_tuples)

#Delete one of the items in the dog dictionary
dog.pop('key5')
print(dog)

#Delete one of the dictionaries
del dog
print(dog) #to check if dictionary got deleted