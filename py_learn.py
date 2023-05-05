import pandas as pd
import json

a = 6
print (a)
print(type(a))
a = "string"
print (a)
print(type(a))


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

number_collection = {"a":6,"b":7}
print(number_collection.items())