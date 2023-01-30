person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #list
person["pets"] = {"dog": "Fido", "cat": "Sox"} 

print(person)

print(person.get("children")[1])
# the name of the second child 

print(person["pets"])
# the name of the cat 

for i in person["children"]:
    print(i)

# use a loop to name each child 

for i,j in person["pets"].items():
    print(f"type of pets:(i) name of pets (j)")

# print out the pets in the format 
# "type of pet; dog name of pet fido"


