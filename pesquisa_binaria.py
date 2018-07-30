def pesquisa_binaria(vetor, n):
    inf = 0
    sup = len(vetor) - 1
    #print("Length: %d" % sup)

    while (inf <= sup):
        meio = (inf + sup)//2 # divisao inteira
        pesquisa = vetor[meio]

        if n == pesquisa:
            return meio
        elif n > pesquisa:
            inf = meio+1
        else:
            sup = meio-1
    return -1 # nao encontrado

def main():
    vetor = [23,27,34,48,49,50,89,95,96,100] # inicializa um vetor ordenado
    n = int (input("Digite o valor a ser procurado: "))
    print("N: %d" % n)
    print("Indice de N: %d" % pesquisa_binaria(vetor,n))
main()