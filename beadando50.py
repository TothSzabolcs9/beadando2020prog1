n = int(input("Útszakasz hossza méterben: "))/1000
m = int(input("Sebességkorlát: "))

line = input("Bemenet: ")

data = []

while line != "end":
    data.append(line.split(" "))
    line = input("Bemenet: ")

for x in range(len(data)):
    hr = int(data[x][3]) - int(data[x][0])
    min = int(data[x][4]) - int(data[x][1])
    sec = int(data[x][5]) - int(data[x][2])

    t = (hr*3600 + min*60 + sec)/3600

    if n/t > m:
      print(data[x][6], "{:.2f}km/h".format(n/t))