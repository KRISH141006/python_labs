n = 1234
mul = 1

while(n>0) :
    rem = n%10
    n = n//10
    mul = mul * rem

print(mul)
