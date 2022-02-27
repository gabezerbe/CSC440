import lexer
import parser
import sys

from sys import argv

if __name__ == '__main__':
    filename = argv[1]
    file = open(filename)
    code = file.read()

    lexer.lexer.input(code)
    
    while True:
        tok = lexer.lexer.token()
        if not tok:
            break

    if lexer.num_errors > 0:
        sys.exit()

    parser.num_lines = lexer.lexer.lineno - 1

    result = parser.parser.parse(code, lexer.lexer, tracking = True)

    if parser.num_errors > 0:
        sys.exit()
