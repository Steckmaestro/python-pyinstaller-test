def add(oper1, oper2):
    if(type(oper1) == 'str' or type(oper2) == 'str'):
        return int(oper1) + int(oper2)
    else:
        return oper1 + oper2


def multiply(oper1, oper2):
    return oper1 * oper2
