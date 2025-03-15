a = [int(s) for s in input().split()]
c = 0
for i in range(len(a)):
    for y in range(i+ 1,len(a)):
        #print(a[i], a[y])
        if a[i] == a[y]:
            c += 1

        #print(c)


print(c)