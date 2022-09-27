newfile= open("../source/sequence.txt", "w+")
with open("../source/sequence.txt") as file:
    sequence = file.readlines()
    for lines in sequence:
        list = lines.rstrip()
        newfile.write(list)

