from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def geraListaInvertida(tam):
    lista = list(range(1, tam+1))
    lista.reverse()
    return lista

mpl.use('Agg')


def selectSort(lista):
    numero_de_comparacoes = 0
    for i in range(len(lista)):
        menor_indice = i
        for j in range(i+1, (len(lista))):
            numero_de_comparacoes = numero_de_comparacoes + 1
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return numero_de_comparacoes


def desenhaGrafico(x,y, y2, file_name, label1, label2, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = label1)
    ax.plot(x,y2, label = label2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

tam = [10000,20000,50000,100000]
tempo_aleatorio = []
tempo_invertido = []
numero_de_comparacoes_aleatorio = []
numero_de_comparacoes_invertido = []

for i in range(4):
    lista = geraLista(tam[i])
    lista_invertida = geraListaInvertida(tam[i])

    tempo_aleatorio.append(timeit.timeit("selectSort({})".format(lista), setup="from __main__ import selectSort", number=1))
    tempo_invertido.append(timeit.timeit("selectSort({})".format(lista_invertida), setup="from __main__ import selectSort", number=1))
    numero_de_comparacoes_aleatorio.append(selectSort(lista))
    numero_de_comparacoes_invertido.append(selectSort(lista_invertida))

desenhaGrafico(tam, tempo_aleatorio, tempo_invertido, "Tempo.png", "Tempo lista aleatória", "Tempo lista invertida")
desenhaGrafico(tam, numero_de_comparacoes_aleatorio, numero_de_comparacoes_invertido, "NumeroDeComparacoes.png", "Numero de comparações lista aleatória", "Numero de comparações lista invertida")