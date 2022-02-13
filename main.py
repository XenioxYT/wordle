from colorama import Fore
from random import choice

word_file = open("Words.txt","r")
words = word_file.readlines()

answer=choice(words)
answer=answer.upper()
answer = answer.rstrip()
word = ""
i = 0
while word != answer and i < 6:

  word = input(Fore.WHITE + "Input a word: ")
  if len(word) != 5:
    print("This word is invalid")
    continue

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
  
  i+= 1

print(Fore.WHITE + "CORRECT!")