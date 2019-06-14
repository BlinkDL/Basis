grammar Basis;
// $antlr-format useTab false ;reflowComments false;
tokens {
    INDENT,
    DEDENT
}
// $antlr-format alignColons hanging;
// $antlr-format columnLimit 128;
@lexer::header {
from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

@lexer::members {
@property
def tokens(self):
    try:
        return self._tokens
    except AttributeError:
        self._tokens = []
        return self._tokens

@property
def indents(self):
    try:
        return self._indents
    except AttributeError:
        self._indents = []
        return self._indents

@property
def opened(self):
    try:
        return self._opened
    except AttributeError:
        self._opened = 0
        return self._opened

@opened.setter
def opened(self, value):
    self._opened = value

@property
def lastToken(self):
    try:
        return self._lastToken
    except AttributeError:
        self._lastToken = None
        return self._lastToken

@lastToken.setter
def lastToken(self, value):
    self._lastToken = value

def reset(self):
    super().reset()
    self.tokens = []
    self.indents = []
    self.opened = 0
    self.lastToken = None

def emitToken(self, t):
    super().emitToken(t)
    self.tokens.append(t)

def nextToken(self):
    if self._input.LA(1) == Token.EOF and self.indents:
        for i in range(len(self.tokens)-1,-1,-1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop(i)

        self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
        while self.indents:
            self.emitToken(self.createDedent())
            self.indents.pop()

        self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
    next = super().nextToken()
    if next.channel == Token.DEFAULT_CHANNEL:
        self.lastToken = next
    return next if not self.tokens else self.tokens.pop(0)

def createDedent(self):
    dedent = self.commonToken(LanguageParser.DEDENT, "")
    dedent.line = self.lastToken.line
    return dedent

def commonToken(self, type, text, indent=0):
    stop = self.getCharIndex()-1-indent
    start = (stop - len(text) + 1) if text else stop
    return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count

def atStartOfInput(self):
    return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1
}
// $antlr-format alignColons trailing;
SPACES : [\t ]+ -> skip;
NEWLINE: ({self.atStartOfInput()}? SPACES | ( '\r'? '\n' | '\r' | '\f') SPACES?) {
tempt = Lexer.text.fget(self)
newLine = re.sub("[^\r\n\f]+", "", tempt)
spaces = re.sub("[\r\n\f]+", "", tempt)
la_char = ""
try:
    la = self._input.LA(1)
    la_char = chr(la)       # Python does not compare char to ints directly
except ValueError:          # End of file
    pass

if self.opened > 0 or la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#':
    self.skip()
else:
    indent = self.getIndentationCount(spaces)
    previous = self.indents[-1] if self.indents else 0
    self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
    if indent == previous:
        self.skip()
    elif indent > previous:
        self.indents.append(indent)
        self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
    else:
        while self.indents and self.indents[-1] > indent:
            self.emitToken(self.createDedent())
            self.indents.pop()
};
Escape   : '\\';
JoinLine : Escape SPACES? ( '\r'? '\n' | '\r') -> skip;
//fragment UnicodeWS : [\p{White_Space}] ;
/*====================================================================================================================*/
program           : (NEWLINE | statement)* EOF;
statement         : simpleStatement | compoundStatement;
simpleStatement   : shortStatement (Semicolon shortStatement)* Semicolon? NEWLINE;
shortStatement    : expression;
compoundStatement : declarePackage | declareImport | ifStatement;
suite             : simpleStatement | NEWLINE INDENT statement+ DEDENT | '{' statement+ '}';
Semicolon         : ';';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
declarePackage: Package symbol;
declareImport
    : Import symbol                       # ImportModule
    | Import symbol Dot Star              # ImportModuleAll
    | Import symbol As identifier # ImportModuleAlias
    | Import symbol With importSuite      # ImportSymbols;
importSuite
    : (importAlias Comma?)*
    | NEWLINE INDENT (importAlias Comma? NEWLINE?)* DEDENT;
importAlias: symbol (As symbol)?;
// $antlr-format alignColons trailing;
Import  : 'import';
Package : 'package';
/*====================================================================================================================*/
With  : 'with';
As    : 'as';
Comma : ',';
Star  : '*';
/*====================================================================================================================*/
ifStatement   : If cond = expression suite elseif* elseStatement?;
elseif        : If Else cond = expression suite;
elseStatement : Else suite;

If   : 'if';
Else : 'else';
/*====================================================================================================================*/
forInStatement : For expression In expression suite elseStatement?;

For : 'for';
In  : 'in';
/*====================================================================================================================*/
// $antlr-format alignColons hanging;
declareFunction: typeExpression functionLHS Colon suite;
functionLHS
    : identifier '[' typeExpression ']'
    | identifier '(' ')'
    | identifier '(' functionParameter (Comma functionParameter)* Comma? ')';
// $antlr-format alignColons trailing;
functionParameter : typeExpression identifier;
typeExpression    : identifier | '[' identifier ']' identifier;

To    : '=>';
Colon : ':';
/*====================================================================================================================*/
expression : data;
/*====================================================================================================================*/
data : string | number;

/*====================================================================================================================*/
// $antlr-format alignColons hanging;
string
    : StringEmpty         # StringEmpty
    | StringEscapeBlock   # StringEscapeBlock
    | StringEscapeSingle  # StringEscapeSingle
    | StringLiteralBlock  # StringLiteralBlock
    | StringLiteralSingle # StringLiteralSingle;
// $antlr-format alignColons trailing;
StringEscapeBlock   : S6 CharLevel1+? S6;
StringEscapeSingle  : S2 CharLevel2+? S2;
StringLiteralBlock  : S3 .+? S3;
StringLiteralSingle : S1 ~[\uFF02]+? S1;
StringEmpty         : S6 S6 | S3 S3 | S2 S2 | S1 S1;
fragment S6         : '"""';
fragment S3         : '\uFF02\uFF02\uFF02';
fragment S2         : '"';
fragment S1         : '\uFF02'; //U+FF02 ＂
fragment CharLevel1 : Escape ~[ ] | ~[\\];
fragment CharLevel2 : Escape ~[ ] | ~["\\];
/*====================================================================================================================*/
// $antlr-format alignColons trailing;
number  : decimal | byte | integer;
decimal : Decimal | DecimalBad;
byte    : Hexadecimal | Octal | Binary;
integer : Integer;

Decimal     : Integer Dot Digit;
DecimalBad  : Integer Dot | Dot Digit+;
Binary      : Zero B Bin+;
Octal       : Zero O Oct+;
Hexadecimal : Zero X Hex+;
Integer     : Zero+ | [1-9] Digit*;
Exponent    : '*^';
Base        : '/^';

fragment Bin   : Zero | [1];
fragment Oct   : Zero | [1-7];
fragment Digit : Zero | [1-9];
fragment Hex   : Zero | [1-9a-fA-F];
fragment Zero  : [0];
/*====================================================================================================================*/
symbol     : Identifier | symbols;
symbols    : Identifier (Dot Identifier)+;
identifier : Identifier;
Identifier : NameStartCharacter NameCharacter*;
Dot        : '.';
Underline  : '_';
fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
// $antlr-format alignColons hanging;
fragment Letter
    : (A | B | C | D | E | F | G)
    | (H | I | J | K | L | M | N)
    | (O | P | Q | R | S | T)
    | (U | V | W | X | Y | Z);
fragment NameStartCharacter
    : (Underline | Letter)
    | [\p{Latin}]
    | [\p{Han}]
    | [\p{Hiragana}]
    | [\p{Katakana}]
    | [\p{Greek}];
// $antlr-format alignColons trailing;
fragment EmojiCharacter : [\p{Emoji}];
fragment NameCharacter  : NameStartCharacter | Digit;
/*====================================================================================================================*/
LineComment : '#' ~[\r\n]* -> channel(HIDDEN);
