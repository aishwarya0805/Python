#Day6_exercise1
#Create an empty tuple
tpl=()
print(tpl)
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros=('Ashay','Yash','Kedar')
print(bros)
sis=('Janhavi','Maithili')
print(sis)
#Join brothers and sisters tuples and assign it to siblings
siblings=bros+sis
print(siblings)
#How many siblings do you have?
siblings_count=len(siblings)
print("I have ",siblings_count,"brothers and sisters in all")
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings_list=list(siblings)
print(siblings_list)
siblings_list.insert(5,'Atul')
siblings_list.insert(6,'Alka')
print(siblings_list)
family_members=tuple(siblings_list)
print(family_members)

#Unpack siblings and parents from family_members
ash,ya,ke,ja,ma,*parents=family_members

print(ash)
print(ya)
print(ke)
print(ja)
print(ma)
print(*parents)


