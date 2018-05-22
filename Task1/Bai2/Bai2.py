# Doc file
def readFile(name, mode):  
    res =[]
    with open(name, mode) as f:
        for line in f:
            for word in line.split():
                res.append(word)
    f.close()
    return res

# Ghi file
def writeFile(name, mode, data):
    with open(name, mode) as f:
        for a in data:
            f.write(str(a) + "\n")
    f.close()



# Dem tan so cua cac tu
def countWord(data):
    res = {}
    for x in data:
        if(x in res.keys()):
            res[x]+= 1
        else:
            res[x] = 1
    return res

# main

data = readFile("input.txt", "r")
keys = countWord(data).keys()
values = countWord(data).values()
count = zip(keys, values)

writeFile("output.txt", "w", list(count))

