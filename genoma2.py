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

def find_word_helper(actual_size, size, word):
    if (not is_ok(word)):
        return 
    elif (actual_size == size):
        print(word)
        return
    else:
        find_word_helper(actual_size + 1, size, word + 'N')
        find_word_helper(actual_size + 1, size, word + 'O')
        find_word_helper(actual_size + 1, size, word + 'P')


def find_word(size):
    find_word_helper(0, size, '')

find_word(int(input()))
