def cria_baralho():
    lista_baralho = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']
    print(len(lista_baralho))
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
    baralho[d] = baralho[o]
    del baralho[o]
    return baralho