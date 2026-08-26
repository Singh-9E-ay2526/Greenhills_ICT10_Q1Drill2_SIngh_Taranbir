# Working with Numbers
from numbers import Number

from pyscript import display, document


def greetings(e):  # creating function
    username = document.getElementById('input1').value  # getting a value from a textbox
    display(f'Hello {username}!', target='result')

    def adding_numbers(e):
        number1 = int(document.getElementById('num1').value)
        number2 = int(document.getElementById('num2').value)
        sum = number1 + number2

        display(f'the sum of {number1} and {number2} is {sum}', target='result')