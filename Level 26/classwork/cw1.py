# შექმენით სია ["cat", "elephant", "dog", "tiger", "ox"], წაშალეთ ყველა სიტყვა რომლის სიგრძეც ნაკლებია 4-ზე

sia = ["cat", "elephant", "dog", "tiger", "ox"]
i = 0
while i < len(sia):
    if len(sia[i])< 4:
        sia.pop(i)
    else:
        i = i+1
print(sia)