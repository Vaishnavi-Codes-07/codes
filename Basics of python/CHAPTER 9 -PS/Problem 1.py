f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word Twinkle is present in content")

else:
    print("The word Twinkle is not present in content")
f.close()