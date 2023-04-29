import turtle
import random
print("Welcome to the HANGMAN game\nThe game will now begin")
hang = turtle.Turtle()
color = input("to pick a colour enter 1\nif not enter 2\n")
color_list = ["black", "yellow", "brown", "red", "purple", "green", " blue", "orange"]
while color != "1" and color != "2":
  print("Invalid input")
  color = input("to pick a colour enter 1\nif not enter 2\n")
if color == "1":
  colour = input("Enter a colour\n").strip().lower()
  while not colour in color_list:
    print("Invalid input")
    colour = input("Enter a colour\n").strip().lower()
elif color == "2":
  colour = "Black"
hang.pencolor(colour)
hangman = 9
choose = input("Choose your own word enter 1\nUse a random word enter 2\n")
while choose != "1" and choose != "2":
  print("Invalid input")
  choose = input("Choose your own word enter 1\nUse a random word enter 2\n")
if choose == "1":
  word0 = input("Enter a word\n").strip().lower()
elif choose == "2":
  #words_list = ["game", "hangman", "banana", "turtle", "word","yes","python"] # this is the list of words # 
  words_list = ["turtle"]
  word0 = random.choice(words_list) ## randomises the word from the word list ##
length = len(word0) ## counts letters in the word ##
word = "_" * length ## "_" times the amount of letters in the word ##
print("_ " * length)
word1 = list(word) ## turns word into a list ##
word2 = list(word0) ## turn word0 (the word chosen) into a list ##
word_list = list(" ") ## this will store the letters input ##
correct = True

def base(): ## draws the base ##
  hang.penup()
  hang.goto(-50,-50)
  hang.pendown()
  hang.forward(100)

def pole(): ## draws the pol ##
  hang.penup()
  hang.goto(0,-50)
  hang.pendown()
  hang.left(90)
  hang.forward(120)

def second_pole(): ## draws the second pol ##
  hang.right(90)
  hang.forward(55)
  hang.right(90)
  hang.forward(10)

def head(): ## draws the head ##
  hang.right(90)
  hang.circle(10)

def body(): ## draws the body ##
  hang.penup()
  hang.goto(55,40)
  hang.pendown()
  hang.left(90)
  hang.forward(50)

def left_arm(): ## draws the left arm ##
  hang.penup()
  hang.goto(55,37)
  hang.pendown()
  hang.right(45)
  hang.forward(20)

def right_arm(): ## draws the right arm ##
  hang.penup()
  hang.goto(55,37)
  hang.pendown()
  hang.left(90)
  hang.forward(20)

def left_leg(): ## draws the left leg ##
  hang.penup()
  hang.goto(55,-10)
  hang.pendown()
  hang.right(90)
  hang.forward(20)

def right_leg(): ## draws the right leg ##
  hang.penup()
  hang.goto(55,-10)
  hang.pendown()
  hang.left(90)
  hang.forward(20)

while "_" in word and correct: ## while the word is not completely guesed the loop wil run ##
  letter = input("Guess a letter \n").strip().lower() ## input the letter and removes all spaces and turns the letters into lowercase
  for i in range(length):
    if len(letter) > 1 or len(letter) <= 0 or not (letter >= 'a' and letter <= 'z'): ## if the input is more than or less than one letter or the input is not a letter the if runs##
      print("Invalid guess, please try again")
      print(word)
      break ## breaks the if and for and the user will need to input the letter again ##
    elif letter in word_list and word2.count(letter) <= 1: ## if the letter input is stored in word_list (it has been guessed) the if runs ##
      print("you already guessed this")
      print(word)
      break ## breaks the if and for and the user will need to input the letter again ##
    elif word0[i] == letter: ## if the letter is in the word ##
      if word2.count(letter) >= 2: ## if the letter input appears more than once in the word the if runs ##
        word1.pop(i) ## takes "_" at the same position out ##
        word1.insert(i,letter) ## puts the letter in the right position ##
        word = " ".join(word1) ## turns word1 into string ##
        word_list.append(letter) ## adds the letter input to word_list ##
        for x in range((i + 1),length): ## repeats the code above but it starts from the letter after ##
          if word0[x] == letter:  
            print("correct, {} is in the word!".format(letter))
            word1.pop(x)
            word1.insert(x,letter)
            word = " ".join(word1)
            print(word)
            word_list.append(letter)
            break
      else:
        print("correct, {} is in the word!".format(letter))
        word1.pop(i)
        word1.insert(i,letter)
        word = " ".join(word1)
        print(word)
        word_list.append(letter)
        break
    elif not letter in word0: ## runs if the letter is not in the word ##
      print("incorrect!")
      hangman -= 1 ## subtracts amount of lives ##
      print("You have {} tries left".format(hangman))
      word_list.append(letter)
      print(word)
      if hangman == 8: ## depending on the number of lives different parts are drawn ##
        base()
      elif hangman == 7:
        pole()
      elif hangman == 6:
        second_pole()
      elif hangman == 5:
        head()
      elif hangman == 4:
        body()
      elif hangman == 3:
        left_arm()
      elif hangman == 2:
        right_arm()
      elif hangman == 1:
        left_leg()
      elif hangman == 0:
        right_leg()
        correct = False
        break
      break
if not "_" in word:
  print("Congratulations you win!")
if hangman == 0:
  print("you lose")
  print("The word was", word0)
