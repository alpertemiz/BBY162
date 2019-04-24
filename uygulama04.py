#soru1
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:20])     # Note: string indexing starts with 0

#soru2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
print(liste)
for i in liste:
    print(i)

#soru3
sozluk = ["Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze"]
xveri=input("hangi kelimeye ulasmak istersiniz? : ")
if xveri == "Elma":
    print(sozluk["Elma"])
elif xveri == "salatalık":
    print(sozluk["salatalık"])
else:
    print("bulunmamaktadır")