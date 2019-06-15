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
        buf.write("\u0227\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\6\b\u00bb\n\b\r\b\16\b\u00bc\3\b\3\b\3\t\3\t\5")
        buf.write("\t\u00c3\n\t\3\t\5\t\u00c6\n\t\3\t\3\t\5\t\u00ca\n\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\5\n\u00d1\n\n\3\n\3\n\5\n\u00d5\n\n")
        buf.write("\3\n\5\n\u00d8\n\n\5\n\u00da\n\n\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\6\33\u011c\n\33\r\33\16\33\u011d\3\33")
        buf.write("\3\33\3\34\3\34\6\34\u0124\n\34\r\34\16\34\u0125\3\34")
        buf.write("\3\34\3\35\3\35\6\35\u012c\n\35\r\35\16\35\u012d\3\35")
        buf.write("\3\35\3\36\3\36\6\36\u0134\n\36\r\36\16\36\u0135\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0146\n\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3$\3$\5$\u0158\n$\3%\3%\3%\3%\5%\u015e")
        buf.write("\n%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\6\'\u0169\n\'\r\'")
        buf.write("\16\'\u016a\5\'\u016d\n\'\3(\3(\3(\6(\u0172\n(\r(\16(")
        buf.write("\u0173\3)\3)\3)\6)\u0179\n)\r)\16)\u017a\3*\3*\3*\6*\u0180")
        buf.write("\n*\r*\16*\u0181\3+\6+\u0185\n+\r+\16+\u0186\3+\3+\7+")
        buf.write("\u018b\n+\f+\16+\u018e\13+\5+\u0190\n+\3,\3,\3,\3-\3-")
        buf.write("\3-\3.\3.\5.\u019a\n.\3/\3/\5/\u019e\n/\3\60\3\60\5\60")
        buf.write("\u01a2\n\60\3\61\3\61\5\61\u01a6\n\61\3\62\3\62\3\63\3")
        buf.write("\63\7\63\u01ac\n\63\f\63\16\63\u01af\13\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3")
        buf.write("N\3N\3O\3O\3P\3P\3P\3P\3P\3P\3P\5P\u01f0\nP\3P\3P\3P\3")
        buf.write("P\3P\3P\3P\5P\u01f9\nP\3P\3P\3P\3P\3P\3P\5P\u0201\nP\3")
        buf.write("P\3P\3P\3P\3P\3P\5P\u0209\nP\5P\u020b\nP\3Q\3Q\5Q\u020f")
        buf.write("\nQ\3Q\5Q\u0212\nQ\3R\3R\3S\3S\5S\u0218\nS\3T\3T\7T\u021c")
        buf.write("\nT\fT\16T\u021f\13T\3T\3T\3U\3U\3V\3V\3V\6\u011d\u0125")
        buf.write("\u012d\u0135\2W\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?\2")
        buf.write("A\2C\2E\2G\2I\2K!M\"O#Q$S%U&W\'Y([\2]\2_\2a\2c\2e)g*i")
        buf.write("+k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2")
        buf.write("\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f")
        buf.write("\2\u00a1\2\u00a3\2\u00a5\2\u00a7,\u00a9-\u00ab.\3\2\'")
        buf.write("\4\2\13\13\"\"\3\2))\3\2\"\"\3\2^^\4\2))^^\3\2\63;\3\2")
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
        buf.write("\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8\3\u0238\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2\u00a7\3\2")
        buf.write("\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\3\u00ad\3\2\2\2\5")
        buf.write("\u00af\3\2\2\2\7\u00b1\3\2\2\2\t\u00b3\3\2\2\2\13\u00b5")
        buf.write("\3\2\2\2\r\u00b7\3\2\2\2\17\u00ba\3\2\2\2\21\u00c0\3\2")
        buf.write("\2\2\23\u00d9\3\2\2\2\25\u00dd\3\2\2\2\27\u00df\3\2\2")
        buf.write("\2\31\u00e1\3\2\2\2\33\u00e8\3\2\2\2\35\u00f0\3\2\2\2")
        buf.write("\37\u00f5\3\2\2\2!\u00f8\3\2\2\2#\u00fa\3\2\2\2%\u00fc")
        buf.write("\3\2\2\2\'\u00ff\3\2\2\2)\u0104\3\2\2\2+\u0108\3\2\2\2")
        buf.write("-\u010b\3\2\2\2/\u010e\3\2\2\2\61\u0110\3\2\2\2\63\u0112")
        buf.write("\3\2\2\2\65\u0119\3\2\2\2\67\u0121\3\2\2\29\u0129\3\2")
        buf.write("\2\2;\u0131\3\2\2\2=\u0145\3\2\2\2?\u0147\3\2\2\2A\u014b")
        buf.write("\3\2\2\2C\u014f\3\2\2\2E\u0151\3\2\2\2G\u0157\3\2\2\2")
        buf.write("I\u015d\3\2\2\2K\u015f\3\2\2\2M\u016c\3\2\2\2O\u016e\3")
        buf.write("\2\2\2Q\u0175\3\2\2\2S\u017c\3\2\2\2U\u018f\3\2\2\2W\u0191")
        buf.write("\3\2\2\2Y\u0194\3\2\2\2[\u0199\3\2\2\2]\u019d\3\2\2\2")
        buf.write("_\u01a1\3\2\2\2a\u01a5\3\2\2\2c\u01a7\3\2\2\2e\u01a9\3")
        buf.write("\2\2\2g\u01b0\3\2\2\2i\u01b2\3\2\2\2k\u01b4\3\2\2\2m\u01b6")
        buf.write("\3\2\2\2o\u01b8\3\2\2\2q\u01ba\3\2\2\2s\u01bc\3\2\2\2")
        buf.write("u\u01be\3\2\2\2w\u01c0\3\2\2\2y\u01c2\3\2\2\2{\u01c4\3")
        buf.write("\2\2\2}\u01c6\3\2\2\2\177\u01c8\3\2\2\2\u0081\u01ca\3")
        buf.write("\2\2\2\u0083\u01cc\3\2\2\2\u0085\u01ce\3\2\2\2\u0087\u01d0")
        buf.write("\3\2\2\2\u0089\u01d2\3\2\2\2\u008b\u01d4\3\2\2\2\u008d")
        buf.write("\u01d6\3\2\2\2\u008f\u01d8\3\2\2\2\u0091\u01da\3\2\2\2")
        buf.write("\u0093\u01dc\3\2\2\2\u0095\u01de\3\2\2\2\u0097\u01e0\3")
        buf.write("\2\2\2\u0099\u01e2\3\2\2\2\u009b\u01e4\3\2\2\2\u009d\u01e6")
        buf.write("\3\2\2\2\u009f\u020a\3\2\2\2\u00a1\u0211\3\2\2\2\u00a3")
        buf.write("\u0213\3\2\2\2\u00a5\u0217\3\2\2\2\u00a7\u0219\3\2\2\2")
        buf.write("\u00a9\u0222\3\2\2\2\u00ab\u0224\3\2\2\2\u00ad\u00ae\7")
        buf.write("}\2\2\u00ae\4\3\2\2\2\u00af\u00b0\7\177\2\2\u00b0\6\3")
        buf.write("\2\2\2\u00b1\u00b2\7]\2\2\u00b2\b\3\2\2\2\u00b3\u00b4")
        buf.write("\7_\2\2\u00b4\n\3\2\2\2\u00b5\u00b6\7*\2\2\u00b6\f\3\2")
        buf.write("\2\2\u00b7\u00b8\7+\2\2\u00b8\16\3\2\2\2\u00b9\u00bb\t")
        buf.write("\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\b\b\2\2\u00bf\20\3\2\2\2\u00c0\u00c2\5\25\13\2")
        buf.write("\u00c1\u00c3\5\17\b\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c9\3\2\2\2\u00c4\u00c6\7\17\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00ca\7\f\2\2\u00c8\u00ca\7\17\2\2\u00c9\u00c5")
        buf.write("\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cc\b\t\2\2\u00cc\22\3\2\2\2\u00cd\u00ce\6\n\2\2\u00ce")
        buf.write("\u00da\5\17\b\2\u00cf\u00d1\7\17\2\2\u00d0\u00cf\3\2\2")
        buf.write("\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d5")
        buf.write("\7\f\2\2\u00d3\u00d5\4\16\17\2\u00d4\u00d0\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d8\5\17\b")
        buf.write("\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00cd\3\2\2\2\u00d9\u00d4\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dc\b\n\3\2\u00dc\24\3\2\2\2\u00dd")
        buf.write("\u00de\7^\2\2\u00de\26\3\2\2\2\u00df\u00e0\7=\2\2\u00e0")
        buf.write("\30\3\2\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7o\2\2\u00e3")
        buf.write("\u00e4\7r\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write("\u00e7\7v\2\2\u00e7\32\3\2\2\2\u00e8\u00e9\7r\2\2\u00e9")
        buf.write("\u00ea\7c\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7m\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\u00ee\7i\2\2\u00ee\u00ef\7g\2\2\u00ef")
        buf.write("\34\3\2\2\2\u00f0\u00f1\7y\2\2\u00f1\u00f2\7k\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3\u00f4\7j\2\2\u00f4\36\3\2\2\2\u00f5")
        buf.write("\u00f6\7c\2\2\u00f6\u00f7\7u\2\2\u00f7 \3\2\2\2\u00f8")
        buf.write("\u00f9\7.\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7,\2\2\u00fb")
        buf.write("$\3\2\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7h\2\2\u00fe")
        buf.write("&\3\2\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7n\2\2\u0101")
        buf.write("\u0102\7u\2\2\u0102\u0103\7g\2\2\u0103(\3\2\2\2\u0104")
        buf.write("\u0105\7h\2\2\u0105\u0106\7q\2\2\u0106\u0107\7t\2\2\u0107")
        buf.write("*\3\2\2\2\u0108\u0109\7k\2\2\u0109\u010a\7p\2\2\u010a")
        buf.write(",\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d\7@\2\2\u010d")
        buf.write(".\3\2\2\2\u010e\u010f\7<\2\2\u010f\60\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\62\3\2\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7v\2\2\u0115\u0116\7w\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7p\2\2\u0118\64\3\2\2\2\u0119\u011b")
        buf.write("\5? \2\u011a\u011c\5G$\2\u011b\u011a\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u0120\5? \2\u0120\66\3\2\2\2\u0121")
        buf.write("\u0123\5C\"\2\u0122\u0124\5I%\2\u0123\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u0128\5C\"\2\u01288\3\2\2\2")
        buf.write("\u0129\u012b\5A!\2\u012a\u012c\13\2\2\2\u012b\u012a\3")
        buf.write("\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\5A!\2\u0130:")
        buf.write("\3\2\2\2\u0131\u0133\5E#\2\u0132\u0134\n\3\2\2\u0133\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\5E#\2\u0138")
        buf.write("<\3\2\2\2\u0139\u013a\5? \2\u013a\u013b\5? \2\u013b\u0146")
        buf.write("\3\2\2\2\u013c\u013d\5A!\2\u013d\u013e\5A!\2\u013e\u0146")
        buf.write("\3\2\2\2\u013f\u0140\5C\"\2\u0140\u0141\5C\"\2\u0141\u0146")
        buf.write("\3\2\2\2\u0142\u0143\5E#\2\u0143\u0144\5E#\2\u0144\u0146")
        buf.write("\3\2\2\2\u0145\u0139\3\2\2\2\u0145\u013c\3\2\2\2\u0145")
        buf.write("\u013f\3\2\2\2\u0145\u0142\3\2\2\2\u0146>\3\2\2\2\u0147")
        buf.write("\u0148\7$\2\2\u0148\u0149\7$\2\2\u0149\u014a\7$\2\2\u014a")
        buf.write("@\3\2\2\2\u014b\u014c\7)\2\2\u014c\u014d\7)\2\2\u014d")
        buf.write("\u014e\7)\2\2\u014eB\3\2\2\2\u014f\u0150\7$\2\2\u0150")
        buf.write("D\3\2\2\2\u0151\u0152\7)\2\2\u0152F\3\2\2\2\u0153\u0154")
        buf.write("\5\25\13\2\u0154\u0155\n\4\2\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0158\n\5\2\2\u0157\u0153\3\2\2\2\u0157\u0156\3\2\2\2")
        buf.write("\u0158H\3\2\2\2\u0159\u015a\5\25\13\2\u015a\u015b\n\4")
        buf.write("\2\2\u015b\u015e\3\2\2\2\u015c\u015e\n\6\2\2\u015d\u0159")
        buf.write("\3\2\2\2\u015d\u015c\3\2\2\2\u015eJ\3\2\2\2\u015f\u0160")
        buf.write("\5U+\2\u0160\u0161\5g\64\2\u0161\u0162\5_\60\2\u0162L")
        buf.write("\3\2\2\2\u0163\u0164\5U+\2\u0164\u0165\5g\64\2\u0165\u016d")
        buf.write("\3\2\2\2\u0166\u0168\5g\64\2\u0167\u0169\5_\60\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016b\u016d\3\2\2\2\u016c\u0163\3")
        buf.write("\2\2\2\u016c\u0166\3\2\2\2\u016dN\3\2\2\2\u016e\u016f")
        buf.write("\5c\62\2\u016f\u0171\5m\67\2\u0170\u0172\5[.\2\u0171\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174P\3\2\2\2\u0175\u0176\5c\62\2\u0176")
        buf.write("\u0178\5\u0087D\2\u0177\u0179\5]/\2\u0178\u0177\3\2\2")
        buf.write("\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017bR\3\2\2\2\u017c\u017d\5c\62\2\u017d\u017f")
        buf.write("\5\u0099M\2\u017e\u0180\5a\61\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182T\3\2\2\2\u0183\u0185\5c\62\2\u0184\u0183\3\2\2")
        buf.write("\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0190\3\2\2\2\u0188\u018c\t\7\2\2\u0189")
        buf.write("\u018b\5_\60\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2")
        buf.write("\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u0190\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018f\u0184\3\2\2\2\u018f\u0188")
        buf.write("\3\2\2\2\u0190V\3\2\2\2\u0191\u0192\7,\2\2\u0192\u0193")
        buf.write("\7`\2\2\u0193X\3\2\2\2\u0194\u0195\7\61\2\2\u0195\u0196")
        buf.write("\7`\2\2\u0196Z\3\2\2\2\u0197\u019a\5c\62\2\u0198\u019a")
        buf.write("\t\b\2\2\u0199\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019a")
        buf.write("\\\3\2\2\2\u019b\u019e\5c\62\2\u019c\u019e\t\t\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e^\3\2\2\2\u019f")
        buf.write("\u01a2\5c\62\2\u01a0\u01a2\t\7\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a0\3\2\2\2\u01a2`\3\2\2\2\u01a3\u01a6\5c\62")
        buf.write("\2\u01a4\u01a6\t\n\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6b\3\2\2\2\u01a7\u01a8\t\13\2\2\u01a8d\3")
        buf.write("\2\2\2\u01a9\u01ad\5\u00a1Q\2\u01aa\u01ac\5\u00a5S\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01aef\3\2\2\2\u01af\u01ad\3\2\2")
        buf.write("\2\u01b0\u01b1\7\60\2\2\u01b1h\3\2\2\2\u01b2\u01b3\7a")
        buf.write("\2\2\u01b3j\3\2\2\2\u01b4\u01b5\t\f\2\2\u01b5l\3\2\2\2")
        buf.write("\u01b6\u01b7\t\r\2\2\u01b7n\3\2\2\2\u01b8\u01b9\t\16\2")
        buf.write("\2\u01b9p\3\2\2\2\u01ba\u01bb\t\17\2\2\u01bbr\3\2\2\2")
        buf.write("\u01bc\u01bd\t\20\2\2\u01bdt\3\2\2\2\u01be\u01bf\t\21")
        buf.write("\2\2\u01bfv\3\2\2\2\u01c0\u01c1\t\22\2\2\u01c1x\3\2\2")
        buf.write("\2\u01c2\u01c3\t\23\2\2\u01c3z\3\2\2\2\u01c4\u01c5\t\24")
        buf.write("\2\2\u01c5|\3\2\2\2\u01c6\u01c7\t\25\2\2\u01c7~\3\2\2")
        buf.write("\2\u01c8\u01c9\t\26\2\2\u01c9\u0080\3\2\2\2\u01ca\u01cb")
        buf.write("\t\27\2\2\u01cb\u0082\3\2\2\2\u01cc\u01cd\t\30\2\2\u01cd")
        buf.write("\u0084\3\2\2\2\u01ce\u01cf\t\31\2\2\u01cf\u0086\3\2\2")
        buf.write("\2\u01d0\u01d1\t\32\2\2\u01d1\u0088\3\2\2\2\u01d2\u01d3")
        buf.write("\t\33\2\2\u01d3\u008a\3\2\2\2\u01d4\u01d5\t\34\2\2\u01d5")
        buf.write("\u008c\3\2\2\2\u01d6\u01d7\t\35\2\2\u01d7\u008e\3\2\2")
        buf.write("\2\u01d8\u01d9\t\36\2\2\u01d9\u0090\3\2\2\2\u01da\u01db")
        buf.write("\t\37\2\2\u01db\u0092\3\2\2\2\u01dc\u01dd\t \2\2\u01dd")
        buf.write("\u0094\3\2\2\2\u01de\u01df\t!\2\2\u01df\u0096\3\2\2\2")
        buf.write("\u01e0\u01e1\t\"\2\2\u01e1\u0098\3\2\2\2\u01e2\u01e3\t")
        buf.write("#\2\2\u01e3\u009a\3\2\2\2\u01e4\u01e5\t$\2\2\u01e5\u009c")
        buf.write("\3\2\2\2\u01e6\u01e7\t%\2\2\u01e7\u009e\3\2\2\2\u01e8")
        buf.write("\u01f0\5k\66\2\u01e9\u01f0\5m\67\2\u01ea\u01f0\5o8\2\u01eb")
        buf.write("\u01f0\5q9\2\u01ec\u01f0\5s:\2\u01ed\u01f0\5u;\2\u01ee")
        buf.write("\u01f0\5w<\2\u01ef\u01e8\3\2\2\2\u01ef\u01e9\3\2\2\2\u01ef")
        buf.write("\u01ea\3\2\2\2\u01ef\u01eb\3\2\2\2\u01ef\u01ec\3\2\2\2")
        buf.write("\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u020b\3")
        buf.write("\2\2\2\u01f1\u01f9\5y=\2\u01f2\u01f9\5{>\2\u01f3\u01f9")
        buf.write("\5}?\2\u01f4\u01f9\5\177@\2\u01f5\u01f9\5\u0081A\2\u01f6")
        buf.write("\u01f9\5\u0083B\2\u01f7\u01f9\5\u0085C\2\u01f8\u01f1\3")
        buf.write("\2\2\2\u01f8\u01f2\3\2\2\2\u01f8\u01f3\3\2\2\2\u01f8\u01f4")
        buf.write("\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f9\u020b\3\2\2\2\u01fa\u0201\5\u0087")
        buf.write("D\2\u01fb\u0201\5\u0089E\2\u01fc\u0201\5\u008bF\2\u01fd")
        buf.write("\u0201\5\u008dG\2\u01fe\u0201\5\u008fH\2\u01ff\u0201\5")
        buf.write("\u0091I\2\u0200\u01fa\3\2\2\2\u0200\u01fb\3\2\2\2\u0200")
        buf.write("\u01fc\3\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2")
        buf.write("\u0200\u01ff\3\2\2\2\u0201\u020b\3\2\2\2\u0202\u0209\5")
        buf.write("\u0093J\2\u0203\u0209\5\u0095K\2\u0204\u0209\5\u0097L")
        buf.write("\2\u0205\u0209\5\u0099M\2\u0206\u0209\5\u009bN\2\u0207")
        buf.write("\u0209\5\u009dO\2\u0208\u0202\3\2\2\2\u0208\u0203\3\2")
        buf.write("\2\2\u0208\u0204\3\2\2\2\u0208\u0205\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0207\3\2\2\2\u0209\u020b\3\2\2\2\u020a")
        buf.write("\u01ef\3\2\2\2\u020a\u01f8\3\2\2\2\u020a\u0200\3\2\2\2")
        buf.write("\u020a\u0208\3\2\2\2\u020b\u00a0\3\2\2\2\u020c\u020f\5")
        buf.write("i\65\2\u020d\u020f\5\u009fP\2\u020e\u020c\3\2\2\2\u020e")
        buf.write("\u020d\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u0212\t\'\2\2")
        buf.write("\u0211\u020e\3\2\2\2\u0211\u0210\3\2\2\2\u0212\u00a2\3")
        buf.write("\2\2\2\u0213\u0214\t(\2\2\u0214\u00a4\3\2\2\2\u0215\u0218")
        buf.write("\5\u00a1Q\2\u0216\u0218\5_\60\2\u0217\u0215\3\2\2\2\u0217")
        buf.write("\u0216\3\2\2\2\u0218\u00a6\3\2\2\2\u0219\u021d\7%\2\2")
        buf.write("\u021a\u021c\n&\2\2\u021b\u021a\3\2\2\2\u021c\u021f\3")
        buf.write("\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0220")
        buf.write("\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0221\bT\4\2\u0221")
        buf.write("\u00a8\3\2\2\2\u0222\u0223\7\'\2\2\u0223\u00aa\3\2\2\2")
        buf.write("\u0224\u0225\7?\2\2\u0225\u0226\7?\2\2\u0226\u00ac\3\2")
        buf.write("\2\2(\2\u00bc\u00c2\u00c5\u00c9\u00d0\u00d4\u00d7\u00d9")
        buf.write("\u011d\u0125\u012d\u0135\u0145\u0157\u015d\u016a\u016c")
        buf.write("\u0173\u017a\u0181\u0186\u018c\u018f\u0199\u019d\u01a1")
        buf.write("\u01a5\u01ad\u01ef\u01f8\u0200\u0208\u020a\u020e\u0211")
        buf.write("\u0217\u021d\5\b\2\2\3\n\2\2\3\2")
        return buf.getvalue()


class BasisLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    SPACES = 7
    JoinLine = 8
    NEWLINE = 9
    Escape = 10
    Semicolon = 11
    Import = 12
    Package = 13
    With = 14
    As = 15
    Comma = 16
    Star = 17
    If = 18
    Else = 19
    For = 20
    In = 21
    To = 22
    Colon = 23
    Set = 24
    Return = 25
    StringEscapeBlock = 26
    StringEscapeSingle = 27
    StringLiteralBlock = 28
    StringLiteralSingle = 29
    StringEmpty = 30
    Decimal = 31
    DecimalBad = 32
    Binary = 33
    Octal = 34
    Hexadecimal = 35
    Integer = 36
    Exponent = 37
    Base = 38
    Identifier = 39
    Dot = 40
    Underline = 41
    LineComment = 42
    Modulo = 43
    Equal = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'['", "']'", "'('", "')'", "'\\'", "';'", "'import'", 
            "'package'", "'with'", "'as'", "','", "'*'", "'if'", "'else'", 
            "'for'", "'in'", "'=>'", "':'", "'='", "'return'", "'*^'", "'/^'", 
            "'.'", "'_'", "'%'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "JoinLine", "NEWLINE", "Escape", "Semicolon", "Import", 
            "Package", "With", "As", "Comma", "Star", "If", "Else", "For", 
            "In", "To", "Colon", "Set", "Return", "StringEscapeBlock", "StringEscapeSingle", 
            "StringLiteralBlock", "StringLiteralSingle", "StringEmpty", 
            "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
            "Exponent", "Base", "Identifier", "Dot", "Underline", "LineComment", 
            "Modulo", "Equal" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "SPACES", 
                  "JoinLine", "NEWLINE", "Escape", "Semicolon", "Import", 
                  "Package", "With", "As", "Comma", "Star", "If", "Else", 
                  "For", "In", "To", "Colon", "Set", "Return", "StringEscapeBlock", 
                  "StringEscapeSingle", "StringLiteralBlock", "StringLiteralSingle", 
                  "StringEmpty", "S6", "S3", "S2", "S1", "CharLevel1", "CharLevel2", 
                  "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", 
                  "Integer", "Exponent", "Base", "Bin", "Oct", "Digit", 
                  "Hex", "Zero", "Identifier", "Dot", "Underline", "A", 
                  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                  "X", "Y", "Z", "Letter", "NameStartCharacter", "EmojiCharacter", 
                  "NameCharacter", "LineComment", "Modulo", "Equal" ]

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
            actions[8] = self.NEWLINE_action 
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
            preds[8] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


