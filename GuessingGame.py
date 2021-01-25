from random import randint
random_num = randint(1,10)
player=None
while True:
    player= input("guess kar number")
    player= int(player)
    if(player > random_num):
        print("chota daal be")
    elif(player < random_num):
        print("bohot kamm")
    else:
        print("sahi h barabar h")
        ask =input("firse khelega? ha ki ni?  ")
        if(ask=="ha"):
            random_num = randint(1,10)
            player=None
        else:
            print("fursat me nikal")
            break


    
