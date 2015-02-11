just_len = 60
text = 'foo = 23 + 42 * 10'

import re
# ?P<TOKENNAME> is used to assign a name to the pattern
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

from collections import namedtuple
Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pattern, text):
    scanner = pattern.scanner(text)

    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


print('get all tokens')
for token in generate_tokens(master_pattern, text):
    print(token)


print('\nget all tokens exclude space tokens')
excluded_ws = (token for token in generate_tokens(master_pattern, text) if token.type != 'WS')
for token in excluded_ws:
    print(token)

NUM = r'(?P<NUM>\d+)'
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
# the pattern's order matters. Longer match should be put first
# like <= should be earlier than = or <
print('\npattern in right order')
master_pattern_in_right_order = re.compile('|'.join([NUM, LE, LT, EQ]))
token_correct = list(generate_tokens(master_pattern_in_right_order, '3<=4'))
for token in token_correct:
    print(token)


# if put < earlier than <=
# then <= will be two token < and = which is incorrect
print('\npattern in wrong order')
master_pattern_in_right_order = re.compile('|'.join([NUM, LT, EQ, LE]))
token_incorrect = list(generate_tokens(master_pattern_in_right_order, '3<=4'))
for token in token_incorrect:
    print(token)