x = int(input())

def exponencial_recursiva(x, max = 995):

    soma = 0

    for k in range(0, max):
        soma += pow(x, k) / fatorial(k)

    return soma

def fatorial(k):
    if k == 0:
        return 1
    else:
        return k * fatorial(k-1)
    
    
print(f'Resultado usando função recursiva: {exponencial_recursiva(x)}')