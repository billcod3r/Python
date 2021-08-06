with open("practice_file.txt", 'w') as handle:
    handle.writelines("Hello this is a string")

with open('practice_file.txt') as f:
    lines = f.readlines()


