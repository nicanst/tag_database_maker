with open("objekt1.txt") as f:
    tag_tmpls = [row for row in f.read().splitlines() if row[0] != "#"]
print(tag_tmpls)
