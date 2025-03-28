#Day5_exercise2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
sorted_ages=ages.sort()
print(sorted_ages)

ages_max=max(ages)
print(ages_max)

ages_min=min(ages)
print(ages_min)

#Find the median age
print (ages)
median=ages[(len(ages)//2)]
print(median)

#Find the average age
avg=sum(ages)/len(ages)
print(avg)

#Find the range of the ages 
range=(max(ages))-(min(ages))
print(range)

countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark','India']
countries_mid=len(countries)//2
print(countries_mid)
#first half list
sublist1=countries[:countries_mid]
print(sublist1)

#second half list
sublist2=countries[countries_mid:]
print(sublist2)

#unpacking countries
ch,rus,usa,*scandic=countries
print(ch)
print(rus)
print(usa)
print(*scandic)