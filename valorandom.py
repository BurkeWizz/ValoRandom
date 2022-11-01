import random
import functools

pistols = [
   "None", "Classic", "Shorty", "Frenzy", "Ghost", "Sheriff"
]
guns = [
   "None", "Bucky", "Stinger", "Marshal", "Spectre", "Ares", "Judge", "Bulldog", "Guardian", "Phantom", "Vandal", "Odin", "Operator"
]

abilities = [
   "no abilities", "one ability", "two abilities", "three abilities", "all abilities"
]


randPistol = random.randint(0, len(pistols) - 1)
randGun = random.randint(0, len(guns) - 1)
print(f"You have to use the {pistols[randPistol]} and the {guns[randGun]} for this round!")

question = input("Would you like a random ability as well? (Y/N) ")
if question == ("Y", "y"): 
   randAbil = random.randint(0, len(abilities) - 1)
   print(f"Alright! You get {abilities[randAbil]} to use!")
else:
   print(f"Alright, maybe next time!")













