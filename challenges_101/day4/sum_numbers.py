


def digit_sum2(number):
    # breakpoint()
    sum = 0
    while number > 0:
        print("number now is: ", number)
        lastdigit = number % 10
        print("lastdigit: ", lastdigit)
        sum = sum + lastdigit
        print("sum updated: ",sum)
        number = number // 10
        print("remainder: ", number)
        

    return sum
    

def digit_sum(number):
    return sum(int(digit) for digit in str(number))


def test_digit_sum(number):

    assert digit_sum2(number) == 14
    assert digit_sum2(number) == 6
    assert digit_sum2(number) == 19
    assert digit_sum2(number) == 21
    assert digit_sum2(number) == 7

    # Test the digit_sum function    
    assert digit_sum(365) == 14
    

    

    
if __name__ == "__main__":
    number = input("Enter a number: ")
    test_digit_sum(int(number))