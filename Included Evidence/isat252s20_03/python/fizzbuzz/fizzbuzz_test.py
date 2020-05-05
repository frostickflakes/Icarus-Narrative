# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz, buzz, fibu, play

#import the method needed to test for exceptions
from pytest import raises

def describe_a_fizzbuzz_program_that():
  """A program to play the FizzBuzz game."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def describes_a_fizz_function_that():
    """Tests for the fizz() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as err_info:
        fizz() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def returns_fizz_if_a_number_is_a_multiple_of_3():
      """
        Takes an input `x` and checks to see if it is a
        number, and if so, also a multiple of 3.
        If it is both, return 'Fizz'.
        Otherwise, return the input.
      """
      assert fizz(3) == 'Fizz'      # multiple of 3
      assert fizz(2) == 2           # non-multiple of 3
      assert fizz(3.5) == 3.5       # non-integer
      assert fizz(0) == 'Fizz'      # zero
      assert fizz(-3) == 'Fizz'     # negative multiple of 3
      assert fizz(-4) == -4         # negative non-multiple of 3
      assert fizz('Buzz') == 'Buzz' # non-numeric input

  def describes_a_buzz_function_that():
    """Tests for the buzz() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as err_info:
        buzz() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def returns_buzz_if_a_number_is_a_multiple_of_5():
      """
        Takes an input `x` and checks to see if it is a
        number, and if so, also a multiple of 5.
        If it is both, return 'Buzz'.
        Otherwise, return the input.
      """
      assert buzz(5) == 'Buzz'      # multiple of 5
      assert buzz(2) == 2           # non-multiple of 5
      assert buzz(5.5) == 5.5       # non-integer
      assert buzz(0) == 'Buzz'      # zero
      assert buzz(-5) == 'Buzz'     # negative multiple of 5
      assert buzz(-4) == -4         # negative non-multiple of 5
      assert buzz('Fizz') == 'Fizz' # non-numeric input

  def describes_a_fibu_function_that():
    """Tests for the fibu() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as err_info:
        fibu() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def returns_fizzbuzz_if_a_number_is_a_multiple_of_15():
      """
        Takes an input `x` and checks to see if it is a
        number, and if so, also a multiple of 15.
        If it is both, return 'FizzBuzz'.
        Otherwise, return the input.
      """
      assert fibu(15) == 'FizzBuzz'  # multiple of 15
      assert fibu(2) == 2            # non-multiple of 15
      assert fibu(5.5) == 5.5        # non-integer
      assert fibu(0) == 'FizzBuzz'   # zero
      assert fibu(-15) == 'FizzBuzz' # negative multiple of 15
      assert fibu(-4) == -4          # negative non-multiple of 15
      assert fibu('Fizz') == 'Fizz'  # non-numeric input

  def plays_FizzBuzz():
    assert play(1,15) == [
      1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'
    ]
    assert play(5,25) == [
      'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19,
      'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz'
    ]
