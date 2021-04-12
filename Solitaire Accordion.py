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