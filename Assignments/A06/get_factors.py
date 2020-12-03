#  NAME:        Semeion Stafford
#  REPO:        4663 Cyptography
#  EMAIL:       semeionsta@hotmail.com
#  ASSIGNMENT:  A06
#  WEBSITE:     https://repl.it/@SemeionStafford/A06#get_factors.py

import sys
import math
import pprint as pp

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}
        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key, val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args, kargs


def eratosthenes(n):
    multiples = []
    result = []
    for i in range(2, n+1):
        if i not in multiples:
            #print (i)
            result.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return result


def main(args, **kwargs):

    f = open(args[0])

    j = 1
    for num in f:

        factors = []
        num = int(num)
        orig = num

        while num % 2 == 0:
            factors.append(2)
            num = num / 2

        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                factors.append(i)
                num = num / i

        if num > 2:
            factors.append(num)

        if(len(factors) != 1):
            print("Number " + str(j) + ": " + str(orig) + " = " +
                  (str(factors)).strip("[]").replace(",", " *"))
        else:
            print("Number " + str(j) + ": " +
                  str(factors[0]).strip("[]") + " - Prime")
        j += 1


def usage(message=None):
    if message:
        print(message)
    print("Usage: python skeleton.py [key1=string]")
    print("Example:\n\t python get_factors.py input_file=numbers")
    sys.exit()


if __name__ == '__main__':

    required_params = 1
    argv = sys.argv[1:]

    if len(argv) < required_params:
        usage()

    #   get processed command line args
    args, kwargs = mykwargs(argv)

    #   send all to main
    main(args, **kwargs)
