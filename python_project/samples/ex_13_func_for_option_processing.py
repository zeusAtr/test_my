import sys
import os
import re
 
def parse_options(*args):
    '''
    Parse options and make list of parsed options
    available to program
    '''
    args = args[0]
 
    options = {}
    get_value = lambda a,x: a[a.index(x)+1]
    is_option = lambda x: x.startswith("--")
    is_next_value = lambda x: not x.startswith("--")
 
    if args:
        for option in args:
            try:
                if is_option(option) and is_next_value(get_value(args,option)):
                    options[option[2:]] = get_value(args,option)
            except IndexError:
                continue
 
    return options
 
def main():
    args = parse_options(sys.argv[1:])
    print args
 
if __name__ == "__main__":
    main()