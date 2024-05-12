import random
from faker import Faker
fake = Faker("id_ID")
name = input("Please enter the players name? ")
#words = ["apple", "banana", "cherry", "orange", "grape", "strawberry"]
word = fake.month_name().lower()
#word = random.choice(words)
guesses = ""
guesses_left = 6
print("Welcome to Hangman!")
print("I am thinking of a word that is", len(word), "letters long.")
while guesses_left > 0:
  print("You have", guesses_left, "guesses left.")
  guess = input("Please guess a letter: ").lower()
  guesses += guess
  wrong = 0
  for letter in word:
    if letter in guesses:
      print(letter)
    else:
      print("_")
      wrong = 1
  if wrong == 0:
    print("Congratulations! ",name,"You guessed all the letters correct.")
    print("The word is: ", word)
    break
  if guess not in word:
    guesses_left-=1
    print("Wrong guess. This letter is not in word.")
    print("You have", guesses_left, 'more guess chances.')
    if guesses_left == 0:
      print("Sorry! Your number of chances are over. You loose.")
      print(word)
