# Carson McDonald
# 5/6/24
# Quiz Game
# This is a code along project I followed along with on Youtube.
print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")
if(playing.lower() != "yes"): # Indenting is important.
  quit()
  
print("Okay! Let's play! :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit": # This changes answer to lowercase.
  # You can also make everything uppercase instead.
  score += 1
  print("That is Correct!")
else:
  print("That is Incorrect...")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("That is Correct!")
  score += 1
else:
  print("That is Incorrect...")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
  print("That is Correct!")
  score += 1
else:
  print("That is Incorrect...")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  print("That is Correct!")
  score += 1
else:
  print("That is Incorrect...")

print("You got " + str(score) + " answers correct!")
print("Thats a " + str((score/4) * 100) + "%!")
if(score == 4):
  print("That's a perfect score!")
if(score == 3):
  print("That's a pretty good score!")
if(score == 2):
    print("That's not too bad.")
if(score == 1):
    print("That's not too good at all.")
if(score == 0):
  print("Yikes! Better luck next time.")