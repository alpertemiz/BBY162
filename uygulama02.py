__author__ = "Alper Temiz"
#Test Uygulaması
print("Test uygulamamız başlıyor")
input("Başlamak için her hangi bir şey yazınız= ")
Sorular = ['Futbolcular bir maçta ortalama ne kadar koşar?',\
           'Mavi rengi görebilen tek kuş türü nedir?',\
           'Ortalama bir insan kaç dakikada uykuya dalar?',\
           'Zıplayamayan tek hayvan türü nedir?',\
           'Yılın 7. ayı hangisidir?']
Cevaplar = ['C', 'B', 'D', 'A', 'D']
cevapA = ['9km',\
          'Güvercin',\
          '4dk',\
          'Fil',\
          'Ocak']
cevapB = ['10km',\
          'Baykuş',\
          '5dk',\
          'Kokarca',\
          'Şubat']
cevapC = ['11km',\
          'Martı',\
          '6dk',\
          'At',\
          'Mart']
cevapD = ['12km',\
          'Kartal',\
          '7dk',\
          'Örümcek',\
          'Temmuz']
Puan=0
for i in range(len(Sorular)):
    print("sorular"+str(i+1)+":"+Sorular[i])
    print("A) " + cevapA[i])
    print("B) " + cevapB[i])
    print("C) " + cevapC[i])
    print("D) " + cevapD[i])
    cevap = input("Cevabınız: ")
    if (Cevaplar[i] == cevap.upper()):
        Puan +=1
print("Testimiz Bitmiştir")
print("Aldığınız puan: "+str(int((Puan/len(Sorular)) * 100)))