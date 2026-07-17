names = ["Alice","Bob","Charlie","David"]
ages = [30,25,35,20]
gender = ["Female", "Male", "Male", "Male"]

for idx in range(min(len(names), len(ages))):
    name = names[idx]
    age = ages[idx]
    print(f"{name} is {age} years old")


combined = list(zip(names, ages, gender))
print(combined)
for name, age, gender in combined:
    print(f"{name} is {age} years old is {gender}")
    