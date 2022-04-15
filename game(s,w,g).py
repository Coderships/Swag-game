import random
def gamewin(cp,you):
    if cp=='s':
        if you=='g':
            return True
        elif you=="w":
            return False
    elif cp=='g':
        if you=='w':
            return True
        elif you=="s":
            return False
    elif cp=='w':
        if you=='g':
            return False
        elif you=="s":
            return True
    elif cp==you:
        return None
you=input("You choose: Snake(s) or Water(w) or Gun(g):-")
print("cp(computer) choice:Snake(s) or Water(w) or Gun(g)")
p=random.randint(1,3)
if p==1:
    cp='s'
elif p==2:
    cp='w'
elif p==3:
    cp='g'
a=gamewin(cp,you)
print(f"Computer Choose:- {cp}")
print(f"You Choose:-{you}")

if a==None:
    print("Game is tie!")
elif a==True:
    print("You win")
elif a==False:
    print("So,You lose")
