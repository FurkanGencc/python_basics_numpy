# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 20:52:15 2025

@author: Turkuaz
numpy kütüphanesi çalışmalarım

"""

import numpy as np

#0-100 arası 10 tane rastgele sayi

dizi=np.random.randint(0,101,10)# 0 ile 100 arasında 10 tane sayi üret 
print(dizi)
#En büyük değeri
print("En büyük deger:",np.max(dizi))
#En küçük değeri
print("En küçük deger:",np.min(dizi))
#Ortalama
print("Ortalama: ",np.mean(dizi))
#50'den büyük sayilari filtrele
filtre=dizi[dizi>50]
print("50 den büyük sayilar:",filtre)


#%% 2.örnek
#Carpim toplam matris çarpımı tersi ve determinantı
A=np.array([[1,2],[3,4]])
B=np.array([[2,0],[1,3]])
print("Toplam: ",A+B)
print("Eleman carpımı:",A*B)
print("Matris Carpimi:",A@B)
#Determinant alma
det_A=np.linalg.det(A)
print("Determinant(A):",det_A)
#Tersini alma
ters_A=np.linalg.inv(A)
print("Ters(A): ",ters_A)

"""
Matris çarpımı 


A=[1 ,2]  B=[2 ,0]
  [3,4]     [1, 3]
  
  C11=1*2+2*1=4
  C12=1*0+2*3=6
  C21=3*2+4*1=10
  C22=3*0+4*3=12
  C=[4 ,6]
    [10,12]

"""
#%%Sıcaklık analizi
sicakliklar=np.random.uniform(-5,35,365)#-5 ile 35 arasında 365 tane değer ürettirdim.Uniform her sayının seçilme olasılıgı eşit.Ondalıklı sayılar ürettik
print("En soğuk gün:",np.min(sicakliklar),"En sıcak gün:",np.max(sicakliklar))
print("Sıfırın altındaki ilk 5 gün:",sicakliklar[sicakliklar<0][:5])# son beş gün için[-5:]
print("Ortalama Sıcaklık: ",np.mean(sicakliklar))
#%% argmax argmin
dizi=np.array([4,7,8,64,10,4,8,3])
eb_index=np.argmax(dizi)#argmax,argmindizide ki en büyük ve en küçük elemanın indexini verir
ek_index=np.argmin(dizi)
print("En büyük elemanın indexi: ",eb_index)
print("En küçük elemanın indexi: ",ek_index)
print(dizi[(dizi>3) & (dizi<8)])
print("Bir koşulun en az bir yerde doğru oldugunu soruglama: ",np.any(dizi>7))
print("Bir koşulun her zaman doğru oldugunu sorgulama: ",np.all(dizi>2))
indeksler=np.where(dizi>8)#Bir koşulu sağlayan değerlerin indisleri where ile bulabilirz
print(indeksler)
matris=np.array([[1,2,3],[7,8,9]])
print(np.sum(matris,axis=0))#axis=0 sutun toplamı
print(np.sum(matris,axis=1))#axis=1 satırlar toplamı 

#%%50 öğrenci notları
dizi=np.random.randint(0,100,50)
print(dizi)
print("En yüksek not alan öğrenci: ",np.max(dizi))
print("Ortalama başarı: ",np.mean(dizi))
gecen=dizi[dizi>=50]
kalan=dizi[dizi<50]
basari_oranı=len(gecen)/len(dizi)*100
print("Geçen ögrenci sayisi: ",len(gecen))
print("Kalan öğrenci sayisi: ",len(kalan))
print("Basari oranı: ",round(basari_oranı,2))#virgülden sonra 2 basamak bırak 
#%%  5x5 lik matris
matris=np.random.randint(0,51,(5,5))
print("Orijinal matris: \n",matris)
matris_T=matris.T
print("Transpoz: \n",matris_T)#satırlar sütun sütunlar satır oldu 
det=np.linalg.det(matris)
print("Determinant:",det)
filtre=matris[matris>25]
print("Filtrelenmiş: ",filtre)
#%% normalize etme
veri=np.random.randint(10,200,10)
norm=(veri-np.min(veri))/(np.max(veri)-np.min(veri))#normalize etme adımı 1 e yaklaştırma
print(norm)
print(veri)

#%% 1D,2D,3D örnekleri

boyut1=np.array([1,2,3,4,5])
print("1D dizi: ",boyut1)
print("Boyutu: ",boyut1.ndim)
print("Şekli: ",boyut1.shape)
boyut2=np.array([[1,2,3,4],[7,8,6,9]])
print("2D dizi: \n",boyut2)
print("Boyutu: ",boyut2.ndim)
print("Şekli: ",boyut2.shape)
boyut3=np.array([[[1,2,3,4],[7,8,9,10]],[[3,4,5,6],[2,3,4,6]]])
print("3D dizi: \n",boyut3)
print("Boyutu: ",boyut3.ndim)
print("Şekli: ",boyut3.shape)




















