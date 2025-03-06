"""
 Ask the farmer to enter how many eggs they have picked up this morning.
 Work out how many boxes of 12 eggs will be needed today.
 Work out if the farmer will also need a box of 6.
 Finally let the farmer know how many eggs they will have left to cook for breakfast.
"""

def pick_morning_eggs(eggs_picked):
    eggs_in_a_box = 12
    eggs_in_a_box2 = 6

    boxes_needed = eggs_picked // eggs_in_a_box
    eggs_left = eggs_picked % eggs_in_a_box
    
    boxes_needed2 = eggs_left // eggs_in_a_box2
    eggs_left2 = eggs_left % eggs_in_a_box2

    return boxes_needed, boxes_needed2, eggs_left2

def test_pick_morning_eggs():
    test_cases = [
        (128, (10, 1, 2)),
        (149, (12, 0, 5)),
        (105, (8, 1, 3)),
    ]

    for eggs_picked, expected in test_cases:
        result = pick_morning_eggs(eggs_picked)
        assert result == expected, f"Test failed for {eggs_picked} eggs: expected {expected}, got {result}"
    print("All tests passed.")

def main():
    # eggs_picked = int(input("How many eggs have you picked up this morning? "))
    # boxes_12, boxes_6, eggs_left = pick_morning_eggs(eggs_picked)

    # print(f"You will need {boxes_12} boxes of 12 eggs.")
    # print(f"You will need {boxes_6} boxes of 6 eggs.")
    # print(f"You will have {eggs_left} eggs left to cook for breakfast.")
    test_pick_morning_eggs()
    
if __name__ == "__main__":
    
    main()
