with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    out.write(f1.read())
    out.write(f2.read())


with open("merged.txt") as f :
    print(f.read().split())