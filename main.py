from pyscript import display, document

def adding_numbers(e):

    number1 = int(document.getElementById('num1').value)
    number2 = int(document.getElementById('num2').value)

    add = number1 + number2
    sub = number1 - number2
    mul = number1 * number2
    div = number1 / number2

    document.getElementById('result').innerHTML = ""

    display(f"""
    <h3>Results</h3>

    Addition: {add}<br>
    Subtraction: {sub}<br>
    Multiplication: {mul}<br>
    Division: {div}
    """, target='result')
