import ast
from ast import alias, ImportFrom


class Import:
    @staticmethod
    def import_module(name: str, to: str = None):
        return ast.Import(names=[alias(name=name, asname=to)])

    @staticmethod
    def import_module_all(name: str):
        return ImportFrom(
            module=name,
            names=[alias(name='*', asname=None)],
            level=0
        )
