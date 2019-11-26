from braf import compiler
from lexer import *;

import ply.yacc as yacc;

precedence = (
    ('left', 'HEX_A'),
    ('left', 'HEX_B'),
    ('left', 'DEC'),
    ('left', 'BIN_A'),
    ('left', 'BIN_B'),

    ('left', 'REG'),

    ('left', 'LPAR'),
    ('left', 'RPAR'),

    ('left', 'CMD'),
    ('left', 'COMMA'),

    ('left', 'NEWLINE'),
)

def p_start(p):
    """ start : code
              |
    """
    if len(p) == 2:
        print(compiler(p[1]))

def p_code(p):
    """ code : code stmt
             | stmt
    """
    if len(p) == 3:
        p[0] = [*p[1], p[2]]
    else:
        p[0] = [ p[1],]

def p_stmt(p):
    """ stmt : CMD args NEWLINE
             | CMD args
    """
    p[0] = (p[1], p[2])

def p_args(p):
    """ args : args COMMA arg
             | arg
    """
    if len(p) == 4:
        p[0] = (*p[1], p[3])
    else:
        p[0] = ( p[1],)

def p_arg(p):
    """ arg : literal LPAR literal RPAR
            | literal
    """
    if len(p) == 5:
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]


def p_literal(p):
    """ literal : HEX_A
                | HEX_B
                | DEC
                | BIN_A
                | BIN_B
                | REG
    """
    p[0] = p[1]

def p_error(p):
    print('YaccError: {}'.format(p))

parser = yacc.yacc()
