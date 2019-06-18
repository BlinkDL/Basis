from ..lexer.BasisVisitor import BasisVisitor
from ..lexer.BasisParser import BasisParser

from unittest import TestCase
from ..lexer.BasisLexer import BasisLexer
from antlr4 import FileStream, CommonTokenStream
from .builder import Import, Literal, ast_build


class Python_IR(BasisVisitor):
    def visitProgram(self, ctx: BasisParser.ProgramContext):
        stats = list(map(self.visit, ctx.statement()))
        return ast_build(stats)

    def visitStatement(self, ctx: BasisParser.StatementContext):
        # debug_print("Statement", self.visitChildren(ctx))
        return self.visitChildren(ctx)

    # region Import
    def visitImportModule(self, ctx: BasisParser.ImportModuleContext):
        module = self.visit(ctx.symbol())
        return Import.import_module(module, None)

    def visitImportModuleAlias(self, ctx: BasisParser.ImportModuleAliasContext):
        module = self.visit(ctx.symbol())
        alias = self.visit(ctx.identifier())
        return Import.import_module(module, alias)

    def visitImportModuleAll(self, ctx: BasisParser.ImportModuleAllContext):
        module = self.visit(ctx.symbol())
        return Import.import_module_all(module)

    def visitImportSymbols(self, ctx: BasisParser.ImportSymbolsContext):
        module = self.visit(ctx.symbol())
        symbol = self.visit(ctx.importSuite())
        return Import.import_symbols(module, symbol)

    def visitImportSuite(self, ctx: BasisParser.ImportSuiteContext):
        symbols = map(self.visit, ctx.importAlias())
        return list(symbols)

    def visitImportAlias(self, ctx: BasisParser.ImportAliasContext):
        if len(ctx.symbol()) == 1:
            alias = None
        else:
            alias = self.visit(ctx.symbol(1)),
        return Import.symbol_pair(self.visit(ctx.symbol(0)), alias)

    # endregion

    # region Function

    # endregion

    # region Atom
    def visitSymbol(self, ctx: BasisParser.SymbolContext):
        return ctx.getText()

    def visitIdentifier(self, ctx: BasisParser.IdentifierContext):
        return ctx.getText()

    def visitInteger(self, ctx: BasisParser.IntegerContext):
        return Literal.from_int_dec(ctx.getText())

    def visitDecimal(self, ctx: BasisParser.DecimalContext):
        return Literal.from_float(ctx.getText())

    # endregion


class ParserTests(TestCase):
    @staticmethod
    def aster(path):
        lexer = BasisLexer(FileStream(path))
        stream = CommonTokenStream(lexer)
        parser = BasisParser(stream)
        visitor = Python_IR()
        return visitor.visitProgram(parser.program())

    def test_ast_print(self):
        ast = self.aster("../../examples/import.basis")
        print(ast)
