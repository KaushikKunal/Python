from random import randint

def scramble_word(word):
    ipls = list(word)
    c = 1
    opls = []
    while (c < (len(ipls) - 1)):
        char = ipls[c]
        randnum = randint(0, len(opls))
        opls.insert(randnum, char)
        c = c + 1
    op = str(ipls[0])
    for c in range(0, len(opls)):
        op = op + str(opls[c])
    if (len(ipls) > 1):
        op = op + str(ipls[(len(ipls) - 1)])
    return(op)

op = ""
c = 0
ip = input("Enter sentence: ")
ipls = list(ip)
while (c < len(ipls)):
    word = ""
    char = ""
    mixed = "false"
    tries = 0
    while (mixed == "false"):
        while (char != " " and c < len(ipls)):
            char = str(ip[c])
            if (char != " "):
                word = word + char
            c = c + 1
        mixedword = scramble_word(word)
        tries = tries + 1
        if (len(list(word)) <= 3 or mixedword != word or tries > 100):
            mixed = "true"
    print (word , " ---> " , mixedword)
    op = op + mixedword + " "
print(op)
