# 9) შექმენი ფუქნცია რომელიც მიიღებს რიცხვების სიას და დააბრუნებს მხოლოდ ლუწ რიცხვებს
def even_number(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result

arafrismomcemi_ricxvebiscvladi = [1,2,2,34,34,344,53,456,546]
print(even_number(arafrismomcemi_ricxvebiscvladi))
