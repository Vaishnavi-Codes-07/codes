# Write a python function to remove a given word from a list ad strip it at the same time.

# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l
        
# l = ["Vaishnavi", "Omkar", "Ajay", "Rohan", "an"]

# print(rem(l, "an"))


def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
        
l = ["Vaishnavi", "Omkar", "Ajay", "Rohan", "an"]

print(rem(l, "an"))




