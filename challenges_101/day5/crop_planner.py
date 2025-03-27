#The Allotment Crop Planner - www.101computing.net/allotment-crop-planner
import json
 
def whatToPlantThisMonth():
   print()
   print(" --- What to plant this month ---")
   print()
   month = input("Enter a month of the year: (e.g. April) ").title()
   # load JSON data from file
   with open('/opt/services/challenges_101/challenges_101/day8/data/crop.json','r') as file:
      data = json.load(file)

   # print(data.)
   # Perform a linear search using the JSON data
   crops = data.get("crops") #["crops"]
   print("In " + month + ", you can plant the following crops:")

   for crop in crops:
      if month in crop.get("planting_season"):
         print(" > " + crop.get("name"))
     
def cropToHArvestThisMonth():
   print()
   print(" --- What to harvest this month ---")
   print()
   month = input("Enter a month of the year: (e.g. April) ").title()
   # load JSON data from file
   with open('/opt/services/challenges_101/challenges_101/day8/data/crop.json','r') as file:
      data = json.load(file)

   crops = data.get("crops") #["crops"]
   print("In " + month + ", you can crops to harvest this month:")

   for crop in crops:
      if month in crop.get("harvest_season"):
         print(" > " + crop.get("name"))
         
         
         

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
   cropToHArvestThisMonth()
elif option=="3":
   print("This option is not available yet!")
elif option=="4":
   print("This option is not available yet!")
elif option=="5":
   print("This option is not available yet!")
