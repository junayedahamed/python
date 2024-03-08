
locations = {
    "DU": "Dhaka", "JU": "Savar",
    "IU": "Kushtia",
    "DIU": "Khagan"
}


print(locations.keys)

name = locations.copy()
print(name)

locations.popitem()  # this will pop an item from last of dictionary

locations.update({"Plsck": "Kushtia"})  # update dictionary

print(locations.get("Plsck"))
locations.update({"junayed": "Kushtia"})
print(locations.keys())

print(locations)


d = {
    1: "one",  # list dict set map
    2: "two",
    3: "three"
}
# print(d.get(1))
# num = input("number:")
# output = ""

# for e in num:
#     output += d.get(int(e), "NAN")+" "

# print(output, end=" ")


print(d.items())
print(d.keys())
d.update({4: "Four"})
val = d.pop(3)
print(val)

print(d.fromkeys(d, val))  # new dict created with poped item and values
