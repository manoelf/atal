from itertools import combinations


def convert(num):
    num = int(num)
    new = bin(num)[2:]
    new = ((32 - len(new)) * '0') + new
    return new

def maping_one(num, indexs):
    for i in range(len(num)):
        if (i not in indexs):
            indexs[i] = [0, []]
        if (num[i] == '1'):
            indexs[i][0] += 1
            indexs[i][1].append(num)
    return indexs


def mapping_all(nums, indexs):
    for num in nums:
        maping_one(num, indexs)
    return indexs


def find_it(nums, k, start, got):
    indexs = dict()
    indexs = mapping_all(nums, indexs)
    #print(indexs)
    #print('k', k, 'start', start)
    for i in range(start, 32):
        if (indexs[i][0] ==  k):
            return AND(indexs[i][1])
        elif(indexs[i][0] > k):
            return find_it(indexs[i][1], k, i + 1, True)
        if (indexs[i][0] < k and i < 32):
            continue
        if (indexs[i][0] < k and i == 31):
            return AND(nums)
    if (start >= 31):
        return AND(nums[:k])
    if (len(nums) > k):
        return AND(nums[:k])
    return '0'

def AND(nums):
    result = '0'
    if (len(nums) > 0):
        result = nums[0] 
    for i in range(1, len(nums)):
        aux = ''
        for j in range(len(nums[i])):
            if (nums[i][j] == result[j] and nums[i][j] == '1'):
                aux += '1'
            else:
                aux += '0'
        result = aux
    return result



 


tests = int(input())


for i in range(tests):
    n, k = map(int, input().split())
    conj = list(map(convert, input().split()))    
    bin_set = dict()
    indexs = dict()
    if (n < k):
        print(0)
    else:
        sume = find_it(conj, k, 0, False) 
        print(int(sume, 2)) 
