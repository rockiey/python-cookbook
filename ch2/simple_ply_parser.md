ply stands for python lex and yacc. it can be used to design parser/compiler/interpreter
while it's not standard library.
can be installed with: pip install ply

```python
just_len = 60

from ply.lex import lex
from ply.yacc import yacc

```

Token List
```python
tokens = ['NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN']

```

ignored characters
```python
t_ignore = ' \t\n'

```

Token specifications (as regexs)
```python
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

```

Token processing functions
```python
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)

    return t

```

Error handler
```python
def t_error(t):
    print('Bad character: {!r}'.format(t.value[0]))
    t.skip(1)

```

build the lexer
```python
lexer = lex()

```

Grammar rules and handler functions
```python
def p_expr(p):
    '''
    expr : expr PLUS term
         | expr MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expr_term(p):
    '''
    expr : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]


def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''

    p[0] = p[2]

def p_error(p):
    print('Syntax error')


parser = yacc()
print('parse 2'.ljust(just_len),
      parser.parse('2'))

print('parse 2 + 3'.ljust(just_len),
      parser.parse('2 + 3'))
print('parse 2 + 3 * 4'.ljust(just_len),
      parser.parse('2 + 3 * 4'))

print('parse (2 + 3) * 4'.ljust(just_len),
      parser.parse('(2 + 3) * 4'))

```
