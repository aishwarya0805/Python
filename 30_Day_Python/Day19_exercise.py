#Day19_exercise
#Write a function which count number of lines and number of words in a text.

# def count_lines_words(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             lines = file.readlines()
#             num_lines = len(lines)
#             num_words = sum(len(line.split()) for line in lines)
#             return num_lines, num_words
#     except FileNotFoundError:
#         print("File not found.")
#         return 0, 0
    
# print("Number of lines and words for the given file are: ",count_lines_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/obama_speech.txt'))
# print("Number of lines and words for the given file are: ",count_lines_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/michelle_obama_speech.txt'))
# print("Number of lines and words for the given file are: ",count_lines_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/melina_trump_speech.txt'))
# print("Number of lines and words for the given file are: ",count_lines_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/donald_speech.txt'))

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
# import json

# def most_spoken_languages(file_path, top_n):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             countries = json.load(file)

#         language_freq = {}

#         for country in countries:
#             for language in country.get('languages', []):
#                 if language in language_freq:
#                     language_freq[language] += 1
#                 else:
#                     language_freq[language] = 1

#         # Sort the dictionary by frequency in descending order
#         sorted_languages = sorted(language_freq.items(), key=lambda x: x[1], reverse=True)

#         return sorted_languages[:top_n]

#     except FileNotFoundError:
#         print("File not found.")
#         return []

# print(most_spoken_languages('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/countries_data.json',10))

#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json

# def most_populated_countries(file_path,top_n=10):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             countries = json.load(file)

#         country_population = [
#                     (country['name'], country.get('population', 0))
#                     for country in countries
#                 ]

#         # Sort the dictionary by frequency in descending order
#         sorted_by_pop = sorted(country_population, key=lambda x: x[1], reverse=True)

#         return sorted_by_pop[:top_n]

#     except FileNotFoundError:
#         print("File not found.")
#         return []
    
# print(most_populated_countries('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/countries_data.json'))

# #Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# import re

# def extract_emails(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()

#         email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

#         emails = re.findall(email_pattern, content)

#         return emails

#     except FileNotFoundError:
#         print("File not found.")
#         return []
    
# print(extract_emails('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/email_exchanges_big.txt'))

# #Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. 
# import re
# import os

# def find_most_common_words(data, num):
#     if isinstance(data, str) and os.path.isfile(data):
#         with open(data, 'r', encoding='utf-8') as f:
#             text = f.read()
#     elif isinstance(data, str):
#         text = data
#     else:
#         return []

#     # Clean the text: remove punctuation and lower the case
#     text = re.sub(r'[^\w\s]', '', text).lower()

#     words = text.split()
#     word_freq = {}

#     for word in words:
#         word_freq[word] = word_freq.get(word, 0) + 1

#     # Sort by frequency
#     sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

#     return sorted_words[:num]

# print("Most common words by Obama are: ",find_most_common_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/obama_speech.txt',10))
# print("Most common words by Michelle Obama are: ",find_most_common_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/michelle_obama_speech.txt',10))
# print("Most common words by Melina Trump are: ",find_most_common_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/melina_trump_speech.txt',10))
# print("Most common words by Donald Trump are: ",find_most_common_words('/Users/sameer/Aish_prac/Aish/30_Day_Python/data/donald_speech.txt',10))

