# last update: 11/1/2013
# python version: 2.7.5

import sys,string

'''
    Way to reverse string:
        1) Simple for loop
        2) List splicing
        3) List comprehension (and string joining)
'''
TYPE = 3

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: reverse.py string_to_reverse"
        sys.exit(0)

    str_to_rev = sys.argv[1]
    if TYPE == 1:
        output = ""
        for i in range(len(str_to_rev)):
            output += str_to_rev[len(str_to_rev)-1-i]
        print output
    elif TYPE == 2:
        print str_to_rev[::-1]
    elif TYPE == 3:
        print string.join([str_to_rev[x] for x in range((len(str_to_rev)-1),-1,-1)],"")
    else:
        print "Invalid type"