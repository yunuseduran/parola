import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHJLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Sifre uzunlugu: "))
sifre =""
for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)

print(sifre)
