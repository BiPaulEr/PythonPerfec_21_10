liste = ["A", "B", "C", "D"]
def minuscule(string):
    return string.lower()

test = list(map(minuscule, liste))

for index, letter in enumerate(liste):
    liste[index] = minuscule(letter)

print(test)
liste.append("Z")
print(list(test))