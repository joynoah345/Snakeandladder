from random import randint

def dice():
    return (randint(1,6))

def lad(pos):
    if(pos==1):
        playerpos[i] = 38
    elif(pos==4):
        playerpos[i] = 14
    elif(pos==8):
        playerpos[i] = 30
    elif(pos==21):
        playerpos[i] = 42
    elif(pos==28):
        playerpos[i] = 76
    elif(pos==50):
        playerpos[i] = 67
    elif(pos==71): 
        playerpos[i] = 92
    else:
        playerpos[i] = 99



def snake(pos):
    if(pos==32):
        playerpos[i] = 10
    elif(pos==36):
        playerpos[i] = 6
    elif(pos == 86):
        playerpos[i] = 24
    elif(pos==48):
        playerpos[i] = 26
    elif(pos==62):
        playerpos[i] = 18
    elif(pos==95):
        playerpos[i] = 56
    else:
        playerpos[i] = 78


noofplayers = int(input("Enter number of players"))
if(noofplayers>4):
    print("Max players = 4,But Alright!!!")
print("----------------------------START------------------------------")
playerpos = [0 for _ in range(noofplayers)]
names = []
for i in range(noofplayers):
    print("Player {} Enter your name:".format(i+1))
    names.append(input())
i = 0
box = [ 0 for i in range(101)] 
ladder = [1,4,8,21,28,50,71,80]
snakes = [32,36,86,48,62,95,97]
while(max(playerpos)!=100):
    # print("Player",i+1)
    x = playerpos[i]
    if(input("{} press when ready".format(names[i]))):
        val = dice()
    else :
        continue
    print("Dice =",val)
    if(playerpos[i]+val<=100):
        playerpos[i]+=val
    else :
        print("{} you missed the chance... Better luck Next time ....".format(names[i]))
    if(playerpos[i] in ladder):
        print("Yayy!! Ladder.......... at {} ".format(playerpos[i]))
        lad(playerpos[i])
        print("You Reached {}".format(playerpos[i]))
    elif(playerpos[i] in snakes):
        print("------>>>>>   Snake   .........")
        snake(playerpos[i])
        print("You Reached {}".format(playerpos[i]))
    print(playerpos)
    if(x+val<=100):
        if(box[playerpos[i]] == 0 ):
                box[playerpos[i]] = i+1
                box[x] = 0
        else :
            box[playerpos[i]] = str(box[playerpos[i]])+","+str(i+1)
            box[x] = 0 

    for j in range(noofplayers):
        print("{}---{}".format(j+1,names[j]))
    for j in range(101):
        print(box[j],end = " ")
        if(j%10==0):
            print()
    print()
    i = (i+1)%noofplayers 

print()
print()
print("--------------------------WIN!!!!!!------------------------")
print()
print()
print("***********--------",names[playerpos.index(max(playerpos))],"Wins----------************")
print()
print()
print()