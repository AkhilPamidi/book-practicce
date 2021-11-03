def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiplication(n1,n2):
  return n1*n2
def division(n1,n2):
  return n1/n2
operators={
  "+":add,
  "-":subtract,
  "*":multiplication,
  "/":division,
}
again=True
num1=float(input("give the number perform the calculation  "))
for symbols in operators:
    print(symbols)
operation=input("type one of the operation from the above to perform the action  ")
num2=float(input("give other number to perform the operation  "))
while again:
  answer=round(operators[operation](num1,num2),2)
  print(f"{num1}{operation}{num2}={answer}")
  
  if input("if you want to continue type 'y' else type 'n'" ).lower()=="y":
    operation=input("type one of the operation from the above to perform the action  ")
    num1=answer
    num2=float(input("give other number to perform the operation  "))
  else:
    again=False
    
