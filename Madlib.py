story_selector = {
  "1": "The {noun} is very {adjective} and is going to {verb}",
  "2": "The {adjective} {noun} went to {verb}",
  "3": "At the top of the hill a {noun} was feeling {adjective} and decided to {verb}",
  "4": "Inside the car a {noun} was {adjective} and insisted to {verb}",
  "5": "After school the {noun} was {adjective} and decided to {verb}",
}

number = input("Select a random story from numbers 1-5: ")
print(story_selector.get(number))
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("enter a verb: ")

if number == "1":
  print(f"The {noun} is very {adjective} and is going to {verb}")
elif number == "2":
  print(f"The {adjective} {noun} went to {verb}")
elif number == "3":
  print(f"At the top of the hill a {noun} was feeling {adjective} and decided to {verb}")
elif number == "4":
  print(f"Inside the car a {noun} was {adjective} and insisted to {verb}")
elif number == "5":
  print(f"After school the {noun} was {adjective} and decided to {verb}")
else:
  print("You did not select a correct number, try again.")
