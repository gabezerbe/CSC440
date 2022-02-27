import ply.lex as lex

num_errors = 0;

reserved = {
    'and'   :   'AND',
    'do'    :   'DO',
    'else'  :   'ELSE',
    'while' :   'WHILE',
    'for'   :   'FOR',
    'then'  :   'THEN',
    'end'   :   'END',
    'if'    :   'IF',
    'var'   :   'VAR',
    'or'    :   'OR',
    'not'   :   'NOT',
    'in'    :   'IN'
}

tokens = [
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUAL', 'NOTEQUAL', 'LESSEQUAL',
    'GREATEREQUAL', 'LESS', 'GREATER', 'ASSIGN', 'LPAREN', 'RPAREN', 'SEMICOLON', 'COMMA',
    'STRING'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'=='
t_NOTEQUAL = r'~='
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_LESS = r'<'
t_GREATER = r'>'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','

def t_ID(token):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    token.type = reserved.get(token.value, 'ID')
    return token

def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_STRING(token):
    r'"([^"\n]|(\\))*"$'
    token.type = reserved.get(token.value, 'STRING')
    return token

t_ignore = ' \t\r\n'

def t_NUMBER(token):
    r'\d+'
    token.value = int(token.value)
    return token

def t_error(token):
    global num_errors
    print("Illegal Character '%s' at line: %d" % (token.value[0], token.lexer.lineno))
    num_errors += 1
    token.lexer.skip(1)

lexer = lex.lex()

# from sys import argv

# with open(argv[1]) as file:
#     while line := file.readline():
#         print(f"line: {line}", end="")
#         lexer.input(line)
#         while True:
#             tok = lexer.token()
#             if not tok:
#                 break
#             print(f"    {tok}")

