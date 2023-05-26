num = [5, 2, 8, 4, 3, 10]
# nilai = []
# banyak = int(input("Banyak angka: "))
# for i in range (0, banyak):
#     a = int(input("Angka: "))
#     nilai.append(a)

# urut = sorted(nilai, reverse=False)
urut = sorted(num, reverse=False)
print(urut)

for i in range (0,len(urut)):
    if urut[i] + 1 != urut[i+1]:
        print(urut[i] + 1)
        break