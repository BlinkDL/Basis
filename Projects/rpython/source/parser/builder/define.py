from ast import arg, Name, Load, arguments


class Define:
    @staticmethod
    def from_arg(symbol: str):
        arg(arg=symbol, annotation=None)
        pass

    @staticmethod
    def from_arg_typed(symbol: str, typed: str):
        return arg(
            arg=symbol,
            annotation=Name(id=typed, ctx=Load())
        )

    @staticmethod
    def from_arg_typed_expr(symbol: str, typed: str):
        return arg(
            arg=symbol,
            annotation=typed
        )

    @staticmethod
    def arg_list(*args):
        return arguments(
            args=args,
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        )
