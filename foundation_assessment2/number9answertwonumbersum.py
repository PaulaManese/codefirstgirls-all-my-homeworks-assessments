def printPairs(array, arr_size, targetsum):
    dict = {}
    arr = []
    
    for i in range(0, arr_size):
        temp = targetsum - array[i]
        if (temp in dict):
            print(f'Pair with given sum {targetsum} is ({temp} , {array[i]}) at indices ({dict[temp]}, {i})')
            arr.append(temp)
            arr.append(array[i])
        dict[array[i]] = i
        
    print(f'Array is {array}.')    
    print(f'Pairs for given sum {targetsum} are {arr}.') 
    
        
A = [1, 4, 45, 6, 10, 8]
n = 12
# printPairs(A, len(A), n)
printPairs([1,2,3,4,5,6,7,8], 8, 15)
printPairs([1,2,3,4,5,6,7,8], 8, 16)
printPairs([1,2,3,4,5,6,7,8], 8, 5)