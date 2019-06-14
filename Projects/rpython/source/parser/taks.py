from enum import Enum


class Tasks(Enum):
    Module = 0

    ImportModule = 100
    ImportSymbol = 101

    FunctionDeclaration = 1000
    FunctionParameter = 1001
    FunctionParameterNormal = 1002
    FunctionParameterArgs = 1003
    FunctionParameterKWs = 1004

    ClassDeclaration = 2000
