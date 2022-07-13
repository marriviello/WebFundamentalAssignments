person = {
    "first": "Ada", 
    "last": "Lovelace", 
    "age": 42, 
    "is_organ_donor": True
}

# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)

person["age"] = 103
person["hair"] = "brown"
print(person)

if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")




