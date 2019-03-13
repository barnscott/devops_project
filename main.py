import time
#import sys
import os

#run at terminal in manuall debugging: export parg1='time'
#and remove env: unset parg1

#get my PyARG#1 from env
first_arg = os.environ.get('parg1')

#use this code IF passing as argument
# if len(sys.argv) == 2:
#     first_arg = sys.argv[1]
#     print("Length:%s" % (len(sys.argv)))
# else:
#     first_arg = 'not-here'

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