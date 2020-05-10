import statistics


n = int(input("n = "))
c = 0

data = []

while c != n:
    line = input("Bemenet: ")
    data.append(line.split(" "))
    c += 1

for x in range(len(data)):
    pos, neg = [], []
    for y in range(len(data[x])):

        if int(data[x][y]) > 0:
            pos.append(int(data[x][y]))
        elif int(data[x][y]) < 0:
            neg.append(int(data[x][y]))
        else:
            continue

    output = ""

    if len(pos) == 0:
        output += "Pozitív szórás nem számolható. "
    else:
        output += "Pozitív szórás: {:.3f}. ".format(statistics.pstdev(pos))

    if len(neg) == 0:
        output += "Negatív szórás nem számolható. "
    else:
        output += "Negatív szórás: {:.3f}. ".format(statistics.pstdev(neg))

    print(output)
