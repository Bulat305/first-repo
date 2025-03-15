text = []

while True:
    a = str(input())
    if a == "":
        break
    try:
        text.append(a)
    except:
        break

for i in range(len(text)):
    if i % 2 == 1:
        print(text[i])

отсюда убирать
text = []
str.split(' ')
while True:
    a = str(input())
    if a == "":
        break
    try:
        text.append(a)
    except:
        break

print(text)

# a = str(input())