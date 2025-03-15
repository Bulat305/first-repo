a = str(input())
b = ''.join(reversed(a)) #разворот строки
print(b)
abc = [] #Создаём пустой cписок
с = '' #Создаём пустую строку
for i in range(len(b)): # работа с каждым элементом строки,
    if b[i] == "T":
        print("A", end='') # вывод на экран в зависимости замены.... но без создание новой строки, спросить у даниса как закинуть новую строку
    if b[i] == "G":
        print("C", end='')
    if b[i] == "C":
        print("G", end='')
    if b[i] == "A":
        print("T", end='')
print(" ")
print(b)
#abc.append(i)
for i in range(len(b)): # работа с каждым элементом строки, и добавление элементов в список
    if b[i] == "T":
        abc.append("A")
    if b[i] == "G":
        abc.append("C")
    if b[i] == "C":
        abc.append("G")
    if b[i] == "A":
        abc.append("T")
print(abc)

for i in range(len(b)): # работа с каждым элементом строки, и добавление элементов в строку
    if b[i] == "T":
        с += "A"
        abc.append("A")
    if b[i] == "G":
        с += "C"
    if b[i] == "C":
        с += "G"
    if b[i] == "A":
        с += "T"
print(с)
