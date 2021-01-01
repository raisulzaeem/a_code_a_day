"""
Problem Statement: 

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""

import argparse

def arg_parse():
    parser=argparse.ArgumentParser()
    parser.add_argument('-l','--list',type=str, default="[10,15,3,7]",help='Input list of numbers')
    parser.add_argument('-k','--number_k',type=int,default=17,help='The number to comapare the addition')
    args=parser.parse_args()
    return args

def check_k(num_list, k):

    sorted_list = sorted(num_list)
    i = 0
    j = len(num_list) - 1
    ret_bool = False

    while i<j:
        sum_ij = sorted_list[i] + sorted_list[j]
        if sum_ij < k:
            i+=1
            continue
        elif sum_ij > k:
            j-=1
            continue
        elif sum_ij == k:
            ret_bool = True
            break
        else:
            raise Exception("This was not supposed to be executed.")
    return ret_bool


if __name__ == "__main__":
    
    args = arg_parse()
    my_list = eval(args.list)
    my_number = args.number_k

    result = check_k(my_list, my_number)
    print(result)