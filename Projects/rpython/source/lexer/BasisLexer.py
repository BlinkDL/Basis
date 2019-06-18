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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.")
        buf.write("\u022d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\3\2\6\2\u00af\n\2\r\2\16\2\u00b0\3\2\3\2\3\3\3")
        buf.write("\3\5\3\u00b7\n\3\3\3\5\3\u00ba\n\3\3\3\3\3\5\3\u00be\n")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\5\4\u00c5\n\4\3\4\3\4\5\4\u00c9")
        buf.write("\n\4\3\4\5\4\u00cc\n\4\5\4\u00ce\n\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\6\25")
        buf.write("\u0110\n\25\r\25\16\25\u0111\3\25\3\25\3\26\3\26\6\26")
        buf.write("\u0118\n\26\r\26\16\26\u0119\3\26\3\26\3\27\3\27\6\27")
        buf.write("\u0120\n\27\r\27\16\27\u0121\3\27\3\27\3\30\3\30\6\30")
        buf.write("\u0128\n\30\r\30\16\30\u0129\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u013a")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u014c\n\36\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0152\n\37\3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\3!\6!\u015d\n!\r!\16!\u015e\5!\u0161\n!\3\"\3\"\3\"\6")
        buf.write("\"\u0166\n\"\r\"\16\"\u0167\3#\3#\3#\6#\u016d\n#\r#\16")
        buf.write("#\u016e\3$\3$\3$\6$\u0174\n$\r$\16$\u0175\3%\6%\u0179")
        buf.write("\n%\r%\16%\u017a\3%\3%\7%\u017f\n%\f%\16%\u0182\13%\5")
        buf.write("%\u0184\n%\3&\3&\3&\3\'\3\'\3\'\3(\3(\5(\u018e\n(\3)\3")
        buf.write(")\5)\u0192\n)\3*\3*\5*\u0196\n*\3+\3+\5+\u019a\n+\3,\3")
        buf.write(",\3-\3-\7-\u01a0\n-\f-\16-\u01a3\13-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3J\3J\3J\3J\5J\u01e4\n")
        buf.write("J\3J\3J\3J\3J\3J\3J\3J\5J\u01ed\nJ\3J\3J\3J\3J\3J\3J\5")
        buf.write("J\u01f5\nJ\3J\3J\3J\3J\3J\3J\5J\u01fd\nJ\5J\u01ff\nJ\3")
        buf.write("K\3K\5K\u0203\nK\3K\5K\u0206\nK\3L\3L\3M\3M\5M\u020c\n")
        buf.write("M\3N\3N\7N\u0210\nN\fN\16N\u0213\13N\3N\3N\3O\3O\3O\3")
        buf.write("P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3V\3")
        buf.write("V\3V\6\u0111\u0119\u0121\u0129\2W\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\2\65\2\67\2")
        buf.write("9\2;\2=\2?\33A\34C\35E\36G\37I K!M\"O\2Q\2S\2U\2W\2Y#")
        buf.write("[$]%_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("&\u009d\'\u009f(\u00a1)\u00a3*\u00a5+\u00a7,\u00a9-\u00ab")
        buf.write(".\3\2\'\4\2\13\13\"\"\3\2))\3\2\"\"\3\2^^\4\2))^^\3\2")
        buf.write("\63;\3\2\63\63\3\2\639\5\2\63;CHch\3\2\62\62\4\2CCcc\4")
        buf.write("\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJj")
        buf.write("j\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2")
        buf.write("QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4")
        buf.write("\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f\17\17")
        buf.write("\4Y\2C\2\\\2c\2|\2\u00ac\2\u00ac\2\u00bc\2\u00bc\2\u00c2")
        buf.write("\2\u00d8\2\u00da\2\u00f8\2\u00fa\2\u02ba\2\u02e2\2\u02e6")
        buf.write("\2\u0372\2\u0375\2\u0377\2\u0379\2\u037c\2\u037f\2\u0381")
        buf.write("\2\u0381\2\u0386\2\u0386\2\u0388\2\u0388\2\u038a\2\u038c")
        buf.write("\2\u038e\2\u038e\2\u0390\2\u03a3\2\u03a5\2\u03e3\2\u03f2")
        buf.write("\2\u0401\2\u1d02\2\u1d2c\2\u1d2e\2\u1d79\2\u1d7b\2\u1dc1")
        buf.write("\2\u1e02\2\u1f17\2\u1f1a\2\u1f1f\2\u1f22\2\u1f47\2\u1f4a")
        buf.write("\2\u1f4f\2\u1f52\2\u1f59\2\u1f5b\2\u1f5b\2\u1f5d\2\u1f5d")
        buf.write("\2\u1f5f\2\u1f5f\2\u1f61\2\u1f7f\2\u1f82\2\u1fb6\2\u1fb8")
        buf.write("\2\u1fc6\2\u1fc8\2\u1fd5\2\u1fd8\2\u1fdd\2\u1fdf\2\u1ff1")
        buf.write("\2\u1ff4\2\u1ff6\2\u1ff8\2\u2000\2\u2073\2\u2073\2\u2081")
        buf.write("\2\u2081\2\u2092\2\u209e\2\u2128\2\u2128\2\u212c\2\u212d")
        buf.write("\2\u2134\2\u2134\2\u2150\2\u2150\2\u2162\2\u218a\2\u2c62")
        buf.write("\2\u2c81\2\u2e82\2\u2e9b\2\u2e9d\2\u2ef5\2\u2f02\2\u2fd7")
        buf.write("\2\u3007\2\u3007\2\u3009\2\u3009\2\u3023\2\u302b\2\u303a")
        buf.write("\2\u303d\2\u3043\2\u3098\2\u309f\2\u30a1\2\u30a3\2\u30fc")
        buf.write("\2\u30ff\2\u3101\2\u31f2\2\u3201\2\u32d2\2\u3300\2\u3302")
        buf.write("\2\u3359\2\u3402\2\u4db7\2\u4e02\2\u9fec\2\ua724\2\ua789")
        buf.write("\2\ua78d\2\ua7b0\2\ua7b2\2\ua7b9\2\ua7f9\2\ua801\2\uab32")
        buf.write("\2\uab5c\2\uab5e\2\uab67\2\uf902\2\ufa6f\2\ufa72\2\ufadb")
        buf.write("\2\ufb02\2\ufb08\2\uff23\2\uff3c\2\uff43\2\uff5c\2\uff68")
        buf.write("\2\uff71\2\uff73\2\uff9f\2\u0142\3\u0190\3\u01a2\3\u01a2")
        buf.write("\3\ub002\3\ub120\3\ud202\3\ud247\3\uf202\3\uf202\3\2\4")
        buf.write("\ua6d8\4\ua702\4\ub736\4\ub742\4\ub81f\4\ub822\4\ucea3")
        buf.write("\4\uceb2\4\uebe2\4\uf802\4\ufa1f\4\u0093\2%\2%\2,\2,\2")
        buf.write("\62\2;\2\u00ab\2\u00ab\2\u00b0\2\u00b0\2\u203e\2\u203e")
        buf.write("\2\u204b\2\u204b\2\u2124\2\u2124\2\u213b\2\u213b\2\u2196")
        buf.write("\2\u219b\2\u21ab\2\u21ac\2\u231c\2\u231d\2\u232a\2\u232a")
        buf.write("\2\u23d1\2\u23d1\2\u23eb\2\u23f5\2\u23fa\2\u23fc\2\u24c4")
        buf.write("\2\u24c4\2\u25ac\2\u25ad\2\u25b8\2\u25b8\2\u25c2\2\u25c2")
        buf.write("\2\u25fd\2\u2600\2\u2602\2\u2606\2\u2610\2\u2610\2\u2613")
        buf.write("\2\u2613\2\u2616\2\u2617\2\u261a\2\u261a\2\u261f\2\u261f")
        buf.write("\2\u2622\2\u2622\2\u2624\2\u2625\2\u2628\2\u2628\2\u262c")
        buf.write("\2\u262c\2\u2630\2\u2631\2\u263a\2\u263c\2\u2642\2\u2642")
        buf.write("\2\u2644\2\u2644\2\u264a\2\u2655\2\u2662\2\u2662\2\u2665")
        buf.write("\2\u2665\2\u2667\2\u2668\2\u266a\2\u266a\2\u267d\2\u267d")
        buf.write("\2\u2681\2\u2681\2\u2694\2\u2699\2\u269b\2\u269b\2\u269d")
        buf.write("\2\u269e\2\u26a2\2\u26a3\2\u26ac\2\u26ad\2\u26b2\2\u26b3")
        buf.write("\2\u26bf\2\u26c0\2\u26c6\2\u26c7\2\u26ca\2\u26ca\2\u26d0")
        buf.write("\2\u26d1\2\u26d3\2\u26d3\2\u26d5\2\u26d6\2\u26eb\2\u26ec")
        buf.write("\2\u26f2\2\u26f7\2\u26f9\2\u26fc\2\u26ff\2\u26ff\2\u2704")
        buf.write("\2\u2704\2\u2707\2\u2707\2\u270a\2\u270f\2\u2711\2\u2711")
        buf.write("\2\u2714\2\u2714\2\u2716\2\u2716\2\u2718\2\u2718\2\u271f")
        buf.write("\2\u271f\2\u2723\2\u2723\2\u272a\2\u272a\2\u2735\2\u2736")
        buf.write("\2\u2746\2\u2746\2\u2749\2\u2749\2\u274e\2\u274e\2\u2750")
        buf.write("\2\u2750\2\u2755\2\u2757\2\u2759\2\u2759\2\u2765\2\u2766")
        buf.write("\2\u2797\2\u2799\2\u27a3\2\u27a3\2\u27b2\2\u27b2\2\u27c1")
        buf.write("\2\u27c1\2\u2936\2\u2937\2\u2b07\2\u2b09\2\u2b1d\2\u2b1e")
        buf.write("\2\u2b52\2\u2b52\2\u2b57\2\u2b57\2\u3032\2\u3032\2\u303f")
        buf.write("\2\u303f\2\u3299\2\u3299\2\u329b\2\u329b\2\uf006\3\uf006")
        buf.write("\3\uf0d1\3\uf0d1\3\uf172\3\uf173\3\uf180\3\uf181\3\uf190")
        buf.write("\3\uf190\3\uf193\3\uf19c\3\uf1e8\3\uf201\3\uf203\3\uf204")
        buf.write("\3\uf21c\3\uf21c\3\uf231\3\uf231\3\uf234\3\uf23c\3\uf252")
        buf.write("\3\uf253\3\uf302\3\uf323\3\uf326\3\uf395\3\uf398\3\uf399")
        buf.write("\3\uf39b\3\uf39d\3\uf3a0\3\uf3f2\3\uf3f5\3\uf3f7\3\uf3f9")
        buf.write("\3\uf4ff\3\uf501\3\uf53f\3\uf54b\3\uf550\3\uf552\3\uf569")
        buf.write("\3\uf571\3\uf572\3\uf575\3\uf57c\3\uf589\3\uf589\3\uf58c")
        buf.write("\3\uf58f\3\uf592\3\uf592\3\uf597\3\uf598\3\uf5a6\3\uf5a7")
        buf.write("\3\uf5aa\3\uf5aa\3\uf5b3\3\uf5b4\3\uf5be\3\uf5be\3\uf5c4")
        buf.write("\3\uf5c6\3\uf5d3\3\uf5d5\3\uf5de\3\uf5e0\3\uf5e3\3\uf5e3")
        buf.write("\3\uf5e5\3\uf5e5\3\uf5ea\3\uf5ea\3\uf5f1\3\uf5f1\3\uf5f5")
        buf.write("\3\uf5f5\3\uf5fc\3\uf651\3\uf682\3\uf6c7\3\uf6cd\3\uf6d4")
        buf.write("\3\uf6e2\3\uf6e7\3\uf6eb\3\uf6eb\3\uf6ed\3\uf6ee\3\uf6f2")
        buf.write("\3\uf6f2\3\uf6f5\3\uf6fa\3\uf912\3\uf93c\3\uf93e\3\uf940")
        buf.write("\3\uf942\3\uf947\3\uf949\3\uf94e\3\uf952\3\uf96d\3\uf982")
        buf.write("\3\uf999\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8\3\u023e\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\3\u00ae\3\2\2\2\5\u00b4\3\2\2\2\7\u00cd\3\2\2")
        buf.write("\2\t\u00d1\3\2\2\2\13\u00d3\3\2\2\2\r\u00d5\3\2\2\2\17")
        buf.write("\u00dc\3\2\2\2\21\u00e4\3\2\2\2\23\u00e9\3\2\2\2\25\u00ec")
        buf.write("\3\2\2\2\27\u00ee\3\2\2\2\31\u00f0\3\2\2\2\33\u00f3\3")
        buf.write("\2\2\2\35\u00f8\3\2\2\2\37\u00fc\3\2\2\2!\u00ff\3\2\2")
        buf.write("\2#\u0102\3\2\2\2%\u0104\3\2\2\2\'\u0106\3\2\2\2)\u010d")
        buf.write("\3\2\2\2+\u0115\3\2\2\2-\u011d\3\2\2\2/\u0125\3\2\2\2")
        buf.write("\61\u0139\3\2\2\2\63\u013b\3\2\2\2\65\u013f\3\2\2\2\67")
        buf.write("\u0143\3\2\2\29\u0145\3\2\2\2;\u014b\3\2\2\2=\u0151\3")
        buf.write("\2\2\2?\u0153\3\2\2\2A\u0160\3\2\2\2C\u0162\3\2\2\2E\u0169")
        buf.write("\3\2\2\2G\u0170\3\2\2\2I\u0183\3\2\2\2K\u0185\3\2\2\2")
        buf.write("M\u0188\3\2\2\2O\u018d\3\2\2\2Q\u0191\3\2\2\2S\u0195\3")
        buf.write("\2\2\2U\u0199\3\2\2\2W\u019b\3\2\2\2Y\u019d\3\2\2\2[\u01a4")
        buf.write("\3\2\2\2]\u01a6\3\2\2\2_\u01a8\3\2\2\2a\u01aa\3\2\2\2")
        buf.write("c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3\2\2\2i\u01b2\3")
        buf.write("\2\2\2k\u01b4\3\2\2\2m\u01b6\3\2\2\2o\u01b8\3\2\2\2q\u01ba")
        buf.write("\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01c0\3\2\2\2")
        buf.write("y\u01c2\3\2\2\2{\u01c4\3\2\2\2}\u01c6\3\2\2\2\177\u01c8")
        buf.write("\3\2\2\2\u0081\u01ca\3\2\2\2\u0083\u01cc\3\2\2\2\u0085")
        buf.write("\u01ce\3\2\2\2\u0087\u01d0\3\2\2\2\u0089\u01d2\3\2\2\2")
        buf.write("\u008b\u01d4\3\2\2\2\u008d\u01d6\3\2\2\2\u008f\u01d8\3")
        buf.write("\2\2\2\u0091\u01da\3\2\2\2\u0093\u01fe\3\2\2\2\u0095\u0205")
        buf.write("\3\2\2\2\u0097\u0207\3\2\2\2\u0099\u020b\3\2\2\2\u009b")
        buf.write("\u020d\3\2\2\2\u009d\u0216\3\2\2\2\u009f\u0219\3\2\2\2")
        buf.write("\u00a1\u021c\3\2\2\2\u00a3\u021f\3\2\2\2\u00a5\u0222\3")
        buf.write("\2\2\2\u00a7\u0225\3\2\2\2\u00a9\u0228\3\2\2\2\u00ab\u022a")
        buf.write("\3\2\2\2\u00ad\u00af\t\2\2\2\u00ae\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b3\b\2\2\2\u00b3\4\3\2\2")
        buf.write("\2\u00b4\u00b6\5\t\5\2\u00b5\u00b7\5\3\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00bd\3\2\2\2\u00b8")
        buf.write("\u00ba\7\17\2\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2")
        buf.write("\2\u00ba\u00bb\3\2\2\2\u00bb\u00be\7\f\2\2\u00bc\u00be")
        buf.write("\7\17\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c0\b\3\2\2\u00c0\6\3\2\2\2\u00c1")
        buf.write("\u00c2\6\4\2\2\u00c2\u00ce\5\3\2\2\u00c3\u00c5\7\17\2")
        buf.write("\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00c9\7\f\2\2\u00c7\u00c9\4\16\17\2\u00c8")
        buf.write("\u00c4\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00cb\3\2\2\2")
        buf.write("\u00ca\u00cc\5\3\2\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3")
        buf.write("\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00c1\3\2\2\2\u00cd\u00c8")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\b\4\3\2\u00d0")
        buf.write("\b\3\2\2\2\u00d1\u00d2\7^\2\2\u00d2\n\3\2\2\2\u00d3\u00d4")
        buf.write("\7=\2\2\u00d4\f\3\2\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7o\2\2\u00d7\u00d8\7r\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7t\2\2\u00da\u00db\7v\2\2\u00db\16\3\2\2\2\u00dc\u00dd")
        buf.write("\7r\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7m\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7i\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\20\3\2\2\2\u00e4\u00e5\7y\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8\7j\2\2\u00e8\22")
        buf.write("\3\2\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7u\2\2\u00eb\24")
        buf.write("\3\2\2\2\u00ec\u00ed\7.\2\2\u00ed\26\3\2\2\2\u00ee\u00ef")
        buf.write("\7,\2\2\u00ef\30\3\2\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2\32\3\2\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7\7g\2\2\u00f7\34")
        buf.write("\3\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\36\3\2\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe \3\2\2\2\u00ff\u0100\7?\2\2\u0100\u0101")
        buf.write("\7@\2\2\u0101\"\3\2\2\2\u0102\u0103\7<\2\2\u0103$\3\2")
        buf.write("\2\2\u0104\u0105\7?\2\2\u0105&\3\2\2\2\u0106\u0107\7t")
        buf.write("\2\2\u0107\u0108\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7t\2\2\u010b\u010c\7p\2\2\u010c(\3")
        buf.write("\2\2\2\u010d\u010f\5\63\32\2\u010e\u0110\5;\36\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\5")
        buf.write("\63\32\2\u0114*\3\2\2\2\u0115\u0117\5\67\34\2\u0116\u0118")
        buf.write("\5=\37\2\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\3\2\2\2")
        buf.write("\u011b\u011c\5\67\34\2\u011c,\3\2\2\2\u011d\u011f\5\65")
        buf.write("\33\2\u011e\u0120\13\2\2\2\u011f\u011e\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0121\u011f\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\u0124\5\65\33\2\u0124.\3\2\2\2\u0125")
        buf.write("\u0127\59\35\2\u0126\u0128\n\3\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129\u012a\3\2\2\2\u0129\u0127\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\59\35\2\u012c\60")
        buf.write("\3\2\2\2\u012d\u012e\5\63\32\2\u012e\u012f\5\63\32\2\u012f")
        buf.write("\u013a\3\2\2\2\u0130\u0131\5\65\33\2\u0131\u0132\5\65")
        buf.write("\33\2\u0132\u013a\3\2\2\2\u0133\u0134\5\67\34\2\u0134")
        buf.write("\u0135\5\67\34\2\u0135\u013a\3\2\2\2\u0136\u0137\59\35")
        buf.write("\2\u0137\u0138\59\35\2\u0138\u013a\3\2\2\2\u0139\u012d")
        buf.write("\3\2\2\2\u0139\u0130\3\2\2\2\u0139\u0133\3\2\2\2\u0139")
        buf.write("\u0136\3\2\2\2\u013a\62\3\2\2\2\u013b\u013c\7$\2\2\u013c")
        buf.write("\u013d\7$\2\2\u013d\u013e\7$\2\2\u013e\64\3\2\2\2\u013f")
        buf.write("\u0140\7)\2\2\u0140\u0141\7)\2\2\u0141\u0142\7)\2\2\u0142")
        buf.write("\66\3\2\2\2\u0143\u0144\7$\2\2\u01448\3\2\2\2\u0145\u0146")
        buf.write("\7)\2\2\u0146:\3\2\2\2\u0147\u0148\5\t\5\2\u0148\u0149")
        buf.write("\n\4\2\2\u0149\u014c\3\2\2\2\u014a\u014c\n\5\2\2\u014b")
        buf.write("\u0147\3\2\2\2\u014b\u014a\3\2\2\2\u014c<\3\2\2\2\u014d")
        buf.write("\u014e\5\t\5\2\u014e\u014f\n\4\2\2\u014f\u0152\3\2\2\2")
        buf.write("\u0150\u0152\n\6\2\2\u0151\u014d\3\2\2\2\u0151\u0150\3")
        buf.write("\2\2\2\u0152>\3\2\2\2\u0153\u0154\5I%\2\u0154\u0155\5")
        buf.write("[.\2\u0155\u0156\5S*\2\u0156@\3\2\2\2\u0157\u0158\5I%")
        buf.write("\2\u0158\u0159\5[.\2\u0159\u0161\3\2\2\2\u015a\u015c\5")
        buf.write("[.\2\u015b\u015d\5S*\2\u015c\u015b\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0161\3\2\2\2\u0160\u0157\3\2\2\2\u0160\u015a\3\2\2\2")
        buf.write("\u0161B\3\2\2\2\u0162\u0163\5W,\2\u0163\u0165\5a\61\2")
        buf.write("\u0164\u0166\5O(\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2")
        buf.write("\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168D\3")
        buf.write("\2\2\2\u0169\u016a\5W,\2\u016a\u016c\5{>\2\u016b\u016d")
        buf.write("\5Q)\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016fF\3\2\2\2\u0170\u0171")
        buf.write("\5W,\2\u0171\u0173\5\u008dG\2\u0172\u0174\5U+\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176H\3\2\2\2\u0177\u0179\5W,\2")
        buf.write("\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017b\u0184\3\2\2\2\u017c\u0180")
        buf.write("\t\7\2\2\u017d\u017f\5S*\2\u017e\u017d\3\2\2\2\u017f\u0182")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0178\3\2\2\2")
        buf.write("\u0183\u017c\3\2\2\2\u0184J\3\2\2\2\u0185\u0186\7,\2\2")
        buf.write("\u0186\u0187\7`\2\2\u0187L\3\2\2\2\u0188\u0189\7\61\2")
        buf.write("\2\u0189\u018a\7`\2\2\u018aN\3\2\2\2\u018b\u018e\5W,\2")
        buf.write("\u018c\u018e\t\b\2\2\u018d\u018b\3\2\2\2\u018d\u018c\3")
        buf.write("\2\2\2\u018eP\3\2\2\2\u018f\u0192\5W,\2\u0190\u0192\t")
        buf.write("\t\2\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192R")
        buf.write("\3\2\2\2\u0193\u0196\5W,\2\u0194\u0196\t\7\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0195\u0194\3\2\2\2\u0196T\3\2\2\2\u0197\u019a")
        buf.write("\5W,\2\u0198\u019a\t\n\2\2\u0199\u0197\3\2\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019aV\3\2\2\2\u019b\u019c\t\13\2\2\u019cX\3")
        buf.write("\2\2\2\u019d\u01a1\5\u0095K\2\u019e\u01a0\5\u0099M\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2Z\3\2\2\2\u01a3\u01a1\3\2\2")
        buf.write("\2\u01a4\u01a5\7\60\2\2\u01a5\\\3\2\2\2\u01a6\u01a7\7")
        buf.write("a\2\2\u01a7^\3\2\2\2\u01a8\u01a9\t\f\2\2\u01a9`\3\2\2")
        buf.write("\2\u01aa\u01ab\t\r\2\2\u01abb\3\2\2\2\u01ac\u01ad\t\16")
        buf.write("\2\2\u01add\3\2\2\2\u01ae\u01af\t\17\2\2\u01aff\3\2\2")
        buf.write("\2\u01b0\u01b1\t\20\2\2\u01b1h\3\2\2\2\u01b2\u01b3\t\21")
        buf.write("\2\2\u01b3j\3\2\2\2\u01b4\u01b5\t\22\2\2\u01b5l\3\2\2")
        buf.write("\2\u01b6\u01b7\t\23\2\2\u01b7n\3\2\2\2\u01b8\u01b9\t\24")
        buf.write("\2\2\u01b9p\3\2\2\2\u01ba\u01bb\t\25\2\2\u01bbr\3\2\2")
        buf.write("\2\u01bc\u01bd\t\26\2\2\u01bdt\3\2\2\2\u01be\u01bf\t\27")
        buf.write("\2\2\u01bfv\3\2\2\2\u01c0\u01c1\t\30\2\2\u01c1x\3\2\2")
        buf.write("\2\u01c2\u01c3\t\31\2\2\u01c3z\3\2\2\2\u01c4\u01c5\t\32")
        buf.write("\2\2\u01c5|\3\2\2\2\u01c6\u01c7\t\33\2\2\u01c7~\3\2\2")
        buf.write("\2\u01c8\u01c9\t\34\2\2\u01c9\u0080\3\2\2\2\u01ca\u01cb")
        buf.write("\t\35\2\2\u01cb\u0082\3\2\2\2\u01cc\u01cd\t\36\2\2\u01cd")
        buf.write("\u0084\3\2\2\2\u01ce\u01cf\t\37\2\2\u01cf\u0086\3\2\2")
        buf.write("\2\u01d0\u01d1\t \2\2\u01d1\u0088\3\2\2\2\u01d2\u01d3")
        buf.write("\t!\2\2\u01d3\u008a\3\2\2\2\u01d4\u01d5\t\"\2\2\u01d5")
        buf.write("\u008c\3\2\2\2\u01d6\u01d7\t#\2\2\u01d7\u008e\3\2\2\2")
        buf.write("\u01d8\u01d9\t$\2\2\u01d9\u0090\3\2\2\2\u01da\u01db\t")
        buf.write("%\2\2\u01db\u0092\3\2\2\2\u01dc\u01e4\5_\60\2\u01dd\u01e4")
        buf.write("\5a\61\2\u01de\u01e4\5c\62\2\u01df\u01e4\5e\63\2\u01e0")
        buf.write("\u01e4\5g\64\2\u01e1\u01e4\5i\65\2\u01e2\u01e4\5k\66\2")
        buf.write("\u01e3\u01dc\3\2\2\2\u01e3\u01dd\3\2\2\2\u01e3\u01de\3")
        buf.write("\2\2\2\u01e3\u01df\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01ff\3\2\2\2\u01e5")
        buf.write("\u01ed\5m\67\2\u01e6\u01ed\5o8\2\u01e7\u01ed\5q9\2\u01e8")
        buf.write("\u01ed\5s:\2\u01e9\u01ed\5u;\2\u01ea\u01ed\5w<\2\u01eb")
        buf.write("\u01ed\5y=\2\u01ec\u01e5\3\2\2\2\u01ec\u01e6\3\2\2\2\u01ec")
        buf.write("\u01e7\3\2\2\2\u01ec\u01e8\3\2\2\2\u01ec\u01e9\3\2\2\2")
        buf.write("\u01ec\u01ea\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ff\3")
        buf.write("\2\2\2\u01ee\u01f5\5{>\2\u01ef\u01f5\5}?\2\u01f0\u01f5")
        buf.write("\5\177@\2\u01f1\u01f5\5\u0081A\2\u01f2\u01f5\5\u0083B")
        buf.write("\2\u01f3\u01f5\5\u0085C\2\u01f4\u01ee\3\2\2\2\u01f4\u01ef")
        buf.write("\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01ff\3\2\2\2")
        buf.write("\u01f6\u01fd\5\u0087D\2\u01f7\u01fd\5\u0089E\2\u01f8\u01fd")
        buf.write("\5\u008bF\2\u01f9\u01fd\5\u008dG\2\u01fa\u01fd\5\u008f")
        buf.write("H\2\u01fb\u01fd\5\u0091I\2\u01fc\u01f6\3\2\2\2\u01fc\u01f7")
        buf.write("\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fc\u01f9\3\2\2\2\u01fc")
        buf.write("\u01fa\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01ff\3\2\2\2")
        buf.write("\u01fe\u01e3\3\2\2\2\u01fe\u01ec\3\2\2\2\u01fe\u01f4\3")
        buf.write("\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u0094\3\2\2\2\u0200\u0203")
        buf.write("\5]/\2\u0201\u0203\5\u0093J\2\u0202\u0200\3\2\2\2\u0202")
        buf.write("\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0206\t\'\2\2")
        buf.write("\u0205\u0202\3\2\2\2\u0205\u0204\3\2\2\2\u0206\u0096\3")
        buf.write("\2\2\2\u0207\u0208\t(\2\2\u0208\u0098\3\2\2\2\u0209\u020c")
        buf.write("\5\u0095K\2\u020a\u020c\5S*\2\u020b\u0209\3\2\2\2\u020b")
        buf.write("\u020a\3\2\2\2\u020c\u009a\3\2\2\2\u020d\u0211\7%\2\2")
        buf.write("\u020e\u0210\n&\2\2\u020f\u020e\3\2\2\2\u0210\u0213\3")
        buf.write("\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214")
        buf.write("\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0215\bN\4\2\u0215")
        buf.write("\u009c\3\2\2\2\u0216\u0217\7*\2\2\u0217\u0218\bO\5\2\u0218")
        buf.write("\u009e\3\2\2\2\u0219\u021a\7+\2\2\u021a\u021b\bP\6\2\u021b")
        buf.write("\u00a0\3\2\2\2\u021c\u021d\7]\2\2\u021d\u021e\bQ\7\2\u021e")
        buf.write("\u00a2\3\2\2\2\u021f\u0220\7_\2\2\u0220\u0221\bR\b\2\u0221")
        buf.write("\u00a4\3\2\2\2\u0222\u0223\7}\2\2\u0223\u0224\bS\t\2\u0224")
        buf.write("\u00a6\3\2\2\2\u0225\u0226\7\177\2\2\u0226\u0227\bT\n")
        buf.write("\2\u0227\u00a8\3\2\2\2\u0228\u0229\7\'\2\2\u0229\u00aa")
        buf.write("\3\2\2\2\u022a\u022b\7?\2\2\u022b\u022c\7?\2\2\u022c\u00ac")
        buf.write("\3\2\2\2(\2\u00b0\u00b6\u00b9\u00bd\u00c4\u00c8\u00cb")
        buf.write("\u00cd\u0111\u0119\u0121\u0129\u0139\u014b\u0151\u015e")
        buf.write("\u0160\u0167\u016e\u0175\u017a\u0180\u0183\u018d\u0191")
        buf.write("\u0195\u0199\u01a1\u01e3\u01ec\u01f4\u01fc\u01fe\u0202")
        buf.write("\u0205\u020b\u0211\13\b\2\2\3\4\2\2\3\2\3O\3\3P\4\3Q\5")
        buf.write("\3R\6\3S\7\3T\b")
        return buf.getvalue()


class BasisLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SPACES = 1
    JoinLine = 2
    NEWLINE = 3
    Escape = 4
    Semicolon = 5
    Import = 6
    Package = 7
    With = 8
    As = 9
    Comma = 10
    Star = 11
    If = 12
    Else = 13
    For = 14
    In = 15
    To = 16
    Colon = 17
    Set = 18
    Return = 19
    StringEscapeBlock = 20
    StringEscapeSingle = 21
    StringLiteralBlock = 22
    StringLiteralSingle = 23
    StringEmpty = 24
    Decimal = 25
    DecimalBad = 26
    Binary = 27
    Octal = 28
    Hexadecimal = 29
    Integer = 30
    Exponent = 31
    Base = 32
    Identifier = 33
    Dot = 34
    Underline = 35
    LineComment = 36
    OPEN_PAREN = 37
    CLOSE_PAREN = 38
    OPEN_BRACK = 39
    CLOSE_BRACK = 40
    OPEN_BRACE = 41
    CLOSE_BRACE = 42
    Modulo = 43
    Equal = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "';'", "'import'", "'package'", "'with'", "'as'", "','", 
            "'*'", "'if'", "'else'", "'for'", "'in'", "'=>'", "':'", "'='", 
            "'return'", "'*^'", "'/^'", "'.'", "'_'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'%'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "JoinLine", "NEWLINE", "Escape", "Semicolon", "Import", 
            "Package", "With", "As", "Comma", "Star", "If", "Else", "For", 
            "In", "To", "Colon", "Set", "Return", "StringEscapeBlock", "StringEscapeSingle", 
            "StringLiteralBlock", "StringLiteralSingle", "StringEmpty", 
            "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
            "Exponent", "Base", "Identifier", "Dot", "Underline", "LineComment", 
            "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
            "CLOSE_BRACE", "Modulo", "Equal" ]

    ruleNames = [ "SPACES", "JoinLine", "NEWLINE", "Escape", "Semicolon", 
                  "Import", "Package", "With", "As", "Comma", "Star", "If", 
                  "Else", "For", "In", "To", "Colon", "Set", "Return", "StringEscapeBlock", 
                  "StringEscapeSingle", "StringLiteralBlock", "StringLiteralSingle", 
                  "StringEmpty", "S6", "S3", "S2", "S1", "CharLevel1", "CharLevel2", 
                  "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", 
                  "Integer", "Exponent", "Base", "Bin", "Oct", "Digit", 
                  "Hex", "Zero", "Identifier", "Dot", "Underline", "A", 
                  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                  "X", "Y", "Z", "Letter", "NameStartCharacter", "EmojiCharacter", 
                  "NameCharacter", "LineComment", "OPEN_PAREN", "CLOSE_PAREN", 
                  "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", 
                  "Modulo", "Equal" ]

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
            actions[77] = self.OPEN_PAREN_action 
            actions[78] = self.CLOSE_PAREN_action 
            actions[79] = self.OPEN_BRACK_action 
            actions[80] = self.CLOSE_BRACK_action 
            actions[81] = self.OPEN_BRACE_action 
            actions[82] = self.CLOSE_BRACE_action 
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

     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened += 1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened -= 1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened += 1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.opened -= 1
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.opened += 1
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.opened -= 1
     

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
         


