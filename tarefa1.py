import sys
import time
from grafos import Grafo 

#Variável global para armazenar o maior clique encontrado
maior_clique = []


def algoritmo_bron(clique_atual, vert_cand, vert_excluida, grafo, tempo_inicio, tempo_exe):
    global maior_clique

    #Verifica se o tempo de execucao foi atingido
    if time.time() - tempo_inicio >= tempo_exe:
        return
    
    #Verifica se as vertices candidadtas e excluidas nao forem vazias
    if not vert_cand and not vert_excluida:
        #Verifica se o tamanho da clique atual é maior encontrado ate o momento
        if len(clique_atual) > len(maior_clique):
            maior_clique = clique_atual
        return
    
    #Escolhe a primeira vertice para ser pivo dentre as candidatas ou excluidas
    if vert_cand:
        pivo = vert_cand[0]
    else:
        pivo = vert_excluida[0]
    
    #Atribui a variavel quais vertices sao adjacentes(vizinhos)
    vizinho_pivo = grafo.get_adj(pivo)

    candidatos = []

    #Adiciona a lista vertices candidatas que nao sao adjacente ao pivo
    for j in vert_cand:
        if j not in vizinho_pivo:
            candidatos.append(j)
    
    for v in candidatos:
        #Atribui para a lista novos candidatos com base na adjacencia
        novos_cand = [x for x in vert_cand if grafo.grafo[v][x] == 1]
        
        #Atribui para a lista novos vertices excluidas com base na adjacencia
        novos_excl = [x for x in vert_excluida if grafo.grafo[v][x] == 1]
        
        #Adiciona o vertice v na clique atual
        algoritmo_bron(clique_atual + [v], novos_cand, novos_excl, grafo, tempo_inicio, tempo_exe)
        
        #Remove v da lista de camdidatos
        vert_cand.remove(v)
        #Adiciona v na lista de excluidos
        vert_excluida.append(v)
        
def main():
    #varivavel global para armazenar o maior clique encontrado
    global maior_clique

    #sys.argv é uma lista que contém os argumentos passados pela linha de comando
    #sys.argv[0] é o nome do script
    #sys.argv[1] em diante são os argumentos passados
    caminho = sys.argv[1]
    temp_exe = int(sys.argv[2])

    arquivo = open(caminho, 'r')

    #Loop que percorre o arquivo e adiciona as vertices na matriz de adjacencia
    cont = 0
    for i in arquivo:
        cont += 1
        if i[0] == 'c':
            pass
        elif i[0] == 'p':
            qtd_vertice = int(i.split(" ")[2])
            grafo = Grafo(qtd_vertice)
        elif i[0] == 'e':
            v1 = int(i.split(" ")[1])
            v2 = int(i.split(" ")[2])
            grafo.adicionaAresta(v1, v2)
        elif cont == 1:
            qtd_vertice = int(i.split(" ")[0])
            grafo = Grafo(qtd_vertice)
        else:
            v1 = int(i.split(" ")[0])
            v2 = int(i.split(" ")[1])
            grafo.adicionaAresta(v1, v2)
    
    arquivo.close()

    vertices = list(range(grafo.vertices))
    tempo_inicio = time.time()
    algoritmo_bron([], vertices, [], grafo, tempo_inicio, temp_exe)

    if maior_clique:
        print(len(maior_clique))
        print(" ".join(map(str, maior_clique)))
    else:
        print("Nenhum clique encontrado")

if __name__ == '__main__':
    main()