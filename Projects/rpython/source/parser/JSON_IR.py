from ..lexer.BasisVisitor import BasisVisitor
from ..lexer.BasisParser import BasisParser

from unittest import TestCase
import os
from ..lexer.BasisLexer import BasisLexer
from antlr4 import FileStream, CommonTokenStream


class JSON_IR(BasisVisitor):
    def visitProgram(self, ctx: BasisParser.ProgramContext):
        print(ctx.getText())
        return self.visitChildren(ctx)


class ParserTests(TestCase):
    def aster(self, path):
        lexer = BasisLexer(FileStream(path))
        stream = CommonTokenStream(lexer)
        parser = JSON_IR(stream)
        parser.program()

    def test_ast_print(self):
        self.aster("../../examples/import.ba")
