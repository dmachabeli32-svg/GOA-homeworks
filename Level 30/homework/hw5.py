
# 5) შექმენით სტრინგის ცვლადი და ცარიელი სია, თუ სტრინგის ასო არის პატარა, მაშინ ცარიელ სიაში ჩაამატეთ "%" ნიშანი, ხოლო თუ სტრინგის
# ასო არის დიდი, მაშინ ცარიელ სიაში ჩაამატეთ "@" ნიშანი.
# თუ მინუსების რაოდენობა სიაში არის ლუწი, მაშინ წაშალე ყველა "%" ნიშანი, ხოლო თუ მინუსების რაოდენობა სიაში არის კენტი
# წაშალე ყველა "@" ნიშანი. "%" და "@" -ების თავიდან
# სიაში ჩასაგდებად გამოიყენეთ for ციკლი, ხოლო "%" ან "@" -ების
#  წასაშლელად გამოიყენეთ while ციკლი.

text = "HeLloWoRLd"
symbols = []

for char in text:
    if char.islower():
        symbols.append("%")
    elif char.isupper():
        symbols.append("@")

percent_count = symbols.count("%")

if percent_count % 2 == 0:
    i = 0
    while i < len(symbols):
        if symbols[i] == "%":
            symbols.pop(i)
        else:
            i += 1
else:
    i = 0
    while i < len(symbols):
        if symbols[i] == "@":
            symbols.pop(i)
        else:
            i += 1

print("Final list:", symbols)
