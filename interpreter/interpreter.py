def main():
    exp = input("Expression:")
    [ind, op] = find_operator(exp)
    if ind == -1:
        return
    operand1 = int(exp[0:ind])
    operand2 = int(exp[ind + 1:])
    #print(ind, op, operand1, operand2)
    result = operate(operand1, operand2, op)
    print(F"{result:.1f}")

def operate(operand1, operand2, operator):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            
            return operand1 * operand2
        case "/":
            return operand1 / operand2
def find_operator(exp):
    # without using loop!
    ind = exp.find("+")
    if ind != -1:
        return [ind, "+"]
    ind = exp.find("-")
    if ind != -1:
        return [ind, "-"]
    ind = exp.find("*")
    if ind != -1:
        return [ind, "*"]
    ind = exp.find("/")
    if ind != -1:
        return [ind, "/"]
    return [-1, ""]

main()






