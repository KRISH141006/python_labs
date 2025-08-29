List = [1,2,2,3,4,4,5,6]
result = []

for item in List:
    if item not in result:
        result.append(item)

print(result)
