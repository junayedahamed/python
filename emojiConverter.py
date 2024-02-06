import emoji

message= input(">")
words= message.split(" ") # here space (" ") determine it as a boundary

imoje={
     ":)":"😃"
    ,":(":"🙁"
    ,"(|":"😐"
}
output=""
for each in words:
   output += imoje.get(each,each)+" "

print(output)
