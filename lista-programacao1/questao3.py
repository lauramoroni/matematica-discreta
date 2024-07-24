import time


x = int(input())

    # Cálculo utilizando recursividade

def exponencial_recursiva(x, max = 998): # Testes com o valor max acima de 998 dão erro

    soma = 0

    for k in range(0, max):
        soma += pow(x, k) / fatorial_recursiva(k)

    return soma

def fatorial_recursiva(k):
    if k == 0:
        return 1
    else:
        return k * fatorial_recursiva(k-1)
    

    # Cálculo utilizando programação dinâmica

def exponencial_dinamica(x, max = 10000): # 10,000 demora 133.05 seg

    soma = 0

    for k in range(0, max):
        soma += pow(x, k) / fatorial_programacao_dinamica(k)

    return soma

def fatorial_programacao_dinamica(k):

    if k < 1:
        return 1
    
    f = [1] * (k + 1) # Criação do array

    for i in range(2, k + 1):
        f[i] = f[i - 1] * i # Cada elemento de f guarda o fatorial de k, evitando recalcular os valores
    return f[k]

    # Resultado e tempo de execução utilizando função recursiva
inicio_recursiva = time.time()
res_recursiva = exponencial_recursiva(x)
fim_recursiva = time.time()

print(f'Resultado usando função recursiva: {res_recursiva:.5f}')
print(f'Tempo de execução {fim_recursiva-inicio_recursiva:.5f} segundos')

    # Resultado e tempo de execução utilizando programação dinâmica
inicio_dinamica = time.time()
res_dinamica = exponencial_dinamica(x)
fim_dinamica = time.time()

print(f'Resultado usando programação dinâmica: {res_dinamica:.5f}')
print(f'Tempo de execução {fim_dinamica-inicio_dinamica:.5f} segundos')