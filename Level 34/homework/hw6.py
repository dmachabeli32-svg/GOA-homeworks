# 6) შექმენით ფუნქცია. მომხმარებელს შემოატანინე წინადადება. იპოვე და დაბეჭდე ყველაზე გრძელი სიტყვა ამ წინადადებაში. გამოიყენეთ while ციკლი. გამოიძახეთ ფუნქცია.

# def sentence():
#     name = input("sheiyvanet raime winadadeba:")
#     i=0
#     count = 0
#     total = 0
#     while i< len(name):
#         if i != " ":
#             count +=1
#         else:
#             total = count
#             count = 0
#             if total > 0 and count > total:
#                 total = count
#     if count > total:
#         total = count
#     print(total)
# sentence()
def longest_word():
    sentence = input("sheiyvanet winadadeba:")
    words = sentence.split()
    i = 0
    longest = "" 

    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1
    print(longest)
longest_word()
