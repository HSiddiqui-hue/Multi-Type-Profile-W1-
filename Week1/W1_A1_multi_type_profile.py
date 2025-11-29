# Week 1 - Activity 1: Build a Multi-Type Profile

#This program demonstrates different basic Python data types:
# String - Integer - List - Tuple - Dictionary - Set

# Output: It then prints them in a simple table format.

#STRING
# A string stores text inside quotes and is used for textual data.
name = "Hassan Siddiqui"

#INTEGER
age = 28

#LIST
# A list stores an ordered collection of items and can be changed (mutable).
skills = ["Python", "SQL", "Power BI"]

#TUPLE
# A tuple is like a list but cannot be changed after creation (immutable).
education = ("BSc Computer Science", 2020)

#DICTIONARY
# A dictionary stores key-value pairs, allowing us to label each piece of data.
contact_details = {
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
}

#SET
# A set stores unique values only and automatically removes duplicates.
certifications = {"Azure", "AWS", "Azure"}  # "Azure" appears twice here on purpose

#PRINTING THE TABLE
# We use ljust() to align the text into neat columns.

print("Component".ljust(20), "Data Type".ljust(15), "Example")
print("-" * 60)

print("Name".ljust(20), "String".ljust(15), name)
print("Age".ljust(20), "Integer".ljust(15), age)
print("Skills".ljust(20), "List".ljust(15), skills)
print("Education".ljust(20), "Tuple".ljust(15), education)
print("Contact Details".ljust(20), "Dictionary".ljust(15), contact_details)
print("Certifications".ljust(20), "Set".ljust(15), certifications)


