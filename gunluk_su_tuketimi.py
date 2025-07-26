# kilo*0.03 = günlük tüketilmesi gereken minimum su

def su_hesapla(kilo):
    erkek_su = kilo*0.04
    kadın_su = kilo*0.03 

    cinsiyet = input("Lütfen cinsiyetinizi giriniz: Erkek/Kadın: ").capitalize()

    if cinsiyet == "Erkek":
        print("-"*30)
        print("Cinsiyetiniz: ",cinsiyet)
        print(erkek_su, "Litre su içmelisiniz.")
        print("-"*30)
    elif cinsiyet == "Kadın":
        print("-"*30)
        print("Cinsiyetiniz: ",cinsiyet)
        print (kadın_su, "Litre su içmelisiniz.")
        print("-"*30)
    else :
        print("Lütfen Cinsiyetinizi Belirtin")

kilo_al = int(input("Lütfen kilonuzu giriniz: "))

su_hesapla(kilo_al)