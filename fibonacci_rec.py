def fibonacci(n):
    if n < 2:
        return n
    else:
        print("n=%d chamada recursiva" % n)
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n=8
    resposta=""
    for n in range(0, n):
        resposta = resposta + " " + str(fibonacci(n))

    print(resposta)

main()
