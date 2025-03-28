#Day7_exercise1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Walmart','Nvidia','Snowflake','Accenture','Discord'])
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.remove('Accenture')
print(it_companies)

#Join A and B
uni=A.union(B)
print("Union result set is: ",uni)

#Find A intersection B
inter=A.intersection(B)
print("Intersection result set is: ",inter)

#Is A subset of B
subset=A.issubset(B)
if subset==True:
    print("A is subset of B")
else:
    print("A is not a subset of B")

#Are A and B disjoint sets
disjoint=A.isdisjoint(B)
if disjoint==True:
    print("A and B are disjoint sets")
else:
    print("A and B are not disjoint sets")

#Join A with B and B with A
AB=A.union(B)
print(AB,"Here set B is joined to set A")

BA=B.union(A)
print(BA,"Here set A is joined to set B")

#What is the symmetric difference between A and B
AB_symm_diff=A.symmetric_difference(B)
print("Symmetric difference of A and B is: ",AB_symm_diff)

#Delete the sets completely
del A 
print(A)
del B
print(B)

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age=set(age)
print(set_age)

if (len(age)>len(set_age)):
    print("List is bigger than set")
elif (len(age)<len(set_age)):
    print("Set is bigger than list")
else:
    print("Both list and set are equal in length")
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
string= "I am a teacher and I love to inspire and teach people."
string_split=string.split(' ')
string_split.sort()
print(string_split)
string_set=set(string_split)
print("Unique words identified from above string are: ",string_set)