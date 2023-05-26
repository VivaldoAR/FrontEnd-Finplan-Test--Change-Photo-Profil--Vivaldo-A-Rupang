import re

kalimat = "Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah"
target = ["sang gajah", "serigala", "harimau"]

# kalimat = input("Kalimat: ")
# pemisah = input("Pemisah dua kalimat (agar dua kalimat menjadi 1 string): ")

kecil = kalimat.lower()
clear = kecil.replace(".", "")
print(clear)
print(" ")
# clear_split = re.split(fr"(?<!{pemisah})\s", clear)
clear_split = re.split(fr"(?<!sang)\s", clear)

print(clear_split)
print(" ")

# target = []
# banyak = int(input("Banyak kata yang ingin dicari: "))
# for i in range (0, banyak):
#     key = input("keyword= ")
#     target.append(key)

hasil = []

for a in clear_split:
    if a in target:
        hasil.append(a)
        
print(hasil)
print(" - ".join(hasil))