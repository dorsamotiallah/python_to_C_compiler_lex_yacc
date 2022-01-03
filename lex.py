import ply.lex as lex

tokens = [
    'NUM',
    'ADD',
    'SUB',
    'MULT',
    'DIVIDE',
    'REMAINDER',
    'LPR',
    'RPR',
    'COM',
    'ID',
    'ASSIGN',
    'LBRC',
    'RBRC',
    'RELOP'

]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE',
    ':': 'CLN'
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_ADD = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIVIDE = r'/'
t_REMAINDER = r'%'
t_LPR = r'\('
t_RPR = r'\)'
t_LBRC = r'{'
t_RBRC = r'}'
t_COM = r','


# IDs
def t_ID(t):
    r':|[_a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_RELOP(t):
    r'<|<=|!=|>|>=|=='
    t.type = reserved.get(t.value, 'RELOP')  # Check for reserved words
    return t


def t_ASSIGN(t):
    r'\+=|-=|\*=|/=|=|%='
    t.type = reserved.get(t.value, 'ASSIGN')  # Check for reserved words
    return t


# A regular expression rule with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Character not expected '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
