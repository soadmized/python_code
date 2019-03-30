import math

x = 38.07987
y = 44.17544

data = []
with open("data.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
#print(data)

#нахождение длины отрезка
#c = data[0]
#pos1 = [abs(x-c[0]), abs(y-c[1])]
#pos2 = [abs(x-c[2]), abs(y-c[3])]
#length = math.sqrt(math.pow(c[2]-c[0], 2) + math.pow(c[3] - c[1], 2))
#print(length)
