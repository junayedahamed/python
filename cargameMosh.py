
command=0
while(True):
    car=input(">")
    if(car.lower()=='help'):
        print("type (start) for start car")
        print("type (stop) for stop car")
        print("type (quit) for quit game")
    elif car.lower()=='start':
        if(command==0):
            print("Car started........")
            command+=1
        else:
            print("car already started....")
    elif car.lower()=='stop':
        if command>0:
            command=0
            print("Car stopped.")
        else:
            print("Car already stopped.")
    elif car.lower()=='quit':
        break
    else:
        print("I don't understand this command")
