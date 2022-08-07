# favirite_languages_0
favirite_languages ={
    'alen': ['python', 'ruby'],
    'jack': ['java', 'c'],
    'ensa': ['c'],
    'phil': ['python', 'haskell'],
}
for name, languages in favirite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")