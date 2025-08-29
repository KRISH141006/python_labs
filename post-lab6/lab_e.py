n = 1243
n = str(n)
n_list = list(n)
temp = n_list[0]
n_list[0] = n_list[len(n)-1]
n_list[len(n)-1] = temp

n = int("".join(n_list))
print(n)
