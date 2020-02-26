# écriture postfixée 

def is_operation(char):
    if char == "+" or char == "-" or char == "*":
        return True
    else:
        return False

def exec_operation(a,b,op):
    if op == "+":
        return (a+b)
    elif op == "-":
        return (a-b)
    elif op == "*":
        return (a*b)
    else:
        print("uniquement + , - , * autorisés")
        return 

def postfixee(l):
    