# 4) შექმენი ფუნქცია რომელიც მიიღებს სიტყვების სიას და დააბრუნებს მხოლოდ
# იმ სიტყვებს რომლებიც იწყება დიდი ასოთი
def capital_letter(words):
    saxeli = []
    for i in words:
        if i[0].isupper():
            saxeli.append(i)
    return saxeli

sia = ["Gela","mela", "nela", "Yvela", ]
print(capital_letter(sia))