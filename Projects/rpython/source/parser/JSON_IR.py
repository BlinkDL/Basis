from ..lexer.BasisVisitor import BasisVisitor
from ..lexer.BasisParser import BasisParser

from unittest import TestCase
from ..lexer.BasisLexer import BasisLexer
from antlr4 import FileStream, CommonTokenStream

DEBUG = {
    "STATEMENT": False,
    "IMPORT": False,
}


def debug_print(head, string=None):
    if string is None:
        print(f"{head}")
    else:
        print("\033[36m" + head + ":\033[0m")
        print(f"{string}")


class JSON_IR(BasisVisitor):
    def visitStatement(self, ctx: BasisParser.StatementContext):
        if DEBUG["STATEMENT"]:
            debug_print("Statement", ctx.getText())
        return self.visitChildren(ctx)

    # region Import
    def visitImportModule(self, ctx: BasisParser.ImportModuleContext):
        module = ctx.symbol()
        if DEBUG["IMPORT"]:
            debug_print("Import", module.getText())
        return self.visitChildren(ctx)

    def visitImportModuleAll(self, ctx: BasisParser.ImportModuleAllContext):
        module = ctx.symbol()
        if DEBUG["IMPORT"]:
            debug_print("Import", module.getText())
            debug_print("*")
        return self.visitChildren(ctx)

    def visitImportModuleAlias(self, ctx: BasisParser.ImportModuleAliasContext):
        module = ctx.symbol()
        alias = ctx.identifier()
        if DEBUG["IMPORT"]:
            debug_print("Import", module.getText() + " -> " + alias.getText())
        return self.visitChildren(ctx)

    def visitImportSymbols(self, ctx: BasisParser.ImportSymbolsContext):
        module = ctx.symbol()
        if DEBUG["IMPORT"]:
            debug_print("Import", module.getText())
        return self.visitChildren(ctx)

    def visitImportSuite(self, ctx: BasisParser.ImportSuiteContext):
        symbols = map(self.visit, ctx.importAlias())
        debug_print(list(symbols))
        return self.visitChildren(ctx)

    def visitImportAlias(self, ctx: BasisParser.ImportAliasContext):
        if len(ctx.symbol()) == 1:
            return self.visit(ctx.symbol(0))
        else:
            return self.visit(ctx.symbol(0)), self.visit(ctx.symbol(1))

    # endregion

    # region Atom
    def visitSymbol(self, ctx: BasisParser.SymbolContext):
        return ctx.getText()

    def visitIdentifier(self, ctx: BasisParser.IdentifierContext):
        return ctx.getText()
    # endregion


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
