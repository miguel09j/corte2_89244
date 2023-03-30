def k(n, p):
   
    if n == 1:
        return p

    else:
        return n*p + k(n-1, p)

resultado = k(5, 3)


print(resultado) 