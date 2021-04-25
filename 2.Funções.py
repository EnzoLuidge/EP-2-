jogar = "s"
while jogar == "s":
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
        for i in range(1,len(cartas)):
            if extrai_valor(cartas[i]) in cartas[i-1] or extrai_naipe(cartas[i]) in cartas[i-1]:
                    return True
            if i > 2:
                if extrai_valor(cartas[i]) in cartas[i-3] or extrai_naipe(cartas[i]) in cartas[i-3]:
                    return True
        return False
    
    def empilha(baralho,o,d):
        o = int(o)
        d = int(d)
        baralho[d-1] = baralho[o-1]
        del baralho[o-1]
        return baralho

    def movimento_possivel(cartas,i):
        if i == "":
            return False
        i = int(i)
        if i == 1:
            return False
        
        if extrai_valor(cartas[i-1]) in cartas[i-2] or extrai_naipe(cartas[i-1]) in cartas[i-2]:
            return True
        
        if i>3:
            if extrai_valor(cartas[i-1]) in cartas[i-4] or extrai_naipe(cartas[i-1]) in cartas[i-4]:
                return True
            else:
                return False
        else:
            return False

    volta = 0
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
        if i==1:
            print("O estado atual do baralho é: ")
            while i < len(novo_baralho)+1:
                print("{0}.  {1}".format(i,novo_baralho[i-1]))
                i+=1
        numero_escolhido=input("Escolha uma carta (digite um número entre 1 e {0}): ".format(52-volta))
        while numero_escolhido.isnumeric() == False:
            numero_escolhido = input("Posição inválida. Por favor, digite um número entre 1 e {0}: ".format(52-volta))
        while int(numero_escolhido) > 52-volta or int(numero_escolhido)<1 or numero_escolhido =="":
            numero_escolhido = input("Posição inválida. Por favor, digite um número entre 1 e {0}: ".format(52-volta))
        movimento = False
        while movimento == False: 
            if numero_escolhido.isnumeric() == False:
                numero_escolhido=input("Posição inválida. Por favor, digite um número entre 1 e {0}: ".format(52-volta))
            elif int(numero_escolhido) > 52-volta or int(numero_escolhido)<1 or numero_escolhido == "":
                numero_escolhido=input("Posição inválida. Por favor, digite um número entre 1 e {0}: ".format(52-volta))
            elif movimento_possivel(novo_baralho,numero_escolhido) == False:
                numero_escolhido=input("A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}: ".format((novo_baralho[int(numero_escolhido)-1]),52-volta))
            else:
                movimento = True

        if lista_movimentos_possiveis(novo_baralho,int(numero_escolhido)-1) == [1]:
            novo_baralho = empilha(novo_baralho,numero_escolhido,int(numero_escolhido)-1)
        elif lista_movimentos_possiveis(novo_baralho,int(numero_escolhido)-1) == [3]:
            novo_baralho = empilha(novo_baralho,numero_escolhido,int(numero_escolhido)-3)
        elif lista_movimentos_possiveis(novo_baralho,int(numero_escolhido)-1) == [1,3]:
            print("Sobre qual carta você quer empilhar o {0}?".format(novo_baralho[int(numero_escolhido)-1]))
            print("  1. {0}".format(novo_baralho[int(numero_escolhido)-2]))
            decisao = input("  2. {0} ".format(novo_baralho[int(numero_escolhido)-4]))
            while decisao != '1' and decisao != '2':
                print("Opção inválida. Sobre qual carta você quer empilhar o {0}? digite 1 ou 2: ")
                print("  1. {0}".format(novo_baralho[int(numero_escolhido)-2]))
                decisao = input("  2. {0} ".format(novo_baralho[int(numero_escolhido)-4]))
            if decisao == "1":
                novo_baralho = empilha(novo_baralho,numero_escolhido,(int(numero_escolhido)-1))
            elif decisao == "2":
                novo_baralho = empilha(novo_baralho,numero_escolhido,(int(numero_escolhido)-3))
        i = 1
        volta +=1
    if len(novo_baralho) == 1:
        print("Você venceu!!")
    else:
        print("Você perdeu :(. ")
        jogar = input("Você quer jogar novamente? (digite s ou n): ")
        if jogar != "s":
            break