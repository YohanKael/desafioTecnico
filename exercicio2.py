
string = input("Digite uma palavra: ")
palavraLower = string.lower()

def VerificaString(palavraLower):
    contador = 0    
    for caracter in palavraLower:
        if caracter == "a": 
            contador += 1
    print(contador)
    return contador
    
    
VerificaString(palavraLower)