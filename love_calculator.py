print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1+name2
lower_names= combined_names.lower() #bütün harfleri küçük harfe çevirir

t = lower_names.count("t") #kaç tane t içeridiğini kontrol ettik ve bu değere t ismini verdik
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e #ilk değeri hesapladık, sıra loveda

l = lower_names.count ("l")
o = lower_names.count ("o")
v = lower_names.count ("v")
e = lower_names.count ("e")
second_digit = l + o + v + e


total = int(str(first_digit)+ str(second_digit))


if total < 10 or total > 90:
  print (f"Your score is {total}, you go together like coke and mentos.")
elif 40<total<50:
  print (f"Your score is {total}, you are alright together.")
else:
  print (f"Your score is {total}.")
  
 