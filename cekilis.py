import random

kullanicilar = list()

def kullanici_ekle (x):
    print("*"*30)
    print("Kullanıcı ekleme ekranına hoşgeldiniz.")


    ekle = input("Eklemek istediğiniz kullanıcıları giriniz: ")
    kullanicilar.append(ekle)
    input("Devam etmek için Enter tuşuna basınız.")

def kullanici_gor(x):
    sayac = 1
    print("*"*30)
    for i in x:
        print(str(sayac)+"-",i)
        sayac+=1
    print("*"*30)
    input("Devam etmek için Enter tuşuna basınız.")


def sec(x):
    print("*"*30)
    sayac =1
    kisi_sec = int(input("Kaç kişi seçilsin?: "))
    cek= random.sample(x,kisi_sec)

    for i in cek:
        print(str(sayac) +"-", i)
    print("*"*30)
    input("Devam etmek için Enter tuşuna basınız.")

def mix(x):
    sayac = 1
    random.shuffle(x)
    for i in x:
        print(str(sayac) +"-", i)
        sayac+=1
    input("Devam etmek için Enter tuşuna basınız.")

while True:
    print("--- Çekiliş Uygulamasına Hoşgeldiniz ---")
    secim = int(input("1- Kullanıcı ekle\n2- Kullanıcıları gör\n3- Kullanıcıları karıştır\n4- Rastgele seç\n"))

    if secim==1:
        kullanici_ekle(kullanicilar)

    elif secim==2:
        kullanici_gor(kullanicilar)

    elif secim==3:
        mix(kullanicilar)

    elif secim ==4:
        sec(kullanicilar)

    else:
        print("Hatalı seçim yaptınız. Lütfen kontrol ediniz.")