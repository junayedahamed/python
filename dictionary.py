
customar={
    "name":"Junayed",
    "email":"junayedahamed.dev@gmail.com",
    "phone":"01721143298"

}

customar["name"]="Nahidul" #we can update value like that
customar["birthdate"]="feb 4 2003"

print(customar)
print(customar["name"])
print(customar["email"])

# print(customar["birthdate"]) #this unknown key returns key error
print(customar.get("birthdate"))   # this will simply return  none or (absance of birthdate) and also we can add new key and value


#practice

num=input("enter number:")
digit_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
}

output=" "

for e in num:
    output+=digit_mapping.get(e,"!")+" "

print(output,end=" ")