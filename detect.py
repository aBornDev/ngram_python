import sys
import json
import ngram_utils

max_score = 100000

# Generic Function to sort the scores.
def sort_scores(scores):
    return sorted(scores.items(), key=lambda item: item[1])

if len(sys.argv) != 2:
    print("Usage: python detect.py <phrase>")
    sys.exit(1)

NOT_FOUND = 1000

# Loading our language profiles
print("Reading Language Profiles from [language-profile.json]")
with open('language-profile.json', 'r', encoding='utf-8') as file:
    language_profiles = json.load(file)

# Reading the text the user wants to detect from the input.
text = sys.argv[1]
print("Determining Language for [text: {}]".format(text))

# Generate the ngrams from the document.
document_profile = ngram_utils.generate_profile(text, 300)

# Create an empty scores dictionary
scores = {}

# Initialize this with 0 for each language
for language in language_profiles:
    scores[language] = 0

# Compute the out of index for each language.
for document_ngram in document_profile:
    document_index = document_ngram['index']
    languages = language_profiles.keys()

    for language in languages:
        language_profile = language_profiles[language]
        language_ngram = [ln for ln in language_profile if ln['ngram'] == document_ngram['ngram']]

        if len(language_ngram) == 1:
            scores[language] += abs(language_ngram[0]['index'] - document_index)
        else:
            scores[language] += NOT_FOUND

sorted_scores = sort_scores(scores)
print("Results ===============")
for language, score in sorted_scores:
    percentage = (max_score - score) / 1000
    print(language + " kans: " + str(percentage))

ngram_utils.evaluate_ngram_performance(text, 300)