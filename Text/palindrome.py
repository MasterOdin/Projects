# last update: 11/1/2013
# python version: 2.7.5

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python palindrome.py word"
        sys.exit(0)

    word = sys.argv[1]

    palindrome = False

    if len(word) % 2 == 0:
        mid = len(word)/2
        if word[0:mid] == word[mid:][::-1]:
            palindrome = True
    else:
        mid = len(word)/2
        if word[0:mid] == word[(mid+1):][::-1]:
            palindrome = True

    if palindrome == True:
        print "%s is a palindrome!" % (word)
    else:
        print "%s is not a palindrome!" % (word)