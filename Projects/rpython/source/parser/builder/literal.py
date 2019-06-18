from ast import Num, Name, Load, Store


class Literal:
    @staticmethod
    def from_int_dec(raw: str):
        return Num(n=int(raw))

    @staticmethod
    def from_float(raw: str):
        return Num(n=float(raw))

    @staticmethod
    def from_symbol_get(raw: str):
        return Name(id=raw, ctx=Load())

    @staticmethod
    def from_symbol_set(raw: str):
        return Name(id=raw, ctx=Store())
