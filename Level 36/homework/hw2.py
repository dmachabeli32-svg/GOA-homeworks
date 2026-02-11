# 2) შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და დაითვლის ამ ტექსტში ხმოვნების რაოდენობას
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count

print(count_vowels("jizn varam"))
