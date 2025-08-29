n = 123
def numOfDigits(n) :
    count = 0
    while (n>0) :
        n = n//10
        count +=1
    return count

print(numOfDigits(n))
