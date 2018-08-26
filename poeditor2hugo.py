#!/usr/bin/env python3
import sys, os, os.path, errno
import requests
from tqdm import tqdm



# Greeting
os.system('cls' if os.name == 'nt' else 'clear')
print()
print("                                                     (c) by @Lednerb ")
print("                      _ _ _            ____  _                       ")
print(" _ __   ___   ___  __| (_) |_ ___  _ _|___ \| |__  _   _  __ _  ___  ")
print("| '_ \ / _ \ / _ \/ _` | | __/ _ \| '__|__) | '_ \| | | |/ _` |/ _ \ ")
print("| |_) | (_) |  __/ (_| | | || (_) | |  / __/| | | | |_| | (_| | (_) |")
print("| .__/ \___/ \___|\__,_|_|\__\___/|_| |_____|_| |_|\__,_|\__, |\___/ ")
print("|_|                                                      |___/       ")
print()


# Settings
POEDITOR_API_KEY = input("Enter your API KEY: ")
POEDITOR_ID = input("Enter the project ID: ")
LANGUAGE_FILE_PATH = 'i18n/'

# Margin after input
print()
print()


# Get languages
r = requests.post('https://api.poeditor.com/v2/languages/list', {
    'api_token': POEDITOR_API_KEY,
    'id': POEDITOR_ID
}).json()

if r.get('response').get('code') != '200':
    sys.exit("ERROR: Can't get list of languages")

# Create i18n directory if it does not exist
if not os.path.exists(LANGUAGE_FILE_PATH):
    os.makedirs(LANGUAGE_FILE_PATH, 0o755, True)

# Export languages
for language in tqdm(r.get('result').get('languages'), "Processing languages from poeditor"):
    if language.get('translations') > 0:

        e = requests.post('https://api.poeditor.com/v2/projects/export', {
            'api_token': POEDITOR_API_KEY,
            'id': POEDITOR_ID,
            'language': language.get('code'),
            'type': 'json'
        }).json()

        if e.get('response').get('code') != '200':
            sys.exit("ERROR: Can't export language:" + language.get('name'))

        # Download the language file
        f = requests.get(e.get('result').get('url'))

        if f.status_code != 200:
            sys.exit("ERROR: Can't download language file:" + language.get('name'))

        # Convert and write file
        with open(LANGUAGE_FILE_PATH + language.get('code') + '.toml', 'w', 1, 'utf-8') as file:
            for string in f.json():
                if string.get('definition') is not None:
                    file.write("[" + string.get('term') + "]\n")
                    if string.get('term_plural') is not '':
                        file.write('one = "' + string.get('definition') + '"\n')
                        file.write('other = "' + string.get('term_plural') + '"\n')
                    else:
                        file.write('other = "' + string.get('definition') + '"\n')

                    file.write("\n")

print()
print("All available translations downloaded successfully!")
print("Don't forget to adjust the file permissions.")
print()
