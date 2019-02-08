import FizzBuzz

def test_divisible_by_3():
    assert FizzBuzz.divisible_by_3(3) == True

def test_divisible_by_5():
    assert FizzBuzz.divisible_by_5(5) == True

def test_divisible_by_number():
    assert FizzBuzz.divisible_by_number(5, 5) == True
    assert FizzBuzz.divisible_by_number(3, 3) == True
