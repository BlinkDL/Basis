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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0211\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b\u00b3\n\b\r\b")
        buf.write("\16\b\u00b4\3\b\3\b\3\t\3\t\3\t\5\t\u00bc\n\t\3\t\3\t")
        buf.write("\5\t\u00c0\n\t\3\t\5\t\u00c3\n\t\5\t\u00c5\n\t\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\5\13\u00cd\n\13\3\13\5\13\u00d0\n\13")
        buf.write("\3\13\3\13\5\13\u00d4\n\13\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\6\31\u010b\n\31\r\31\16\31\u010c\3\31\3\31")
        buf.write("\3\32\3\32\6\32\u0113\n\32\r\32\16\32\u0114\3\32\3\32")
        buf.write("\3\33\3\33\6\33\u011b\n\33\r\33\16\33\u011c\3\33\3\33")
        buf.write("\3\34\3\34\6\34\u0123\n\34\r\34\16\34\u0124\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0135\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3")
        buf.write("\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\5\"\u0147\n\"\3#")
        buf.write("\3#\3#\3#\5#\u014d\n#\3$\3$\3$\3$\3%\3%\3%\3%\3%\6%\u0158")
        buf.write("\n%\r%\16%\u0159\5%\u015c\n%\3&\3&\3&\6&\u0161\n&\r&\16")
        buf.write("&\u0162\3\'\3\'\3\'\6\'\u0168\n\'\r\'\16\'\u0169\3(\3")
        buf.write("(\3(\6(\u016f\n(\r(\16(\u0170\3)\6)\u0174\n)\r)\16)\u0175")
        buf.write("\3)\3)\7)\u017a\n)\f)\16)\u017d\13)\5)\u017f\n)\3*\3*")
        buf.write("\3*\3+\3+\3+\3,\3,\5,\u0189\n,\3-\3-\5-\u018d\n-\3.\3")
        buf.write(".\5.\u0191\n.\3/\3/\5/\u0195\n/\3\60\3\60\3\61\3\61\7")
        buf.write("\61\u019b\n\61\f\61\16\61\u019e\13\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3")
        buf.write("K\3L\3L\3M\3M\3N\3N\3N\3N\3N\3N\3N\5N\u01df\nN\3N\3N\3")
        buf.write("N\3N\3N\3N\3N\5N\u01e8\nN\3N\3N\3N\3N\3N\3N\5N\u01f0\n")
        buf.write("N\3N\3N\3N\3N\3N\3N\5N\u01f8\nN\5N\u01fa\nN\3O\3O\5O\u01fe")
        buf.write("\nO\3O\5O\u0201\nO\3P\3P\3Q\3Q\5Q\u0207\nQ\3R\3R\7R\u020b")
        buf.write("\nR\fR\16R\u020e\13R\3R\3R\6\u010c\u0114\u011c\u0124\2")
        buf.write("S\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\2=\2?\2A\2C\2E\2G\37I K")
        buf.write("!M\"O#Q$S%U&W\2Y\2[\2]\2_\2a\'c(e)g\2i\2k\2m\2o\2q\2s")
        buf.write("\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("*\3\2\'\4\2\13\13\"\"\3\2\uff04\uff04\3\2\"\"\3\2^^\4")
        buf.write("\2$$^^\3\2\63;\3\2\63\63\3\2\639\5\2\63;CHch\3\2\62\62")
        buf.write("\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2I")
        buf.write("Iii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4")
        buf.write("\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVv")
        buf.write("v\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4")
        buf.write("\2\f\f\17\17\4Y\2C\2\\\2c\2|\2\u00ac\2\u00ac\2\u00bc\2")
        buf.write("\u00bc\2\u00c2\2\u00d8\2\u00da\2\u00f8\2\u00fa\2\u02ba")
        buf.write("\2\u02e2\2\u02e6\2\u0372\2\u0375\2\u0377\2\u0379\2\u037c")
        buf.write("\2\u037f\2\u0381\2\u0381\2\u0386\2\u0386\2\u0388\2\u0388")
        buf.write("\2\u038a\2\u038c\2\u038e\2\u038e\2\u0390\2\u03a3\2\u03a5")
        buf.write("\2\u03e3\2\u03f2\2\u0401\2\u1d02\2\u1d2c\2\u1d2e\2\u1d79")
        buf.write("\2\u1d7b\2\u1dc1\2\u1e02\2\u1f17\2\u1f1a\2\u1f1f\2\u1f22")
        buf.write("\2\u1f47\2\u1f4a\2\u1f4f\2\u1f52\2\u1f59\2\u1f5b\2\u1f5b")
        buf.write("\2\u1f5d\2\u1f5d\2\u1f5f\2\u1f5f\2\u1f61\2\u1f7f\2\u1f82")
        buf.write("\2\u1fb6\2\u1fb8\2\u1fc6\2\u1fc8\2\u1fd5\2\u1fd8\2\u1fdd")
        buf.write("\2\u1fdf\2\u1ff1\2\u1ff4\2\u1ff6\2\u1ff8\2\u2000\2\u2073")
        buf.write("\2\u2073\2\u2081\2\u2081\2\u2092\2\u209e\2\u2128\2\u2128")
        buf.write("\2\u212c\2\u212d\2\u2134\2\u2134\2\u2150\2\u2150\2\u2162")
        buf.write("\2\u218a\2\u2c62\2\u2c81\2\u2e82\2\u2e9b\2\u2e9d\2\u2ef5")
        buf.write("\2\u2f02\2\u2fd7\2\u3007\2\u3007\2\u3009\2\u3009\2\u3023")
        buf.write("\2\u302b\2\u303a\2\u303d\2\u3043\2\u3098\2\u309f\2\u30a1")
        buf.write("\2\u30a3\2\u30fc\2\u30ff\2\u3101\2\u31f2\2\u3201\2\u32d2")
        buf.write("\2\u3300\2\u3302\2\u3359\2\u3402\2\u4db7\2\u4e02\2\u9fec")
        buf.write("\2\ua724\2\ua789\2\ua78d\2\ua7b0\2\ua7b2\2\ua7b9\2\ua7f9")
        buf.write("\2\ua801\2\uab32\2\uab5c\2\uab5e\2\uab67\2\uf902\2\ufa6f")
        buf.write("\2\ufa72\2\ufadb\2\ufb02\2\ufb08\2\uff23\2\uff3c\2\uff43")
        buf.write("\2\uff5c\2\uff68\2\uff71\2\uff73\2\uff9f\2\u0142\3\u0190")
        buf.write("\3\u01a2\3\u01a2\3\ub002\3\ub120\3\ud202\3\ud247\3\uf202")
        buf.write("\3\uf202\3\2\4\ua6d8\4\ua702\4\ub736\4\ub742\4\ub81f\4")
        buf.write("\ub822\4\ucea3\4\uceb2\4\uebe2\4\uf802\4\ufa1f\4\u0093")
        buf.write("\2%\2%\2,\2,\2\62\2;\2\u00ab\2\u00ab\2\u00b0\2\u00b0\2")
        buf.write("\u203e\2\u203e\2\u204b\2\u204b\2\u2124\2\u2124\2\u213b")
        buf.write("\2\u213b\2\u2196\2\u219b\2\u21ab\2\u21ac\2\u231c\2\u231d")
        buf.write("\2\u232a\2\u232a\2\u23d1\2\u23d1\2\u23eb\2\u23f5\2\u23fa")
        buf.write("\2\u23fc\2\u24c4\2\u24c4\2\u25ac\2\u25ad\2\u25b8\2\u25b8")
        buf.write("\2\u25c2\2\u25c2\2\u25fd\2\u2600\2\u2602\2\u2606\2\u2610")
        buf.write("\2\u2610\2\u2613\2\u2613\2\u2616\2\u2617\2\u261a\2\u261a")
        buf.write("\2\u261f\2\u261f\2\u2622\2\u2622\2\u2624\2\u2625\2\u2628")
        buf.write("\2\u2628\2\u262c\2\u262c\2\u2630\2\u2631\2\u263a\2\u263c")
        buf.write("\2\u2642\2\u2642\2\u2644\2\u2644\2\u264a\2\u2655\2\u2662")
        buf.write("\2\u2662\2\u2665\2\u2665\2\u2667\2\u2668\2\u266a\2\u266a")
        buf.write("\2\u267d\2\u267d\2\u2681\2\u2681\2\u2694\2\u2699\2\u269b")
        buf.write("\2\u269b\2\u269d\2\u269e\2\u26a2\2\u26a3\2\u26ac\2\u26ad")
        buf.write("\2\u26b2\2\u26b3\2\u26bf\2\u26c0\2\u26c6\2\u26c7\2\u26ca")
        buf.write("\2\u26ca\2\u26d0\2\u26d1\2\u26d3\2\u26d3\2\u26d5\2\u26d6")
        buf.write("\2\u26eb\2\u26ec\2\u26f2\2\u26f7\2\u26f9\2\u26fc\2\u26ff")
        buf.write("\2\u26ff\2\u2704\2\u2704\2\u2707\2\u2707\2\u270a\2\u270f")
        buf.write("\2\u2711\2\u2711\2\u2714\2\u2714\2\u2716\2\u2716\2\u2718")
        buf.write("\2\u2718\2\u271f\2\u271f\2\u2723\2\u2723\2\u272a\2\u272a")
        buf.write("\2\u2735\2\u2736\2\u2746\2\u2746\2\u2749\2\u2749\2\u274e")
        buf.write("\2\u274e\2\u2750\2\u2750\2\u2755\2\u2757\2\u2759\2\u2759")
        buf.write("\2\u2765\2\u2766\2\u2797\2\u2799\2\u27a3\2\u27a3\2\u27b2")
        buf.write("\2\u27b2\2\u27c1\2\u27c1\2\u2936\2\u2937\2\u2b07\2\u2b09")
        buf.write("\2\u2b1d\2\u2b1e\2\u2b52\2\u2b52\2\u2b57\2\u2b57\2\u3032")
        buf.write("\2\u3032\2\u303f\2\u303f\2\u3299\2\u3299\2\u329b\2\u329b")
        buf.write("\2\uf006\3\uf006\3\uf0d1\3\uf0d1\3\uf172\3\uf173\3\uf180")
        buf.write("\3\uf181\3\uf190\3\uf190\3\uf193\3\uf19c\3\uf1e8\3\uf201")
        buf.write("\3\uf203\3\uf204\3\uf21c\3\uf21c\3\uf231\3\uf231\3\uf234")
        buf.write("\3\uf23c\3\uf252\3\uf253\3\uf302\3\uf323\3\uf326\3\uf395")
        buf.write("\3\uf398\3\uf399\3\uf39b\3\uf39d\3\uf3a0\3\uf3f2\3\uf3f5")
        buf.write("\3\uf3f7\3\uf3f9\3\uf4ff\3\uf501\3\uf53f\3\uf54b\3\uf550")
        buf.write("\3\uf552\3\uf569\3\uf571\3\uf572\3\uf575\3\uf57c\3\uf589")
        buf.write("\3\uf589\3\uf58c\3\uf58f\3\uf592\3\uf592\3\uf597\3\uf598")
        buf.write("\3\uf5a6\3\uf5a7\3\uf5aa\3\uf5aa\3\uf5b3\3\uf5b4\3\uf5be")
        buf.write("\3\uf5be\3\uf5c4\3\uf5c6\3\uf5d3\3\uf5d5\3\uf5de\3\uf5e0")
        buf.write("\3\uf5e3\3\uf5e3\3\uf5e5\3\uf5e5\3\uf5ea\3\uf5ea\3\uf5f1")
        buf.write("\3\uf5f1\3\uf5f5\3\uf5f5\3\uf5fc\3\uf651\3\uf682\3\uf6c7")
        buf.write("\3\uf6cd\3\uf6d4\3\uf6e2\3\uf6e7\3\uf6eb\3\uf6eb\3\uf6ed")
        buf.write("\3\uf6ee\3\uf6f2\3\uf6f2\3\uf6f5\3\uf6fa\3\uf912\3\uf93c")
        buf.write("\3\uf93e\3\uf940\3\uf942\3\uf947\3\uf949\3\uf94e\3\uf952")
        buf.write("\3\uf96d\3\uf982\3\uf999\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8")
        buf.write("\3\u0222\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2")
        buf.write("K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2")
        buf.write("\2U\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2\u00a3\3")
        buf.write("\2\2\2\3\u00a5\3\2\2\2\5\u00a7\3\2\2\2\7\u00a9\3\2\2\2")
        buf.write("\t\u00ab\3\2\2\2\13\u00ad\3\2\2\2\r\u00af\3\2\2\2\17\u00b2")
        buf.write("\3\2\2\2\21\u00c4\3\2\2\2\23\u00c8\3\2\2\2\25\u00ca\3")
        buf.write("\2\2\2\27\u00d7\3\2\2\2\31\u00d9\3\2\2\2\33\u00e0\3\2")
        buf.write("\2\2\35\u00e8\3\2\2\2\37\u00ed\3\2\2\2!\u00f0\3\2\2\2")
        buf.write("#\u00f2\3\2\2\2%\u00f4\3\2\2\2\'\u00f7\3\2\2\2)\u00fc")
        buf.write("\3\2\2\2+\u0100\3\2\2\2-\u0103\3\2\2\2/\u0106\3\2\2\2")
        buf.write("\61\u0108\3\2\2\2\63\u0110\3\2\2\2\65\u0118\3\2\2\2\67")
        buf.write("\u0120\3\2\2\29\u0134\3\2\2\2;\u0136\3\2\2\2=\u013a\3")
        buf.write("\2\2\2?\u013e\3\2\2\2A\u0140\3\2\2\2C\u0146\3\2\2\2E\u014c")
        buf.write("\3\2\2\2G\u014e\3\2\2\2I\u015b\3\2\2\2K\u015d\3\2\2\2")
        buf.write("M\u0164\3\2\2\2O\u016b\3\2\2\2Q\u017e\3\2\2\2S\u0180\3")
        buf.write("\2\2\2U\u0183\3\2\2\2W\u0188\3\2\2\2Y\u018c\3\2\2\2[\u0190")
        buf.write("\3\2\2\2]\u0194\3\2\2\2_\u0196\3\2\2\2a\u0198\3\2\2\2")
        buf.write("c\u019f\3\2\2\2e\u01a1\3\2\2\2g\u01a3\3\2\2\2i\u01a5\3")
        buf.write("\2\2\2k\u01a7\3\2\2\2m\u01a9\3\2\2\2o\u01ab\3\2\2\2q\u01ad")
        buf.write("\3\2\2\2s\u01af\3\2\2\2u\u01b1\3\2\2\2w\u01b3\3\2\2\2")
        buf.write("y\u01b5\3\2\2\2{\u01b7\3\2\2\2}\u01b9\3\2\2\2\177\u01bb")
        buf.write("\3\2\2\2\u0081\u01bd\3\2\2\2\u0083\u01bf\3\2\2\2\u0085")
        buf.write("\u01c1\3\2\2\2\u0087\u01c3\3\2\2\2\u0089\u01c5\3\2\2\2")
        buf.write("\u008b\u01c7\3\2\2\2\u008d\u01c9\3\2\2\2\u008f\u01cb\3")
        buf.write("\2\2\2\u0091\u01cd\3\2\2\2\u0093\u01cf\3\2\2\2\u0095\u01d1")
        buf.write("\3\2\2\2\u0097\u01d3\3\2\2\2\u0099\u01d5\3\2\2\2\u009b")
        buf.write("\u01f9\3\2\2\2\u009d\u0200\3\2\2\2\u009f\u0202\3\2\2\2")
        buf.write("\u00a1\u0206\3\2\2\2\u00a3\u0208\3\2\2\2\u00a5\u00a6\7")
        buf.write("}\2\2\u00a6\4\3\2\2\2\u00a7\u00a8\7\177\2\2\u00a8\6\3")
        buf.write("\2\2\2\u00a9\u00aa\7]\2\2\u00aa\b\3\2\2\2\u00ab\u00ac")
        buf.write("\7_\2\2\u00ac\n\3\2\2\2\u00ad\u00ae\7*\2\2\u00ae\f\3\2")
        buf.write("\2\2\u00af\u00b0\7+\2\2\u00b0\16\3\2\2\2\u00b1\u00b3\t")
        buf.write("\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b7\b\b\2\2\u00b7\20\3\2\2\2\u00b8\u00b9\6\t\2\2\u00b9")
        buf.write("\u00c5\5\17\b\2\u00ba\u00bc\7\17\2\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c0")
        buf.write("\7\f\2\2\u00be\u00c0\4\16\17\2\u00bf\u00bb\3\2\2\2\u00bf")
        buf.write("\u00be\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00c3\5\17\b")
        buf.write("\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5")
        buf.write("\3\2\2\2\u00c4\u00b8\3\2\2\2\u00c4\u00bf\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\b\t\3\2\u00c7\22\3\2\2\2\u00c8")
        buf.write("\u00c9\7^\2\2\u00c9\24\3\2\2\2\u00ca\u00cc\5\23\n\2\u00cb")
        buf.write("\u00cd\5\17\b\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2")
        buf.write("\2\u00cd\u00d3\3\2\2\2\u00ce\u00d0\7\17\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d4\7\f\2\2\u00d2\u00d4\7\17\2\2\u00d3\u00cf\3\2\2")
        buf.write("\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6")
        buf.write("\b\13\2\2\u00d6\26\3\2\2\2\u00d7\u00d8\7=\2\2\u00d8\30")
        buf.write("\3\2\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7o\2\2\u00db\u00dc")
        buf.write("\7r\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7t\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df\32\3\2\2\2\u00e0\u00e1\7r\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7m\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7\7g\2\2\u00e7\34")
        buf.write("\3\2\2\2\u00e8\u00e9\7y\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7j\2\2\u00ec\36\3\2\2\2\u00ed\u00ee")
        buf.write("\7c\2\2\u00ee\u00ef\7u\2\2\u00ef \3\2\2\2\u00f0\u00f1")
        buf.write("\7.\2\2\u00f1\"\3\2\2\2\u00f2\u00f3\7,\2\2\u00f3$\3\2")
        buf.write("\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7h\2\2\u00f6&\3\2")
        buf.write("\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa")
        buf.write("\7u\2\2\u00fa\u00fb\7g\2\2\u00fb(\3\2\2\2\u00fc\u00fd")
        buf.write("\7h\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7t\2\2\u00ff*\3")
        buf.write("\2\2\2\u0100\u0101\7k\2\2\u0101\u0102\7p\2\2\u0102,\3")
        buf.write("\2\2\2\u0103\u0104\7?\2\2\u0104\u0105\7@\2\2\u0105.\3")
        buf.write("\2\2\2\u0106\u0107\7<\2\2\u0107\60\3\2\2\2\u0108\u010a")
        buf.write("\5;\36\2\u0109\u010b\5C\"\2\u010a\u0109\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u010f\5;\36\2\u010f\62\3\2")
        buf.write("\2\2\u0110\u0112\5? \2\u0111\u0113\5E#\2\u0112\u0111\3")
        buf.write("\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\5? \2\u0117\64")
        buf.write("\3\2\2\2\u0118\u011a\5=\37\2\u0119\u011b\13\2\2\2\u011a")
        buf.write("\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\5")
        buf.write("=\37\2\u011f\66\3\2\2\2\u0120\u0122\5A!\2\u0121\u0123")
        buf.write("\n\3\2\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\u0127\5A!\2\u01278\3\2\2\2\u0128\u0129\5;\36\2")
        buf.write("\u0129\u012a\5;\36\2\u012a\u0135\3\2\2\2\u012b\u012c\5")
        buf.write("=\37\2\u012c\u012d\5=\37\2\u012d\u0135\3\2\2\2\u012e\u012f")
        buf.write("\5? \2\u012f\u0130\5? \2\u0130\u0135\3\2\2\2\u0131\u0132")
        buf.write("\5A!\2\u0132\u0133\5A!\2\u0133\u0135\3\2\2\2\u0134\u0128")
        buf.write("\3\2\2\2\u0134\u012b\3\2\2\2\u0134\u012e\3\2\2\2\u0134")
        buf.write("\u0131\3\2\2\2\u0135:\3\2\2\2\u0136\u0137\7$\2\2\u0137")
        buf.write("\u0138\7$\2\2\u0138\u0139\7$\2\2\u0139<\3\2\2\2\u013a")
        buf.write("\u013b\7\uff04\2\2\u013b\u013c\7\uff04\2\2\u013c\u013d")
        buf.write("\7\uff04\2\2\u013d>\3\2\2\2\u013e\u013f\7$\2\2\u013f@")
        buf.write("\3\2\2\2\u0140\u0141\7\uff04\2\2\u0141B\3\2\2\2\u0142")
        buf.write("\u0143\5\23\n\2\u0143\u0144\n\4\2\2\u0144\u0147\3\2\2")
        buf.write("\2\u0145\u0147\n\5\2\2\u0146\u0142\3\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147D\3\2\2\2\u0148\u0149\5\23\n\2\u0149\u014a")
        buf.write("\n\4\2\2\u014a\u014d\3\2\2\2\u014b\u014d\n\6\2\2\u014c")
        buf.write("\u0148\3\2\2\2\u014c\u014b\3\2\2\2\u014dF\3\2\2\2\u014e")
        buf.write("\u014f\5Q)\2\u014f\u0150\5c\62\2\u0150\u0151\5[.\2\u0151")
        buf.write("H\3\2\2\2\u0152\u0153\5Q)\2\u0153\u0154\5c\62\2\u0154")
        buf.write("\u015c\3\2\2\2\u0155\u0157\5c\62\2\u0156\u0158\5[.\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0152\3")
        buf.write("\2\2\2\u015b\u0155\3\2\2\2\u015cJ\3\2\2\2\u015d\u015e")
        buf.write("\5_\60\2\u015e\u0160\5i\65\2\u015f\u0161\5W,\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163L\3\2\2\2\u0164\u0165\5_\60\2\u0165")
        buf.write("\u0167\5\u0083B\2\u0166\u0168\5Y-\2\u0167\u0166\3\2\2")
        buf.write("\2\u0168\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016aN\3\2\2\2\u016b\u016c\5_\60\2\u016c\u016e")
        buf.write("\5\u0095K\2\u016d\u016f\5]/\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171P\3\2\2\2\u0172\u0174\5_\60\2\u0173\u0172\3\2\2")
        buf.write("\2\u0174\u0175\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u017f\3\2\2\2\u0177\u017b\t\7\2\2\u0178")
        buf.write("\u017a\5[.\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017f\3\2\2\2")
        buf.write("\u017d\u017b\3\2\2\2\u017e\u0173\3\2\2\2\u017e\u0177\3")
        buf.write("\2\2\2\u017fR\3\2\2\2\u0180\u0181\7,\2\2\u0181\u0182\7")
        buf.write("`\2\2\u0182T\3\2\2\2\u0183\u0184\7\61\2\2\u0184\u0185")
        buf.write("\7`\2\2\u0185V\3\2\2\2\u0186\u0189\5_\60\2\u0187\u0189")
        buf.write("\t\b\2\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("X\3\2\2\2\u018a\u018d\5_\60\2\u018b\u018d\t\t\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018dZ\3\2\2\2\u018e")
        buf.write("\u0191\5_\60\2\u018f\u0191\t\7\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u018f\3\2\2\2\u0191\\\3\2\2\2\u0192\u0195\5_\60")
        buf.write("\2\u0193\u0195\t\n\2\2\u0194\u0192\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195^\3\2\2\2\u0196\u0197\t\13\2\2\u0197`\3")
        buf.write("\2\2\2\u0198\u019c\5\u009dO\2\u0199\u019b\5\u00a1Q\2\u019a")
        buf.write("\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019db\3\2\2\2\u019e\u019c\3\2\2")
        buf.write("\2\u019f\u01a0\7\60\2\2\u01a0d\3\2\2\2\u01a1\u01a2\7a")
        buf.write("\2\2\u01a2f\3\2\2\2\u01a3\u01a4\t\f\2\2\u01a4h\3\2\2\2")
        buf.write("\u01a5\u01a6\t\r\2\2\u01a6j\3\2\2\2\u01a7\u01a8\t\16\2")
        buf.write("\2\u01a8l\3\2\2\2\u01a9\u01aa\t\17\2\2\u01aan\3\2\2\2")
        buf.write("\u01ab\u01ac\t\20\2\2\u01acp\3\2\2\2\u01ad\u01ae\t\21")
        buf.write("\2\2\u01aer\3\2\2\2\u01af\u01b0\t\22\2\2\u01b0t\3\2\2")
        buf.write("\2\u01b1\u01b2\t\23\2\2\u01b2v\3\2\2\2\u01b3\u01b4\t\24")
        buf.write("\2\2\u01b4x\3\2\2\2\u01b5\u01b6\t\25\2\2\u01b6z\3\2\2")
        buf.write("\2\u01b7\u01b8\t\26\2\2\u01b8|\3\2\2\2\u01b9\u01ba\t\27")
        buf.write("\2\2\u01ba~\3\2\2\2\u01bb\u01bc\t\30\2\2\u01bc\u0080\3")
        buf.write("\2\2\2\u01bd\u01be\t\31\2\2\u01be\u0082\3\2\2\2\u01bf")
        buf.write("\u01c0\t\32\2\2\u01c0\u0084\3\2\2\2\u01c1\u01c2\t\33\2")
        buf.write("\2\u01c2\u0086\3\2\2\2\u01c3\u01c4\t\34\2\2\u01c4\u0088")
        buf.write("\3\2\2\2\u01c5\u01c6\t\35\2\2\u01c6\u008a\3\2\2\2\u01c7")
        buf.write("\u01c8\t\36\2\2\u01c8\u008c\3\2\2\2\u01c9\u01ca\t\37\2")
        buf.write("\2\u01ca\u008e\3\2\2\2\u01cb\u01cc\t \2\2\u01cc\u0090")
        buf.write("\3\2\2\2\u01cd\u01ce\t!\2\2\u01ce\u0092\3\2\2\2\u01cf")
        buf.write("\u01d0\t\"\2\2\u01d0\u0094\3\2\2\2\u01d1\u01d2\t#\2\2")
        buf.write("\u01d2\u0096\3\2\2\2\u01d3\u01d4\t$\2\2\u01d4\u0098\3")
        buf.write("\2\2\2\u01d5\u01d6\t%\2\2\u01d6\u009a\3\2\2\2\u01d7\u01df")
        buf.write("\5g\64\2\u01d8\u01df\5i\65\2\u01d9\u01df\5k\66\2\u01da")
        buf.write("\u01df\5m\67\2\u01db\u01df\5o8\2\u01dc\u01df\5q9\2\u01dd")
        buf.write("\u01df\5s:\2\u01de\u01d7\3\2\2\2\u01de\u01d8\3\2\2\2\u01de")
        buf.write("\u01d9\3\2\2\2\u01de\u01da\3\2\2\2\u01de\u01db\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01fa\3")
        buf.write("\2\2\2\u01e0\u01e8\5u;\2\u01e1\u01e8\5w<\2\u01e2\u01e8")
        buf.write("\5y=\2\u01e3\u01e8\5{>\2\u01e4\u01e8\5}?\2\u01e5\u01e8")
        buf.write("\5\177@\2\u01e6\u01e8\5\u0081A\2\u01e7\u01e0\3\2\2\2\u01e7")
        buf.write("\u01e1\3\2\2\2\u01e7\u01e2\3\2\2\2\u01e7\u01e3\3\2\2\2")
        buf.write("\u01e7\u01e4\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3")
        buf.write("\2\2\2\u01e8\u01fa\3\2\2\2\u01e9\u01f0\5\u0083B\2\u01ea")
        buf.write("\u01f0\5\u0085C\2\u01eb\u01f0\5\u0087D\2\u01ec\u01f0\5")
        buf.write("\u0089E\2\u01ed\u01f0\5\u008bF\2\u01ee\u01f0\5\u008dG")
        buf.write("\2\u01ef\u01e9\3\2\2\2\u01ef\u01ea\3\2\2\2\u01ef\u01eb")
        buf.write("\3\2\2\2\u01ef\u01ec\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u01fa\3\2\2\2\u01f1\u01f8\5\u008f")
        buf.write("H\2\u01f2\u01f8\5\u0091I\2\u01f3\u01f8\5\u0093J\2\u01f4")
        buf.write("\u01f8\5\u0095K\2\u01f5\u01f8\5\u0097L\2\u01f6\u01f8\5")
        buf.write("\u0099M\2\u01f7\u01f1\3\2\2\2\u01f7\u01f2\3\2\2\2\u01f7")
        buf.write("\u01f3\3\2\2\2\u01f7\u01f4\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f6\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01de\3")
        buf.write("\2\2\2\u01f9\u01e7\3\2\2\2\u01f9\u01ef\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01fa\u009c\3\2\2\2\u01fb\u01fe\5e\63\2\u01fc")
        buf.write("\u01fe\5\u009bN\2\u01fd\u01fb\3\2\2\2\u01fd\u01fc\3\2")
        buf.write("\2\2\u01fe\u0201\3\2\2\2\u01ff\u0201\t\'\2\2\u0200\u01fd")
        buf.write("\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\u009e\3\2\2\2\u0202")
        buf.write("\u0203\t(\2\2\u0203\u00a0\3\2\2\2\u0204\u0207\5\u009d")
        buf.write("O\2\u0205\u0207\5[.\2\u0206\u0204\3\2\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u00a2\3\2\2\2\u0208\u020c\7%\2\2\u0209")
        buf.write("\u020b\n&\2\2\u020a\u0209\3\2\2\2\u020b\u020e\3\2\2\2")
        buf.write("\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020f\3")
        buf.write("\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210\bR\4\2\u0210\u00a4")
        buf.write("\3\2\2\2(\2\u00b4\u00bb\u00bf\u00c2\u00c4\u00cc\u00cf")
        buf.write("\u00d3\u010c\u0114\u011c\u0124\u0134\u0146\u014c\u0159")
        buf.write("\u015b\u0162\u0169\u0170\u0175\u017b\u017e\u0188\u018c")
        buf.write("\u0190\u0194\u019c\u01de\u01e7\u01ef\u01f7\u01f9\u01fd")
        buf.write("\u0200\u0206\u020c\5\b\2\2\3\t\2\2\3\2")
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
    NEWLINE = 8
    Escape = 9
    JoinLine = 10
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
    StringEscapeBlock = 24
    StringEscapeSingle = 25
    StringLiteralBlock = 26
    StringLiteralSingle = 27
    StringEmpty = 28
    Decimal = 29
    DecimalBad = 30
    Binary = 31
    Octal = 32
    Hexadecimal = 33
    Integer = 34
    Exponent = 35
    Base = 36
    Identifier = 37
    Dot = 38
    Underline = 39
    LineComment = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'['", "']'", "'('", "')'", "'\\'", "';'", "'import'", 
            "'package'", "'with'", "'as'", "','", "'*'", "'if'", "'else'", 
            "'for'", "'in'", "'=>'", "':'", "'*^'", "'/^'", "'.'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "NEWLINE", "Escape", "JoinLine", "Semicolon", "Import", 
            "Package", "With", "As", "Comma", "Star", "If", "Else", "For", 
            "In", "To", "Colon", "StringEscapeBlock", "StringEscapeSingle", 
            "StringLiteralBlock", "StringLiteralSingle", "StringEmpty", 
            "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
            "Exponent", "Base", "Identifier", "Dot", "Underline", "LineComment" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "SPACES", 
                  "NEWLINE", "Escape", "JoinLine", "Semicolon", "Import", 
                  "Package", "With", "As", "Comma", "Star", "If", "Else", 
                  "For", "In", "To", "Colon", "StringEscapeBlock", "StringEscapeSingle", 
                  "StringLiteralBlock", "StringLiteralSingle", "StringEmpty", 
                  "S6", "S3", "S2", "S1", "CharLevel1", "CharLevel2", "Decimal", 
                  "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
                  "Exponent", "Base", "Bin", "Oct", "Digit", "Hex", "Zero", 
                  "Identifier", "Dot", "Underline", "A", "B", "C", "D", 
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                  "Letter", "NameStartCharacter", "EmojiCharacter", "NameCharacter", 
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
            actions[7] = self.NEWLINE_action 
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
            preds[7] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


