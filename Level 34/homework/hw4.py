# 4) შექმენით ფუნქცია. მომხმარებელს შემოატანინეთ წინადადების სტრინგი. დათვალე, რამდენი სიტყვის სიგრძე არის 4-ზე მეტი. დაპრინტე ასეთი სიტყვების რაოდენობა. დაწერეთ ეს დავალება ორნაირად - split() ფუნქციით და split() ფუნქციის გარეშე.

def count_letters():
    count = 0 
    count1 = 0
    sen = input("shemoiyvane raime winadadeba:")
    for i in sen:
        if i != " ":
            count +=1
        else:
            if count > 4:
                count1 +=1
            count = 0
    if count > 4:
        count1 += 1
    print(count1)
count_letters()


def count_long_words_split():
    sentence = input("shemoiyvane raime winadadeba:")
    words = sentence.split()
    count = 0
    for word in words:
        if len(word) > 4:
            count += 1
    print(count)
count_long_words_split()
