import random
import json

with open("flashcards.json", "r") as f:
    flashcards_dict = json.load(f)
    flashcards = list (flashcards_dict.keys())

random.shuffle(flashcards)

for flashcard_key in flashcards:
  question = flashcard_key
  answer = flashcards_dict[flashcard_key]

  response = input(question)
  
  if response == answer:
      print("Correct")
  else:
      print("Incorrect")