#Day18_exercise
#What is the most frequent word in the following paragraph?
import re
import keyword

paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love.'''

words = re.findall(r'\b\w+\b', paragraph.lower())

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)

most_frequent_word = ''
max_count = 0

for word, count in word_freq.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count

print("Most frequent word:", most_frequent_word)
print("Frequency:", max_count)



# # The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 
in the negative direction, 0 at origin, 4 and 8 in the positive direction."""

points = re.findall(r'-?\d+', text)

points = [int(point) for point in points]

sorted_points = sorted(points)

distance = sorted_points[-1] - sorted_points[0]

print("Extracted points:", sorted_points)
print("Distance between furthest particles:", distance)


# #Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(var_name):

    if keyword.iskeyword(var_name):
        return False
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var_name) is not None

# Test cases
print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True
print(is_valid_variable('for'))          # False (it's a keyword)

# #Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& 
@emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting 
tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned = re.sub(r'[^a-zA-Z\s]', '', sentence)

cleaned = cleaned.lower()
print("Cleaned string is: ",cleaned)

words = cleaned.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

top_three = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 most frequent words:")
for word, freq in top_three:
    print(f"{word}: {freq}")

