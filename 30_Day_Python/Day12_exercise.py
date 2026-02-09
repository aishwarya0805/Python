# #Day12_exercise
# #Writ a function which generates a six digit/character random_user_id.

import random
import string

def random_user_id_chars():
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=6))

print(random_user_id_chars())

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_ids=int(input("Enter number of ids that should be created: "))
    num_chars=int(input("Enter number of characters id should be: "))
    user_id=[]
    for i in range(num_ids):
        characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        u_id= ''.join(random.choices(characters, k=num_chars))
        user_id.append(u_id)

    for u_id in user_id:
        print(u_id)

user_id_gen_by_user()

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
def rgb_color_gen():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)

rgb_color= rgb_color_gen()
print(rgb_color)

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(color_num):
    hexa_color=[]
    for i in range(color_num):
        hex_num= '#'+ ''.join(random.choices('0123456789ABCDEF',k=6))
        hexa_color.append(hex_num)
    return hexa_color

color_num=int(input("Enter number of hexa colors you want to generate: "))
print(list_of_hexa_colors(color_num))

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():
    # Generate a random number of colors between 1 and 10
    num_colors = random.randint(1, 10)
    
    rgb_colors = []
    for _ in range(num_colors):
        # Generate random RGB values (R, G, B) between 0 and 255
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    
    return rgb_colors, num_colors  # Return both the list of colors and the count

# Example usage
colors, num_colors = list_of_rgb_colors()

# Print the generated RGB colors
print(f"Generated {num_colors} RGB Colors:")
for color in colors:
    print(color)

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    shuffled=input_list[:]
    random.shuffle(shuffled)
    return shuffled

my_list=[1,2,3,4,5]
shuffled_version=shuffle_list(my_list)

print("The original list was: ",my_list)
print("Shuffled list is: ",shuffled_version)

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_arr():
    return random.sample(range(10),7)

nums_generated=random_arr()
print("Unique number array generated is: ",nums_generated)