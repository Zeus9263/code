# open
text_path = 'chapter_10/pi_digits.txt'
with open(text_path) as file_object:
    for line in file_object:
        print(line.strip())
