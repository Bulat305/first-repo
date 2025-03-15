a = str(input())
print(a[2])
print(a[-2])
print(a[0:5])
print(a[0:-2])
print(a[0::2])
print(a[1::2])
print(a[::-1])
print(a[-1::-2])
print(len(a))
print(a.count(' ') + 1)
print(len(a)/2)
print(a[int((len(a)/2) +0.5):len(a)] + a[0:int((len(a)/2) + 0.5)])
print(a.find(' '))
print(a[a.find(' ')+ 1:len(a)], a[0:a.find(' ')])
print(a.find('f'))
print(a.count('f'))

if a.count('f') == 1:
    print(a.find('f'))
if a.count('f') > 1:
    print(a.find('f'), a.rfind('f'))


if a.count('f') == 1:
    print("-1")
if a.count('f') == 0:
    print('-2')
elif a.count('f') > 1:
    print(a.find('f', (a.find('f') + 1)))
print(a[a.find('h'):a.rfind('h')])
print(a[a.find('h'):a.rfind('h'):-1])
print(a[a.find('h')::-1])
print(a[a.find('h') - 1 :a.rfind('h'):-1])
print(a[a.find('h'):a.rfind('h') + 1])
print(a[a.rfind('h'):a.find('h') - 1:-1])
if a[0] == "h":
    print(a[::-1])
else:
    print(a.replace(a[a.find('h'):a.rfind('h') +1], a[a.rfind('h'):a.find('h') -1: - 1]))
print(a.replace("h", "H"))
print(a.replace(a[a.find('h') + 1:a.rfind('h') ], a.replace("h", "H")))
print(a[:a.find('h') + 1] + a[a.find('h') +1 :a.rfind('h')].replace("h", "H") + a[a.rfind('h'):])
#[a.find('h'):a.rfind('h') + 1]h
print("отсюда Булат")
print(a[::3])
print(a.replace(a[2], "H"))

for i in range(len(a)):
    if i % 3 != 0:
        print(a[i], end="")
