def divisible_by_3(number):
    return number % 3 == 0

def divisible_by_5(number):
    return number % 5 == 0

def divisible_by_number(number, divisor):
    return number % divisor == 0

def check(number):
    if divisible_by_number(number, 15) == True:
        return 'FizzBuzz'
    elif divisible_by_number(number, 3) == True:
        return 'Fizz'
    elif divisible_by_number(number, 5) == True:
        return 'Buzz'
    else:
        return number
