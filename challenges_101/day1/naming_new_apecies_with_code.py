#The Explorer's Challenge - www.101computing.net/the-explorer-challenge

from stringhandling import *
import random

def generate_animals_name(animalA, animalB):

   left_rand_A_1 = random.randint(1, len(animalA)//2)
   
   subs_rand_A_2_start, subs_rand_A_2_end = (
      random.randint(0, len(animalB)//2), 
      random.randint(2, len(animalB)//2),
   )
   right_rand_A_1 = random.randint(1, len(animalA)//2)

   part1 = left(animalA, left_rand_A_1)
   part2 = substr(animalB, subs_rand_A_2_start, subs_rand_A_2_end)
   part3 = right(animalA, right_rand_A_1)

   return (part1 + part2 + part3).title()

def main():
    
    animalA = input("Enter the first animal name: ").lower()
    animalB = input("Enter the second animal name: ").lower()
    
    while True:
      
        exotic_name = generate_animals_name(animalA, animalB)
      
        print("\nSuggested name:       ", exotic_name)
        print("Number of characters: ", length(exotic_name))

        user_response = input("Do you like this name? (yes/no): ").strip().lower()
        
        if user_response == "yes":
            print("Your new species name is:", exotic_name)
            break
        else:
            print("Let's try another one!\n")

if __name__ == "__main__":
    main()
