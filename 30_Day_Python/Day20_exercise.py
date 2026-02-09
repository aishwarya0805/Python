#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import urllib.request
import re
import ssl
import sys
#import certifi


# def get_text_from_url(url):
#     response = urllib.request.urlopen(url)
#     raw = response.read().decode('utf-8')
#     return raw

# def clean_and_tokenize(text):
#     text = text.lower()
#     text = re.sub(r'[^a-z\s]', '', text)  # Remove punctuation and non-alpha characters
#     words = text.split()
#     return words

# def find_most_frequent_words(text, top_n=10):
#     words = clean_and_tokenize(text)
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
#     return sorted_freq[:top_n]

# # URL of Romeo and Juliet
# #romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# romeo_and_juliet='https://en.wikipedia.org/wiki/Manchurian_hare'
# # Run
# text = get_text_from_url(romeo_and_juliet)
# top_words = find_most_frequent_words(text)

# # Output
# for word, count in top_words:
#     print(f'{word}: {count}')

# #Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find 
# import requests
# import statistics

# cats_api = 'https://api.thecatapi.com/v1/breeds'
# response = requests.get(cats_api)
# cats_data = response.json()

# #the min, max, mean, median, standard deviation of cats' weight in metric units.
# def parse_range(value):
#     try:
#         parts = value.split(' - ')
#         numbers = list(map(float, parts))
#         avg = sum(numbers) / len(numbers)
#         return numbers[0], numbers[1], avg
#     except:
#         return None, None, None

# weights = []
# lifespans = []

# for cat in cats_data:
#     min_w, max_w, avg_w = parse_range(cat['weight']['metric'])
#     if avg_w is not None:
#         weights.append(avg_w)
# #the min, max, mean, median, standard deviation of cats' lifespan in years.
#     if 'life_span' in cat:
#         min_ls, max_ls, avg_ls = parse_range(cat['life_span'])
#         if avg_ls is not None:
#             lifespans.append(avg_ls)

# def summarize(data, label):
#     print(f"\n{label}:")
#     print("Min:", min(data))
#     print("Max:", max(data))
#     print("Mean:", round(statistics.mean(data), 2))
#     print("Median:", statistics.median(data))
#     print("Standard Deviation:", round(statistics.stdev(data), 2))

# summarize(weights, "Cats' Weight (kg)")
# summarize(lifespans, "Cats' Lifespan (years)")

# #Create a frequency table of country and breed of cats
# from collections import defaultdict

# country_breed_map = defaultdict(list)

# for cat in cats_data:
#     country = cat.get('origin', 'Unknown')
#     breed = cat.get('name', 'Unknown')
#     country_breed_map[country].append(breed)

# print("\nFrequency Table (Country: Number of Breeds):")
# for country, breeds in country_breed_map.items():
#     print(f"{country}: {len(breeds)} breeds")

import requests
from collections import defaultdict, Counter

# Step 1: Get all country data
url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)
countries = response.json()

# Step 2: 10 largest countries by area
countries_area = [(country['name']['common'], country.get('area', 0)) for country in countries]
largest_countries = sorted(countries_area, key=lambda x: x[1], reverse=True)[:10]

print("10 Largest Countries by Area:")
for name, area in largest_countries:
    print(f"{name}: {area} km²")

# Step 3: Count all spoken languages
language_counter = Counter()
all_languages = set()

for country in countries:
    langs = country.get('languages', {})
    for lang_code, lang_name in langs.items():
        language_counter[lang_name] += 1
        all_languages.add(lang_name)

# Step 4: 10 most spoken languages
most_spoken = language_counter.most_common(10)

print("\n 10 Most Spoken Languages:")
for lang, count in most_spoken:
    print(f"{lang}: spoken in {count} countries")

# Step 5: Total number of unique languages
print(f"\n Total Unique Languages: {len(all_languages)}")


