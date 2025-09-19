# 1
# fileTxt = open("//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt")

# 2
# fileTxt = open(r"//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt")
# for each in fileTxt :
#     print(each)

# 3 
# fileTxt = open(r"//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt")
# print(fileTxt.read())

# 4
# with open(r"//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt") as fileTxt:  
#     data = fileTxt.read() 
# print(data)

# 5
# fileTxt = open(r"//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt")
# print(fileTxt.read(5))

# 6
# with open(r"//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt") as fileTxt:  
#     data = fileTxt.readlines()
#     for line in data :
#         word = line.split()
#         print(word)

# 7 not for word file
# fileTxt = open("//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt",'w')
# fileTxt.write("ICT Marwadi University\n")
# fileTxt.write("ICT ICT ICT ICT ICT")
# fileTxt.close()

# 8 not for word file
# with open("//run//media//krish//New Volume//d_drive//sem_3//pwp//lab//ict.txt",'w') as fileTxt :
#     fileTxt.write("Krish Sondagar\n")
#     fileTxt.close()

# 9
# with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/ict.txt", "a") as fileTxt:
#     fileTxt.write("\nICT Marwadi University")

# with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/ict.txt", "r") as fileTxt:
#     print(fileTxt.read())

# 10
# with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/a.tif",'rb') as fileTif:
#     print(fileTif.read())
    
# 11
# with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/a.tif",'rb') as fileTif:
#     data = fileTif.read()
#     fileTif.close()

# with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/a.tif",'wb') as fileTif:
#     fileTif.write(data)
#     fileTif.close()

# 12

# import csv

# with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/data-1.csv") as fileCsv :
#     data = csv.reader(fileCsv)
#     for row in data :
#         print(row)
#     fileCsv.close()

# 13

import csv

with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/data-1.csv",'w',newline="") as fileCsv :
    data = csv.writer(fileCsv)
    data.writerow(['Name', 'Subject', 'Marks'])
    data.writerow(['Krish', 'Edcad', '50'])
    data.writerow(['Krisha', 'Edcad', '60'])
    fileCsv.close()

with open("/run/media/krish/New Volume/d_drive/sem_3/pwp/lab/data-1.csv") as fileCsv :
    data = csv.reader(fileCsv)
    for row in data :
        print(row)
    fileCsv.close()
