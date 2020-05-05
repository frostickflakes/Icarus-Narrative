"""A FizzBuzz program"""

# import necessary supporting libraries or packages
from numbers import Number

def fizz(x):
  """
    Takes an input `x` and checks to see if x is a
    number, and if so, also a multiple of 3.
    If it is both, return 'Fizz'.
    Otherwise, return the input.
  """
  return 'Fizz' if isinstance(x, Number) and x % 3 == 0 else x

def buzz(x):
  """
    Takes an input `x` and checks to see if x is a
    number, and if so, also a multiple of 5.
    If it is both, return 'Buzz'.
    Otherwise, return the input.
  """
  return 'Buzz' if isinstance(x, Number) and x % 5 == 0 else x

def fibu(x):
  """
    Takes an input `x` and checks to see if x is a
    number, and if so, also a multiple of 15.
    If it is both, return 'FizzBuzz'.
    Otherwise, return the input.
  """
  return 'FizzBuzz' if isinstance(x, Number) and x % 15 == 0 else x

def play(start, end):
  """
    Given a start number and an end number, produce
    all of the output expected for a game of FizzBuzz
    as an array.
  """
  # initialize an empty list (array) to hold our output
  output = []
  # loop from the start number to the end number
  for x in range(start, end + 1):
    # append the tranformed input to the output array
    output.append(buzz(fizz(fibu(x))))
  return output
