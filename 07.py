#1
i=1
while i<9:
    i+=1
    for a in range(1,10):
        b = a * i
        print(i, "x", a, "=",b)

#2
for j in range(2,10):
    for i in range(1, 10):
        print(j, "x 1 =", j * 1)