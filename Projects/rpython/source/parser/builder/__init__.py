from astunparse import unparse, dump
from ast import Module
from .literal import Literal
from .module import Import


def ast_build(exprs):
    ast = Module(body=exprs)
    debug = exprs[3].names[0].asname
    print(debug)
    dump(debug)
    return unparse(debug)
