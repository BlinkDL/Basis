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


    # Enter a parse tree produced by BasisParser#ImportModule.
    def enterImportModule(self, ctx:BasisParser.ImportModuleContext):
        pass

    # Exit a parse tree produced by BasisParser#ImportModule.
    def exitImportModule(self, ctx:BasisParser.ImportModuleContext):
        pass


    # Enter a parse tree produced by BasisParser#ImportModuleAll.
    def enterImportModuleAll(self, ctx:BasisParser.ImportModuleAllContext):
        pass

    # Exit a parse tree produced by BasisParser#ImportModuleAll.
    def exitImportModuleAll(self, ctx:BasisParser.ImportModuleAllContext):
        pass


    # Enter a parse tree produced by BasisParser#ImportModuleAlias.
    def enterImportModuleAlias(self, ctx:BasisParser.ImportModuleAliasContext):
        pass

    # Exit a parse tree produced by BasisParser#ImportModuleAlias.
    def exitImportModuleAlias(self, ctx:BasisParser.ImportModuleAliasContext):
        pass


    # Enter a parse tree produced by BasisParser#ImportSymbols.
    def enterImportSymbols(self, ctx:BasisParser.ImportSymbolsContext):
        pass

    # Exit a parse tree produced by BasisParser#ImportSymbols.
    def exitImportSymbols(self, ctx:BasisParser.ImportSymbolsContext):
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


    # Enter a parse tree produced by BasisParser#ifStatement.
    def enterIfStatement(self, ctx:BasisParser.IfStatementContext):
        pass

    # Exit a parse tree produced by BasisParser#ifStatement.
    def exitIfStatement(self, ctx:BasisParser.IfStatementContext):
        pass


    # Enter a parse tree produced by BasisParser#elseif.
    def enterElseif(self, ctx:BasisParser.ElseifContext):
        pass

    # Exit a parse tree produced by BasisParser#elseif.
    def exitElseif(self, ctx:BasisParser.ElseifContext):
        pass


    # Enter a parse tree produced by BasisParser#elseStatement.
    def enterElseStatement(self, ctx:BasisParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by BasisParser#elseStatement.
    def exitElseStatement(self, ctx:BasisParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by BasisParser#forInStatement.
    def enterForInStatement(self, ctx:BasisParser.ForInStatementContext):
        pass

    # Exit a parse tree produced by BasisParser#forInStatement.
    def exitForInStatement(self, ctx:BasisParser.ForInStatementContext):
        pass


    # Enter a parse tree produced by BasisParser#declareFunction.
    def enterDeclareFunction(self, ctx:BasisParser.DeclareFunctionContext):
        pass

    # Exit a parse tree produced by BasisParser#declareFunction.
    def exitDeclareFunction(self, ctx:BasisParser.DeclareFunctionContext):
        pass


    # Enter a parse tree produced by BasisParser#declareFunctionComplete.
    def enterDeclareFunctionComplete(self, ctx:BasisParser.DeclareFunctionCompleteContext):
        pass

    # Exit a parse tree produced by BasisParser#declareFunctionComplete.
    def exitDeclareFunctionComplete(self, ctx:BasisParser.DeclareFunctionCompleteContext):
        pass


    # Enter a parse tree produced by BasisParser#declareFunctionCompletion.
    def enterDeclareFunctionCompletion(self, ctx:BasisParser.DeclareFunctionCompletionContext):
        pass

    # Exit a parse tree produced by BasisParser#declareFunctionCompletion.
    def exitDeclareFunctionCompletion(self, ctx:BasisParser.DeclareFunctionCompletionContext):
        pass


    # Enter a parse tree produced by BasisParser#inType.
    def enterInType(self, ctx:BasisParser.InTypeContext):
        pass

    # Exit a parse tree produced by BasisParser#inType.
    def exitInType(self, ctx:BasisParser.InTypeContext):
        pass


    # Enter a parse tree produced by BasisParser#outType.
    def enterOutType(self, ctx:BasisParser.OutTypeContext):
        pass

    # Exit a parse tree produced by BasisParser#outType.
    def exitOutType(self, ctx:BasisParser.OutTypeContext):
        pass


    # Enter a parse tree produced by BasisParser#functionParameter.
    def enterFunctionParameter(self, ctx:BasisParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by BasisParser#functionParameter.
    def exitFunctionParameter(self, ctx:BasisParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by BasisParser#typeExpression.
    def enterTypeExpression(self, ctx:BasisParser.TypeExpressionContext):
        pass

    # Exit a parse tree produced by BasisParser#typeExpression.
    def exitTypeExpression(self, ctx:BasisParser.TypeExpressionContext):
        pass


    # Enter a parse tree produced by BasisParser#declareVariable.
    def enterDeclareVariable(self, ctx:BasisParser.DeclareVariableContext):
        pass

    # Exit a parse tree produced by BasisParser#declareVariable.
    def exitDeclareVariable(self, ctx:BasisParser.DeclareVariableContext):
        pass


    # Enter a parse tree produced by BasisParser#controlFlow.
    def enterControlFlow(self, ctx:BasisParser.ControlFlowContext):
        pass

    # Exit a parse tree produced by BasisParser#controlFlow.
    def exitControlFlow(self, ctx:BasisParser.ControlFlowContext):
        pass


    # Enter a parse tree produced by BasisParser#expression.
    def enterExpression(self, ctx:BasisParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BasisParser#expression.
    def exitExpression(self, ctx:BasisParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BasisParser#data.
    def enterData(self, ctx:BasisParser.DataContext):
        pass

    # Exit a parse tree produced by BasisParser#data.
    def exitData(self, ctx:BasisParser.DataContext):
        pass


    # Enter a parse tree produced by BasisParser#StringEmpty.
    def enterStringEmpty(self, ctx:BasisParser.StringEmptyContext):
        pass

    # Exit a parse tree produced by BasisParser#StringEmpty.
    def exitStringEmpty(self, ctx:BasisParser.StringEmptyContext):
        pass


    # Enter a parse tree produced by BasisParser#StringEscapeBlock.
    def enterStringEscapeBlock(self, ctx:BasisParser.StringEscapeBlockContext):
        pass

    # Exit a parse tree produced by BasisParser#StringEscapeBlock.
    def exitStringEscapeBlock(self, ctx:BasisParser.StringEscapeBlockContext):
        pass


    # Enter a parse tree produced by BasisParser#StringEscapeSingle.
    def enterStringEscapeSingle(self, ctx:BasisParser.StringEscapeSingleContext):
        pass

    # Exit a parse tree produced by BasisParser#StringEscapeSingle.
    def exitStringEscapeSingle(self, ctx:BasisParser.StringEscapeSingleContext):
        pass


    # Enter a parse tree produced by BasisParser#StringLiteralBlock.
    def enterStringLiteralBlock(self, ctx:BasisParser.StringLiteralBlockContext):
        pass

    # Exit a parse tree produced by BasisParser#StringLiteralBlock.
    def exitStringLiteralBlock(self, ctx:BasisParser.StringLiteralBlockContext):
        pass


    # Enter a parse tree produced by BasisParser#StringLiteralSingle.
    def enterStringLiteralSingle(self, ctx:BasisParser.StringLiteralSingleContext):
        pass

    # Exit a parse tree produced by BasisParser#StringLiteralSingle.
    def exitStringLiteralSingle(self, ctx:BasisParser.StringLiteralSingleContext):
        pass


    # Enter a parse tree produced by BasisParser#number.
    def enterNumber(self, ctx:BasisParser.NumberContext):
        pass

    # Exit a parse tree produced by BasisParser#number.
    def exitNumber(self, ctx:BasisParser.NumberContext):
        pass


    # Enter a parse tree produced by BasisParser#decimal.
    def enterDecimal(self, ctx:BasisParser.DecimalContext):
        pass

    # Exit a parse tree produced by BasisParser#decimal.
    def exitDecimal(self, ctx:BasisParser.DecimalContext):
        pass


    # Enter a parse tree produced by BasisParser#byte.
    def enterByte(self, ctx:BasisParser.ByteContext):
        pass

    # Exit a parse tree produced by BasisParser#byte.
    def exitByte(self, ctx:BasisParser.ByteContext):
        pass


    # Enter a parse tree produced by BasisParser#integer.
    def enterInteger(self, ctx:BasisParser.IntegerContext):
        pass

    # Exit a parse tree produced by BasisParser#integer.
    def exitInteger(self, ctx:BasisParser.IntegerContext):
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


    # Enter a parse tree produced by BasisParser#identifier.
    def enterIdentifier(self, ctx:BasisParser.IdentifierContext):
        pass

    # Exit a parse tree produced by BasisParser#identifier.
    def exitIdentifier(self, ctx:BasisParser.IdentifierContext):
        pass


    # Enter a parse tree produced by BasisParser#level2.
    def enterLevel2(self, ctx:BasisParser.Level2Context):
        pass

    # Exit a parse tree produced by BasisParser#level2.
    def exitLevel2(self, ctx:BasisParser.Level2Context):
        pass


    # Enter a parse tree produced by BasisParser#level1.
    def enterLevel1(self, ctx:BasisParser.Level1Context):
        pass

    # Exit a parse tree produced by BasisParser#level1.
    def exitLevel1(self, ctx:BasisParser.Level1Context):
        pass


