people = [   
    {"name": "Alice", "age":30},
    {"name": "Bob", "age":25},
    {"name": "Charlie", "age":35},
    {"name": "David", "age":20}
]

# sorted_people = sorted(people, key= lambda person: person["age"])
sorted_people = sorted(people, key= lambda person: person["age"], reverse=True)
print(sorted_people)