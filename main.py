import time
import sys

if len(sys.argv) == 2:
    first_arg = sys.argv[1]
    print("Length:%s" % (len(sys.argv)))
else:
    first_arg = 'not-here'

def main(arg1=first_arg):

    rtime = time.strftime("%Y/%m/%d %H:%M:%S")

    if arg1 == 'time':
        print("The time is:%s. Wow, great machine learning." % (rtime))
    elif arg1 == 'not-here':
        print("You need to prove exactly one argument.")
    else:
        print("Additional machine learning coming soon.")

if __name__ == '__main__':
    main()