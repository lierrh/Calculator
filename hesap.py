# paketler

import math
import os
import time

os.system('cls' if os.name=='nt' else 'clear')

print("--------------------------------------")

print("")

print("")

# başlık

print("         🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁 V1.3")

print("")

print("         Instagram:piersym667         ")


print("")

print("--------------------------------------")


print("SiZE iŞLEM NUMARASI SORULDUĞU ZAMAN") 

print("------------------------------")

print("1 (toplama)")     
print("------------------------------")
print("2 (çıkarma)") 
print("------------------------------")
print("3 (çarpma)") 
print("------------------------------")
print("4 (bölme)")
print("------------------------------")
print("5 (üss alma)")
print("------------------------------")
print("6 (bölümünden kalan)")  
print("------------------------------")
print("7 (karekökü)")
print("------------------------------")
print("8 (ortalama)")
print("------------------------------")
print("9 (tam bölümü)")
print("------------------------------")

print("")

print("###############################")

print("")

print("DİKKAT : 7(karekök)'ü seçecekseniz 2.sayının bir önemi yoktur! rastgele bir sayı yazın ama boş bırakmayın , harf veya özel karakter girmeyin!")

print("")

print("###############################")

print("")


print("")
sayi1=(float(input('1. SAYIYI GİRİNİZ :')))
print("")
sayi4=(float(input('2. SAYIYI GİRİNİZ :')))


print("")

print("###############################")

print("")

print("")

print("ÖRNEK : 1 yazarsanız 1. sayı ile 2. sayı toplanacak 2 yazarsaniz 1.sayıdan 2.sayı cıkarılacaktır. UNUTMA! 1.sayı önceliklidir...")

print("")

print("")

print("###############################")

print("")


sayilar=(int(input('İŞLEM NUMARASINI GİRİNİZ :')))


print("")

print("")

print("")

os.system('cls' if os.name=='nt' else 'clear')

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print ("        SONUCUNUZ")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("")

print("")

print("")

if sayilar==1 :
    print ((sayi1+sayi4))
    
elif sayilar==2 :
    print ((sayi1-sayi4))
    
elif sayilar==3 :
    print ((sayi1*sayi4))
    
elif sayilar==4 :
    print ((sayi1/sayi4))
    
elif sayilar==5 :
    print ((sayi1**sayi4))
    
elif sayilar==6 :
    print ((sayi1%sayi4))
    
elif sayilar==7 :
	print ((math.sqrt(sayi1)))
    
elif sayilar==8 :
	print ((sayi1+sayi4) / 2)

elif sayilar==9 :
        print (sayi1//sayi4)
    
else :
    print("LÜTFEN iŞLEM NUMARASI KISMINA GEÇERLi BiR RAKAM GiRiNiZ")
    
print("")

print("")

print("")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# bilgilendirme 
print("--------------------------------------------")
print("BİLGİLENDİRME : bu yazılım denenmiştir ve bir sıkıntı çıkmamıştır ! ama eğer bir sıkıntı görürseniz , birşey sormak isterseniz veya iletişim kurmak için bana ==> https://instagram.com/piersym667 <== 'dan ulaşabilirsiniz")
print("--------------------------------------------")
print("20 SANİYE SONRA OTOMATİK ÇIKIŞ YAPILACAKTIR")
print("--------------------------------------------")

time.sleep(20)

os.system('cls' if os.name=='nt' else 'clear')
