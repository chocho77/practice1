# declaring a dictionary variable
empty = {} # empty dictionary

# dictionary with one key/value pair
person = {"name" : "John Smith"}

print(person['name']) # print John Smith

customer = {
    "name" : "Morty",
    "age": 26
}

print(customer) # {'name': 'Morty', 'age': 26}

d = dict() # empty dictionary , create with function dict()

print(d)

# accessing dictionary information through keys

person ={"name": "John"}

#access information through the key

print(person["name"]) # John

print(d.get('name')) # None

d['name'] = "John"
d['age'] = 21

print(d.get("name")) # John

print(d.get('age')) # 21


d = {
    '1' :'one',
    '2': 'two'
}
letter = d.get('3')

if not letter:  # if letter == None
    print("Invalid Key")
else:
    print(letter)

data = {"sports": ['baseball', 'footbal', 'hockey', 'soccer']}

print(data["sports"][0]) # baseball

sports = ["baseball", "football", "hockey", "handball"]

# sports_dic = dict(sports) # will produce error no key

sport_dict = dict({"sports": sports})

print(sport_dict)









