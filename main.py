result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        try:
            operand = input()
            operand = int(operand)
        except ValueError:
            print(f"{operand} is not a number. Try again.")
            continue
        wait_for_number = False
        if result is None:
            result = operand
        elif operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '/':
            result /= operand
        elif operator == '*':
            result *= operand

    if not wait_for_number:
        operator = input()
        if operator == '-' or operator == '+' or operator == '/' or operator == '*':
            wait_for_number = True
        elif operator == '=':
            print(f"Result: {result}")
            break
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
            continue
