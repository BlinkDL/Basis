import numpy as np
import os
import random
import math

code = open('function.basis', 'w')

count = 0

def write(token):
    token = process(token)
    code.write(''.join(token) + '\n\n')

def process(token):

    global count
    count += 1
    f = 'F_' + str(count)

    token = [
        (a.replace('F', f)) + (' ' * random.randint(0, 2))    
        for a in token
    ]
    return token

IN = ['int x', 'x']
OUT = ['bool']
V = 'x == 6'
V_WITHOUT_IN = 'true'

for i in IN:
    for o in OUT:

        code.write('# @def f: i => o\n')
        write( ['F', ':', '(', i, ')', '=>', o, '{', V, '}'] )

        code.write('# @def f: i o\n')
        write( ['F', ':', '(', i, ')', o, '{', V, '}'] )

        code.write('# @def f i : o\n')
        write( ['F', '(', i, ')', ':', o, '{', V, '}'] )

        code.write('# @def f: o i\n')
        write( ['F', ':', o, '(', i, ')', '{', V, '}'] )

        code.write('# @def o f i :\n')
        write( [o, ' F', '(', i, ')', ':', '{', V, '}'] )

        code.write('# @def o i f :\n')
        write( [o, '(', i, ')', 'F', ':', '{', V, '}'] )

        code.write('# @def i o f :\n')
        write( ['(', i, ')', o, ' F', ':', '{', V, '}'] )

        code.write('# @def (i => o) f :\n')
        write( ['(', i, ')', '=>', o, ' F', ':', '{', V, '}'] )

for i in IN:
    code.write('# @def f: i\n')
    write( ['F', ':', '(', i, ')', '{', V, '}'] )

    code.write('# @def f i :\n')
    write( ['F', '(', i, ')', ':', '{', V, '}'] )

    code.write('# @def i f :\n')
    write( ['(', i, ')', ' F', ':', '{', V, '}'] )

for o in OUT:
    code.write('# @def f: o\n')
    write( ['F', ':', o, '{', V_WITHOUT_IN, '}'] )

    code.write('# @def o f:\n')
    write( [o, ' F', ':', '{', V_WITHOUT_IN, '}'] )

code.write('# @def f:\n')
write( ['F', ':', '{', V_WITHOUT_IN, '}'] )

code.close()
