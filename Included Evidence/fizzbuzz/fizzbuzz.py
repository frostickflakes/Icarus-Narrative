number_given = input('What is the given number?: ')
def fizz_buzz(input):
        if (input % 3 == 0) and (input % 5 == 0):
            return "FizzBuzz"
        if input % 3 == 0:
            return "Fizz"
        if input % 5 == 0:
            return "Buzz"
        return input
print(fizz_buzz(int(number_given)))