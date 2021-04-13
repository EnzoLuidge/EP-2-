print("O estado atual do baralho é:")
import random
i = 1
lista_baralho = cria_baralho()
while i < 53:
    x = ''.join(random.sample(lista_baralho,1))
    print("{0}.  {1}".format(i,x))
    del lista_baralho[lista_baralho.index(x)]
    i +=1