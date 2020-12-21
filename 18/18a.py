data = open("input.txt").read().split("\n")


def evaluate_simple(expression):
    result = 0
    op = None

    for idx, char in enumerate(expression.split()):
        if char.isdigit():
            char = int(char)
            if op == "+":
                result += char
            elif op == "*":
                result *= char
            else:
                result = char
        else:
            op = char

    return result

def evaluate(expression):
    while True:
        left_bracket_idx = -1
        right_bracket_idx = -1
        for idx in range(len(expression)):

            if expression[idx] == ")":
                right_bracket_idx = idx
                simpl_epxression = expression[left_bracket_idx+1:right_bracket_idx]
                result = evaluate_simple(simpl_epxression)
                expression = expression.replace(f"({simpl_epxression})", str(result))
                break

            if expression[idx] == "(":
                left_bracket_idx = idx

        if left_bracket_idx == -1 and right_bracket_idx == -1:
            return evaluate_simple(expression)

print(sum([evaluate(line) for line in data]))
