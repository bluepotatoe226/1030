import calculator

operation = input("Would you like to add/subtract/multiple/divide: ")
first_input = float(input("Enter in first number: "))
second_input = float(input("Enter in second number: "))


if operation == "add":
            result = calculator.add(first_input, second_input)
elif operation == "subtract":
            result = calculator.subtract(first_input, second_input)
elif operation == "multiply":
            result = calculator.multiply(first_input, second_input)
elif operation == "divide":
            result = calculator.divide(first_input, second_input)
print(result)
