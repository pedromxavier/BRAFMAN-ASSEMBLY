from ply import lex

tokens = {
    'COMMA',

    'LPAR',
    'RPAR',

    'HEX',
    'DEC',
    'BIN',

    'REG',

    'CMD',
}

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_COMMA = r'\,'

t_LPAR = r'\('
t_RPAR = r'\)'

def t_HEX(t):
    r'[0-9a-fA-F]+[hH]|0[xX][0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t

def t_DEC(t):
    r'[0-9]+'
    t.value = int(t.value, 10)
    return t

def t_BIN(t):
    r'[01]+[bB]|0[bB][01]+'
    t.value = int(t.value, 2)
    return t

def t_REG(t):
    r'[rR][0-9]+'
    t.value = int(t.value[1:], 10)
    return t

def t_CMD(t):
    r"[a-zA-Z_][a-zA-Z]*"
    t.value = str(t.value).upper()
    return t

def t_error(t):
    print('Error: {}'.format(t))


t_ignore = " \t"

t_ignore_COMMENT = r'\;.*'

lexer = lex.lex()
