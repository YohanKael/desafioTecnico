def fibonacci(n):
    sequencia = [0, 1]  
    
    while len(sequencia) < n:
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
    return sequencia
    
    
n = 20
resultado = fibonacci(n)
print(resultado)





