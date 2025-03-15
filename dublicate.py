n = input()
rost = input()
mesto = 0
for i in range(len(list(reversed(sorted([int(s) for s in (n + " " +rost).split()]))))):
    if int(rost) == (list(reversed(sorted([int(s) for s in (n + " " +rost).split()]))))[i]:
        mesto = i + 1
print(mesto)









#n =input()
#a = n.split()
#maxindex = 0

#for i in range(1, len(a)):
        #print(int(a[i]), int(a[i - 1]))
                #if int(a[i]) > int(a[maxindex]):
                        #maxindex = i

#print(a[maxindex], maxindex)

