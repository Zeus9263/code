# 调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'daming': 'java',
    'sam': 'c++',
}

people = {'tom', 'sam', 'daming', 'lingling'}

for man in people:

    if man in favorite_languages.keys():

        print("thanks " + man)

    else:

        print("would you like to join us? " + man)
