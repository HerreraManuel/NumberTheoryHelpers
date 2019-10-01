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
    
print('First polynomial h(n) = 103n^2-3945n+34381')
i = 0
while (i < 100):
    x = (103 * (pow(i, 2))) - (3945 * i) + 34381
    if isComposite(x):
        print("Integer {} : {}".format(i, x))
    i += 1

print('Second Polynomial k(n) = 36n^2-810n+2753')
j = 0
while (j < 100):
    y = (36 * (pow(j, 2))) - (810 * j) + 2753
    if isComposite(y):
        print("Integer {} : {}".format(j, y))
    j += 1
