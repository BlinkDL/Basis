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
    f = 'FUN_' + str(count)

    token = [(a if a!='F' else f) + (' ' * random.randint(0, 2)) for a in token]
    return token

IN = ['int x', 'x']
OUT = ['bool']
V = 'x == 6'

for i in IN:
    for o in OUT:

        code.write('# @def f: i => o\n')
        write( ['F', ':', i, '=>', o, '{', V, '}'] )

        code.write('# @def f: i o\n')
        write( ['F', ':', '(', i, ')', o, '{', V, '}'] )

        code.write('# @def f: o i\n')
        write( ['F', ':', o, '(', i, ')', '{', V, '}'] )

for o in OUT:
    code.write('# @def f: o\n')
    write( ['F', ':', o, '{', V, '}'] )

for i in IN:
    code.write('# @def f: i\n')
    write( ['F', ':', '(', i, ')', '{', V, '}'] )

code.write('# @def f:\n')
write( ['F', ':', '{', V, '}'] )

code.close()
