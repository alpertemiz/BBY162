__author__ = "ALPER TEMİZ\n"
print(__author__)
print("Adam Asmaca Oyununa Hoşgeldiniz\n")
isim = input("Oyuncu adı. : ")
print (isim, "Başlayabilirsin...\n")

import random

liste = random.choice(["ford", "mazda", "toyota", "bmw", "mercedes", "auidi", "citröen", "renault", "fiat"])

listuzunluk = len(liste)
print("Bu el {} harfli kelime geldi :)).\n".format(listuzunluk))
can = 5
arabamarkaları = []
tahminler = []
çiftcizgi = "___"
for kelime in liste:
    arabamarkaları.append(çiftcizgi)
print(arabamarkaları)
while can > 0:
    i = 0
    giriş = input("\nTahmini kelime? : ").lower()
    if giriş in liste:
        for kontrol in liste:
            if liste[i] == giriş:
                arabamarkaları[i] = giriş
            i += 1
        print("")
        print(arabamarkaları)
        print("\n\t DOĞRU BİLDİNİZ! ")
    else:
        can -= 1
        print("")
        print(arabamarkaları)
        print("\n\t YANLIŞ BİLDİNİZ!")
        print("\n\t Kalan canınız = %s" %can)
    if can == 0:
        print("\nKAYBETTİNİZ! Cevap: % .." %liste)
        break
    if çiftcizgi not in arabamarkaları:
        print("\nİyi oyundu.\t Tekrar oynamaya ne dersin ? :)")
        break
