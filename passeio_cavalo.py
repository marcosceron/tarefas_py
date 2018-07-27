count=0

def aceitavel(x, y):
    if x >= 0 and x <= num-1 and y >= 0 and y <= num-1 and tabuleiro[x][y] == 0:
        return True
    else:
        return False

def tenta(i, x, y): # Tenta o i-esimo movimento em (x,y), 1 <= i <= n^2
    done = i > numSqr # True ou False
    k = 0
    while done == False and k < 8:
        if k==7: # Se forem tentados todos os movimentos possiveis, backtracking.
            global count
            print("Backtracking %d" % count)
            count+=1
        xn = x + h[k] # Proximo movimento x
        yn = y + v[k] # Proximo movimento y
        if aceitavel(xn, yn):
            tabuleiro[xn][yn] = i
            done = tenta(i+1, xn, yn) # Tenta outro movimento
            if done == False:
                tabuleiro[xn][yn] = 0 # Sem sucesso, descarta movimento
        k += 1 # Passa ao proximo movimento possivel
    return done

def imprime(x, y):
    tabuleiro[x][y] = 1
    done = tenta(2, x, y)
    string = ""
    if done == True:
        for x in range(0, num):
            for y in range(0, num):
                if tabuleiro[x][y] < 10:
                    string += "0" + str(tabuleiro[x][y]) + " "
                else:
                    string += str(tabuleiro[x][y]) + " "
            string += "\n"
        print(string)
    else:
        print("Nao ha passeio possivel\n")

h = [2, 1, -1, -2, -2, -1, 1, 2] # Movimentos na horizontal
v = [1, 2, 2, 1, -1, -2, -2, -1] # Movimentos na vertical

# N=6
num = 6 # Numero de posicoes do tabuleiro
print("X inicial: ")
x = int(input())
print("Y inicial")
y = int(input())
numSqr = num * num # Numero total de casas
tabuleiro = [[],[],[],[],[],[],[],[],[],[]]
for x in range(0, num):
    for y in range(0, num):
        tabuleiro[x].append(0)
#print tabuleiro
imprime(x, y)