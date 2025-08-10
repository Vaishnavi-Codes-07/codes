# # Write a program to generate multiplication tables  from 2 to 20 and write it to the different files. Place these files in a folder for a 13 - year old. 

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n*i}\n"
    
#     with open(f"tables/table_{n}", "w") as f:
#         f.write(table)


# for i in range(2, 21):
#     generateTable(i)

import os

# Create the folder if it doesn't exist
os.makedirs("tables", exist_ok=True)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"
    
    # Save each table to a file named table_n.txt inside 'tables' folder
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 2 to 20
for i in range(2, 21):
    generateTable(i)
