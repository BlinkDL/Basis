# Generated from D:/Hybrid/Basis/Projects/rpython\Basis.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasisParser import BasisParser
else:
    from BasisParser import BasisParser

# This class defines a complete generic visitor for a parse tree produced by BasisParser.

class BasisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasisParser#program.
    def visitProgram(self, ctx:BasisParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#statement.
    def visitStatement(self, ctx:BasisParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#simpleStatement.
    def visitSimpleStatement(self, ctx:BasisParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#shortStatement.
    def visitShortStatement(self, ctx:BasisParser.ShortStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#compoundStatement.
    def visitCompoundStatement(self, ctx:BasisParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#suite.
    def visitSuite(self, ctx:BasisParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#declarePackage.
    def visitDeclarePackage(self, ctx:BasisParser.DeclarePackageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#declareImport.
    def visitDeclareImport(self, ctx:BasisParser.DeclareImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#importSuite.
    def visitImportSuite(self, ctx:BasisParser.ImportSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#importAlias.
    def visitImportAlias(self, ctx:BasisParser.ImportAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#symbol.
    def visitSymbol(self, ctx:BasisParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#symbols.
    def visitSymbols(self, ctx:BasisParser.SymbolsContext):
        return self.visitChildren(ctx)



del BasisParser