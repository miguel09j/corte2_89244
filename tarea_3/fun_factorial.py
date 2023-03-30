n = int(input("ingrese el numero factorial: "))

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n-1)

resultado = factorial(n)


print(resultado) 