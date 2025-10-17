# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 02:02:47 2025

@author: Turkuaz
numpy kütüphanesi çalışmaları
"""

#%% numpy kütüphanesi
"""
-Büyük çok boyutlu matrisler için hesaplama kolaylıgı sağlar
-Yapay zeka,Derin öğrenme,Görüntü işleme gibi alanlarda kullanılır
-Aslında bir array yapısıdır

"""

import numpy as np

# 1* 15 boytunda array-dizi

dizi=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) #dizinin şekline boyutuna bakmış olduk sonuç (15,) yazar 1 e15 lik dizi arrayin boyutuna baktık

dizi2=dizi.reshape(3, 5)#Diziyi 2 boyutlu yaptık 3 satır 5 sutun haline getirdik
print("Şekil: ",dizi2.shape)
print("Boyut:  ",dizi2.ndim)
print("Veri tipi: ",dizi2.dtype.name)
print("Boy: ",dizi2.size)
print("Type: " ,type(dizi2))

# 2 boyutlu array(matris)
dizi2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,23,25]])# 3 satır 4 sütun
print(dizi2d)
# 2 boyutlu sıfırlardan oluşan array(matris)
sifir_dizi=np.zeros((3,5))#Bir dizi e başta for ile oluşturunca memory de fazla yer kaplar sıfırlardan oluşturup doldurursak daha az yer kaplar 
print(sifir_dizi)
# Birlerden oluşan
bir_dizi=np.ones((3,4))
print(bir_dizi)
#Boş array
bos_dizi=np.empty((3,3))
print(bos_dizi) # Boş dediğimiz kavram sıfıra yakın anlamında yani hiçbirşey diye bir kavra yok dizi oluşturdugumuz zaman


# arange fonksiyonu  arange(x,y,basamak) x den başlar y dahil değil basamak büyüklüğünü arttıarak gidiyor.
# Belirli bir aralıkta ki  sayılardan bir dizi(array) oluşturmak için kullanılır
dizi_aralik=np.arange(10,50,3 )
print(dizi_aralik)

#linspace(x,y,basamak)
# Girilen iki sayı aralıgını verilen sayı değerine göre eşit aralıklı sayılar üretiyor örneğin 5 verdik 10 ile 20 arasında burada 10 ile 20 dahil 
#10 ile 20 arasınnda eşit aralıklar ile sayılar üretecel
#linspace, başlangıç ve bitiş değerleri arasında, belirli sayıda eşit aralıklı değer üretir.

dizi_bosluk=np.linspace(10, 15,4)# 10 ve 15 ile beraber 4 sayı üretti ve her sayının arası eşit 
print(dizi_bosluk)


#Matematiksel işlemler
a=np.array([1,2,3,1])
b=np.array([7,5,4,1])

print("toplam",a+b,"Çikarma",a-b,"üs: ",a**2)

#Dizi elemanlarını toplama fonk
print(np.sum(a))
#max değer
print(np.max(a))
#min değer
print(np.min(a))
#mean(ortalama)
print(np.mean(a))
#median(dizinin ortasındaki sayıyı bulur )
print(np.median(a))
#median diziyi önce sıralar sonra ortadaki sayıyı verir

#Rastgele sayı üretme [0,1] arasında sürekli uniform 3*3
rastgele_dizi=np.random.random((3,3))
print(rastgele_dizi)



dizi=np.array([1,2,3,4,5,6,7,8,9])
#dizinin ilk 4 elemanı
print(dizi[0:4])
#dizinin tersi
print(dizi[::-1])


dizi2D=np.array([[1,2,3,4,5,6],[5,4,3,2,1,0]])

#dizinin 1.satır 1.sütunun da bulunan eleman
print(dizi2D[1,1])
#dizinin 1.sütunun da ki tüm satırlar 
print(dizi2D[:,1])
# Satır 1,sütün 1,2,3
print(dizi2D[1,1:4])
#dizinin son satır tüm sütünları
print(dizi2D[-1:])

#vektör haline getirme
vektor=dizi2D.ravel()
print(vektor)




