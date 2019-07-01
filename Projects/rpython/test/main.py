import datetime
import os
from unittest import TestCase

from antlr4 import FileStream, CommonTokenStream

from ..source.lexer.BasisLexer import BasisLexer
from ..source.lexer.BasisParser import BasisParser
from ..source.parser.python_target import PythonTarget
from ..source.parser.debug import debug_print


class ParserTests(TestCase):
    @staticmethod
    def aster(path):
        lexer = BasisLexer(FileStream(path))
        stream = CommonTokenStream(lexer)
        parser = BasisParser(stream)
        visitor = PythonTarget()
        return visitor.visitProgram(parser.program())

    def python_gen(self, name: str):
        now = datetime.datetime.now()
        here = os.path.split(os.path.realpath(__file__))[0]
        target = os.path.join(here, "as_python", name.split(".")[0] + ".py")
        ast = self.aster(f"../examples/{name}")
        with open(target, "w") as f:
            f.write(ast)
        debug_print("Testing", name)
        print(datetime.datetime.now() - now)

    def test_import(self):
        self.python_gen("import.basis")

    def test_literal(self):
        self.python_gen("literal.basis")
