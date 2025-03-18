# listas_analex.py
# 2023-03-21 by jcr
# ----------------------
import ply.lex as lex

tokens = ('NUM', 'PLUS', 'MINUS', 'TIMES')


t_PLUS  = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()
