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
    count = []
    label = set(value for value in data)
    label = sorted(label)

    for labelData in label:
        countTemp = 0
        for j in range(len(data)):
            if(data[j] == labelData):
                countTemp += 1
                data[j]= None
        count.append(countTemp)

    zipped = zip(label, count)
    return list(zipped)

# main

data = readFile("input.txt", "r")
count = countWord(data)
writeFile("output.txt", "w", count)

