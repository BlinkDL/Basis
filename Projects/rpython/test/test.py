from ast import parse, Module, Expr, Num, BinOp, Add, FunctionDef, arguments, arg, Return, Name, Load, Assign, Store, \
    Compare, Eq, ImportFrom, alias, Import, List
from astunparse import unparse, dump


def add(arg1: str, arg2: str) -> str:
    return arg1 + arg2


def F_6(x: int, y, *args: [str]) -> bool:
    return x == 6


expr = """
def F_6(x: int, y, *args: [str]) -> bool:
    return x == 6
"""

if __name__ == "__main__":
    mod = Module(body=[FunctionDef(
        name='F_6',
        args=arguments(
            args=[
                arg(
                    arg='x',
                    annotation=Name(
                        id='int',
                        ctx=Load())),
                arg(
                    arg='y',
                    annotation=None)],
            vararg=arg(
                arg='args',
                annotation=List(
                    elts=[Name(
                        id='str',
                        ctx=Load())],
                    ctx=Load())),
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]),
        body=[Return(value=Compare(
            left=Name(
                id='x',
                ctx=Load()),
            ops=[Eq()],
            comparators=[Num(n=6)]))],
        decorator_list=[],
        returns=Name(
            id='bool',
            ctx=Load()))])
    expr_ast = parse(expr)
    print(expr_ast)
    print(f"{dump(expr_ast)}\n")
    print(unparse(mod))
