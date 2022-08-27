# from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  # print(logo)
  
  num1 = float(input("Enter the first number: "))
  for symbol in operations:
    print(symbol)
  
  keep_running = True
  while keep_running is True:
    operation_symbol = input("Choose an operation: ")
    next_num = float(input("Enter the second number: "))
    
    calculate = operations[operation_symbol]
    answer = calculate(num1, next_num)
    print(f"{num1} {operation_symbol} {next_num} = {answer}")
    
    again = input(f"Type 'y' to continue calculating with {answer}, type 'n' to reset the calculator: ").lower()
    if again == 'y':
      num1 = answer
    else:
      keep_running = False
      calculator()  # Recursion, a function that calls itself. Beware of infinite loop. 


calculator()