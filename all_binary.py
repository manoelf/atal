def print_all_binary_helper(digit, output):
    if (digit == 0):
        print(output)
        return
    else:
        print_all_binary_helper(digit - 1, output + '0')
        print_all_binary_helper(digit - 1, output + '1')

def print_all_binary(digit):
    print_all_binary_helper(digit, '')

print_all_binary(int(input()))
