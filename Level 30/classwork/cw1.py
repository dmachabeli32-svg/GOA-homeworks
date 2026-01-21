sia = ["Goga", "dachi", "gio", "Elene", "Gela"]

i = 0
sia1 = []
while i <len(sia):
    if i %2 !=0:
        sia.pop(i)
    else:
        sia1.append(sia[i].upper())
    i +=1
print(sia1)

