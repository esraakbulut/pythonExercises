tel_rehberi = dict()

def no_ekle(x):
    print("-Numara Ekleme Ekranı-")
    numara_isim_al=input("Eklenecek Kişinin Adını Yazınız: ")
    numara_no_al = input("Eklenecek Kişinin Numarasını Giriniz: ")
    
    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al} adlı kişi telefon rehberine eklendi.")


def rehber_goster(x):
    print ("Rehbere Hoşgeldiniz")
    kişi_sayisi= len(x)
    print(f"Rehberinizdeki kayıtlı kişi sayısı: {kişi_sayisi} ")


    for i,j in x.items():
        print(i, ": ", j)
    input("Devam Edilsin mi?")


def no_sil(x):
    print("-Kişi Silme Ekranı-")
    silinecek_kisi = input("Silinecek kişiyi yazınız: ")
    x = tel_rehberi.pop(silinecek_kisi)
    input("Devam Edilsin mi?")

def kisi_ara(x):
    print("-Kişi Arama Ekranı-")
    aranan = input("Aranacak ismi yazınız: ")
    if aranan in x:
        print(f"{aranan}: {x[aranan]}")
    else:
        print("Kişi rehberde bulunamadı.")
    input("Devam etmek için Enter'a basın.")


while True:
        print ("-Hoşgeldiniz-")
        print("Seçim Yapınız")
        secim= int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n4-Kişi ara"))

        if secim==1:
            no_ekle(tel_rehberi)
        elif secim ==2:
            no_sil(tel_rehberi)
        elif secim == 3:
            rehber_goster(tel_rehberi)
        elif secim == 4:
             kisi_ara(tel_rehberi)

        else:
            print("Geçersiz Seçim Yaptınız.")