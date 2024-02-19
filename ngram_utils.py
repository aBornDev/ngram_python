import re
import time

# Function to sort ngrams
def sort_ngrams(ngrams):
    sorted_ngrams = [{'ngram': key, 'freq': ngrams[key]} for key in ngrams]
    sorted_ngrams.sort(key=lambda x: (-x['freq'], x['ngram']))
    for index, ngram in enumerate(sorted_ngrams):
        ngram['index'] = index
    return sorted_ngrams


# Function to merge two dictionaries
def merge_dicts(obj1, obj2, obj3):
    obj4 = obj1.copy()
    obj4.update(obj2)
    obj4.update(obj3)

    return obj4


# Function to get ngrams from text
def get_ngrams(text, n):
    ngrams = {}
    content = text.replace('. ', '_').lower()
    content = re.sub(r'[0-9]', '', content)
    content = re.sub(r'[&\/\\#,+()$~%.:"*?<>{}]', '', content)
    content = re.sub(r'\s+', ' ', content)

    for i in range(len(content) - n + 1):
        token = content[i:i + n]
        if token in ngrams:
            ngrams[token] += 1
        else:
            ngrams[token] = 1
    return ngrams


# Function to generate a profile
def generate_profile(text, top_n):
    bi_grams = get_ngrams(text, 2)
    tri_grams = get_ngrams(text, 3)
    quad_grams = get_ngrams(text, 4)
    ngrams = merge_dicts(bi_grams, tri_grams, quad_grams)
    sorted_ngrams = sort_ngrams(ngrams)
    return sorted_ngrams[:top_n]

def evaluate_ngram_performance(text, top_n):
    # Bi-grams evaluatie
    start_time = time.time()
    bi_gram_profile = generate_profile(text, top_n)
    bi_gram_time = time.time() - start_time

    # Tri-grams evaluatie
    start_time = time.time()
    tri_gram_profile = generate_profile(text, top_n)
    tri_gram_time = time.time() - start_time

    # Tri-grams evaluatie
    start_time = time.time()
    quad_gram_profile = generate_profile(text, top_n)
    quad_gram_time = time.time() - start_time


    return bi_gram_profile, tri_gram_profile, quad_gram_profile, bi_gram_time, tri_gram_time, quad_gram_time

# Voorbeeldtekst
sample_text = "Dit is een voorbeeldtekst voor evaluatie."

# Aantal top n-grams om te evalueren
top_n = 10

# Uitvoeren van de evaluatie
bi_gram_profile, tri_gram_profile, quad_gram_profile, bi_gram_time, tri_gram_time, quad_gram_time = evaluate_ngram_performance(sample_text, top_n)

# Resultaten voor bi-grams
print("Bi-grams profiel:")
for ngram in bi_gram_profile:
    print(ngram)

print("Tijd voor Bi-grams:", bi_gram_time, "seconden")

# Resultaten voor tri-grams
print("Tri-grams profiel:")
for ngram in tri_gram_profile:
    print(ngram)

print("Tijd voor Tri-grams:", tri_gram_time, "seconden")

# Resultaten voor quad-grams
print("quad-grams profiel:")
for ngram in quad_gram_profile:
    print(ngram)

print("Tijd voor quad-grams:", quad_gram_time, "seconden")