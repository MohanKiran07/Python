import random 
def   g(pc,cc):
    if     pc==cc:
        return "tie"
    elif (pc=='r' and cc=='s') or \
         (pc=='p' and cc=='r') or \
          (pc=='s' and cc=='p'):
            return "you win"
    else:
        return "you lose"

print("welcome to my rock, paper,siccors game")
while True:
    c=['r','p','s']
    pc=input("choose from (rock,paper, siccors):")
    cc=random.choice(c)
    print("computer choice:",cc)
    print("your choice:",pc)
    result=g(pc,cc)
    print(result)


