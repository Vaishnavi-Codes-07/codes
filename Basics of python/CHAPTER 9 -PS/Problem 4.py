# A file contains a word "Donkey" multiple times. you need to WAP which replace this word with ##### by updating the same file 

word = "Donkey" 

with open("files.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("files.txt", "w") as f:
    f.write(contentNew)




