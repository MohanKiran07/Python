import random 
def g(p,c):
    if p==c:
        return "u guess the number correct"
    else :
        return "u guess the number was worng"

while True:
    p=input("guess a number between 1 to 5:")
    c=['1','2','3','4','5']
    c=random.choice(c)
    result=g(p,c)
    print(result)








