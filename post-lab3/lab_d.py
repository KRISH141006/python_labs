string = 'Earth goes round the sun .'
string1 = string.split()
length = 0
word = 0
for i in string1 :
    if length<len(i) :
        length = len(i)
        word = i

print("longest word =",word)
