"""
  An example of a procedural style FizzBuzz program.
  For coding interviews, this is okay, but in general,
  I do NOT recommend this approach to coding as it is
  nearly impossible to test its correctness.
"""
for x in range(1, 101):
  if x % 15 is 0:
    print("FizzBuzz")
  elif x % 3 is 0:
    print("Fizz")
  elif x % 5 is 0:
    print("Buzz")
  else:
    print(x)
