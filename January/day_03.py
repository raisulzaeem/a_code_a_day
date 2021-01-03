import argparse

def get_combination(input_str):
    mapping_dict = {"1": ["."],"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"], "6":["m","n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9":["w", "x", "y", "z"], "0": [" "]}

    digit = int(input_str) # To make sure a valid digit is entered
    input_str_list = [i for i in  input_str]

    list_output = [""]

    for char in input_str_list:
        list_output = concat(list_output, mapping_dict[char])

    return list_output

def concat(a, b):
    return [i+j for i in a for j in b]


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--input',type=str, default="2441139",help='Input digit string')
    args=parser.parse_args()

    in_str = args.input

    result = get_combination(in_str)

    print(result)



