import random
lista = []
for i in range(10):
    lista.append(random.randint(1, 50))
print(lista)
######################################################################################
def mayor():
    num = lista[0]
    for x in lista:
        if x > num:
            num = x
            print("el numero mayor es igual a: ", num)
######################################################################################
def primo(lista):
    primos = []
    for num in lista:
        if num > 1:
            es_primo = True
            for i in range(2, num):
                if (num % i) == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)
    return primos, print("los numeros primos son: ", primos)
############################################################################################
if __name__ == "__main__":
    mayor() 
    primo(lista)     
############################################################################################