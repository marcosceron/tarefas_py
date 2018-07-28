import random

def ordenacao_insercao(vetor):
    i=1 # comeca pela segunda posicao do vetor
    while i < len(vetor):
        elemento = vetor[i]
        trocou = False
        j = i-1
        while j>=0 and vetor[j]>elemento:
            vetor[j+1] = vetor[j]
            trocou = True
            j-=1
        if trocou:
            vetor[j+1] = elemento
        i+=1

vetor = list(range(0,10)) # cria vetor com 10 elementos
random.shuffle(vetor) # embaralha vetor
print ("Vetor antes: ")
print(vetor)
ordenacao_insercao(vetor)
print("Vetor depois: ")
print(vetor)