import os
import glob
import json
import ngram_utils

ngrams = {}

print("Started Application")

file_paths = glob.glob("subset/*.txt")
language_profile = {}

for file_path in file_paths:
    lang = os.path.splitext(os.path.basename(file_path))[0]
    print(f"Training [Language: {lang}] [File: {file_path}]")

    with open(file_path, 'r', encoding='utf8') as file:
        text = file.read()
        language_profile[lang] = ngram_utils.generate_profile(text, 300)

with open('language-profile.json', 'w', encoding='utf8') as output_file:
    json.dump(language_profile, output_file, ensure_ascii=False, indent=4)

print("Written Language Profile to File [language-profile.json]")