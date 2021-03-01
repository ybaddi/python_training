import json
person = '{"name":"baddi",\
"email":"baddiyoussef@gmail.com",\
"loisirs": ["sport", "dev", "cinema", "voyage"]\
}'

person_to_dict = json.loads(person)
print(person_to_dict)
print(type(person_to_dict))

print(person_to_dict['loisirs'])

with open('./file.json') as file:
    jsonData = json.load(file)

print(jsonData)

personObj = {"name":"baddi",
"email":"baddiyoussef@gmail.com",
"loisirs": ["sport", "dev", "cinema", "voyage"]
}
jsonData_3 = json.dumps(personObj)

print(jsonData_3)

# Python            | json
# dict              | object
# list,tuple         | array

# sql => simple query language 
# SGBD => systeme de gestion de base de donne
# SQL based => sqlite3 mysql postgresql, sql server, oracle database

import sqlite3

conn = sqlite3.connect("ex1")
cur = conn.cursor()
req="SELECT * FROM users"
res = cur.execute(req)
for row in res:
    print("ID", row[0])
    print("nom", row[1])
    print("email", row[2])
