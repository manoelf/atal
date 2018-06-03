last = -1
def is_ok(word):
    size = int(len(word)/2) 
    for i in range(1, size + 1):
        for j in range(len(word) - i):
            first = word[j:j+i]
            second = word[j+i:j+i+i]
            if (len(first) and len(second)):
                if (first == second):
                    return False
            else:
                break
    return True


def add_letter(word, last):
    if (is_ok(word + 'N')):
        last = 0
        return word + 'N', last
    elif (is_ok(word + 'O')):
        last = 1
        return word + 'O', last
    elif (is_ok(word + 'P')):
        last = 2
        return word + 'P', last
    else:
        word, last = remove_last(word, last)
        return  word, last
    

def remove_last(word, last):
    word = word[:-1] + letters[(last + 1) % 3]
    last = (last + 1) % 3
    if (is_ok(word)):
        return word, last
    return remove_last(word, last)


n = int(input())
while n:
    if (n >= 7):
        n += 1
    cont = 0
    word = ''
    letters = ['N', 'O', 'P']
    last = -1
    while True:
        if (n == cont):
            print(word)
            break
        else:
            word, last = add_letter(word, last)
            cont += 1
    n = int(input())

        




