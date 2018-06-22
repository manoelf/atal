


def combina(tor, al, pesos, conj):
    cal = 0
    if (tor == 3):
        for i in range(1, al + 1):
            for j in range(1, al + 1):
                for k in range(1, al + 1):
                    cal = (i * pesos[0]) + (j * pesos[1]) + (k * pesos[2])
                    if (cal in conj):
                        return False
                    else:
                        conj[cal] = True
        return True
    elif (tor == 2):
        for i in range(1, al + 1):
            for j in range(1, al + 1):
                cal = (i * pesos[0]) + (j * pesos[1])
                if (cal in conj):
                    return False
                else:
                    conj[cal] = True
        return True
    else:
        for i in range(1, al + 1):
            cal = i * pesos[0]
            if (cal in conj):
                return False
            else:
                conj[cal] = True
        return True
   

while True:
    try:
        tor, al = map(int, input().split()) 
        pesos = list(map(int, input().split()))
        conj = dict()
        result = combina(tor, al, pesos, conj)
        if (result):
            print('Lucky Denis!')
        else:
            print('Try again later, Denis...')
    except EOFError:
        break
        
