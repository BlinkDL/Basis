# Generated from D:/Hybrid/Basis/Projects/rpython\Basis.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0185\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\u0081\n\3")
        buf.write("\r\3\16\3\u0082\3\3\3\3\3\4\3\4\3\4\5\4\u008a\n\4\3\4")
        buf.write("\3\4\5\4\u008e\n\4\3\4\5\4\u0091\n\4\5\4\u0093\n\4\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\5\6\u009b\n\6\3\6\5\6\u009e\n\6\3")
        buf.write("\6\3\6\5\6\u00a2\n\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\6\17\u00cc\n\17\r\17\16")
        buf.write("\17\u00cd\5\17\u00d0\n\17\3\20\3\20\3\20\6\20\u00d5\n")
        buf.write("\20\r\20\16\20\u00d6\3\21\3\21\3\21\6\21\u00dc\n\21\r")
        buf.write("\21\16\21\u00dd\3\22\3\22\3\22\6\22\u00e3\n\22\r\22\16")
        buf.write("\22\u00e4\3\23\6\23\u00e8\n\23\r\23\16\23\u00e9\3\23\3")
        buf.write("\23\7\23\u00ee\n\23\f\23\16\23\u00f1\13\23\5\23\u00f3")
        buf.write("\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\5\26\u00fd")
        buf.write("\n\26\3\27\3\27\5\27\u0101\n\27\3\30\3\30\5\30\u0105\n")
        buf.write("\30\3\31\3\31\5\31\u0109\n\31\3\32\3\32\3\33\3\33\7\33")
        buf.write("\u010f\n\33\f\33\16\33\u0112\13\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\3")
        buf.write("8\38\38\58\u0153\n8\38\38\38\38\38\38\38\58\u015c\n8\3")
        buf.write("8\38\38\38\38\38\58\u0164\n8\38\38\38\38\38\38\58\u016c")
        buf.write("\n8\58\u016e\n8\39\39\59\u0172\n9\39\59\u0175\n9\3:\3")
        buf.write(":\3;\3;\5;\u017b\n;\3<\3<\7<\u017f\n<\f<\16<\u0182\13")
        buf.write("<\3<\3<\2\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\2-\2/\2\61\2\63\2\65\27\67\309\31;\2=\2?\2A\2C\2E\2")
        buf.write("G\2I\2K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2")
        buf.write("k\2m\2o\2q\2s\2u\2w\32\3\2#\4\2\13\13\"\"\3\2\63;\3\2")
        buf.write("\63\63\3\2\639\5\2\63;CHch\3\2\62\62\4\2CCcc\4\2DDdd\4")
        buf.write("\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKk")
        buf.write("k\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2")
        buf.write("RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4")
        buf.write("\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f\17\17\4Y\2C\2")
        buf.write("\\\2c\2|\2\u00ac\2\u00ac\2\u00bc\2\u00bc\2\u00c2\2\u00d8")
        buf.write("\2\u00da\2\u00f8\2\u00fa\2\u02ba\2\u02e2\2\u02e6\2\u0372")
        buf.write("\2\u0375\2\u0377\2\u0379\2\u037c\2\u037f\2\u0381\2\u0381")
        buf.write("\2\u0386\2\u0386\2\u0388\2\u0388\2\u038a\2\u038c\2\u038e")
        buf.write("\2\u038e\2\u0390\2\u03a3\2\u03a5\2\u03e3\2\u03f2\2\u0401")
        buf.write("\2\u1d02\2\u1d2c\2\u1d2e\2\u1d79\2\u1d7b\2\u1dc1\2\u1e02")
        buf.write("\2\u1f17\2\u1f1a\2\u1f1f\2\u1f22\2\u1f47\2\u1f4a\2\u1f4f")
        buf.write("\2\u1f52\2\u1f59\2\u1f5b\2\u1f5b\2\u1f5d\2\u1f5d\2\u1f5f")
        buf.write("\2\u1f5f\2\u1f61\2\u1f7f\2\u1f82\2\u1fb6\2\u1fb8\2\u1fc6")
        buf.write("\2\u1fc8\2\u1fd5\2\u1fd8\2\u1fdd\2\u1fdf\2\u1ff1\2\u1ff4")
        buf.write("\2\u1ff6\2\u1ff8\2\u2000\2\u2073\2\u2073\2\u2081\2\u2081")
        buf.write("\2\u2092\2\u209e\2\u2128\2\u2128\2\u212c\2\u212d\2\u2134")
        buf.write("\2\u2134\2\u2150\2\u2150\2\u2162\2\u218a\2\u2c62\2\u2c81")
        buf.write("\2\u2e82\2\u2e9b\2\u2e9d\2\u2ef5\2\u2f02\2\u2fd7\2\u3007")
        buf.write("\2\u3007\2\u3009\2\u3009\2\u3023\2\u302b\2\u303a\2\u303d")
        buf.write("\2\u3043\2\u3098\2\u309f\2\u30a1\2\u30a3\2\u30fc\2\u30ff")
        buf.write("\2\u3101\2\u31f2\2\u3201\2\u32d2\2\u3300\2\u3302\2\u3359")
        buf.write("\2\u3402\2\u4db7\2\u4e02\2\u9fec\2\ua724\2\ua789\2\ua78d")
        buf.write("\2\ua7b0\2\ua7b2\2\ua7b9\2\ua7f9\2\ua801\2\uab32\2\uab5c")
        buf.write("\2\uab5e\2\uab67\2\uf902\2\ufa6f\2\ufa72\2\ufadb\2\ufb02")
        buf.write("\2\ufb08\2\uff23\2\uff3c\2\uff43\2\uff5c\2\uff68\2\uff71")
        buf.write("\2\uff73\2\uff9f\2\u0142\3\u0190\3\u01a2\3\u01a2\3\ub002")
        buf.write("\3\ub120\3\ud202\3\ud247\3\uf202\3\uf202\3\2\4\ua6d8\4")
        buf.write("\ua702\4\ub736\4\ub742\4\ub81f\4\ub822\4\ucea3\4\uceb2")
        buf.write("\4\uebe2\4\uf802\4\ufa1f\4\u0093\2%\2%\2,\2,\2\62\2;\2")
        buf.write("\u00ab\2\u00ab\2\u00b0\2\u00b0\2\u203e\2\u203e\2\u204b")
        buf.write("\2\u204b\2\u2124\2\u2124\2\u213b\2\u213b\2\u2196\2\u219b")
        buf.write("\2\u21ab\2\u21ac\2\u231c\2\u231d\2\u232a\2\u232a\2\u23d1")
        buf.write("\2\u23d1\2\u23eb\2\u23f5\2\u23fa\2\u23fc\2\u24c4\2\u24c4")
        buf.write("\2\u25ac\2\u25ad\2\u25b8\2\u25b8\2\u25c2\2\u25c2\2\u25fd")
        buf.write("\2\u2600\2\u2602\2\u2606\2\u2610\2\u2610\2\u2613\2\u2613")
        buf.write("\2\u2616\2\u2617\2\u261a\2\u261a\2\u261f\2\u261f\2\u2622")
        buf.write("\2\u2622\2\u2624\2\u2625\2\u2628\2\u2628\2\u262c\2\u262c")
        buf.write("\2\u2630\2\u2631\2\u263a\2\u263c\2\u2642\2\u2642\2\u2644")
        buf.write("\2\u2644\2\u264a\2\u2655\2\u2662\2\u2662\2\u2665\2\u2665")
        buf.write("\2\u2667\2\u2668\2\u266a\2\u266a\2\u267d\2\u267d\2\u2681")
        buf.write("\2\u2681\2\u2694\2\u2699\2\u269b\2\u269b\2\u269d\2\u269e")
        buf.write("\2\u26a2\2\u26a3\2\u26ac\2\u26ad\2\u26b2\2\u26b3\2\u26bf")
        buf.write("\2\u26c0\2\u26c6\2\u26c7\2\u26ca\2\u26ca\2\u26d0\2\u26d1")
        buf.write("\2\u26d3\2\u26d3\2\u26d5\2\u26d6\2\u26eb\2\u26ec\2\u26f2")
        buf.write("\2\u26f7\2\u26f9\2\u26fc\2\u26ff\2\u26ff\2\u2704\2\u2704")
        buf.write("\2\u2707\2\u2707\2\u270a\2\u270f\2\u2711\2\u2711\2\u2714")
        buf.write("\2\u2714\2\u2716\2\u2716\2\u2718\2\u2718\2\u271f\2\u271f")
        buf.write("\2\u2723\2\u2723\2\u272a\2\u272a\2\u2735\2\u2736\2\u2746")
        buf.write("\2\u2746\2\u2749\2\u2749\2\u274e\2\u274e\2\u2750\2\u2750")
        buf.write("\2\u2755\2\u2757\2\u2759\2\u2759\2\u2765\2\u2766\2\u2797")
        buf.write("\2\u2799\2\u27a3\2\u27a3\2\u27b2\2\u27b2\2\u27c1\2\u27c1")
        buf.write("\2\u2936\2\u2937\2\u2b07\2\u2b09\2\u2b1d\2\u2b1e\2\u2b52")
        buf.write("\2\u2b52\2\u2b57\2\u2b57\2\u3032\2\u3032\2\u303f\2\u303f")
        buf.write("\2\u3299\2\u3299\2\u329b\2\u329b\2\uf006\3\uf006\3\uf0d1")
        buf.write("\3\uf0d1\3\uf172\3\uf173\3\uf180\3\uf181\3\uf190\3\uf190")
        buf.write("\3\uf193\3\uf19c\3\uf1e8\3\uf201\3\uf203\3\uf204\3\uf21c")
        buf.write("\3\uf21c\3\uf231\3\uf231\3\uf234\3\uf23c\3\uf252\3\uf253")
        buf.write("\3\uf302\3\uf323\3\uf326\3\uf395\3\uf398\3\uf399\3\uf39b")
        buf.write("\3\uf39d\3\uf3a0\3\uf3f2\3\uf3f5\3\uf3f7\3\uf3f9\3\uf4ff")
        buf.write("\3\uf501\3\uf53f\3\uf54b\3\uf550\3\uf552\3\uf569\3\uf571")
        buf.write("\3\uf572\3\uf575\3\uf57c\3\uf589\3\uf589\3\uf58c\3\uf58f")
        buf.write("\3\uf592\3\uf592\3\uf597\3\uf598\3\uf5a6\3\uf5a7\3\uf5aa")
        buf.write("\3\uf5aa\3\uf5b3\3\uf5b4\3\uf5be\3\uf5be\3\uf5c4\3\uf5c6")
        buf.write("\3\uf5d3\3\uf5d5\3\uf5de\3\uf5e0\3\uf5e3\3\uf5e3\3\uf5e5")
        buf.write("\3\uf5e5\3\uf5ea\3\uf5ea\3\uf5f1\3\uf5f1\3\uf5f5\3\uf5f5")
        buf.write("\3\uf5fc\3\uf651\3\uf682\3\uf6c7\3\uf6cd\3\uf6d4\3\uf6e2")
        buf.write("\3\uf6e7\3\uf6eb\3\uf6eb\3\uf6ed\3\uf6ee\3\uf6f2\3\uf6f2")
        buf.write("\3\uf6f5\3\uf6fa\3\uf912\3\uf93c\3\uf93e\3\uf940\3\uf942")
        buf.write("\3\uf947\3\uf949\3\uf94e\3\uf952\3\uf96d\3\uf982\3\uf999")
        buf.write("\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8\3\u0193\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2w\3\2\2\2\3y\3\2\2\2\5\u0080\3\2\2\2\7\u0092\3\2\2\2")
        buf.write("\t\u0096\3\2\2\2\13\u0098\3\2\2\2\r\u00a5\3\2\2\2\17\u00a7")
        buf.write("\3\2\2\2\21\u00ae\3\2\2\2\23\u00b6\3\2\2\2\25\u00bb\3")
        buf.write("\2\2\2\27\u00be\3\2\2\2\31\u00c0\3\2\2\2\33\u00c2\3\2")
        buf.write("\2\2\35\u00cf\3\2\2\2\37\u00d1\3\2\2\2!\u00d8\3\2\2\2")
        buf.write("#\u00df\3\2\2\2%\u00f2\3\2\2\2\'\u00f4\3\2\2\2)\u00f7")
        buf.write("\3\2\2\2+\u00fc\3\2\2\2-\u0100\3\2\2\2/\u0104\3\2\2\2")
        buf.write("\61\u0108\3\2\2\2\63\u010a\3\2\2\2\65\u010c\3\2\2\2\67")
        buf.write("\u0113\3\2\2\29\u0115\3\2\2\2;\u0117\3\2\2\2=\u0119\3")
        buf.write("\2\2\2?\u011b\3\2\2\2A\u011d\3\2\2\2C\u011f\3\2\2\2E\u0121")
        buf.write("\3\2\2\2G\u0123\3\2\2\2I\u0125\3\2\2\2K\u0127\3\2\2\2")
        buf.write("M\u0129\3\2\2\2O\u012b\3\2\2\2Q\u012d\3\2\2\2S\u012f\3")
        buf.write("\2\2\2U\u0131\3\2\2\2W\u0133\3\2\2\2Y\u0135\3\2\2\2[\u0137")
        buf.write("\3\2\2\2]\u0139\3\2\2\2_\u013b\3\2\2\2a\u013d\3\2\2\2")
        buf.write("c\u013f\3\2\2\2e\u0141\3\2\2\2g\u0143\3\2\2\2i\u0145\3")
        buf.write("\2\2\2k\u0147\3\2\2\2m\u0149\3\2\2\2o\u016d\3\2\2\2q\u0174")
        buf.write("\3\2\2\2s\u0176\3\2\2\2u\u017a\3\2\2\2w\u017c\3\2\2\2")
        buf.write("yz\7u\2\2z{\7j\2\2{|\7q\2\2|}\7t\2\2}~\7v\2\2~\4\3\2\2")
        buf.write("\2\177\u0081\t\2\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\b\3\2\2\u0085\6\3\2\2\2\u0086\u0087")
        buf.write("\6\4\2\2\u0087\u0093\5\5\3\2\u0088\u008a\7\17\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u008e\7\f\2\2\u008c\u008e\4\16\17\2\u008d\u0089")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\u0090\3\2\2\2\u008f")
        buf.write("\u0091\5\5\3\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u0093\3\2\2\2\u0092\u0086\3\2\2\2\u0092\u008d\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\b\4\3\2\u0095\b")
        buf.write("\3\2\2\2\u0096\u0097\7^\2\2\u0097\n\3\2\2\2\u0098\u009a")
        buf.write("\5\t\5\2\u0099\u009b\5\5\3\2\u009a\u0099\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u00a1\3\2\2\2\u009c\u009e\7\17\2")
        buf.write("\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u00a2\7\f\2\2\u00a0\u00a2\7\17\2\2\u00a1")
        buf.write("\u009d\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\b\6\2\2\u00a4\f\3\2\2\2\u00a5\u00a6\7=\2")
        buf.write("\2\u00a6\16\3\2\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7o")
        buf.write("\2\2\u00a9\u00aa\7r\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7v\2\2\u00ad\20\3\2\2\2\u00ae\u00af")
        buf.write("\7r\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2")
        buf.write("\7m\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7i\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\22\3\2\2\2\u00b6\u00b7\7y\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7j\2\2\u00ba\24")
        buf.write("\3\2\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7u\2\2\u00bd\26")
        buf.write("\3\2\2\2\u00be\u00bf\7.\2\2\u00bf\30\3\2\2\2\u00c0\u00c1")
        buf.write("\7,\2\2\u00c1\32\3\2\2\2\u00c2\u00c3\5%\23\2\u00c3\u00c4")
        buf.write("\5\67\34\2\u00c4\u00c5\5/\30\2\u00c5\34\3\2\2\2\u00c6")
        buf.write("\u00c7\5%\23\2\u00c7\u00c8\5\67\34\2\u00c8\u00d0\3\2\2")
        buf.write("\2\u00c9\u00cb\5\67\34\2\u00ca\u00cc\5/\30\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00c6\3\2\2\2")
        buf.write("\u00cf\u00c9\3\2\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\5\63")
        buf.write("\32\2\u00d2\u00d4\5=\37\2\u00d3\u00d5\5+\26\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7 \3\2\2\2\u00d8\u00d9\5\63\32\2\u00d9")
        buf.write("\u00db\5W,\2\u00da\u00dc\5-\27\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\"\3\2\2\2\u00df\u00e0\5\63\32\2\u00e0\u00e2\5i")
        buf.write("\65\2\u00e1\u00e3\5\61\31\2\u00e2\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5$\3\2\2\2\u00e6\u00e8\5\63\32\2\u00e7\u00e6\3\2")
        buf.write("\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00f3\3\2\2\2\u00eb\u00ef\t\3\2\2\u00ec")
        buf.write("\u00ee\5/\30\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f3\3")
        buf.write("\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00e7\3\2\2\2\u00f2\u00eb")
        buf.write("\3\2\2\2\u00f3&\3\2\2\2\u00f4\u00f5\7,\2\2\u00f5\u00f6")
        buf.write("\7`\2\2\u00f6(\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8\u00f9")
        buf.write("\7`\2\2\u00f9*\3\2\2\2\u00fa\u00fd\5\63\32\2\u00fb\u00fd")
        buf.write("\t\4\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write(",\3\2\2\2\u00fe\u0101\5\63\32\2\u00ff\u0101\t\5\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101.\3\2\2\2\u0102")
        buf.write("\u0105\5\63\32\2\u0103\u0105\t\3\2\2\u0104\u0102\3\2\2")
        buf.write("\2\u0104\u0103\3\2\2\2\u0105\60\3\2\2\2\u0106\u0109\5")
        buf.write("\63\32\2\u0107\u0109\t\6\2\2\u0108\u0106\3\2\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109\62\3\2\2\2\u010a\u010b\t\7\2\2\u010b")
        buf.write("\64\3\2\2\2\u010c\u0110\5q9\2\u010d\u010f\5u;\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\66\3\2\2\2\u0112\u0110\3\2")
        buf.write("\2\2\u0113\u0114\7\60\2\2\u01148\3\2\2\2\u0115\u0116\7")
        buf.write("a\2\2\u0116:\3\2\2\2\u0117\u0118\t\b\2\2\u0118<\3\2\2")
        buf.write("\2\u0119\u011a\t\t\2\2\u011a>\3\2\2\2\u011b\u011c\t\n")
        buf.write("\2\2\u011c@\3\2\2\2\u011d\u011e\t\13\2\2\u011eB\3\2\2")
        buf.write("\2\u011f\u0120\t\f\2\2\u0120D\3\2\2\2\u0121\u0122\t\r")
        buf.write("\2\2\u0122F\3\2\2\2\u0123\u0124\t\16\2\2\u0124H\3\2\2")
        buf.write("\2\u0125\u0126\t\17\2\2\u0126J\3\2\2\2\u0127\u0128\t\20")
        buf.write("\2\2\u0128L\3\2\2\2\u0129\u012a\t\21\2\2\u012aN\3\2\2")
        buf.write("\2\u012b\u012c\t\22\2\2\u012cP\3\2\2\2\u012d\u012e\t\23")
        buf.write("\2\2\u012eR\3\2\2\2\u012f\u0130\t\24\2\2\u0130T\3\2\2")
        buf.write("\2\u0131\u0132\t\25\2\2\u0132V\3\2\2\2\u0133\u0134\t\26")
        buf.write("\2\2\u0134X\3\2\2\2\u0135\u0136\t\27\2\2\u0136Z\3\2\2")
        buf.write("\2\u0137\u0138\t\30\2\2\u0138\\\3\2\2\2\u0139\u013a\t")
        buf.write("\31\2\2\u013a^\3\2\2\2\u013b\u013c\t\32\2\2\u013c`\3\2")
        buf.write("\2\2\u013d\u013e\t\33\2\2\u013eb\3\2\2\2\u013f\u0140\t")
        buf.write("\34\2\2\u0140d\3\2\2\2\u0141\u0142\t\35\2\2\u0142f\3\2")
        buf.write("\2\2\u0143\u0144\t\36\2\2\u0144h\3\2\2\2\u0145\u0146\t")
        buf.write("\37\2\2\u0146j\3\2\2\2\u0147\u0148\t \2\2\u0148l\3\2\2")
        buf.write("\2\u0149\u014a\t!\2\2\u014an\3\2\2\2\u014b\u0153\5;\36")
        buf.write("\2\u014c\u0153\5=\37\2\u014d\u0153\5? \2\u014e\u0153\5")
        buf.write("A!\2\u014f\u0153\5C\"\2\u0150\u0153\5E#\2\u0151\u0153")
        buf.write("\5G$\2\u0152\u014b\3\2\2\2\u0152\u014c\3\2\2\2\u0152\u014d")
        buf.write("\3\2\2\2\u0152\u014e\3\2\2\2\u0152\u014f\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\u016e\3\2\2\2")
        buf.write("\u0154\u015c\5I%\2\u0155\u015c\5K&\2\u0156\u015c\5M\'")
        buf.write("\2\u0157\u015c\5O(\2\u0158\u015c\5Q)\2\u0159\u015c\5S")
        buf.write("*\2\u015a\u015c\5U+\2\u015b\u0154\3\2\2\2\u015b\u0155")
        buf.write("\3\2\2\2\u015b\u0156\3\2\2\2\u015b\u0157\3\2\2\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015c\u016e\3\2\2\2\u015d\u0164\5W,\2\u015e\u0164\5Y")
        buf.write("-\2\u015f\u0164\5[.\2\u0160\u0164\5]/\2\u0161\u0164\5")
        buf.write("_\60\2\u0162\u0164\5a\61\2\u0163\u015d\3\2\2\2\u0163\u015e")
        buf.write("\3\2\2\2\u0163\u015f\3\2\2\2\u0163\u0160\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0162\3\2\2\2\u0164\u016e\3\2\2\2")
        buf.write("\u0165\u016c\5c\62\2\u0166\u016c\5e\63\2\u0167\u016c\5")
        buf.write("g\64\2\u0168\u016c\5i\65\2\u0169\u016c\5k\66\2\u016a\u016c")
        buf.write("\5m\67\2\u016b\u0165\3\2\2\2\u016b\u0166\3\2\2\2\u016b")
        buf.write("\u0167\3\2\2\2\u016b\u0168\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016b\u016a\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u0152\3")
        buf.write("\2\2\2\u016d\u015b\3\2\2\2\u016d\u0163\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016ep\3\2\2\2\u016f\u0172\59\35\2\u0170\u0172")
        buf.write("\5o8\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0175")
        buf.write("\3\2\2\2\u0173\u0175\t#\2\2\u0174\u0171\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175r\3\2\2\2\u0176\u0177\t$\2\2\u0177")
        buf.write("t\3\2\2\2\u0178\u017b\5q9\2\u0179\u017b\5/\30\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017bv\3\2\2\2\u017c")
        buf.write("\u0180\7%\2\2\u017d\u017f\n\"\2\2\u017e\u017d\3\2\2\2")
        buf.write("\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3")
        buf.write("\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184")
        buf.write("\b<\4\2\u0184x\3\2\2\2!\2\u0082\u0089\u008d\u0090\u0092")
        buf.write("\u009a\u009d\u00a1\u00cd\u00cf\u00d6\u00dd\u00e4\u00e9")
        buf.write("\u00ef\u00f2\u00fc\u0100\u0104\u0108\u0110\u0152\u015b")
        buf.write("\u0163\u016b\u016d\u0171\u0174\u017a\u0180\5\b\2\2\3\4")
        buf.write("\2\2\3\2")
        return buf.getvalue()


class BasisLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    SPACES = 2
    NEWLINE = 3
    Escape = 4
    JoinLine = 5
    Semicolon = 6
    Import = 7
    Package = 8
    With = 9
    As = 10
    Comma = 11
    Star = 12
    Decimal = 13
    DecimalBad = 14
    Binary = 15
    Octal = 16
    Hexadecimal = 17
    Integer = 18
    Exponent = 19
    Base = 20
    Symbol = 21
    Dot = 22
    Underline = 23
    LineComment = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'short'", "'\\'", "';'", "'import'", "'package'", "'with'", 
            "'as'", "','", "'*'", "'*^'", "'/^'", "'.'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "NEWLINE", "Escape", "JoinLine", "Semicolon", "Import", 
            "Package", "With", "As", "Comma", "Star", "Decimal", "DecimalBad", 
            "Binary", "Octal", "Hexadecimal", "Integer", "Exponent", "Base", 
            "Symbol", "Dot", "Underline", "LineComment" ]

    ruleNames = [ "T__0", "SPACES", "NEWLINE", "Escape", "JoinLine", "Semicolon", 
                  "Import", "Package", "With", "As", "Comma", "Star", "Decimal", 
                  "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
                  "Exponent", "Base", "Bin", "Oct", "Digit", "Hex", "Zero", 
                  "Symbol", "Dot", "Underline", "A", "B", "C", "D", "E", 
                  "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Letter", 
                  "NameStartCharacter", "EmojiCharacter", "NameCharacter", 
                  "LineComment" ]

    grammarFileName = "Basis.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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

     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[2] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


