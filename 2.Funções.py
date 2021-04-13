def cria_baralho():
    lista_baralho = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']
    return lista_baralho

def extrai_naipe(carta):
    lista_naipe = ['♥','♦','♠','♣']
    for i in lista_naipe:
        if i in carta:
            return i

def extrai_valor(carta):
    lista = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for i in lista:
        if i in carta:
            return i

def lista_movimentos_possiveis(cartas,i):
    i=int(i)
    lista_movimento = []
    if i == 0:
        return []
    else:
        if extrai_valor(cartas[i]) in cartas[i-1] or extrai_naipe(cartas[i]) in cartas[i-1]:
            lista_movimento.append(1)
        if i > 2:
            if extrai_valor(cartas[i]) in cartas[i-3] or extrai_naipe(cartas[i]) in cartas[i-3]:
                lista_movimento.append(3)
    return lista_movimento 

def possui_movimentos_possiveis(cartas):
    for i in range(len(cartas)):
        if extrai_valor(cartas[i]) in cartas[i-1] or extrai_naipe(cartas[i]) in cartas[i-1]:
                return True
        if i > 2:
            if extrai_valor(cartas[i]) in cartas[i-3] or extrai_naipe(cartas[i]) in cartas[i-3]:
                return True
    return False
    
def empilha(baralho,o,d):
    o = int(o)
    d = int(d)
    baralho[d] = baralho[o]
    del baralho[o]
    return baralho

def movimento_possivel(cartas,i):
    i = int(i)
    if extrai_valor(cartas[i-1]) in cartas[i-2] or extrai_naipe(cartas[i-1]) in cartas[i-2]:
        return True
    if extrai_valor(cartas[i-1]) in cartas[i-4] or extrai_naipe(cartas[i-1]) in cartas[i-4]:
        return True
    else:
        return False

print("O estado atual do baralho é:")
import random
i = 1
lista_baralho = cria_baralho()
novo_baralho = []
while i < 53:
    x = ''.join(random.sample(lista_baralho,1))
    print("{0}.  {1}".format(i,x))
    del lista_baralho[lista_baralho.index(x)]
    novo_baralho.append(x)
    i +=1
while possui_movimentos_possiveis(novo_baralho) == True:
    numero_escolhido=input("Escolha uma carta (digite um número entre 1 e 52): ")
    movimento= False
    while movimento == False: 
        if movimento_possivel(novo_baralho,numero_escolhido) == False:
            numero_escolhido=input("A carta {0} não pode ser movida. Por favor, digite um número entre 1 e 52: ".format(novo_baralho[int(numero_escolhido)-1]))
        else:
            movimento = True

##não funciona direito, precisa de ajuste
##Tentativa de fazer as condições para empilhar

    if lista_movimentos_possiveis(novo_baralho,numero_escolhido) == [1]:
        empilha(novo_baralho,numero_escolhido,(int(numero_escolhido)-1))
    elif lista_movimentos_possiveis(novo_baralho,numero_escolhido) == [3]:
        empilha(novo_baralho,numero_escolhido,numero_escolhido-3)
    elif lista_movimentos_possiveis(novo_baralho,numero_escolhido) == [1,3]:
        print("Sobre qual carta você quer empilhar o {0}?".format(novo_baralho[int(numero_escolhido)-1]))
        print("  1. {0}".format(novo_baralho[int(numero_escolhido)-2]))
        print("  2. {0}".format(novo_baralho[int(numero_escolhido)-4]))
