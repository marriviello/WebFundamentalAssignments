x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #Change value 10 in x to 15
x = [[5,2,3], [15,8,9]]
print(x)

# #Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(students[0]['last_name'])

# #Change Messi to Andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

# #Change value 20 in z to 30
z[0]['y'] = 30
print(z)

# #Iterate Through a List of Dictionaries 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary():
    for person in students:
        print(f"first_name - {person['first_name']}, last_name - {person['last_name']}")

print(iterateDictionary())

#Get Values From a List of Dictionaries

def iterate_dict2(key_name,list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)

iterate_dict2('first_name',students)
iterate_dict2('last_name',students)


# def iterateDictionary2(some_key, some_list):
#     for person in students:
#         for key,val in list[students].items():
#             if key == some_key:
#                 print(val)

# print(iterateDictionary2('first_name', students))


dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key,val in dict.items():
        print ("---------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print(printInfo(dojo))

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

