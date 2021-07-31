#Calculator

#Add
def add(n1,n2):
  return n1 + n2

#sub
def sub(n1,n2):
  return n1 - n2

#Mult
def multi(n1,n2):
  return n1 * n2

#div
def div(n1,n2):
  return n1 / n2

operations = {
  '+':add,
  '-':sub,
  '*':multi,
  '/':div,
}

num1 = int(input("What's the first number? "))

for sign in operations:
  print(sign)
operation_sign = input('Pick an operation from the line above ')
num2 = int(input("What's the second number? "))

calculation_function = operations[operation_sign]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_sign} {num2} = {answer}")