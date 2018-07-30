moedas = [100, 50, 25, 10, 5, 1]
total = 0

troco = int(input("Digite o valor do troco: "))
string = ""

for i in range(len(moedas)):
    num_moedas = troco // moedas[i]
    if num_moedas > 1:
        string="moedas"
    elif num_moedas == 1:
        string="moeda"
    if num_moedas > 0:
        print("%d %s de %d" %(num_moedas, string, moedas[i]))
    troco -= num_moedas * moedas[i]
    total += num_moedas

print("Total de moedas: %d" % total)