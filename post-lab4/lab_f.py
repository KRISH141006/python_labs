nums = [1,32, 3, 45]
ans = 0
for i in nums:
    digits = len(str(i))          
    ans = ans * (10 ** digits) + i
print(ans)