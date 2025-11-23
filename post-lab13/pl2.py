lines = []
with open(r"post-lab13\example.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

print(lines)
