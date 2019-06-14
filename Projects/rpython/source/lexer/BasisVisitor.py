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


    # Visit a parse tree produced by BasisParser#ImportModule.
    def visitImportModule(self, ctx:BasisParser.ImportModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#ImportModuleAll.
    def visitImportModuleAll(self, ctx:BasisParser.ImportModuleAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#ImportModuleAlias.
    def visitImportModuleAlias(self, ctx:BasisParser.ImportModuleAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#ImportSymbols.
    def visitImportSymbols(self, ctx:BasisParser.ImportSymbolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#importSuite.
    def visitImportSuite(self, ctx:BasisParser.ImportSuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#importAlias.
    def visitImportAlias(self, ctx:BasisParser.ImportAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#ifStatement.
    def visitIfStatement(self, ctx:BasisParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#elseif.
    def visitElseif(self, ctx:BasisParser.ElseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#elseStatement.
    def visitElseStatement(self, ctx:BasisParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#forInStatement.
    def visitForInStatement(self, ctx:BasisParser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#declareFunction.
    def visitDeclareFunction(self, ctx:BasisParser.DeclareFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#inType.
    def visitInType(self, ctx:BasisParser.InTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#outType.
    def visitOutType(self, ctx:BasisParser.OutTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#functionParameter.
    def visitFunctionParameter(self, ctx:BasisParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#typeExpression.
    def visitTypeExpression(self, ctx:BasisParser.TypeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#controlFlow.
    def visitControlFlow(self, ctx:BasisParser.ControlFlowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#expression.
    def visitExpression(self, ctx:BasisParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#data.
    def visitData(self, ctx:BasisParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#StringEmpty.
    def visitStringEmpty(self, ctx:BasisParser.StringEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#StringEscapeBlock.
    def visitStringEscapeBlock(self, ctx:BasisParser.StringEscapeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#StringEscapeSingle.
    def visitStringEscapeSingle(self, ctx:BasisParser.StringEscapeSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#StringLiteralBlock.
    def visitStringLiteralBlock(self, ctx:BasisParser.StringLiteralBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#StringLiteralSingle.
    def visitStringLiteralSingle(self, ctx:BasisParser.StringLiteralSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#number.
    def visitNumber(self, ctx:BasisParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#decimal.
    def visitDecimal(self, ctx:BasisParser.DecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#byte.
    def visitByte(self, ctx:BasisParser.ByteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#integer.
    def visitInteger(self, ctx:BasisParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#symbol.
    def visitSymbol(self, ctx:BasisParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#symbols.
    def visitSymbols(self, ctx:BasisParser.SymbolsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#identifier.
    def visitIdentifier(self, ctx:BasisParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#level2.
    def visitLevel2(self, ctx:BasisParser.Level2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasisParser#level1.
    def visitLevel1(self, ctx:BasisParser.Level1Context):
        return self.visitChildren(ctx)



del BasisParser