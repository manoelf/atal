
def all_sub_set(A):
    
    for i in range(len(A)):
        aux = []
        for j in range(len(A) - i):
            aux.append(A[j:])
        print(aux)

all_sub_set([1, 2, 3])
