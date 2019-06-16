import numpy as np
import os
import random
import math

code = open('function.basis', 'w')
count = 0

IN = ['int x', 'x']
OUT = ['bool']
TAB = '\t' if random.random() > 0.5 else '    '

def write(token):

    global count

    contains_IN = any(elem in token for elem in IN)
    V = 'x == 6' if contains_IN else 'true'

    token_bak = token.copy()

    for newline_STYLE in range(3):

        if newline_STYLE == 0:
            token += ['{', V, '}']
        elif newline_STYLE == 1:
            token += ['\n' + TAB + 'return ', V]
        else:
            token += ['{', '\n', 'return ', V, '\n', '}']

        count += 1
        f = 'F_' + str(count)

        space_count = random.randint(0, 2)
        token = [
            (a.replace('F', f)) + (' ' * space_count)    
            for a in token
        ]

        code.write(''.join(token) + '\n\n')

        token = token_bak.copy()


for i in IN:
    for o in OUT:

        code.write('# @def f: i => o\n')
        write( ['F', ':', '(', i, ')', '=>', o] )

        code.write('# @def f: i o\n')
        write( ['F', ':', '(', i, ')', o] )

        code.write('# @def f i : o\n')
        write( ['F', '(', i, ')', ':', o] )

        code.write('# @def f: o i\n')
        write( ['F', ':', o, '(', i, ')'] )

        code.write('# @def o f i :\n')
        write( [o, ' F', '(', i, ')', ':'] )

        code.write('# @def o i f :\n')
        write( [o, '(', i, ')', 'F', ':'] )

        code.write('# @def i o f :\n')
        write( ['(', i, ')', o, ' F', ':'] )

        code.write('# @def (i => o) f :\n')
        write( ['(', i, ')', '=>', o, ' F', ':'] )

for i in IN:
    code.write('# @def f: i\n')
    write( ['F', ':', '(', i, ')'] )

    code.write('# @def f i :\n')
    write( ['F', '(', i, ')', ':'] )

    code.write('# @def i f :\n')
    write( ['(', i, ')', ' F', ':'] )

for o in OUT:
    code.write('# @def f: o\n')
    write( ['F', ':', o] )

    code.write('# @def o f:\n')
    write( [o, ' F', ':'] )

code.write('# @def f:\n')
write( ['F', ':'] )

code.close()
