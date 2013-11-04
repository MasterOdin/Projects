# last update: 11/4/2013
# python version: 2.7.5

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage:",sys.argv[0]," n"
        sys.exit(0)

    try:
        n = int(sys.argv[1])
        if n < 1:
            raise ValueError("negative number")
    except ValueError:
        print "ValueError: n must be a valid integer greater than 1"
        exit(0)

    steps = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3+1
        steps += 1

    print "Steps taken to reach 1:",steps

