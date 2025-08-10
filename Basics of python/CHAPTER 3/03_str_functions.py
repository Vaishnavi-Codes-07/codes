# name = "welcome harry"
# print(len(name))
# print(name.endswith("rry"))
# print(name.startswith("Ha"))
# print(name.capitalize())    #capitalize only first char

# # Searching & Checking
# print(name.lower())          #Converts all characters to lowercase.
# print(name.upper())          #Converts all characters to uppercase.
# print(name.capitalize())     #Capitalizes the first character.
# print(name.title())          #Capitalizes the first letter of each word.
# print(name.swapcase())       #Swaps uppercase to lowercase and vice versa.

# # String Trimming & Stripping
# str = "Welcome Harry "
# print(str.strip())          #Removes whitespace (or specified characters) from both ends.
# print(str.lstrip())         #Removes leading whitespace.
# print(str.rstrip())         #Removes trailing whitespace.

# Searching & Checking
str = "subject"
print(str.find("je"))          #Returns the first index of sub, or -1 if not found.
print(str.rfind("sub"))         #Finds the last occurrence of sub.
print(str.index("sub"))         #Like find() but raises an error if not found.
print(str.startswith("sub")) #Returns True if string starts with prefix.
print(str.endswith("ct"))   #Returns True if string ends with suffix.
print(str.count("b"))         #Counts how many times sub appears.
print('sub' in str)             #'sub' in string returns True if found.

#Replacing & Splitting
str1 = "old"
print(str1.replace("old", "new"))      #Replaces all occurrences of old with new.
print(str1.split(delim))               #Splits the string into a list by delimiter.
print(str1.rsplit(delim))              #Same as split() but starts from the right.
print(str1.join(iterable))             #Joins an iterable of strings into one string.

#Length and Alignment







