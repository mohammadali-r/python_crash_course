# dictionary
ages = {"dave": 25, "brad": 34, "helen": 18, "mary": 23}

ids = {1: "brad", 2: "shawn", 3: "thomas", 4: "sara"}

sample_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "skills": ["Python", "JavaScript", "Golang"],
    "address": {"city": "New York", "zipcode": "10001"},
}

print(ages["brad"], ages["dave"])

# get
print(ages.get("dave", "not found"))
print(ages.get("bill", "not found"))

# len
print(len(ages))
print(len(sample_dict))
