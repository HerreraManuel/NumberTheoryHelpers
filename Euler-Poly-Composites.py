def isComposite(n):
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False
    if(n % 2 == 0 or n % 3 == 0):
        return True
    i = 5
    while(i * i <= n):
        if(n % 1 == 0 or n % (i + 2) == 0):
            return True
        i = i + 6
    return False
    
i = 0
while (i < 100):
    x = (103 * (pow(i, 2))) - (3945 * i) + 34381
    if isComposite(x):
        print("Integer {} : {}".format(i, x))
    i += 1
