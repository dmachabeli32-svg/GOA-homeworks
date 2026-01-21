# 3) შექმენით ქვეყნების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა სიტყვას ყველა ასო გაუხადეთ დიდი. დაპრინტეთ
# საბოლოო შედეგი. გამოიყენეთ while ციკლი.

countires = ["GEO", "pakistan", "INDIA", "germnay", "sweden"]

i = 0
while i < len(countires):
    if countires[i].isupper():
        countires.pop(i)
    else:
        countires[i] = countires[i].upper()
        i += 1   

print(countires)
