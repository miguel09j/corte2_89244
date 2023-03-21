import random

def aleatorio():
    n=random.randint(100,120)
    return n
def proceso():
    for i in range(10):
     n = aleatorio()
     if n != 115 and n != 110 and n != 119:
        print(n)
    else:
        i-=1
proceso()