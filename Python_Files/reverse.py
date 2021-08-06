def backwords(filename):
    lines = open(filename).readlines()
    rev = reversed(lines)
    for i in rev:
        print(i.rstrip())

backwords("practice_file.txt")
