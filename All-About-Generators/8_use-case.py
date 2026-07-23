import os

file_name = "A:\CODING\ADVANCED PYTHON FOR MASTERY\Python Deep Drive\All-About-Generators\students.csv"


# Generator Function
def csv_reader(file_name):
    with open(file_name, "r") as file:      
        for row in file:
            yield row


# Create Generator
reader = csv_reader(file_name)

print("Type of reader:", type(reader))
print("-" * 40)


# Read using next()
print("Reading using next():\n")

print(next(reader).strip())
print(next(reader).strip())
print(next(reader).strip())

print("-" * 40)


# Continue reading using for loop
print("Remaining lines:\n")

for line in reader:
    print(line.strip())

print("-" * 40)


# Reading the whole file again
print("Reading entire file again:\n")

reader = csv_reader(file_name)

for line in reader:
    print(line.strip())