import random


def get_level(score):
    if 90 < score <= 100:
        return '非常优秀'

    elif 80 < score <= 90:
        return '优秀'

    elif 60 < score <= 80:
        return '及格'

    else:
        return '不及格'


def main():
    for i in range(10):
        score = random.randint(1, 100)
        level = get_level(score)
        print("成绩: %s, 等级: %s" % (score, level))



main()