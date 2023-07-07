from .stack import Stack


def is_match(paren1, paren2):
    if paren1 == "(" and paren2 == ")":
        return True
    elif paren1 == "{" and paren2 == "}":
        return True
    elif paren1 == "[" and paren2 == "]":
        return True
    else:
        return False


# Checking if Brackets are Balanced
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index = index + 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str(i))

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


if __name__ == "__main__":
    # myStack = Stack()
    # myStack.push("A")
    # myStack.push("B")
    # myStack.push("C")
    # myStack.push("D")
    # myStack.push("E")
    # print(myStack.peek())

    # print("String : (((({})))) Balanced or not?")
    # print(is_paren_balanced("(((({}))))"))

    # print("String : [][]]] Balanced or not?")
    # print(is_paren_balanced("[][]]]"))

    # print("String : [][] Balanced or not?")
    # print(is_paren_balanced("[][]"))

    # input_str = "Educative"
    # print(input_str[::-1])

    stack = Stack()
    input_str = "!evitacudE ot emocleW"
    print(reverse_string(stack, input_str))
