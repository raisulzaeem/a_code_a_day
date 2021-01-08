def invalid_parentheses(my_str):
    while True:
        if "()" in my_str:
            my_str = my_str.replacce("()","")
        else:
            break

    num_invalid_parentheses = len(my_str)
    
    return num_invalid_parentheses


if __name__ == "__main__":
    input_string = "()()()()()())((()())())()()"

    result = invalid_parentheses(input_string)