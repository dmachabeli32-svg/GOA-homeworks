# 6) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 5-ზე მეტი სიგრძეში ან დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.

strings = ["male", "female", "femboy", "nika", "sarishvili"]
i = 0
while i < len(strings):
    if len(strings[i]) > 5 or i % 2 == 1:
        strings.remove(strings[i])
    else:
        i += 1
print(strings)
