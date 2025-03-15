a = str(input())
print(a[1:6])
print(len(a))
print(a.count("A"), a.count("C"), a.count("G"), a.count("T")) # подсчитывающие соответствующее количество раз, когда символы «A», «C», «G» и «T» встречаются
new_a = a.replace('T', 'U')
print(new_a)



a = str(input())
# new_a = a.replace('T', 'A') # заменяет все символы 'T' на "A"
# new_a = new_a.replace('G', 'C')
print(a)
for i in range(a):
    print(a[i])
#reversed_s = ''.join(reversed(new_a))
# print(reversed_s)

for i in range(n):