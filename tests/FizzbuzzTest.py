import FizzBuzz

def test_divisible_by_3():
    assert FizzBuzz.divisible_by_3(3) == True

def test_divisible_by_5():
    assert FizzBuzz.divisible_by_5(5) == True

def test_divisible_by_number():
    assert FizzBuzz.divisible_by_number(5, 5) == True
    assert FizzBuzz.divisible_by_number(3, 3) == True

def test_not_divisible_by_number():
    assert FizzBuzz.divisible_by_number(5, 2) == False

def test_returns_fizz_for_divisible_by_3():
    assert FizzBuzz.check(3) == 'Fizz'

def test_returns_buzz_for_divisible_by_5():
    assert FizzBuzz.check(5) == 'Buzz'

def test_returns_number_for_non_3_or_5():
    assert FizzBuzz.check(17) == 17

def test_returns_fizzbuzz_for_divisible_by_3_and_5():
    assert FizzBuzz.check(15) == 'FizzBuzz'
