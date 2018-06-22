CONTROL = dict()

def spreach(word):
    size = len(word)
    if (size > 1):
        for i in range(size):
            new = word[:i] + word[i + 1:]
            if (new not in CONTROL):
                spreach(new)
                add_word(new)
    
    
    

def add_word(word):
    if (word in CONTROL):
        CONTROL[word] += 1
    else:
        CONTROL[word] = 1

while True:
    try:
        word = input()
        CONTROL = dict()
        CONTROL[word] = 1
        spreach(word)
        ans = []

        for item in CONTROL.keys():
            ans.append(item)
        ans.sort()

        for i in ans:
            print(i,)
        print()
    except EOFError:
        break

