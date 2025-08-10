# list1 = [2,3,4,4,4,2,2,3,2,3]
# list2 = [3,4,3,4,2,4,34,2,2]

# def addition(a , b):
#     return a+b

# list3 = []
# size = len(list1)
# for i in range(0, size-1):
#     list3.append(list1[i] + list2[i])

# print(list3)

class human:
    mouth = 1
    nose = 1
    def __init__(self, name , hands = 2):
        self.hands = hands
        self.name = name
        print("Human created")

    def walk(self):
        print(f"{self.name} is walking...")


omkar = human("Omkar")
print(omkar.name)
print(f"Omkar has {omkar.hands} hands")
print(f"omkar has {omkar.mouth} mouth")
omkar.walk()

vaishnavi = human("vaishnavi")
ramesh = human('ramesh')
shanti = human('shanti', 1)
vaishnavi.walk()
ramesh.walk()
shanti.walk()
print(shanti.hands)

