# My Class Register - www.101computing.net/my-class-register/

pupils = ["Joe", "Sonny", "Yassine", "Emma", "Ines", 
          "Satveer", "Lily", "Reuben", "Lucy", "Tom"]

present_counter = 0

for index, name in enumerate(pupils, start=1):
    print(f"{index}. {name}")
    present = input("Is this user present? (y or n): ").strip().lower()

    if present == "y":
        present_counter += 1
    elif present == "n":
        print(f"{name} is not present.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        break  # Exit if invalid input

# Final Summary
absent_counter = len(pupils) - present_counter
print("\n--- ------ ---")
print(f"Total Students: {len(pupils)}")
print(f"Present: {present_counter}")
print(f"Absent: {absent_counter}")
