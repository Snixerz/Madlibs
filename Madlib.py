story_selector = {
  "1": "\033[1;32;40m The {noun} is very {adjective} and is going to {verb} \n",
  "2": "\033[1;32;40m The {adjective} {noun} went to {verb}\n",
  "3": "\033[1;32;40m At the top of the hill a {noun} was feeling {adjective} and decided to {verb}\n",
  "4": "\033[1;32;40m Inside the car a {noun} was {adjective} and insisted to {verb}\n",
  "5": "\033[1;32;40m After school the {noun} was {adjective} and decided to {verb}\n",
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
