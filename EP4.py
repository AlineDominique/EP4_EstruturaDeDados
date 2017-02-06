## Autor: Aline Dominique da Silva Santos
## Professor: Fernando Masanori Ashikaga
## Matéria: Estrutura de Dados
## 3º semestre A

##EP4 - (Algoritmo) O seguinte algoritmo guloso(=greedy) recebe um grafo G
##e devolve um conjunto estável X:
##X <- 0 
##H <- G
##enquanto Vh != 0 faça
##  escolha v em Vh de modo |Nh(v)| seja mínimo
##  X <- X
##  Z <- {v}U Nh(v)
##  H <- H-Z
##devolva X

def main():
    graph = {}
    graph[1] = [6, 7]
    graph[2] = [3, 7]
    graph[3] = [2, 4, 7, 6]
    graph[4] = [3, 7]
    graph[5] = [7]
    graph[6] = [1,3]
    graph[7] = [1, 2, 3, 4, 5]


    #print(len(graph))
    find_stablegroup(graph)

def find_stablegroup(group):
    aux = []
    less = 100000
    point = 10000
    for g in group:
        size = len(group[g])
        if size <= less:
            #print(g)
            if size == less:
                if g < point:
                    less = size
                    point = g 
            else:
                less = size
                point = g
            aux.append(g)            
            
    print(aux)

        
        
main()
