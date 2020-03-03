#!/usr/bin/env python3.8

def three(arg1):

    if arg1 % 3 == 0:
	    return "fizz"
    elif arg1 % 5 == 0:
	    return "buzz"
    elif (arg1 % 3 == 0) and (arg % 5 == 0):
	    return "fizzbuzz"
    else:
        return "null"