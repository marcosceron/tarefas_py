import random
def merge_sort(vetor, pi, pf):
    # condicao de parada
    if pi < pf:
        meio = (pi + pf) // 2 # // -> divisao inteira
        # quebra do vetor
        merge_sort(vetor, pi, meio)
        merge_sort(vetor, meio+1, pf)
        merge(vetor, pi, meio, pf)

def merge(vetor, pi, meio, pf):
    temp = list(vetor)
    i = pi
    j = meio+1
    k = pi
    while k <= pf:
        if i > meio:
            vetor[k] = temp[j]
            j += 1
        elif j > pf:
            vetor[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            vetor[k] = temp[i]
            i += 1
        else:
            vetor[k] = temp[j]
            j += 1
        k += 1

vetor = list(range(0,10)) # cria vetor com 10 elementos
random.shuffle(vetor) # embaralha vetor

print ("Vetor antes: ")
print(vetor)
merge_sort(vetor, 0, len(vetor)-1)
print("Vetor depois: ")
print(vetor)