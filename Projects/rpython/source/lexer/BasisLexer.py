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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2M")
        buf.write("\u02d2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\3\2\6\2\u00ed\n\2\r")
        buf.write("\2\16\2\u00ee\3\2\3\2\3\3\3\3\5\3\u00f5\n\3\3\3\5\3\u00f8")
        buf.write("\n\3\3\3\3\3\5\3\u00fc\n\3\3\3\3\3\3\4\3\4\3\4\5\4\u0103")
        buf.write("\n\4\3\4\3\4\5\4\u0107\n\4\3\4\5\4\u010a\n\4\5\4\u010c")
        buf.write("\n\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\6\25\u014e\n\25\r\25\16\25\u014f")
        buf.write("\3\25\3\25\3\26\3\26\6\26\u0156\n\26\r\26\16\26\u0157")
        buf.write("\3\26\3\26\3\27\3\27\6\27\u015e\n\27\r\27\16\27\u015f")
        buf.write("\3\27\3\27\3\30\3\30\6\30\u0166\n\30\r\30\16\30\u0167")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0178\n\31\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u018a\n\36\3\37\3\37\3\37\3\37\5\37\u0190\n")
        buf.write("\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\6!\u019b\n!\r!\16!\u019c")
        buf.write("\5!\u019f\n!\3\"\3\"\3\"\6\"\u01a4\n\"\r\"\16\"\u01a5")
        buf.write("\3#\3#\3#\6#\u01ab\n#\r#\16#\u01ac\3$\3$\3$\6$\u01b2\n")
        buf.write("$\r$\16$\u01b3\3%\6%\u01b7\n%\r%\16%\u01b8\3%\3%\7%\u01bd")
        buf.write("\n%\f%\16%\u01c0\13%\5%\u01c2\n%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\5(\u01cc\n(\3)\3)\5)\u01d0\n)\3*\3*\5*\u01d4\n")
        buf.write("*\3+\3+\5+\u01d8\n+\3,\3,\3-\3-\7-\u01de\n-\f-\16-\u01e1")
        buf.write("\13-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3")
        buf.write("J\3J\3J\3J\5J\u0222\nJ\3J\3J\3J\3J\3J\3J\3J\5J\u022b\n")
        buf.write("J\3J\3J\3J\3J\3J\3J\5J\u0233\nJ\3J\3J\3J\3J\3J\3J\5J\u023b")
        buf.write("\nJ\5J\u023d\nJ\3K\3K\5K\u0241\nK\3K\5K\u0244\nK\3L\3")
        buf.write("L\3M\3M\5M\u024a\nM\3N\3N\7N\u024e\nN\fN\16N\u0251\13")
        buf.write("N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3")
        buf.write("T\3T\3T\3U\3U\3U\5U\u026a\nU\3V\3V\3V\3W\3W\3X\3X\3X\5")
        buf.write("X\u0274\nX\3Y\3Y\3Y\3Z\3Z\3[\3[\3[\3\\\3\\\3]\3]\3]\3")
        buf.write("^\3^\3_\3_\3_\3_\3_\3_\3`\3`\3a\3a\3a\3b\3b\3b\3b\3b\3")
        buf.write("b\3b\3c\3c\3d\3d\3d\3d\3e\3e\3e\3e\3f\3f\3f\3g\3g\3g\3")
        buf.write("h\3h\3h\3i\3i\3i\5i\u02ad\ni\3j\3j\3j\5j\u02b2\nj\3k\3")
        buf.write("k\3k\3l\3l\3l\5l\u02ba\nl\3m\3m\3n\3n\5n\u02c0\nn\3o\3")
        buf.write("o\3o\3p\3p\3q\3q\3r\3r\3s\3s\3t\3t\3t\3t\3u\3u\6\u014f")
        buf.write("\u0157\u015f\u0167\2v\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\2\65\2\67\29\2;\2=\2?\33")
        buf.write("A\34C\35E\36G\37I K!M\"O\2Q\2S\2U\2W\2Y#[$]%_\2a\2c\2")
        buf.write("e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2")
        buf.write("\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b&\u009d")
        buf.write("\'\u009f(\u00a1)\u00a3*\u00a5+\u00a7,\u00a9-\u00ab.\u00ad")
        buf.write("/\u00af\60\u00b1\61\u00b3\62\u00b5\63\u00b7\64\u00b9\65")
        buf.write("\u00bb\66\u00bd\67\u00bf8\u00c19\u00c3:\u00c5;\u00c7<")
        buf.write("\u00c9=\u00cb>\u00cd?\u00cf@\u00d1A\u00d3B\u00d5C\u00d7")
        buf.write("D\u00d9E\u00dbF\u00ddG\u00dfH\u00e1I\u00e3J\u00e5K\u00e7")
        buf.write("L\u00e9M\3\2(\4\2\13\13\"\"\3\2))\3\2\"\"\3\2^^\4\2))")
        buf.write("^^\3\2\63;\3\2\63\63\3\2\639\5\2\63;CHch\3\2\62\62\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f")
        buf.write("\17\17\4\2##\uff03\uff03\4Y\2C\2\\\2c\2|\2\u00ac\2\u00ac")
        buf.write("\2\u00bc\2\u00bc\2\u00c2\2\u00d8\2\u00da\2\u00f8\2\u00fa")
        buf.write("\2\u02ba\2\u02e2\2\u02e6\2\u0372\2\u0375\2\u0377\2\u0379")
        buf.write("\2\u037c\2\u037f\2\u0381\2\u0381\2\u0386\2\u0386\2\u0388")
        buf.write("\2\u0388\2\u038a\2\u038c\2\u038e\2\u038e\2\u0390\2\u03a3")
        buf.write("\2\u03a5\2\u03e3\2\u03f2\2\u0401\2\u1d02\2\u1d2c\2\u1d2e")
        buf.write("\2\u1d79\2\u1d7b\2\u1dc1\2\u1e02\2\u1f17\2\u1f1a\2\u1f1f")
        buf.write("\2\u1f22\2\u1f47\2\u1f4a\2\u1f4f\2\u1f52\2\u1f59\2\u1f5b")
        buf.write("\2\u1f5b\2\u1f5d\2\u1f5d\2\u1f5f\2\u1f5f\2\u1f61\2\u1f7f")
        buf.write("\2\u1f82\2\u1fb6\2\u1fb8\2\u1fc6\2\u1fc8\2\u1fd5\2\u1fd8")
        buf.write("\2\u1fdd\2\u1fdf\2\u1ff1\2\u1ff4\2\u1ff6\2\u1ff8\2\u2000")
        buf.write("\2\u2073\2\u2073\2\u2081\2\u2081\2\u2092\2\u209e\2\u2128")
        buf.write("\2\u2128\2\u212c\2\u212d\2\u2134\2\u2134\2\u2150\2\u2150")
        buf.write("\2\u2162\2\u218a\2\u2c62\2\u2c81\2\u2e82\2\u2e9b\2\u2e9d")
        buf.write("\2\u2ef5\2\u2f02\2\u2fd7\2\u3007\2\u3007\2\u3009\2\u3009")
        buf.write("\2\u3023\2\u302b\2\u303a\2\u303d\2\u3043\2\u3098\2\u309f")
        buf.write("\2\u30a1\2\u30a3\2\u30fc\2\u30ff\2\u3101\2\u31f2\2\u3201")
        buf.write("\2\u32d2\2\u3300\2\u3302\2\u3359\2\u3402\2\u4db7\2\u4e02")
        buf.write("\2\u9fec\2\ua724\2\ua789\2\ua78d\2\ua7b0\2\ua7b2\2\ua7b9")
        buf.write("\2\ua7f9\2\ua801\2\uab32\2\uab5c\2\uab5e\2\uab67\2\uf902")
        buf.write("\2\ufa6f\2\ufa72\2\ufadb\2\ufb02\2\ufb08\2\uff23\2\uff3c")
        buf.write("\2\uff43\2\uff5c\2\uff68\2\uff71\2\uff73\2\uff9f\2\u0142")
        buf.write("\3\u0190\3\u01a2\3\u01a2\3\ub002\3\ub120\3\ud202\3\ud247")
        buf.write("\3\uf202\3\uf202\3\2\4\ua6d8\4\ua702\4\ub736\4\ub742\4")
        buf.write("\ub81f\4\ub822\4\ucea3\4\uceb2\4\uebe2\4\uf802\4\ufa1f")
        buf.write("\4\u0093\2%\2%\2,\2,\2\62\2;\2\u00ab\2\u00ab\2\u00b0\2")
        buf.write("\u00b0\2\u203e\2\u203e\2\u204b\2\u204b\2\u2124\2\u2124")
        buf.write("\2\u213b\2\u213b\2\u2196\2\u219b\2\u21ab\2\u21ac\2\u231c")
        buf.write("\2\u231d\2\u232a\2\u232a\2\u23d1\2\u23d1\2\u23eb\2\u23f5")
        buf.write("\2\u23fa\2\u23fc\2\u24c4\2\u24c4\2\u25ac\2\u25ad\2\u25b8")
        buf.write("\2\u25b8\2\u25c2\2\u25c2\2\u25fd\2\u2600\2\u2602\2\u2606")
        buf.write("\2\u2610\2\u2610\2\u2613\2\u2613\2\u2616\2\u2617\2\u261a")
        buf.write("\2\u261a\2\u261f\2\u261f\2\u2622\2\u2622\2\u2624\2\u2625")
        buf.write("\2\u2628\2\u2628\2\u262c\2\u262c\2\u2630\2\u2631\2\u263a")
        buf.write("\2\u263c\2\u2642\2\u2642\2\u2644\2\u2644\2\u264a\2\u2655")
        buf.write("\2\u2662\2\u2662\2\u2665\2\u2665\2\u2667\2\u2668\2\u266a")
        buf.write("\2\u266a\2\u267d\2\u267d\2\u2681\2\u2681\2\u2694\2\u2699")
        buf.write("\2\u269b\2\u269b\2\u269d\2\u269e\2\u26a2\2\u26a3\2\u26ac")
        buf.write("\2\u26ad\2\u26b2\2\u26b3\2\u26bf\2\u26c0\2\u26c6\2\u26c7")
        buf.write("\2\u26ca\2\u26ca\2\u26d0\2\u26d1\2\u26d3\2\u26d3\2\u26d5")
        buf.write("\2\u26d6\2\u26eb\2\u26ec\2\u26f2\2\u26f7\2\u26f9\2\u26fc")
        buf.write("\2\u26ff\2\u26ff\2\u2704\2\u2704\2\u2707\2\u2707\2\u270a")
        buf.write("\2\u270f\2\u2711\2\u2711\2\u2714\2\u2714\2\u2716\2\u2716")
        buf.write("\2\u2718\2\u2718\2\u271f\2\u271f\2\u2723\2\u2723\2\u272a")
        buf.write("\2\u272a\2\u2735\2\u2736\2\u2746\2\u2746\2\u2749\2\u2749")
        buf.write("\2\u274e\2\u274e\2\u2750\2\u2750\2\u2755\2\u2757\2\u2759")
        buf.write("\2\u2759\2\u2765\2\u2766\2\u2797\2\u2799\2\u27a3\2\u27a3")
        buf.write("\2\u27b2\2\u27b2\2\u27c1\2\u27c1\2\u2936\2\u2937\2\u2b07")
        buf.write("\2\u2b09\2\u2b1d\2\u2b1e\2\u2b52\2\u2b52\2\u2b57\2\u2b57")
        buf.write("\2\u3032\2\u3032\2\u303f\2\u303f\2\u3299\2\u3299\2\u329b")
        buf.write("\2\u329b\2\uf006\3\uf006\3\uf0d1\3\uf0d1\3\uf172\3\uf173")
        buf.write("\3\uf180\3\uf181\3\uf190\3\uf190\3\uf193\3\uf19c\3\uf1e8")
        buf.write("\3\uf201\3\uf203\3\uf204\3\uf21c\3\uf21c\3\uf231\3\uf231")
        buf.write("\3\uf234\3\uf23c\3\uf252\3\uf253\3\uf302\3\uf323\3\uf326")
        buf.write("\3\uf395\3\uf398\3\uf399\3\uf39b\3\uf39d\3\uf3a0\3\uf3f2")
        buf.write("\3\uf3f5\3\uf3f7\3\uf3f9\3\uf4ff\3\uf501\3\uf53f\3\uf54b")
        buf.write("\3\uf550\3\uf552\3\uf569\3\uf571\3\uf572\3\uf575\3\uf57c")
        buf.write("\3\uf589\3\uf589\3\uf58c\3\uf58f\3\uf592\3\uf592\3\uf597")
        buf.write("\3\uf598\3\uf5a6\3\uf5a7\3\uf5aa\3\uf5aa\3\uf5b3\3\uf5b4")
        buf.write("\3\uf5be\3\uf5be\3\uf5c4\3\uf5c6\3\uf5d3\3\uf5d5\3\uf5de")
        buf.write("\3\uf5e0\3\uf5e3\3\uf5e3\3\uf5e5\3\uf5e5\3\uf5ea\3\uf5ea")
        buf.write("\3\uf5f1\3\uf5f1\3\uf5f5\3\uf5f5\3\uf5fc\3\uf651\3\uf682")
        buf.write("\3\uf6c7\3\uf6cd\3\uf6d4\3\uf6e2\3\uf6e7\3\uf6eb\3\uf6eb")
        buf.write("\3\uf6ed\3\uf6ee\3\uf6f2\3\uf6f2\3\uf6f5\3\uf6fa\3\uf912")
        buf.write("\3\uf93c\3\uf93e\3\uf940\3\uf942\3\uf947\3\uf949\3\uf94e")
        buf.write("\3\uf952\3\uf96d\3\uf982\3\uf999\3\uf9c2\3\uf9c2\3\uf9d2")
        buf.write("\3\uf9e8\3\u02e9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2?\3\2\2\2\2A")
        buf.write("\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2")
        buf.write("K\3\2\2\2\2M\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb")
        buf.write("\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2")
        buf.write("\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9")
        buf.write("\3\2\2\2\2\u00db\3\2\2\2\2\u00dd\3\2\2\2\2\u00df\3\2\2")
        buf.write("\2\2\u00e1\3\2\2\2\2\u00e3\3\2\2\2\2\u00e5\3\2\2\2\2\u00e7")
        buf.write("\3\2\2\2\2\u00e9\3\2\2\2\3\u00ec\3\2\2\2\5\u00f2\3\2\2")
        buf.write("\2\7\u010b\3\2\2\2\t\u010f\3\2\2\2\13\u0111\3\2\2\2\r")
        buf.write("\u0113\3\2\2\2\17\u011a\3\2\2\2\21\u0122\3\2\2\2\23\u0127")
        buf.write("\3\2\2\2\25\u012a\3\2\2\2\27\u012c\3\2\2\2\31\u012e\3")
        buf.write("\2\2\2\33\u0131\3\2\2\2\35\u0136\3\2\2\2\37\u013a\3\2")
        buf.write("\2\2!\u013d\3\2\2\2#\u0140\3\2\2\2%\u0142\3\2\2\2\'\u0144")
        buf.write("\3\2\2\2)\u014b\3\2\2\2+\u0153\3\2\2\2-\u015b\3\2\2\2")
        buf.write("/\u0163\3\2\2\2\61\u0177\3\2\2\2\63\u0179\3\2\2\2\65\u017d")
        buf.write("\3\2\2\2\67\u0181\3\2\2\29\u0183\3\2\2\2;\u0189\3\2\2")
        buf.write("\2=\u018f\3\2\2\2?\u0191\3\2\2\2A\u019e\3\2\2\2C\u01a0")
        buf.write("\3\2\2\2E\u01a7\3\2\2\2G\u01ae\3\2\2\2I\u01c1\3\2\2\2")
        buf.write("K\u01c3\3\2\2\2M\u01c6\3\2\2\2O\u01cb\3\2\2\2Q\u01cf\3")
        buf.write("\2\2\2S\u01d3\3\2\2\2U\u01d7\3\2\2\2W\u01d9\3\2\2\2Y\u01db")
        buf.write("\3\2\2\2[\u01e2\3\2\2\2]\u01e4\3\2\2\2_\u01e6\3\2\2\2")
        buf.write("a\u01e8\3\2\2\2c\u01ea\3\2\2\2e\u01ec\3\2\2\2g\u01ee\3")
        buf.write("\2\2\2i\u01f0\3\2\2\2k\u01f2\3\2\2\2m\u01f4\3\2\2\2o\u01f6")
        buf.write("\3\2\2\2q\u01f8\3\2\2\2s\u01fa\3\2\2\2u\u01fc\3\2\2\2")
        buf.write("w\u01fe\3\2\2\2y\u0200\3\2\2\2{\u0202\3\2\2\2}\u0204\3")
        buf.write("\2\2\2\177\u0206\3\2\2\2\u0081\u0208\3\2\2\2\u0083\u020a")
        buf.write("\3\2\2\2\u0085\u020c\3\2\2\2\u0087\u020e\3\2\2\2\u0089")
        buf.write("\u0210\3\2\2\2\u008b\u0212\3\2\2\2\u008d\u0214\3\2\2\2")
        buf.write("\u008f\u0216\3\2\2\2\u0091\u0218\3\2\2\2\u0093\u023c\3")
        buf.write("\2\2\2\u0095\u0243\3\2\2\2\u0097\u0245\3\2\2\2\u0099\u0249")
        buf.write("\3\2\2\2\u009b\u024b\3\2\2\2\u009d\u0254\3\2\2\2\u009f")
        buf.write("\u0257\3\2\2\2\u00a1\u025a\3\2\2\2\u00a3\u025d\3\2\2\2")
        buf.write("\u00a5\u0260\3\2\2\2\u00a7\u0263\3\2\2\2\u00a9\u0269\3")
        buf.write("\2\2\2\u00ab\u026b\3\2\2\2\u00ad\u026e\3\2\2\2\u00af\u0273")
        buf.write("\3\2\2\2\u00b1\u0275\3\2\2\2\u00b3\u0278\3\2\2\2\u00b5")
        buf.write("\u027a\3\2\2\2\u00b7\u027d\3\2\2\2\u00b9\u027f\3\2\2\2")
        buf.write("\u00bb\u0282\3\2\2\2\u00bd\u0284\3\2\2\2\u00bf\u028a\3")
        buf.write("\2\2\2\u00c1\u028c\3\2\2\2\u00c3\u028f\3\2\2\2\u00c5\u0296")
        buf.write("\3\2\2\2\u00c7\u0298\3\2\2\2\u00c9\u029c\3\2\2\2\u00cb")
        buf.write("\u02a0\3\2\2\2\u00cd\u02a3\3\2\2\2\u00cf\u02a6\3\2\2\2")
        buf.write("\u00d1\u02ac\3\2\2\2\u00d3\u02b1\3\2\2\2\u00d5\u02b3\3")
        buf.write("\2\2\2\u00d7\u02b9\3\2\2\2\u00d9\u02bb\3\2\2\2\u00db\u02bf")
        buf.write("\3\2\2\2\u00dd\u02c1\3\2\2\2\u00df\u02c4\3\2\2\2\u00e1")
        buf.write("\u02c6\3\2\2\2\u00e3\u02c8\3\2\2\2\u00e5\u02ca\3\2\2\2")
        buf.write("\u00e7\u02cc\3\2\2\2\u00e9\u02d0\3\2\2\2\u00eb\u00ed\t")
        buf.write("\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f1\b\2\2\2\u00f1\4\3\2\2\2\u00f2\u00f4\5\t\5\2\u00f3")
        buf.write("\u00f5\5\3\2\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00fb\3\2\2\2\u00f6\u00f8\7\17\2\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fc\7\f\2\2\u00fa\u00fc\7\17\2\2\u00fb\u00f7\3\2\2")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe")
        buf.write("\b\3\2\2\u00fe\6\3\2\2\2\u00ff\u0100\6\4\2\2\u0100\u010c")
        buf.write("\5\3\2\2\u0101\u0103\7\17\2\2\u0102\u0101\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0107\7\f\2\2")
        buf.write("\u0105\u0107\4\16\17\2\u0106\u0102\3\2\2\2\u0106\u0105")
        buf.write("\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u010a\5\3\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2")
        buf.write("\u010b\u00ff\3\2\2\2\u010b\u0106\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010e\b\4\3\2\u010e\b\3\2\2\2\u010f\u0110")
        buf.write("\7^\2\2\u0110\n\3\2\2\2\u0111\u0112\7=\2\2\u0112\f\3\2")
        buf.write("\2\2\u0113\u0114\7k\2\2\u0114\u0115\7o\2\2\u0115\u0116")
        buf.write("\7r\2\2\u0116\u0117\7q\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\16\3\2\2\2\u011a\u011b\7r\2\2\u011b\u011c")
        buf.write("\7c\2\2\u011c\u011d\7e\2\2\u011d\u011e\7m\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7i\2\2\u0120\u0121\7g\2\2\u0121\20")
        buf.write("\3\2\2\2\u0122\u0123\7y\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7j\2\2\u0126\22\3\2\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7u\2\2\u0129\24\3\2\2\2\u012a\u012b")
        buf.write("\7.\2\2\u012b\26\3\2\2\2\u012c\u012d\7,\2\2\u012d\30\3")
        buf.write("\2\2\2\u012e\u012f\7k\2\2\u012f\u0130\7h\2\2\u0130\32")
        buf.write("\3\2\2\2\u0131\u0132\7g\2\2\u0132\u0133\7n\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134\u0135\7g\2\2\u0135\34\3\2\2\2\u0136\u0137")
        buf.write("\7h\2\2\u0137\u0138\7q\2\2\u0138\u0139\7t\2\2\u0139\36")
        buf.write("\3\2\2\2\u013a\u013b\7k\2\2\u013b\u013c\7p\2\2\u013c ")
        buf.write("\3\2\2\2\u013d\u013e\7?\2\2\u013e\u013f\7@\2\2\u013f\"")
        buf.write("\3\2\2\2\u0140\u0141\7<\2\2\u0141$\3\2\2\2\u0142\u0143")
        buf.write("\7?\2\2\u0143&\3\2\2\2\u0144\u0145\7t\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146\u0147\7v\2\2\u0147\u0148\7w\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7p\2\2\u014a(\3\2\2\2\u014b\u014d")
        buf.write("\5\63\32\2\u014c\u014e\5;\36\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0152\5\63\32\2\u0152*\3\2")
        buf.write("\2\2\u0153\u0155\5\67\34\2\u0154\u0156\5=\37\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\5\67\34")
        buf.write("\2\u015a,\3\2\2\2\u015b\u015d\5\65\33\2\u015c\u015e\13")
        buf.write("\2\2\2\u015d\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u0162\5\65\33\2\u0162.\3\2\2\2\u0163\u0165\59\35\2\u0164")
        buf.write("\u0166\n\3\2\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u016a\59\35\2\u016a\60\3\2\2\2\u016b\u016c")
        buf.write("\5\63\32\2\u016c\u016d\5\63\32\2\u016d\u0178\3\2\2\2\u016e")
        buf.write("\u016f\5\65\33\2\u016f\u0170\5\65\33\2\u0170\u0178\3\2")
        buf.write("\2\2\u0171\u0172\5\67\34\2\u0172\u0173\5\67\34\2\u0173")
        buf.write("\u0178\3\2\2\2\u0174\u0175\59\35\2\u0175\u0176\59\35\2")
        buf.write("\u0176\u0178\3\2\2\2\u0177\u016b\3\2\2\2\u0177\u016e\3")
        buf.write("\2\2\2\u0177\u0171\3\2\2\2\u0177\u0174\3\2\2\2\u0178\62")
        buf.write("\3\2\2\2\u0179\u017a\7$\2\2\u017a\u017b\7$\2\2\u017b\u017c")
        buf.write("\7$\2\2\u017c\64\3\2\2\2\u017d\u017e\7)\2\2\u017e\u017f")
        buf.write("\7)\2\2\u017f\u0180\7)\2\2\u0180\66\3\2\2\2\u0181\u0182")
        buf.write("\7$\2\2\u01828\3\2\2\2\u0183\u0184\7)\2\2\u0184:\3\2\2")
        buf.write("\2\u0185\u0186\5\t\5\2\u0186\u0187\n\4\2\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u018a\n\5\2\2\u0189\u0185\3\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a<\3\2\2\2\u018b\u018c\5\t\5\2\u018c")
        buf.write("\u018d\n\4\2\2\u018d\u0190\3\2\2\2\u018e\u0190\n\6\2\2")
        buf.write("\u018f\u018b\3\2\2\2\u018f\u018e\3\2\2\2\u0190>\3\2\2")
        buf.write("\2\u0191\u0192\5I%\2\u0192\u0193\5[.\2\u0193\u0194\5S")
        buf.write("*\2\u0194@\3\2\2\2\u0195\u0196\5I%\2\u0196\u0197\5[.\2")
        buf.write("\u0197\u019f\3\2\2\2\u0198\u019a\5[.\2\u0199\u019b\5S")
        buf.write("*\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u0195\3\2\2\2\u019e\u0198\3\2\2\2\u019fB\3\2\2\2\u01a0")
        buf.write("\u01a1\5W,\2\u01a1\u01a3\5a\61\2\u01a2\u01a4\5O(\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6D\3\2\2\2\u01a7\u01a8\5W,\2")
        buf.write("\u01a8\u01aa\5{>\2\u01a9\u01ab\5Q)\2\u01aa\u01a9\3\2\2")
        buf.write("\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01adF\3\2\2\2\u01ae\u01af\5W,\2\u01af\u01b1")
        buf.write("\5\u008dG\2\u01b0\u01b2\5U+\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2")
        buf.write("\u01b4H\3\2\2\2\u01b5\u01b7\5W,\2\u01b6\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3")
        buf.write("\2\2\2\u01b9\u01c2\3\2\2\2\u01ba\u01be\t\7\2\2\u01bb\u01bd")
        buf.write("\5S*\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01b6\3\2\2\2\u01c1\u01ba\3\2\2\2")
        buf.write("\u01c2J\3\2\2\2\u01c3\u01c4\7,\2\2\u01c4\u01c5\7`\2\2")
        buf.write("\u01c5L\3\2\2\2\u01c6\u01c7\7\61\2\2\u01c7\u01c8\7`\2")
        buf.write("\2\u01c8N\3\2\2\2\u01c9\u01cc\5W,\2\u01ca\u01cc\t\b\2")
        buf.write("\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01ccP\3\2")
        buf.write("\2\2\u01cd\u01d0\5W,\2\u01ce\u01d0\t\t\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0R\3\2\2\2\u01d1\u01d4")
        buf.write("\5W,\2\u01d2\u01d4\t\7\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d4T\3\2\2\2\u01d5\u01d8\5W,\2\u01d6\u01d8")
        buf.write("\t\n\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8")
        buf.write("V\3\2\2\2\u01d9\u01da\t\13\2\2\u01daX\3\2\2\2\u01db\u01df")
        buf.write("\5\u0095K\2\u01dc\u01de\5\u0099M\2\u01dd\u01dc\3\2\2\2")
        buf.write("\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3")
        buf.write("\2\2\2\u01e0Z\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3")
        buf.write("\7\60\2\2\u01e3\\\3\2\2\2\u01e4\u01e5\7a\2\2\u01e5^\3")
        buf.write("\2\2\2\u01e6\u01e7\t\f\2\2\u01e7`\3\2\2\2\u01e8\u01e9")
        buf.write("\t\r\2\2\u01e9b\3\2\2\2\u01ea\u01eb\t\16\2\2\u01ebd\3")
        buf.write("\2\2\2\u01ec\u01ed\t\17\2\2\u01edf\3\2\2\2\u01ee\u01ef")
        buf.write("\t\20\2\2\u01efh\3\2\2\2\u01f0\u01f1\t\21\2\2\u01f1j\3")
        buf.write("\2\2\2\u01f2\u01f3\t\22\2\2\u01f3l\3\2\2\2\u01f4\u01f5")
        buf.write("\t\23\2\2\u01f5n\3\2\2\2\u01f6\u01f7\t\24\2\2\u01f7p\3")
        buf.write("\2\2\2\u01f8\u01f9\t\25\2\2\u01f9r\3\2\2\2\u01fa\u01fb")
        buf.write("\t\26\2\2\u01fbt\3\2\2\2\u01fc\u01fd\t\27\2\2\u01fdv\3")
        buf.write("\2\2\2\u01fe\u01ff\t\30\2\2\u01ffx\3\2\2\2\u0200\u0201")
        buf.write("\t\31\2\2\u0201z\3\2\2\2\u0202\u0203\t\32\2\2\u0203|\3")
        buf.write("\2\2\2\u0204\u0205\t\33\2\2\u0205~\3\2\2\2\u0206\u0207")
        buf.write("\t\34\2\2\u0207\u0080\3\2\2\2\u0208\u0209\t\35\2\2\u0209")
        buf.write("\u0082\3\2\2\2\u020a\u020b\t\36\2\2\u020b\u0084\3\2\2")
        buf.write("\2\u020c\u020d\t\37\2\2\u020d\u0086\3\2\2\2\u020e\u020f")
        buf.write("\t \2\2\u020f\u0088\3\2\2\2\u0210\u0211\t!\2\2\u0211\u008a")
        buf.write("\3\2\2\2\u0212\u0213\t\"\2\2\u0213\u008c\3\2\2\2\u0214")
        buf.write("\u0215\t#\2\2\u0215\u008e\3\2\2\2\u0216\u0217\t$\2\2\u0217")
        buf.write("\u0090\3\2\2\2\u0218\u0219\t%\2\2\u0219\u0092\3\2\2\2")
        buf.write("\u021a\u0222\5_\60\2\u021b\u0222\5a\61\2\u021c\u0222\5")
        buf.write("c\62\2\u021d\u0222\5e\63\2\u021e\u0222\5g\64\2\u021f\u0222")
        buf.write("\5i\65\2\u0220\u0222\5k\66\2\u0221\u021a\3\2\2\2\u0221")
        buf.write("\u021b\3\2\2\2\u0221\u021c\3\2\2\2\u0221\u021d\3\2\2\2")
        buf.write("\u0221\u021e\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3")
        buf.write("\2\2\2\u0222\u023d\3\2\2\2\u0223\u022b\5m\67\2\u0224\u022b")
        buf.write("\5o8\2\u0225\u022b\5q9\2\u0226\u022b\5s:\2\u0227\u022b")
        buf.write("\5u;\2\u0228\u022b\5w<\2\u0229\u022b\5y=\2\u022a\u0223")
        buf.write("\3\2\2\2\u022a\u0224\3\2\2\2\u022a\u0225\3\2\2\2\u022a")
        buf.write("\u0226\3\2\2\2\u022a\u0227\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022a\u0229\3\2\2\2\u022b\u023d\3\2\2\2\u022c\u0233\5")
        buf.write("{>\2\u022d\u0233\5}?\2\u022e\u0233\5\177@\2\u022f\u0233")
        buf.write("\5\u0081A\2\u0230\u0233\5\u0083B\2\u0231\u0233\5\u0085")
        buf.write("C\2\u0232\u022c\3\2\2\2\u0232\u022d\3\2\2\2\u0232\u022e")
        buf.write("\3\2\2\2\u0232\u022f\3\2\2\2\u0232\u0230\3\2\2\2\u0232")
        buf.write("\u0231\3\2\2\2\u0233\u023d\3\2\2\2\u0234\u023b\5\u0087")
        buf.write("D\2\u0235\u023b\5\u0089E\2\u0236\u023b\5\u008bF\2\u0237")
        buf.write("\u023b\5\u008dG\2\u0238\u023b\5\u008fH\2\u0239\u023b\5")
        buf.write("\u0091I\2\u023a\u0234\3\2\2\2\u023a\u0235\3\2\2\2\u023a")
        buf.write("\u0236\3\2\2\2\u023a\u0237\3\2\2\2\u023a\u0238\3\2\2\2")
        buf.write("\u023a\u0239\3\2\2\2\u023b\u023d\3\2\2\2\u023c\u0221\3")
        buf.write("\2\2\2\u023c\u022a\3\2\2\2\u023c\u0232\3\2\2\2\u023c\u023a")
        buf.write("\3\2\2\2\u023d\u0094\3\2\2\2\u023e\u0241\5]/\2\u023f\u0241")
        buf.write("\5\u0093J\2\u0240\u023e\3\2\2\2\u0240\u023f\3\2\2\2\u0241")
        buf.write("\u0244\3\2\2\2\u0242\u0244\t(\2\2\u0243\u0240\3\2\2\2")
        buf.write("\u0243\u0242\3\2\2\2\u0244\u0096\3\2\2\2\u0245\u0246\t")
        buf.write(")\2\2\u0246\u0098\3\2\2\2\u0247\u024a\5\u0095K\2\u0248")
        buf.write("\u024a\5S*\2\u0249\u0247\3\2\2\2\u0249\u0248\3\2\2\2\u024a")
        buf.write("\u009a\3\2\2\2\u024b\u024f\7%\2\2\u024c\u024e\n&\2\2\u024d")
        buf.write("\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2")
        buf.write("\u024f\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3")
        buf.write("\2\2\2\u0252\u0253\bN\4\2\u0253\u009c\3\2\2\2\u0254\u0255")
        buf.write("\7*\2\2\u0255\u0256\bO\5\2\u0256\u009e\3\2\2\2\u0257\u0258")
        buf.write("\7+\2\2\u0258\u0259\bP\6\2\u0259\u00a0\3\2\2\2\u025a\u025b")
        buf.write("\7]\2\2\u025b\u025c\bQ\7\2\u025c\u00a2\3\2\2\2\u025d\u025e")
        buf.write("\7_\2\2\u025e\u025f\bR\b\2\u025f\u00a4\3\2\2\2\u0260\u0261")
        buf.write("\7}\2\2\u0261\u0262\bS\t\2\u0262\u00a6\3\2\2\2\u0263\u0264")
        buf.write("\7\177\2\2\u0264\u0265\bT\n\2\u0265\u00a8\3\2\2\2\u0266")
        buf.write("\u0267\7>\2\2\u0267\u026a\7>\2\2\u0268\u026a\7\u226c\2")
        buf.write("\2\u0269\u0266\3\2\2\2\u0269\u0268\3\2\2\2\u026a\u00aa")
        buf.write("\3\2\2\2\u026b\u026c\7>\2\2\u026c\u026d\7?\2\2\u026d\u00ac")
        buf.write("\3\2\2\2\u026e\u026f\7>\2\2\u026f\u00ae\3\2\2\2\u0270")
        buf.write("\u0271\7@\2\2\u0271\u0274\7@\2\2\u0272\u0274\7\u226d\2")
        buf.write("\2\u0273\u0270\3\2\2\2\u0273\u0272\3\2\2\2\u0274\u00b0")
        buf.write("\3\2\2\2\u0275\u0276\7@\2\2\u0276\u0277\7?\2\2\u0277\u00b2")
        buf.write("\3\2\2\2\u0278\u0279\7@\2\2\u0279\u00b4\3\2\2\2\u027a")
        buf.write("\u027b\7-\2\2\u027b\u027c\7-\2\2\u027c\u00b6\3\2\2\2\u027d")
        buf.write("\u027e\7-\2\2\u027e\u00b8\3\2\2\2\u027f\u0280\7/\2\2\u0280")
        buf.write("\u0281\7/\2\2\u0281\u00ba\3\2\2\2\u0282\u0283\7/\2\2\u0283")
        buf.write("\u00bc\3\2\2\2\u0284\u0285\7v\2\2\u0285\u0286\7k\2\2\u0286")
        buf.write("\u0287\7o\2\2\u0287\u0288\7g\2\2\u0288\u0289\7u\2\2\u0289")
        buf.write("\u00be\3\2\2\2\u028a\u028b\7\u22c7\2\2\u028b\u00c0\3\2")
        buf.write("\2\2\u028c\u028d\7\61\2\2\u028d\u028e\7\61\2\2\u028e\u00c2")
        buf.write("\3\2\2\2\u028f\u0290\7f\2\2\u0290\u0291\7k\2\2\u0291\u0292")
        buf.write("\7x\2\2\u0292\u0293\7k\2\2\u0293\u0294\7f\2\2\u0294\u0295")
        buf.write("\7g\2\2\u0295\u00c4\3\2\2\2\u0296\u0297\7\'\2\2\u0297")
        buf.write("\u00c6\3\2\2\2\u0298\u0299\7?\2\2\u0299\u029a\7?\2\2\u029a")
        buf.write("\u029b\7?\2\2\u029b\u00c8\3\2\2\2\u029c\u029d\7?\2\2\u029d")
        buf.write("\u029e\7#\2\2\u029e\u029f\7?\2\2\u029f\u00ca\3\2\2\2\u02a0")
        buf.write("\u02a1\7?\2\2\u02a1\u02a2\7?\2\2\u02a2\u00cc\3\2\2\2\u02a3")
        buf.write("\u02a4\7\u0080\2\2\u02a4\u02a5\7\u0080\2\2\u02a5\u00ce")
        buf.write("\3\2\2\2\u02a6\u02a7\7\u0080\2\2\u02a7\u02a8\7?\2\2\u02a8")
        buf.write("\u00d0\3\2\2\2\u02a9\u02aa\7~\2\2\u02aa\u02ad\7~\2\2\u02ab")
        buf.write("\u02ad\7\u2229\2\2\u02ac\u02a9\3\2\2\2\u02ac\u02ab\3\2")
        buf.write("\2\2\u02ad\u00d2\3\2\2\2\u02ae\u02af\7(\2\2\u02af\u02b2")
        buf.write("\7(\2\2\u02b0\u02b2\7\u222a\2\2\u02b1\u02ae\3\2\2\2\u02b1")
        buf.write("\u02b0\3\2\2\2\u02b2\u00d4\3\2\2\2\u02b3\u02b4\7#\2\2")
        buf.write("\u02b4\u02b5\7#\2\2\u02b5\u00d6\3\2\2\2\u02b6\u02b7\7")
        buf.write("#\2\2\u02b7\u02ba\7?\2\2\u02b8\u02ba\7\u2262\2\2\u02b9")
        buf.write("\u02b6\3\2\2\2\u02b9\u02b8\3\2\2\2\u02ba\u00d8\3\2\2\2")
        buf.write("\u02bb\u02bc\t\'\2\2\u02bc\u00da\3\2\2\2\u02bd\u02c0\5")
        buf.write("\u00d5k\2\u02be\u02c0\7\u00ae\2\2\u02bf\u02bd\3\2\2\2")
        buf.write("\u02bf\u02be\3\2\2\2\u02c0\u00dc\3\2\2\2\u02c1\u02c2\7")
        buf.write("<\2\2\u02c2\u02c3\7A\2\2\u02c3\u00de\3\2\2\2\u02c4\u02c5")
        buf.write("\7B\2\2\u02c5\u00e0\3\2\2\2\u02c6\u02c7\7b\2\2\u02c7\u00e2")
        buf.write("\3\2\2\2\u02c8\u02c9\7\u00b6\2\2\u02c9\u00e4\3\2\2\2\u02ca")
        buf.write("\u02cb\7)\2\2\u02cb\u00e6\3\2\2\2\u02cc\u02cd\7\60\2\2")
        buf.write("\u02cd\u02ce\7\60\2\2\u02ce\u02cf\7\60\2\2\u02cf\u00e8")
        buf.write("\3\2\2\2\u02d0\u02d1\7\u2161\2\2\u02d1\u00ea\3\2\2\2.")
        buf.write("\2\u00ee\u00f4\u00f7\u00fb\u0102\u0106\u0109\u010b\u014f")
        buf.write("\u0157\u015f\u0167\u0177\u0189\u018f\u019c\u019e\u01a5")
        buf.write("\u01ac\u01b3\u01b8\u01be\u01c1\u01cb\u01cf\u01d3\u01d7")
        buf.write("\u01df\u0221\u022a\u0232\u023a\u023c\u0240\u0243\u0249")
        buf.write("\u024f\u0269\u0273\u02ac\u02b1\u02b9\u02bf\13\b\2\2\3")
        buf.write("\4\2\2\3\2\3O\3\3P\4\3Q\5\3R\6\3S\7\3T\b")
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
    LeftShift = 43
    LessEqual = 44
    Less = 45
    RightShift = 46
    GraterEqual = 47
    Grater = 48
    Increase = 49
    Plus = 50
    Decrease = 51
    Minus = 52
    Times = 53
    DOT = 54
    Quotient = 55
    Divide = 56
    Modulo = 57
    Equivalent = 58
    NotEquivalent = 59
    Equal = 60
    Concat = 61
    Destruct = 62
    LogicOr = 63
    LogicAnd = 64
    DoubleBang = 65
    NotEqual = 66
    BitNot = 67
    LogicNot = 68
    Elvis = 69
    Annotation = 70
    Quote = 71
    Acute = 72
    Quotation = 73
    Ellipsis = 74
    Reciprocal = 75

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "';'", "'import'", "'package'", "'with'", "'as'", "','", 
            "'*'", "'if'", "'else'", "'for'", "'in'", "'=>'", "':'", "'='", 
            "'return'", "'*^'", "'/^'", "'.'", "'_'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'<='", "'<'", "'>='", "'>'", "'++'", "'+'", 
            "'--'", "'-'", "'times'", "'\u22C5'", "'//'", "'divide'", "'%'", 
            "'==='", "'=!='", "'=='", "'~~'", "'~='", "'!!'", "':?'", "'@'", 
            "'`'", "'\u00B4'", "'''", "'...'", "'\u215F'" ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "JoinLine", "NEWLINE", "Escape", "Semicolon", "Import", 
            "Package", "With", "As", "Comma", "Star", "If", "Else", "For", 
            "In", "To", "Colon", "Set", "Return", "StringEscapeBlock", "StringEscapeSingle", 
            "StringLiteralBlock", "StringLiteralSingle", "StringEmpty", 
            "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
            "Exponent", "Base", "Identifier", "Dot", "Underline", "LineComment", 
            "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
            "CLOSE_BRACE", "LeftShift", "LessEqual", "Less", "RightShift", 
            "GraterEqual", "Grater", "Increase", "Plus", "Decrease", "Minus", 
            "Times", "DOT", "Quotient", "Divide", "Modulo", "Equivalent", 
            "NotEquivalent", "Equal", "Concat", "Destruct", "LogicOr", "LogicAnd", 
            "DoubleBang", "NotEqual", "BitNot", "LogicNot", "Elvis", "Annotation", 
            "Quote", "Acute", "Quotation", "Ellipsis", "Reciprocal" ]

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
                  "LeftShift", "LessEqual", "Less", "RightShift", "GraterEqual", 
                  "Grater", "Increase", "Plus", "Decrease", "Minus", "Times", 
                  "DOT", "Quotient", "Divide", "Modulo", "Equivalent", "NotEquivalent", 
                  "Equal", "Concat", "Destruct", "LogicOr", "LogicAnd", 
                  "DoubleBang", "NotEqual", "BitNot", "LogicNot", "Elvis", 
                  "Annotation", "Quote", "Acute", "Quotation", "Ellipsis", 
                  "Reciprocal" ]

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
         


