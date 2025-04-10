import math_utils


def main():
    num1 = int(input('Please enter your first number'))
    num2 = int(input('Please enter your second number'))
    operator = input('Please enter your operator (+, -, *, /, ** or %)')

    ops = {
                '+': math_utils.add,
                '-': math_utils.subtract,
                '*': math_utils.multiply,
                '/': math_utils.divide,
                '**': math_utils.power,
                '%': math_utils.mod
            }

    if operator in ops:
        result = ops[operator](num1,num2)
        print("Result: ", result)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
