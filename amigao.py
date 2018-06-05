
from itertools import combinations

T = int(raw_input())

# Tentando fazer o algoritmo gerando todas as combinacoes possivel de N
# elementos em K posicoes e realizando operacoes para comparar os valores
# e retornar o maior valor possivel, estava custando muito e dando TLE
#
#def operacao(combination):
#   total = combination[0]
#       
#   for c in combination:
#       total = total & c
#       
#       if (len(lista) > 0 and total < max(lista)):
#           return 0
#   
#   return total

while (T):
    try:
        N, K = map(int, raw_input().split())
        
        E = map(int, raw_input().split()[:N])
        
        if (len(E) < K):
            print 0
        
        else:
            R = 0;
            
            for i in range(30,-1,-1):
                
                aux1 = []
                aux2 = []
                Q = 0;
                
                # Como o limite eh 2^(30-1), deslocamos o 1 i vezes para 
                # a direita
                bit = 1 << i;
                
                # Fazendo o AND com todos os elementos da lista
                # verificamos se o bit significativo ocorre no elemento,
                # se sim o elemento vai para aux1, senao, vai para aux2
                for j in range(len(E) - 1,-1,-1):
                    
                    # Se o bit de significancia existir no valor de E[j]
                    # ele retorna o valor verdadeiro (!=0) e adiciona o 
                    # indice do elemento em aux1, caso nao, retorna 
                    # falso e adiciona o indice do elemento em aux2
                    #
                    # Exemplo: 1000000000000000000000000000000 and E[j]
                    # Exemplo: 0100000000000000000000000000000 and E[j]
                    # Exemplo: 0010000000000000000000000000000 and E[j]
                    # Se tiver 1 em E[j] na mesma posicao que na variavel
                    # bit ele retorna verdadeiro
                    #
                    # Assim a variavel bit vai mutando o 1 de posicao
                    # para encontrar todas as ocorrencias de bits
                    # significativos da esquerda para a direita
                    if (bit & E[j]):
                        aux1.append(j)
                        Q += 1
                    else:
                        aux2.append(j)
                
                # Verificamos se a ocorrencia de elementos com tal bit
                # significativo é maior ou igual a K
                if (Q >= K):    
                    
                    aux_R = E[aux1[0]]
                    
                    # Realizamos as operacoes AND com os K ou mais
                    # elementos e salvamos na variavel auxiliar
                    for k in range(1,Q):
                        aux_R &= E[aux1[k]]
                    
                    # Verificamos se aux_R eh maior que o valor anterior
                    # do laço
                    R = max(R, aux_R)
                    
                    # Ao garantir que eu tenho K ou mais ocorrencias
                    # significativas em aux1 removemos da lista E todos
                    # os elementos em que o AND com o bit significativo
                    # deu 0 e que foram para aux2
                    for l in range(len(aux2)):
                        del E[aux2[l]]
                    
                    # Refazemos o processo para todos os 29 bits do
                    # elemento procurando K ou mais elementos com bits
                    # muitos significativos, realizando operacoes and
                    # até encontrarmos o maior possivel
                    
            print R
        T -= 1
        
    except EOFError:
        break
