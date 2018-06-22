

def add_no_lote(lote, inicio, fim, size):
    lista = list(range(inicio, fim+1))
    i = 0
    j = 0
    while (i < size and j < len(lista)):
        if (lote[i] == lista[j]):
            lote.insert(i, lista[j])
            j += 1
        i += 1
    while(j < len(lista)):
        lote.append(lista[j])
        j += 1
    return lote


def primeiro_ultimo(lotes, num, size):
    primeiro = 0
    ultimo = 0 
    comecou = False
    i = 0
    while (i < size):
        if (lotes[i] == num):
            if (not(comecou)):
                comecou = True
                primeiro = i
            else:
                ultimo = i
        i += 1
    return primeiro, ultimo

while True:
    try:
        
        caixas = input()
        if (caixas != ''):
            lotes = []
            size = 0
            for i in range(int(caixas)):
                parafuso, porca = map(int, input().split())
                lotes = add_no_lote(lotes, parafuso, porca, size)
                size += (porca - parafuso) + 1
            num = int(input())
            if (num > lotes[-1]):
                print('%d not found' % num)
            else:
                comeco, fim = primeiro_ultimo(lotes, num, size)
                if (comeco == 0 and fim == 0 and num != lotes[-1]):
                    print('%d not found' % num)
                else:
                    print('%d found from %d to %d' % (num, comeco, fim))
    except EOFError:
        break
