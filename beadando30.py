import numpy as np

chars = ["a", "b", "c", "d", "e", "f", "g",
         "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z"]

n1 = int(input("Adja meg 'n'-t: "))
m1 = int(input("Adja meg 'm'-t: "))

if n1 == m1:
    print("A két szám nem lehet egyenlő!")

def insertStars(n, m):

    arr = np.array("")

    arr.resize((n+2, m+2))

    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if x != 0 and x != arr.shape[0]-1 and y != 0 and y != arr.shape[1]-1:
                arr[x][y] = chars[np.random.randint(0, len(chars)-1)]
            else:
                arr[x][y] = "*"

    return arr

print(insertStars(n1, m1))