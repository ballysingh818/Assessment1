
def one(input1, input2):

	a = input1,input2.split("")
	return max(a, key=len)


def two(input):
	return ""


def three(arg1):

	if arg1 % 3 == 0:
		return "fizz"
	elif arg1 % 5 == 0:
		return "buzz"
	elif (arg1 % 3 == 0) and (arg1 % 5 == 0):
		return "fizzbuzz"
	else:
		return "null"

def four(arg1):
	return 0


def five(input):
	return []


def six(input):

	vowels=0
		
	for i in input:
    	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
			
		return vowels


def seven(input):
    return 0

def eight(input):
	return 1


def nine(inputString, char):
	return -1


def ten(string, int, char):
	return False
