import random
pistols = ["None", "Classic", "Shorty", "Frenzy", "Ghost", "Sheriff"]
guns = ["None", "Bucky", "Stinger", "Marshal", "Spectre", "Ares", "Judge", "Bulldog", "Guardian", "Phantom", "Vandal", "Odin", "Operator"]
sovaPool = ["a recon bolt", "a shock dart", "two shock darts", "an owl drone"]

# sova is Gay as Hell

def cheeseburger():
   q = input("Would you like a random ability as well? (Y/N) ").lower()
   if q == ("y"): 
      randSova = random.randint(0, len(sovaPool) - 1)
      print(f"Alright! You get {sovaPool[randSova]} to use!")   
   else: print(f"Alright, maybe next time!")
def randomizer():
   randPistol = random.randint(0, len(pistols) - 1)
   randGun = random.randint(0, len(guns) - 1)
   print(f"You have to use the {pistols[randPistol]} and the {guns[randGun]} for this round!")
   rerollask = input("Would you like to reroll? (Y/N) ").lower()
   if rerollask == ("y"): randomizer()
   else: cheeseburger()
randomizer()
print("Press enter to close.")
input()











   
   
