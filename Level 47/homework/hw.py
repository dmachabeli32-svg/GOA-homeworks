# codewars1
# def get_middle(s):
#     if len(s) %2 ==0:
#         return(s[(len(s)//2)-1])+(s[len(s)//2])
#     else:
#         return (s[len(s)//2])



# codewars2
# def is_anagram(test, original):
#     return sorted(test.lower()) == sorted(original.lower())

# codewars3
# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     return '#' * (len(cc) - 4) + cc[-4:]

# codewars4
# def check_exam(arr1,arr2):
#     score = 0
    
#     for correct, answer in zip(arr1, arr2):
#         if answer == "":
#             score += 0
#         elif answer == correct:
#             score += 4
#         else:
#             score -= 1
    
#     return max(score, 0)
# codewars5
# ???

# codewars6
# def get_count(sentence):
#     vowels = "aeiou"
#     count = 0
#     for i in sentence:
#         if i in vowels:
#             count += 1
    # return count
