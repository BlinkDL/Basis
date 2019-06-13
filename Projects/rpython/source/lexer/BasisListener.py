# Generated from D:/Hybrid/Basis/Projects/rpython\Basis.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasisParser import BasisParser
else:
    from BasisParser import BasisParser

# This class defines a complete listener for a parse tree produced by BasisParser.
class BasisListener(ParseTreeListener):

    # Enter a parse tree produced by BasisParser#program.
    def enterProgram(self, ctx:BasisParser.ProgramContext):
        pass

    # Exit a parse tree produced by BasisParser#program.
    def exitProgram(self, ctx:BasisParser.ProgramContext):
        pass


    # Enter a parse tree produced by BasisParser#statement.
    def enterStatement(self, ctx:BasisParser.StatementContext):
        pass

    # Exit a parse tree produced by BasisParser#statement.
    def exitStatement(self, ctx:BasisParser.StatementContext):
        pass


    # Enter a parse tree produced by BasisParser#simpleStatement.
    def enterSimpleStatement(self, ctx:BasisParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by BasisParser#simpleStatement.
    def exitSimpleStatement(self, ctx:BasisParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by BasisParser#shortStatement.
    def enterShortStatement(self, ctx:BasisParser.ShortStatementContext):
        pass

    # Exit a parse tree produced by BasisParser#shortStatement.
    def exitShortStatement(self, ctx:BasisParser.ShortStatementContext):
        pass


    # Enter a parse tree produced by BasisParser#compoundStatement.
    def enterCompoundStatement(self, ctx:BasisParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by BasisParser#compoundStatement.
    def exitCompoundStatement(self, ctx:BasisParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by BasisParser#suite.
    def enterSuite(self, ctx:BasisParser.SuiteContext):
        pass

    # Exit a parse tree produced by BasisParser#suite.
    def exitSuite(self, ctx:BasisParser.SuiteContext):
        pass


    # Enter a parse tree produced by BasisParser#declarePackage.
    def enterDeclarePackage(self, ctx:BasisParser.DeclarePackageContext):
        pass

    # Exit a parse tree produced by BasisParser#declarePackage.
    def exitDeclarePackage(self, ctx:BasisParser.DeclarePackageContext):
        pass


    # Enter a parse tree produced by BasisParser#declareImport.
    def enterDeclareImport(self, ctx:BasisParser.DeclareImportContext):
        pass

    # Exit a parse tree produced by BasisParser#declareImport.
    def exitDeclareImport(self, ctx:BasisParser.DeclareImportContext):
        pass


    # Enter a parse tree produced by BasisParser#importSuite.
    def enterImportSuite(self, ctx:BasisParser.ImportSuiteContext):
        pass

    # Exit a parse tree produced by BasisParser#importSuite.
    def exitImportSuite(self, ctx:BasisParser.ImportSuiteContext):
        pass


    # Enter a parse tree produced by BasisParser#importAlias.
    def enterImportAlias(self, ctx:BasisParser.ImportAliasContext):
        pass

    # Exit a parse tree produced by BasisParser#importAlias.
    def exitImportAlias(self, ctx:BasisParser.ImportAliasContext):
        pass


    # Enter a parse tree produced by BasisParser#symbol.
    def enterSymbol(self, ctx:BasisParser.SymbolContext):
        pass

    # Exit a parse tree produced by BasisParser#symbol.
    def exitSymbol(self, ctx:BasisParser.SymbolContext):
        pass


    # Enter a parse tree produced by BasisParser#symbols.
    def enterSymbols(self, ctx:BasisParser.SymbolsContext):
        pass

    # Exit a parse tree produced by BasisParser#symbols.
    def exitSymbols(self, ctx:BasisParser.SymbolsContext):
        pass


