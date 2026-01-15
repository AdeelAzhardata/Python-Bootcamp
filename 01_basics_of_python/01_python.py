import random 

guess_number = random.randint(1,30)

print("Welcome to magic number game")
print("Guess number and win a surprise")
print("Press Q for Quit")

attempts = 0

while attempts<5:

 user_input = int(input("Enter any number to guess"))

 if user_input == "Q" or "q" :
  print("you quit the game , GOODBYE !!")
  break
 
 try:
  guess = int(user_input)
 except ValueError:
  print("Enter a valid number")
  continue
 finally:
  pass
 
 attempts+=1

 if guess == guess_number:
  print("you won")
  break
 elif guess > guess_number:
  print("Too high")

 else :
  print("Too low")

  for dot in range(10):
   print(".",end="")
   print("/n")
else:
 print("you ran out of attempts")
   
  



