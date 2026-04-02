#codewars1: Exes and Ohs
# def xo(s):
#     s = s.lower()
#     count = 0
#     count1 = 0
#     for i in s:
#         if i == "o":
#             count += 1
#         elif i == "x":
#             count1 += 1
#         else:
#             pass
#     if count == count1:
#         return True
#     else:
#         return False 
# codewars2: Summing a number's digits
# def sum_digits(number):
#     count = 0
#     number = abs(number)
#     number  = str(number)
#     for i in number:
#         count += int(i)
#     return count
# codewars3: Disemvowel Trolls
# def disemvowel(s):
#     vowels = "aeiouAEIOU"
#     result = ""
#     count = 0
#     for i in s:
#         if i not in vowels:
#             result += i
#     return result
# codewars4: List Filtering
# def filter_list(l):
#     result = []
#     for i in l:
#         if isinstance(i, int): 
#             result.append(i)
#     return result
# codewars5: Two Oldest Ages
# def two_oldest_ages(ages):
#     ages.sort()
#     return ages[-2:]
# codewars6: Greet Me
# def greet(name): 
#     return "Hello " + name.capitalize() + "!"
# codewars7: Shortest Word
# def find_short(s):
#     name = s.split()
#     name1=[]
#     for i in range[len(name)]:
#         if i[0]< i[0]+1:
#         name1.append(i+1)
        