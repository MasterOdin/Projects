# last update: 11/1/2013
# python version: 2.7.5

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: vowel_count.py string"
        sys.exit(0)

    vowels = "aeiou"
    string = sys.argv[1]
    for v in vowels:
        print "%s: %d" % (v,string.count(v))
