def fibonacci(n):
    fant = 0
    f = 1
    for k in range(0, n):
        print("n=%d loop" % n)
        aux = f
        f = f + fant
        fant = aux
    return fant

def main():
    n=8
    resposta=""
    for n in range(0, n):
        resposta = resposta + " " + str(fibonacci(n))

    print(resposta)

main()
