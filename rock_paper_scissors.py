tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagit = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input("Tas secmek icin 1, kagit secmek icin 2, makas secmek icin 3 tuslayiniz.\n")) #hepsi için seçim yapmasını istedik.
if user_choice == 0:
 print (tas)
elif user_choice == 1:
 print (kagit)
elif user_choice == 2:
 print (makas)
else:
 print ("Gecersiz ssayi girdiniz kaybettiniz!")

print ("Bilgisayar secimi:")

computer_choice = random.randint(0,2) #bilgisayara 0 ve 2 arasında seçim yapmasını söyledik, bunun dışında seçim yapamaz

if computer_choice == 0:
 print (tas)
elif computer_choice == 1:
 print (kagit)
else:
 print (makas)

if user_choice==0 and computer_choice==2:
 print ("Kazandiniz!")
elif user_choice == 2 and computer_choice == 1:
 print ("Kazandiniz!")
elif user_choice == 1 and computer_choice == 0:
 print ("Kazandiniz!")
elif user_choice == computer_choice:
 print ("Berabere")
else:
 print ("Kaybettiniz.")

#kazandığımız ve berabere kaldığımız senaryoları yazdık, geriye sadece kaybettiğimiz senaryo kaldı bunu else komutuyla kısaca yazdık.