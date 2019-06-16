import numpy as np
import os
import random
import math

TAB = '\t' if random.random() < 0.3 else ' ' * random.randint(1, 5)

file = open('../Examples/function.basis', 'w')

def remove_duplicate(seq):
    seen = set()

    # skip 'original form' records, that is, x[-1]
    return [x for x in seq if not (''.join(x[:-1]) in seen or seen.add(''.join(x[:-1])))]

################ FOUND ALL POSSIBLE FORMS ################

form = ['F:(i)=>o',
        'F:(i)o',
        'F:o(i)',
        
        'F(i):o',
        'o F(i):',

        '(i)=>o F:',
        '(i)o F:',
        'o(i)F:',
]

form += [x.replace('(i)', ' ') for x in form]
form += [x.replace('o', ' ') for x in form]

form = [x.replace('o F', 'o_F') for x in form]
form = [x.replace(' ', '') for x in form]
form = [x.replace('o_F', 'o F') for x in form]

form = list(set(form))
form.sort()

print('\nfound', len(form), 'forms\n')
for x in form:
    print(x)

################ EXPAND ################

print('\nexpanding...\n')

IN = ['x', 'int x']
OUT = ['bool']
sentence = []

for f in form:
    ff = list(f.replace('=>','@')) # f => list of token
    for i in IN:
        for o in OUT:
            x = [k.replace('i', i).replace('o', o).replace('@', '=>') for k in ff]
            x.append(f) # x[-1] = 'original form'
            sentence.append(x)

sentence = remove_duplicate(sentence)

print('\nfound', len(sentence), 'sentences\n')
for x in sentence:
    print(''.join(x[:-1]))

################ WRITE ################

count = 0

for x in sentence:

    xx = x[:-1]
    contains_IN = any(elem in xx for elem in IN)
    V = 'x == 6' if contains_IN else 'true'

    file.write('################### @def ' + x[-1] + '\n\n')

    for newline_STYLE in range(3):

        c = x.copy()

        if newline_STYLE == 0:
            c += ['{', V, '}']
        elif newline_STYLE == 1:
            c += ['\n' + TAB + 'return ', V]
        else:
            c += ['{', '\n', 'return ', V, '\n', '}']

        count += 1
        f = 'F_' + str(count)

        space_count = random.randint(0, 2)
        c = [
            (a.replace('F', f)) + (' ' * space_count)   
            for a in c
        ]
        file.write(''.join(c) + '\n\n')

print('\ndone:', count, 'results\n')

file.close()
