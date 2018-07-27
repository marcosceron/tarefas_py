count = 0
def maxmin4(vetor, linf, lsup):
    maxmin = [0,0]
    if (lsup - linf) <= 1:
        if vetor[linf] < vetor[lsup]:
            maxmin[0] = vetor[lsup]
            maxmin[1] = vetor[linf]
        else:
            maxmin[0] = vetor[linf]
            maxmin[1] = vetor[lsup]
    else:   # Acha o menor e maior elementos de cada particao
        meio = (linf+lsup) // 2 # divisao inteira
        global count
        count += 1
        print ("Dividiu: %d" % count)
        print ("Linf: %d, Lsup: %d" % (linf, lsup))

        maxmin = maxmin4(vetor, linf, meio)
        max1 = maxmin[0]
        min1 = maxmin[1]
        maxmin = maxmin4(vetor, meio+1, lsup)
        max2 = maxmin[0]
        min2 = maxmin[1]
        if (max1 > max2):
            maxmin[0] = max1
        else:
            maxmin[0] = max2
        if (min1 < min2):
            maxmin[1] = min1
        else:
            maxmin[1] = min2
    return maxmin


def main():
    vetor = [7, 4, 94, 53, 8, 1, 9, 88, 5, 67]
    print("Tamanho vetor: %d" % len(vetor))
    maxmin=maxmin4(vetor, 0, len(vetor)-1)
    print("Maximo: %d, Minimo: %d" % (maxmin[0], maxmin[1]))
main()