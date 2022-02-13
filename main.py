from colorama import Fore
from random import choice

word_file = open("Words.txt","r")
words = word_file.readlines()
# allowedwords_file = open("Allowed_words.txt","r")

#function to check the word against the 
def check(word):
    with open('Allowed_words.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if word in line:
            return True
    return False  # Because you finished the search without finding


#choose a random word
answer=choice(words)
answer=answer.upper()
answer = answer.rstrip()
word = ""
wordcorrect = False
print(answer) #remove after (used for debugging)
i = 0
while word != answer and i < 6:

  #get the user to input a word
  word = input(Fore.WHITE + "Input a word: ")
  word = word.upper() #make it uppercase
  if len(word) != 5: #check the length of the word
    print("This word is invalid")
    continue #try again basically
  
  #check the word against the allowed_words.txt file
  if check(word.lower()) == False:
    print("The word is not an acceptable word")
    continue

  #check each stage of the word to check if it is valid or not

  if word[0] == answer[0]:
    print(Fore.GREEN + word[0], "is in the correct position")
  elif word[0] in answer:
    print(Fore.YELLOW + word[0], "is in the word but not in that position")
  else:
    print(Fore.RED + word[0], "is not in the word")

  if word[1] == answer[1]:
    print(Fore.GREEN + word[1], "is in the correct position")
  elif word[1] in answer:
    print(Fore.YELLOW + word[1], "is in the word but not in that position")
  else:
    print(Fore.RED + word[1], "is not in the word")

  if word[2] == answer[2]:
    print(Fore.GREEN + word[2], "is in the correct position")
  elif word[2] in answer:
    print(Fore.YELLOW + word[2], "is in the word but not in that position")
  else:
    print(Fore.RED + word[2], "is not in the word")  

  if word[3] == answer[3]:
    print(Fore.GREEN + word[3], "is in the correct position")
  elif word[3] in answer:
    print(Fore.YELLOW + word[3], "is in the word but not in that position")
  else:
    print(Fore.RED + word[3], "is not in the word")

  if word[4] == answer[4]:
    print(Fore.GREEN + word[4], "is in the correct position")
  elif word[4] in answer:
    print(Fore.YELLOW + word[4], "is in the word but not in that position")
  else:
    print(Fore.RED + word[4], "is not in the word")
  #next i
  i+= 1

#final checks because the program would still output the word was correct
if i > 6:
  print(Fore.WHITE + "CORRECT!")
else:
  print(Fore.WHITE + "You didn't get the word in 6 guesses, try again!")
