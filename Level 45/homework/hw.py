# codewars1
# def accum(st):
#     result = ""
    
#     for i in range(len(st)):
#         result += st[i].upper()
        
#         for j in range(i):
#             result += st[i].lower()

#         if i != len(st) - 1:
#             result += "-"
#     return result

# codewars2
# def litres(time):
#     return time //2
# codewars3

# def to_jaden_case(string):
#     words = string.split()
#     result = []
#     for word in words:
#         if word:
#             first = word[0].upper()
#             rest = word[1:].lower() if len(word) > 1 else ''
#             result.append(first + rest)
#     return ' '.join(result)
# codewars4
# def lovefunc( flower1, flower2 ):
#     return (flower1 % 2) != (flower2 % 2)
# codewars5
# def maps(a):
#     result = []
#     for i in a:
#         result.append(i * 2)
#     return result
# codewars6
# def solution(text, ending):
#     return text.endswith(ending)