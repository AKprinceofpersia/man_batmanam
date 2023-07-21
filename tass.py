import random

print("be barnameye andakhtane tass khosh amadid")
while True :
    RandomNumber=random.randint(1 , 6)
    x=input("tass partab shavad(partab) ya mikhahid az barnam kharej shavid(exit)?")
    if x==("partab") :
        print(RandomNumber)
        if RandomNumber==6 :
            print("shoma barande shodid!jayze:")


    if x==("exit") :
        print("shoma az barname kharej shodid")
        break