from ..lexer.BasisVisitor import BasisVisitor
from ..lexer.BasisParser import BasisParser

from unittest import TestCase
from ..lexer.BasisLexer import BasisLexer
from antlr4 import FileStream, CommonTokenStream


def debug_print(head, string):
    print("\033[36m" + head + ":\033[0m")
    print(f"{string}\n")


class JSON_IR(BasisVisitor):
    def visitStatement(self, ctx: BasisParser.StatementContext):
        # print(f"Statement: {ctx.getText()}\n")
        return self.visitChildren(ctx)

    def visitImportModule(self, ctx: BasisParser.ImportModuleContext):
        debug_print("Import", ctx.symbol().getText())
        return self.visitChildren(ctx)

    def visitImportModuleAll(self, ctx: BasisParser.ImportModuleAllContext):
        debug_print("Import", ctx.symbol().getText())
        return self.visitChildren(ctx)

    def visitImportModuleAlias(self, ctx: BasisParser.ImportModuleAliasContext):
        debug_print("Import", ctx.symbol().getText())
        return self.visitChildren(ctx)

    def visitImportSymbols(self, ctx: BasisParser.ImportSymbolsContext):
        debug_print("Import", ctx.symbol().getText())
        return self.visitChildren(ctx)


class ParserTests(TestCase):
    @staticmethod
    def aster(path):
        lexer = BasisLexer(FileStream(path))
        stream = CommonTokenStream(lexer)
        parser = BasisParser(stream)
        visitor = JSON_IR()
        visitor.visitProgram(parser.program())

    def test_ast_print(self):
        self.aster("../../examples/import.ba")
