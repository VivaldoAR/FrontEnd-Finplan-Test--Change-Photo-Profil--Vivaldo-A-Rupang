n = int(input("Panjang: "))
lis = []
i=1
# print(len(list))

while len(lis)+1 <= n:
    if i % 3 == 0 and i % 7 == 0:
        lis.append("Z")
    elif i % 3 == 0 or i % 7 == 0:
        lis.append(i)
    i += 1

print(lis)