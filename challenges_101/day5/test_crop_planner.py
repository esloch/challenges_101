#The Allotment Crop Planner - www.101computing.net/allotment-crop-planner
import json
 
def whatToPlantThisMonth():
   print(" --- What to plant this month ---")
   month = input("Enter a month of the year: (e.g. April) ").title()
   # load JSON data from file
   with open('/opt/services/challenges_101/challenges_101/day5/data/crop.json','r') as file:
      data = json.load(file)

   print("In " + month + ", you can plant the following crops:")   
   # Perform a linear search using the JSON data
   crops = data["crops"]
   for crop in crops:
      if month in crop["planting_season"]:
         print(" > " + crop["name"])

def whatToharvestThisMonth():
   print(" --- What to harvest this month ---")
   month = input("Enter a month of the year: (e.g. April) ").title()

   with open('/opt/services/challenges_101/challenges_101/day5/data/crop.json','r') as file:
      data = json.load(file)

   print("In " + month + ", you can harvest the following crops:")   
   crops = data["crops"]
#    breakpoint()
   for crop in crops:
      if month in crop["harvest_season"]:
         print(" > " + crop["name"])


def listCropsToPot():
    print(" --- Container-Friendly Crops ---")

    with open('/opt/services/challenges_101/challenges_101/day5/data/crop.json','r') as file:
        data = json.load(file)

    crops = data["crops"]
    for crop in crops:
        
        if crop["container_friendly"]:
            print(" > " + crop["name"])


def bestCropsForYourGarden():

    # soil_type = input("Enter your soil type: (e.g. Rich, well-drained) ").title()
    sunlight = input("Enter your sunlight condition (Full sun/Partial shade): (e.g. Full sun) ").title()

    with open('/opt/services/challenges_101/challenges_101/day5/data/crop.json','r') as file:
        data = json.load(file)

    crops = data["crops"]
    for crop in crops:
        breakpoint()
        if sunlight in crop["sunlight"]:
            print(" > " + crop["name"])
        # if crop["container_friendly"]:
        #     print(" > " + crop["name"])



### Main Code Starts Here ###
print("##############################")
print("#         Allotment          #")
print("#     Crop Planner v1.01     #")
print("##############################")
print("")
print(" >>> Menu Options:")
print("  > Option 1: Find out what you can plant on a specific month of the year")
print("  > Option 2: Find out what you can harvest on a specific month of the year")
print("  > Option 3: Find out a list of crops that you can grow in a pot (container friendly crops)")
print("  > Option 4: Find out what crops to plant in your garden based on soil type and sunlight conditions")
print("  > Option 5: Find out all the information to grow a specific crop")
option = input("Enter your option (1 to 5):")
while option not in (["1","2","3","4","5"]):
   print(" > Invalid option, try again...")
   option = input(" > Enter your option (1 to 5):")

if option=="1":   
    whatToPlantThisMonth()
elif option=="2":   
    whatToharvestThisMonth()
elif option=="3":
    listCropsToPot()
elif option=="4":
    bestCropsForYourGarden()
elif option=="5":
    print("This option is not available yet!")
