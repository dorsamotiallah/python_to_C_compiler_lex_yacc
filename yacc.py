# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens


def p_e(p):
    'e : stmts '
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUM'
    p[0] = str(p[1])


def p_factor_id(p):
    'factor : ID'
    p[0] = str(p[1])


def p_factor_expr(p):
    'factor : LPR expr RPR'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_expon_factor(p):
    'expon : factor'
    p[0] = p[1]


def p_term_mult(p):
    'term : term MULT expon'
    p[0] = p[1] + p[2] + p[3]


def p_term_div(p):
    'term : term DIVIDE expon'
    p[0] = p[1] + p[2] + p[3]


def p_term_rem(p):
    'term : term REMAINDER expon'
    p[0] = p[1] + p[2] + p[3]


def p_term_expon(p):
    'term : expon'
    p[0] = p[1]


def p_expr_add(p):
    'expr : expr ADD term'
    p[0] = p[1] + p[2] + p[3]


def p_expr_sub(p):
    'expr : expr SUB term'
    p[0] = p[1] + p[2] + p[3]


def p_expr_term(p):
    'expr : term '
    p[0] = p[1]


def p_assign(p):
    'assign : ID ASSIGN expr'
    p[0] = p[1] + p[2] + p[3]


def p_condition_expr(p):
    'condition : expr RELOP expr'
    p[0] = p[1] + p[2] + p[3]


def p_condition(p):
    'condition : expr'
    p[0] = p[1]


def p_range_2(p):
    'range : expr COM expr'
    p[0] = [p[1], p[3]]


def p_range(p):
    'range : expr'
    p[0] = [p[1]]


def p_statment_if(p):
    'stmt : IF condition CLN LBRC stmts RBRC'
    p[0] = str(p[1]) + "(" + str(p[2]) + ")" + str(p[4]) +"\n"+ str(p[5]) + str(p[6])


def p_statment_if_else(p):
    'stmt : IF condition CLN LBRC stmts RBRC ELSE CLN LBRC stmts RBRC'
    p[0] = p[1] + "(" + p[2] + ")" + p[4] + p[5] + p[6]+"\n" + p[7] + p[9] + p[10] + p[11]


def p_statment_while(p):
    'stmt : WHILE condition CLN LBRC stmts RBRC'
    p[0] = p[1] + "(" + p[2] + ")" + p[4]+"\n" + p[5] + p[6]


def p_statment_for(p):
    'stmt : FOR ID IN RANGE LPR range RPR CLN LBRC stmts RBRC'
    if len(p[6]) == 1:
        p[0] = p[1] + "(" + p[2] + "= 0 ; " + p[2] + "<" + p[6][0] + ";" + p[2] + "++" + ")" + p[9]+"\n" + p[10] + p[11]
    else:
        p[0] = p[1] + "(" + p[2] + "= " + p[6][0] + " ; " + p[2] + "<" + p[6][1] + ";" + p[2] + "++" + ")" + p[9]+"\n" + p[
            10] + p[11]


def p_statment_expr(p):
    'stmt : expr'
    p[0] = p[1] + ";\n"


def p_statment_assign(p):
    'stmt : assign'
    p[0] = p[1] + ";\n"


def p_statments_stmt(p):
    'stmts : stmt stmts'
    p[0] = str(p[1]) + str(p[2])


def p_statments(p):
    'stmts : '
    p[0] = ""


# Error rule for syntax errors
def p_error(p):
    print("Syntax error!")


# Build the parser
parser = yacc.yacc()
f = open("p.txt", "r")
s = f.read()
result = parser.parse(s)
print(result)
f = open("c.txt", "w")
f.write(result)
f.close()
