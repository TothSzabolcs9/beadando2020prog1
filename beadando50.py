n = int(input("Útszakasz hossza méterben: "))/1000
m = int(input("Sebességkorlát: "))


line = input("Adja meg az útszakaszra való belépés időpontját,kilépés időpontját és az autó rendszámát: ")

data = []


try:
    while line != "end":
        data.append(line.split(" "))
        line = input("Adja meg az útszakaszra való belépés időpontját,kilépés időpontját és az autó rendszámát: ")

    for x in range(len(data)):
        hr = int(data[x][3]) - int(data[x][0])
        min = int(data[x][4]) - int(data[x][1])
        sec = int(data[x][5]) - int(data[x][2])

        t = (hr*3600 + min*60 + sec)/3600

        if n/t > m:
            print(data[x][6], "{:.2f}km/h".format(n/t))

except IndexError:
    print("Nem jó formátumban adtad meg az értékeket!")
