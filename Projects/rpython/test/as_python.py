from ..source.lexer.BasisParser import BasisParser
from ..source.lexer.BasisLexer import BasisLexer
from ..source.parser.Python_IR import Python_IR
from ..source.parser.debug import debug_print
from unittest import TestCase
from antlr4 import FileStream, CommonTokenStream

import os, datetime


class ParserTests(TestCase):
    @staticmethod
    def aster(path):
        lexer = BasisLexer(FileStream(path))
        stream = CommonTokenStream(lexer)
        parser = BasisParser(stream)
        visitor = Python_IR()
        return visitor.visitProgram(parser.program())

    def do_test(self, name: str):
        now = datetime.datetime.now()
        here = os.path.split(os.path.realpath(__file__))[0]
        target = os.path.join(here, "as_python", name.split(".")[0] + ".py")
        ast = self.aster(f"../examples/{name}")
        with open(target, "w") as f:
            f.write(ast)
        debug_print("Testing", name)
        print(datetime.datetime.now() - now)

    def test_import(self):
        self.do_test("import.basis")
