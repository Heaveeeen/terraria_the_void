import textParser
uid = 1234567890
while True:
    i = input()
    if i != "":
        if i[0] == "-":
            uid = int(i[1:])
        else:
            print(textParser(i,uid))
