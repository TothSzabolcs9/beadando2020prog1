try:
    sor = input("Adja meg az útszakasz hosszát méterben és a sebességkorlátot: ")
    tomb = sor.split(" ")
    n = int(tomb[0])/1000
    m = int(tomb[1])

    line = input("Adja meg az útszakaszra való belépés időpontját,kilépés időpontját és az autó rendszámát: ")

    data = []



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
    print("Nem a helyes sorrendben adtad meg az értékeket!")
except ValueError:
    print("Nem jó formátumban adtad meg az értékeket!")
