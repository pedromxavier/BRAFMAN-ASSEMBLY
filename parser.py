from lexer import *;

import ply.yacc as yacc;

precedence = (

)

def p_start(p):
    """ start : code
    """
    print(p)

def p_code(p):
    """ code : code stmt
             | stmt
    """
    if len(p) == 3:
        p[0] = [*p[1], p[2]]
    else:
        p[0] = [ p[1],]

def p_stmt(p):
    """ stmt : CMD args
    """
    p[0] = p[1]

def p_args(p):
    """ args : arg COMMA arg
             | arg
    """
    if len(p) == 4:
        p[0] = (*p[1], p[3])
    else:
        p[0] = ( p[1],)

def p_arg(p):
    """ arg : literal
            | literal LPAR literal RPAR
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])

def p_error(p):
    print('Error: {}'.format(p))

parser = yacc.yacc()
