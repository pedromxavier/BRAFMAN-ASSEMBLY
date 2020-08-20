import parser
import sys

argv = sys.argv
argc = len(argv)

if argc < 2:
    print('Missing source file')
    sys.exit(1)
else:
    with open(argv[1], 'r') as file:
        source = file.read()
        parser.parser.parse(source)
    ##sys.exit(0)
