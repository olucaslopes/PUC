def is_wffr(formula):
    if formula == '': return False
    if formula[0] == '¬': return is_wffr(formula[1:])
    if formula[0] == '(':
        if formula[-1] != ')': return False
        count = 1
        index = -1
        for i in range(1, len(formula) - 1):
            if formula[i] == '*' and count == 1:
                index = i
                break
            elif formula[i] == '(':
                count += 1
            elif formula[i] == ')':
                count -= 1
        return index > 0 and is_wffr(formula[1:index]) and is_wffr(formula[index + 1:-1])
    return not "(" in formula and not ")" in formula and not "*" in formula


def is_wff(formula):
    list_op = ["∧", "∨", "≡", "⊃"]
    for op in list_op: formula = formula.replace(op, "*")
    formula = formula.replace(" ", "")
    return is_wffr(formula)