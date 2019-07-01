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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2T")
        buf.write("\u0305\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\3\2\6\2\u00fb\n\2\r\2\16\2\u00fc")
        buf.write("\3\2\3\2\3\3\3\3\5\3\u0103\n\3\3\3\5\3\u0106\n\3\3\3\3")
        buf.write("\3\5\3\u010a\n\3\3\3\3\3\3\4\3\4\3\4\5\4\u0111\n\4\3\4")
        buf.write("\3\4\5\4\u0115\n\4\3\4\5\4\u0118\n\4\5\4\u011a\n\4\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\6\25\u015c\n\25\r\25\16\25\u015d\3\25\3\25")
        buf.write("\3\26\3\26\6\26\u0164\n\26\r\26\16\26\u0165\3\26\3\26")
        buf.write("\3\27\3\27\6\27\u016c\n\27\r\27\16\27\u016d\3\27\3\27")
        buf.write("\3\30\3\30\6\30\u0174\n\30\r\30\16\30\u0175\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0186\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u0198\n\36\3\37\3\37\3\37\3\37\5\37\u019e\n\37\3 \3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\6!\u01a9\n!\r!\16!\u01aa\5!\u01ad")
        buf.write("\n!\3\"\3\"\3\"\5\"\u01b2\n\"\3\"\6\"\u01b5\n\"\r\"\16")
        buf.write("\"\u01b6\3#\3#\3#\5#\u01bc\n#\3#\6#\u01bf\n#\r#\16#\u01c0")
        buf.write("\3$\3$\3$\5$\u01c6\n$\3$\6$\u01c9\n$\r$\16$\u01ca\3%\6")
        buf.write("%\u01ce\n%\r%\16%\u01cf\3%\3%\5%\u01d4\n%\3%\7%\u01d7")
        buf.write("\n%\f%\16%\u01da\13%\5%\u01dc\n%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\5(\u01e6\n(\3)\3)\5)\u01ea\n)\3*\3*\5*\u01ee\n")
        buf.write("*\3+\3+\5+\u01f2\n+\3,\3,\3-\3-\7-\u01f8\n-\f-\16-\u01fb")
        buf.write("\13-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3")
        buf.write("J\3J\3J\3J\5J\u023c\nJ\3J\3J\3J\3J\3J\3J\3J\5J\u0245\n")
        buf.write("J\3J\3J\3J\3J\3J\3J\5J\u024d\nJ\3J\3J\3J\3J\3J\3J\5J\u0255")
        buf.write("\nJ\5J\u0257\nJ\3K\3K\5K\u025b\nK\3K\3K\3K\5K\u0260\n")
        buf.write("K\3K\5K\u0263\nK\3L\3L\3M\3M\5M\u0269\nM\3N\3N\7N\u026d")
        buf.write("\nN\fN\16N\u0270\13N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q")
        buf.write("\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3U\3U\3V\3V\3V\5V\u028d")
        buf.write("\nV\3W\3W\3W\3X\3X\3Y\3Y\3Y\3Y\3Z\3Z\3Z\5Z\u029b\nZ\3")
        buf.write("[\3[\3[\3\\\3\\\3]\3]\3]\3^\3^\3_\3_\3_\3`\3`\3a\3a\3")
        buf.write("a\3a\3a\3a\5a\u02b2\na\3b\3b\3b\3c\3c\3c\3c\3c\3c\3c\3")
        buf.write("d\3d\3e\3e\3e\3e\3f\3f\3f\3f\3g\3g\3g\3h\3h\3h\5h\u02ce")
        buf.write("\nh\3i\3i\3j\3j\3j\5j\u02d5\nj\3k\3k\3l\3l\3l\3m\3m\3")
        buf.write("m\5m\u02df\nm\3n\3n\5n\u02e3\nn\3o\3o\3p\3p\3p\3q\3q\3")
        buf.write("r\3r\3s\3s\3t\3t\3u\3u\3u\3v\3v\3v\3w\3w\3x\3x\3y\3y\3")
        buf.write("z\3z\3{\3{\3{\3{\3|\3|\6\u015d\u0165\u016d\u0175\2}\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\2\65\2\67\29\2;\2=\2?\33A\34C\35E\36G\37I K!M\"")
        buf.write("O\2Q\2S\2U\2W\2Y#[$]%_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2")
        buf.write("u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b&\u009d\'\u009f(\u00a1)\u00a3")
        buf.write("*\u00a5+\u00a7,\u00a9-\u00ab.\u00ad/\u00af\60\u00b1\61")
        buf.write("\u00b3\62\u00b5\63\u00b7\64\u00b9\65\u00bb\66\u00bd\67")
        buf.write("\u00bf8\u00c19\u00c3:\u00c5;\u00c7<\u00c9=\u00cb>\u00cd")
        buf.write("?\u00cf@\u00d1A\u00d3B\u00d5C\u00d7D\u00d9E\u00dbF\u00dd")
        buf.write("G\u00dfH\u00e1I\u00e3J\u00e5K\u00e7L\u00e9M\u00ebN\u00ed")
        buf.write("O\u00efP\u00f1Q\u00f3R\u00f5S\u00f7T\3\2(\4\2\13\13\"")
        buf.write("\"\3\2))\3\2\"\"\3\2^^\4\2))^^\3\2\63;\3\2\63\63\3\2\63")
        buf.write("9\5\2\63;CHch\3\2\62\62\4\2CCcc\4\2DDdd\4\2EEee\4\2FF")
        buf.write("ff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2")
        buf.write("MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4")
        buf.write("\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZz")
        buf.write("z\4\2[[{{\4\2\\\\||\4\2\f\f\17\17\4\2##\uff03\uff03\4")
        buf.write("Y\2C\2\\\2c\2|\2\u00ac\2\u00ac\2\u00bc\2\u00bc\2\u00c2")
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
        buf.write("\3\uf999\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8\3\u0324\2\3\3")
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
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2")
        buf.write("\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7")
        buf.write("\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2")
        buf.write("\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5")
        buf.write("\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2")
        buf.write("\2\2\u00dd\3\2\2\2\2\u00df\3\2\2\2\2\u00e1\3\2\2\2\2\u00e3")
        buf.write("\3\2\2\2\2\u00e5\3\2\2\2\2\u00e7\3\2\2\2\2\u00e9\3\2\2")
        buf.write("\2\2\u00eb\3\2\2\2\2\u00ed\3\2\2\2\2\u00ef\3\2\2\2\2\u00f1")
        buf.write("\3\2\2\2\2\u00f3\3\2\2\2\2\u00f5\3\2\2\2\2\u00f7\3\2\2")
        buf.write("\2\3\u00fa\3\2\2\2\5\u0100\3\2\2\2\7\u0119\3\2\2\2\t\u011d")
        buf.write("\3\2\2\2\13\u011f\3\2\2\2\r\u0121\3\2\2\2\17\u0128\3\2")
        buf.write("\2\2\21\u0130\3\2\2\2\23\u0135\3\2\2\2\25\u0138\3\2\2")
        buf.write("\2\27\u013a\3\2\2\2\31\u013c\3\2\2\2\33\u013f\3\2\2\2")
        buf.write("\35\u0144\3\2\2\2\37\u0148\3\2\2\2!\u014b\3\2\2\2#\u014e")
        buf.write("\3\2\2\2%\u0150\3\2\2\2\'\u0152\3\2\2\2)\u0159\3\2\2\2")
        buf.write("+\u0161\3\2\2\2-\u0169\3\2\2\2/\u0171\3\2\2\2\61\u0185")
        buf.write("\3\2\2\2\63\u0187\3\2\2\2\65\u018b\3\2\2\2\67\u018f\3")
        buf.write("\2\2\29\u0191\3\2\2\2;\u0197\3\2\2\2=\u019d\3\2\2\2?\u019f")
        buf.write("\3\2\2\2A\u01ac\3\2\2\2C\u01ae\3\2\2\2E\u01b8\3\2\2\2")
        buf.write("G\u01c2\3\2\2\2I\u01db\3\2\2\2K\u01dd\3\2\2\2M\u01e0\3")
        buf.write("\2\2\2O\u01e5\3\2\2\2Q\u01e9\3\2\2\2S\u01ed\3\2\2\2U\u01f1")
        buf.write("\3\2\2\2W\u01f3\3\2\2\2Y\u01f5\3\2\2\2[\u01fc\3\2\2\2")
        buf.write("]\u01fe\3\2\2\2_\u0200\3\2\2\2a\u0202\3\2\2\2c\u0204\3")
        buf.write("\2\2\2e\u0206\3\2\2\2g\u0208\3\2\2\2i\u020a\3\2\2\2k\u020c")
        buf.write("\3\2\2\2m\u020e\3\2\2\2o\u0210\3\2\2\2q\u0212\3\2\2\2")
        buf.write("s\u0214\3\2\2\2u\u0216\3\2\2\2w\u0218\3\2\2\2y\u021a\3")
        buf.write("\2\2\2{\u021c\3\2\2\2}\u021e\3\2\2\2\177\u0220\3\2\2\2")
        buf.write("\u0081\u0222\3\2\2\2\u0083\u0224\3\2\2\2\u0085\u0226\3")
        buf.write("\2\2\2\u0087\u0228\3\2\2\2\u0089\u022a\3\2\2\2\u008b\u022c")
        buf.write("\3\2\2\2\u008d\u022e\3\2\2\2\u008f\u0230\3\2\2\2\u0091")
        buf.write("\u0232\3\2\2\2\u0093\u0256\3\2\2\2\u0095\u0262\3\2\2\2")
        buf.write("\u0097\u0264\3\2\2\2\u0099\u0268\3\2\2\2\u009b\u026a\3")
        buf.write("\2\2\2\u009d\u0273\3\2\2\2\u009f\u0276\3\2\2\2\u00a1\u0279")
        buf.write("\3\2\2\2\u00a3\u027c\3\2\2\2\u00a5\u027f\3\2\2\2\u00a7")
        buf.write("\u0282\3\2\2\2\u00a9\u0285\3\2\2\2\u00ab\u028c\3\2\2\2")
        buf.write("\u00ad\u028e\3\2\2\2\u00af\u0291\3\2\2\2\u00b1\u0293\3")
        buf.write("\2\2\2\u00b3\u029a\3\2\2\2\u00b5\u029c\3\2\2\2\u00b7\u029f")
        buf.write("\3\2\2\2\u00b9\u02a1\3\2\2\2\u00bb\u02a4\3\2\2\2\u00bd")
        buf.write("\u02a6\3\2\2\2\u00bf\u02a9\3\2\2\2\u00c1\u02b1\3\2\2\2")
        buf.write("\u00c3\u02b3\3\2\2\2\u00c5\u02b6\3\2\2\2\u00c7\u02bd\3")
        buf.write("\2\2\2\u00c9\u02bf\3\2\2\2\u00cb\u02c3\3\2\2\2\u00cd\u02c7")
        buf.write("\3\2\2\2\u00cf\u02cd\3\2\2\2\u00d1\u02cf\3\2\2\2\u00d3")
        buf.write("\u02d4\3\2\2\2\u00d5\u02d6\3\2\2\2\u00d7\u02d8\3\2\2\2")
        buf.write("\u00d9\u02de\3\2\2\2\u00db\u02e2\3\2\2\2\u00dd\u02e4\3")
        buf.write("\2\2\2\u00df\u02e6\3\2\2\2\u00e1\u02e9\3\2\2\2\u00e3\u02eb")
        buf.write("\3\2\2\2\u00e5\u02ed\3\2\2\2\u00e7\u02ef\3\2\2\2\u00e9")
        buf.write("\u02f1\3\2\2\2\u00eb\u02f4\3\2\2\2\u00ed\u02f7\3\2\2\2")
        buf.write("\u00ef\u02f9\3\2\2\2\u00f1\u02fb\3\2\2\2\u00f3\u02fd\3")
        buf.write("\2\2\2\u00f5\u02ff\3\2\2\2\u00f7\u0303\3\2\2\2\u00f9\u00fb")
        buf.write("\t\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u00ff\b\2\2\2\u00ff\4\3\2\2\2\u0100\u0102\5\t\5")
        buf.write("\2\u0101\u0103\5\3\2\2\u0102\u0101\3\2\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103\u0109\3\2\2\2\u0104\u0106\7\17\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u010a\7\f\2\2\u0108\u010a\7\17\2\2\u0109\u0105")
        buf.write("\3\2\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010c\b\3\2\2\u010c\6\3\2\2\2\u010d\u010e\6\4\2\2\u010e")
        buf.write("\u011a\5\3\2\2\u010f\u0111\7\17\2\2\u0110\u010f\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0115")
        buf.write("\7\f\2\2\u0113\u0115\4\16\17\2\u0114\u0110\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0118\5\3\2\2")
        buf.write("\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a\3")
        buf.write("\2\2\2\u0119\u010d\3\2\2\2\u0119\u0114\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011c\b\4\3\2\u011c\b\3\2\2\2\u011d\u011e")
        buf.write("\7^\2\2\u011e\n\3\2\2\2\u011f\u0120\7=\2\2\u0120\f\3\2")
        buf.write("\2\2\u0121\u0122\7k\2\2\u0122\u0123\7o\2\2\u0123\u0124")
        buf.write("\7r\2\2\u0124\u0125\7q\2\2\u0125\u0126\7t\2\2\u0126\u0127")
        buf.write("\7v\2\2\u0127\16\3\2\2\2\u0128\u0129\7r\2\2\u0129\u012a")
        buf.write("\7c\2\2\u012a\u012b\7e\2\2\u012b\u012c\7m\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7i\2\2\u012e\u012f\7g\2\2\u012f\20")
        buf.write("\3\2\2\2\u0130\u0131\7y\2\2\u0131\u0132\7k\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7j\2\2\u0134\22\3\2\2\2\u0135\u0136")
        buf.write("\7c\2\2\u0136\u0137\7u\2\2\u0137\24\3\2\2\2\u0138\u0139")
        buf.write("\7.\2\2\u0139\26\3\2\2\2\u013a\u013b\7,\2\2\u013b\30\3")
        buf.write("\2\2\2\u013c\u013d\7k\2\2\u013d\u013e\7h\2\2\u013e\32")
        buf.write("\3\2\2\2\u013f\u0140\7g\2\2\u0140\u0141\7n\2\2\u0141\u0142")
        buf.write("\7u\2\2\u0142\u0143\7g\2\2\u0143\34\3\2\2\2\u0144\u0145")
        buf.write("\7h\2\2\u0145\u0146\7q\2\2\u0146\u0147\7t\2\2\u0147\36")
        buf.write("\3\2\2\2\u0148\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a ")
        buf.write("\3\2\2\2\u014b\u014c\7?\2\2\u014c\u014d\7@\2\2\u014d\"")
        buf.write("\3\2\2\2\u014e\u014f\7<\2\2\u014f$\3\2\2\2\u0150\u0151")
        buf.write("\7?\2\2\u0151&\3\2\2\2\u0152\u0153\7t\2\2\u0153\u0154")
        buf.write("\7g\2\2\u0154\u0155\7v\2\2\u0155\u0156\7w\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157\u0158\7p\2\2\u0158(\3\2\2\2\u0159\u015b")
        buf.write("\5\63\32\2\u015a\u015c\5;\36\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015d\u015b\3\2\2\2")
        buf.write("\u015e\u015f\3\2\2\2\u015f\u0160\5\63\32\2\u0160*\3\2")
        buf.write("\2\2\u0161\u0163\5\67\34\2\u0162\u0164\5=\37\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\5\67\34")
        buf.write("\2\u0168,\3\2\2\2\u0169\u016b\5\65\33\2\u016a\u016c\13")
        buf.write("\2\2\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write("\u0170\5\65\33\2\u0170.\3\2\2\2\u0171\u0173\59\35\2\u0172")
        buf.write("\u0174\n\3\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\3")
        buf.write("\2\2\2\u0177\u0178\59\35\2\u0178\60\3\2\2\2\u0179\u017a")
        buf.write("\5\63\32\2\u017a\u017b\5\63\32\2\u017b\u0186\3\2\2\2\u017c")
        buf.write("\u017d\5\65\33\2\u017d\u017e\5\65\33\2\u017e\u0186\3\2")
        buf.write("\2\2\u017f\u0180\5\67\34\2\u0180\u0181\5\67\34\2\u0181")
        buf.write("\u0186\3\2\2\2\u0182\u0183\59\35\2\u0183\u0184\59\35\2")
        buf.write("\u0184\u0186\3\2\2\2\u0185\u0179\3\2\2\2\u0185\u017c\3")
        buf.write("\2\2\2\u0185\u017f\3\2\2\2\u0185\u0182\3\2\2\2\u0186\62")
        buf.write("\3\2\2\2\u0187\u0188\7$\2\2\u0188\u0189\7$\2\2\u0189\u018a")
        buf.write("\7$\2\2\u018a\64\3\2\2\2\u018b\u018c\7)\2\2\u018c\u018d")
        buf.write("\7)\2\2\u018d\u018e\7)\2\2\u018e\66\3\2\2\2\u018f\u0190")
        buf.write("\7$\2\2\u01908\3\2\2\2\u0191\u0192\7)\2\2\u0192:\3\2\2")
        buf.write("\2\u0193\u0194\5\t\5\2\u0194\u0195\n\4\2\2\u0195\u0198")
        buf.write("\3\2\2\2\u0196\u0198\n\5\2\2\u0197\u0193\3\2\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198<\3\2\2\2\u0199\u019a\5\t\5\2\u019a")
        buf.write("\u019b\n\4\2\2\u019b\u019e\3\2\2\2\u019c\u019e\n\6\2\2")
        buf.write("\u019d\u0199\3\2\2\2\u019d\u019c\3\2\2\2\u019e>\3\2\2")
        buf.write("\2\u019f\u01a0\5I%\2\u01a0\u01a1\5[.\2\u01a1\u01a2\5S")
        buf.write("*\2\u01a2@\3\2\2\2\u01a3\u01a4\5I%\2\u01a4\u01a5\5[.\2")
        buf.write("\u01a5\u01ad\3\2\2\2\u01a6\u01a8\5[.\2\u01a7\u01a9\5S")
        buf.write("*\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac")
        buf.write("\u01a3\3\2\2\2\u01ac\u01a6\3\2\2\2\u01adB\3\2\2\2\u01ae")
        buf.write("\u01af\5W,\2\u01af\u01b4\5a\61\2\u01b0\u01b2\5]/\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b5\5O(\2\u01b4\u01b1\3\2\2\2\u01b5\u01b6\3\2")
        buf.write("\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7D\3")
        buf.write("\2\2\2\u01b8\u01b9\5W,\2\u01b9\u01be\5{>\2\u01ba\u01bc")
        buf.write("\5]/\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01bf\5Q)\2\u01be\u01bb\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("F\3\2\2\2\u01c2\u01c3\5W,\2\u01c3\u01c8\5\u008dG\2\u01c4")
        buf.write("\u01c6\5]/\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c9\5U+\2\u01c8\u01c5\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01cbH\3\2\2\2\u01cc\u01ce\5W,\2\u01cd\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3")
        buf.write("\2\2\2\u01d0\u01dc\3\2\2\2\u01d1\u01d8\t\7\2\2\u01d2\u01d4")
        buf.write("\5]/\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d7\5S*\2\u01d6\u01d3\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01cd\3\2\2\2")
        buf.write("\u01db\u01d1\3\2\2\2\u01dcJ\3\2\2\2\u01dd\u01de\7,\2\2")
        buf.write("\u01de\u01df\7`\2\2\u01dfL\3\2\2\2\u01e0\u01e1\7\61\2")
        buf.write("\2\u01e1\u01e2\7`\2\2\u01e2N\3\2\2\2\u01e3\u01e6\5W,\2")
        buf.write("\u01e4\u01e6\t\b\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3")
        buf.write("\2\2\2\u01e6P\3\2\2\2\u01e7\u01ea\5W,\2\u01e8\u01ea\t")
        buf.write("\t\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eaR")
        buf.write("\3\2\2\2\u01eb\u01ee\5W,\2\u01ec\u01ee\t\7\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ec\3\2\2\2\u01eeT\3\2\2\2\u01ef\u01f2")
        buf.write("\5W,\2\u01f0\u01f2\t\n\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0")
        buf.write("\3\2\2\2\u01f2V\3\2\2\2\u01f3\u01f4\t\13\2\2\u01f4X\3")
        buf.write("\2\2\2\u01f5\u01f9\5\u0095K\2\u01f6\u01f8\5\u0099M\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01faZ\3\2\2\2\u01fb\u01f9\3\2\2")
        buf.write("\2\u01fc\u01fd\7\60\2\2\u01fd\\\3\2\2\2\u01fe\u01ff\7")
        buf.write("a\2\2\u01ff^\3\2\2\2\u0200\u0201\t\f\2\2\u0201`\3\2\2")
        buf.write("\2\u0202\u0203\t\r\2\2\u0203b\3\2\2\2\u0204\u0205\t\16")
        buf.write("\2\2\u0205d\3\2\2\2\u0206\u0207\t\17\2\2\u0207f\3\2\2")
        buf.write("\2\u0208\u0209\t\20\2\2\u0209h\3\2\2\2\u020a\u020b\t\21")
        buf.write("\2\2\u020bj\3\2\2\2\u020c\u020d\t\22\2\2\u020dl\3\2\2")
        buf.write("\2\u020e\u020f\t\23\2\2\u020fn\3\2\2\2\u0210\u0211\t\24")
        buf.write("\2\2\u0211p\3\2\2\2\u0212\u0213\t\25\2\2\u0213r\3\2\2")
        buf.write("\2\u0214\u0215\t\26\2\2\u0215t\3\2\2\2\u0216\u0217\t\27")
        buf.write("\2\2\u0217v\3\2\2\2\u0218\u0219\t\30\2\2\u0219x\3\2\2")
        buf.write("\2\u021a\u021b\t\31\2\2\u021bz\3\2\2\2\u021c\u021d\t\32")
        buf.write("\2\2\u021d|\3\2\2\2\u021e\u021f\t\33\2\2\u021f~\3\2\2")
        buf.write("\2\u0220\u0221\t\34\2\2\u0221\u0080\3\2\2\2\u0222\u0223")
        buf.write("\t\35\2\2\u0223\u0082\3\2\2\2\u0224\u0225\t\36\2\2\u0225")
        buf.write("\u0084\3\2\2\2\u0226\u0227\t\37\2\2\u0227\u0086\3\2\2")
        buf.write("\2\u0228\u0229\t \2\2\u0229\u0088\3\2\2\2\u022a\u022b")
        buf.write("\t!\2\2\u022b\u008a\3\2\2\2\u022c\u022d\t\"\2\2\u022d")
        buf.write("\u008c\3\2\2\2\u022e\u022f\t#\2\2\u022f\u008e\3\2\2\2")
        buf.write("\u0230\u0231\t$\2\2\u0231\u0090\3\2\2\2\u0232\u0233\t")
        buf.write("%\2\2\u0233\u0092\3\2\2\2\u0234\u023c\5_\60\2\u0235\u023c")
        buf.write("\5a\61\2\u0236\u023c\5c\62\2\u0237\u023c\5e\63\2\u0238")
        buf.write("\u023c\5g\64\2\u0239\u023c\5i\65\2\u023a\u023c\5k\66\2")
        buf.write("\u023b\u0234\3\2\2\2\u023b\u0235\3\2\2\2\u023b\u0236\3")
        buf.write("\2\2\2\u023b\u0237\3\2\2\2\u023b\u0238\3\2\2\2\u023b\u0239")
        buf.write("\3\2\2\2\u023b\u023a\3\2\2\2\u023c\u0257\3\2\2\2\u023d")
        buf.write("\u0245\5m\67\2\u023e\u0245\5o8\2\u023f\u0245\5q9\2\u0240")
        buf.write("\u0245\5s:\2\u0241\u0245\5u;\2\u0242\u0245\5w<\2\u0243")
        buf.write("\u0245\5y=\2\u0244\u023d\3\2\2\2\u0244\u023e\3\2\2\2\u0244")
        buf.write("\u023f\3\2\2\2\u0244\u0240\3\2\2\2\u0244\u0241\3\2\2\2")
        buf.write("\u0244\u0242\3\2\2\2\u0244\u0243\3\2\2\2\u0245\u0257\3")
        buf.write("\2\2\2\u0246\u024d\5{>\2\u0247\u024d\5}?\2\u0248\u024d")
        buf.write("\5\177@\2\u0249\u024d\5\u0081A\2\u024a\u024d\5\u0083B")
        buf.write("\2\u024b\u024d\5\u0085C\2\u024c\u0246\3\2\2\2\u024c\u0247")
        buf.write("\3\2\2\2\u024c\u0248\3\2\2\2\u024c\u0249\3\2\2\2\u024c")
        buf.write("\u024a\3\2\2\2\u024c\u024b\3\2\2\2\u024d\u0257\3\2\2\2")
        buf.write("\u024e\u0255\5\u0087D\2\u024f\u0255\5\u0089E\2\u0250\u0255")
        buf.write("\5\u008bF\2\u0251\u0255\5\u008dG\2\u0252\u0255\5\u008f")
        buf.write("H\2\u0253\u0255\5\u0091I\2\u0254\u024e\3\2\2\2\u0254\u024f")
        buf.write("\3\2\2\2\u0254\u0250\3\2\2\2\u0254\u0251\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0254\u0253\3\2\2\2\u0255\u0257\3\2\2\2")
        buf.write("\u0256\u023b\3\2\2\2\u0256\u0244\3\2\2\2\u0256\u024c\3")
        buf.write("\2\2\2\u0256\u0254\3\2\2\2\u0257\u0094\3\2\2\2\u0258\u025b")
        buf.write("\5]/\2\u0259\u025b\5\u0093J\2\u025a\u0258\3\2\2\2\u025a")
        buf.write("\u0259\3\2\2\2\u025b\u0263\3\2\2\2\u025c\u0260\5\u00e3")
        buf.write("r\2\u025d\u0260\5\u00e5s\2\u025e\u0260\5\u00e7t\2\u025f")
        buf.write("\u025c\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u025e\3\2\2\2")
        buf.write("\u0260\u0263\3\2\2\2\u0261\u0263\t(\2\2\u0262\u025a\3")
        buf.write("\2\2\2\u0262\u025f\3\2\2\2\u0262\u0261\3\2\2\2\u0263\u0096")
        buf.write("\3\2\2\2\u0264\u0265\t)\2\2\u0265\u0098\3\2\2\2\u0266")
        buf.write("\u0269\5\u0095K\2\u0267\u0269\5S*\2\u0268\u0266\3\2\2")
        buf.write("\2\u0268\u0267\3\2\2\2\u0269\u009a\3\2\2\2\u026a\u026e")
        buf.write("\7%\2\2\u026b\u026d\n&\2\2\u026c\u026b\3\2\2\2\u026d\u0270")
        buf.write("\3\2\2\2\u026e\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f")
        buf.write("\u0271\3\2\2\2\u0270\u026e\3\2\2\2\u0271\u0272\bN\4\2")
        buf.write("\u0272\u009c\3\2\2\2\u0273\u0274\7*\2\2\u0274\u0275\b")
        buf.write("O\5\2\u0275\u009e\3\2\2\2\u0276\u0277\7+\2\2\u0277\u0278")
        buf.write("\bP\6\2\u0278\u00a0\3\2\2\2\u0279\u027a\7]\2\2\u027a\u027b")
        buf.write("\bQ\7\2\u027b\u00a2\3\2\2\2\u027c\u027d\7_\2\2\u027d\u027e")
        buf.write("\bR\b\2\u027e\u00a4\3\2\2\2\u027f\u0280\7}\2\2\u0280\u0281")
        buf.write("\bS\t\2\u0281\u00a6\3\2\2\2\u0282\u0283\7\177\2\2\u0283")
        buf.write("\u0284\bT\n\2\u0284\u00a8\3\2\2\2\u0285\u0286\7>\2\2\u0286")
        buf.write("\u0287\7>\2\2\u0287\u0288\7>\2\2\u0288\u00aa\3\2\2\2\u0289")
        buf.write("\u028a\7>\2\2\u028a\u028d\7>\2\2\u028b\u028d\7\u226c\2")
        buf.write("\2\u028c\u0289\3\2\2\2\u028c\u028b\3\2\2\2\u028d\u00ac")
        buf.write("\3\2\2\2\u028e\u028f\7>\2\2\u028f\u0290\7?\2\2\u0290\u00ae")
        buf.write("\3\2\2\2\u0291\u0292\7>\2\2\u0292\u00b0\3\2\2\2\u0293")
        buf.write("\u0294\7@\2\2\u0294\u0295\7@\2\2\u0295\u0296\7@\2\2\u0296")
        buf.write("\u00b2\3\2\2\2\u0297\u0298\7@\2\2\u0298\u029b\7@\2\2\u0299")
        buf.write("\u029b\7\u226d\2\2\u029a\u0297\3\2\2\2\u029a\u0299\3\2")
        buf.write("\2\2\u029b\u00b4\3\2\2\2\u029c\u029d\7@\2\2\u029d\u029e")
        buf.write("\7?\2\2\u029e\u00b6\3\2\2\2\u029f\u02a0\7@\2\2\u02a0\u00b8")
        buf.write("\3\2\2\2\u02a1\u02a2\7-\2\2\u02a2\u02a3\7-\2\2\u02a3\u00ba")
        buf.write("\3\2\2\2\u02a4\u02a5\7-\2\2\u02a5\u00bc\3\2\2\2\u02a6")
        buf.write("\u02a7\7/\2\2\u02a7\u02a8\7/\2\2\u02a8\u00be\3\2\2\2\u02a9")
        buf.write("\u02aa\7/\2\2\u02aa\u00c0\3\2\2\2\u02ab\u02ac\7v\2\2\u02ac")
        buf.write("\u02ad\7k\2\2\u02ad\u02ae\7o\2\2\u02ae\u02af\7g\2\2\u02af")
        buf.write("\u02b2\7u\2\2\u02b0\u02b2\7\u22c7\2\2\u02b1\u02ab\3\2")
        buf.write("\2\2\u02b1\u02b0\3\2\2\2\u02b2\u00c2\3\2\2\2\u02b3\u02b4")
        buf.write("\7\61\2\2\u02b4\u02b5\7\61\2\2\u02b5\u00c4\3\2\2\2\u02b6")
        buf.write("\u02b7\7f\2\2\u02b7\u02b8\7k\2\2\u02b8\u02b9\7x\2\2\u02b9")
        buf.write("\u02ba\7k\2\2\u02ba\u02bb\7f\2\2\u02bb\u02bc\7g\2\2\u02bc")
        buf.write("\u00c6\3\2\2\2\u02bd\u02be\7\'\2\2\u02be\u00c8\3\2\2\2")
        buf.write("\u02bf\u02c0\7?\2\2\u02c0\u02c1\7?\2\2\u02c1\u02c2\7?")
        buf.write("\2\2\u02c2\u00ca\3\2\2\2\u02c3\u02c4\7?\2\2\u02c4\u02c5")
        buf.write("\7#\2\2\u02c5\u02c6\7?\2\2\u02c6\u00cc\3\2\2\2\u02c7\u02c8")
        buf.write("\7?\2\2\u02c8\u02c9\7?\2\2\u02c9\u00ce\3\2\2\2\u02ca\u02cb")
        buf.write("\7~\2\2\u02cb\u02ce\7~\2\2\u02cc\u02ce\7\u2229\2\2\u02cd")
        buf.write("\u02ca\3\2\2\2\u02cd\u02cc\3\2\2\2\u02ce\u00d0\3\2\2\2")
        buf.write("\u02cf\u02d0\7~\2\2\u02d0\u00d2\3\2\2\2\u02d1\u02d2\7")
        buf.write("(\2\2\u02d2\u02d5\7(\2\2\u02d3\u02d5\7\u222a\2\2\u02d4")
        buf.write("\u02d1\3\2\2\2\u02d4\u02d3\3\2\2\2\u02d5\u00d4\3\2\2\2")
        buf.write("\u02d6\u02d7\7(\2\2\u02d7\u00d6\3\2\2\2\u02d8\u02d9\7")
        buf.write("#\2\2\u02d9\u02da\7#\2\2\u02da\u00d8\3\2\2\2\u02db\u02dc")
        buf.write("\7#\2\2\u02dc\u02df\7?\2\2\u02dd\u02df\7\u2262\2\2\u02de")
        buf.write("\u02db\3\2\2\2\u02de\u02dd\3\2\2\2\u02df\u00da\3\2\2\2")
        buf.write("\u02e0\u02e3\5\u00d7l\2\u02e1\u02e3\7\u00ae\2\2\u02e2")
        buf.write("\u02e0\3\2\2\2\u02e2\u02e1\3\2\2\2\u02e3\u00dc\3\2\2\2")
        buf.write("\u02e4\u02e5\t\'\2\2\u02e5\u00de\3\2\2\2\u02e6\u02e7\7")
        buf.write("<\2\2\u02e7\u02e8\7A\2\2\u02e8\u00e0\3\2\2\2\u02e9\u02ea")
        buf.write("\7B\2\2\u02ea\u00e2\3\2\2\2\u02eb\u02ec\7&\2\2\u02ec\u00e4")
        buf.write("\3\2\2\2\u02ed\u02ee\7\u62e4\2\2\u02ee\u00e6\3\2\2\2\u02ef")
        buf.write("\u02f0\7\u697e\2\2\u02f0\u00e8\3\2\2\2\u02f1\u02f2\7\u0080")
        buf.write("\2\2\u02f2\u02f3\7\u0080\2\2\u02f3\u00ea\3\2\2\2\u02f4")
        buf.write("\u02f5\7\u0080\2\2\u02f5\u02f6\7?\2\2\u02f6\u00ec\3\2")
        buf.write("\2\2\u02f7\u02f8\7\u0080\2\2\u02f8\u00ee\3\2\2\2\u02f9")
        buf.write("\u02fa\7b\2\2\u02fa\u00f0\3\2\2\2\u02fb\u02fc\7\u00b6")
        buf.write("\2\2\u02fc\u00f2\3\2\2\2\u02fd\u02fe\7)\2\2\u02fe\u00f4")
        buf.write("\3\2\2\2\u02ff\u0300\7\60\2\2\u0300\u0301\7\60\2\2\u0301")
        buf.write("\u0302\7\60\2\2\u0302\u00f6\3\2\2\2\u0303\u0304\7\u2161")
        buf.write("\2\2\u0304\u00f8\3\2\2\2\64\2\u00fc\u0102\u0105\u0109")
        buf.write("\u0110\u0114\u0117\u0119\u015d\u0165\u016d\u0175\u0185")
        buf.write("\u0197\u019d\u01aa\u01ac\u01b1\u01b6\u01bb\u01c0\u01c5")
        buf.write("\u01ca\u01cf\u01d3\u01d8\u01db\u01e5\u01e9\u01ed\u01f1")
        buf.write("\u01f9\u023b\u0244\u024c\u0254\u0256\u025a\u025f\u0262")
        buf.write("\u0268\u026e\u028c\u029a\u02b1\u02cd\u02d4\u02de\u02e2")
        buf.write("\13\b\2\2\3\4\2\2\3\2\3O\3\3P\4\3Q\5\3R\6\3S\7\3T\b")
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
    Read = 43
    LeftShift = 44
    LessEqual = 45
    Less = 46
    Write = 47
    RightShift = 48
    GraterEqual = 49
    Grater = 50
    Increase = 51
    Plus = 52
    Decrease = 53
    Minus = 54
    Times = 55
    Quotient = 56
    Divide = 57
    Modulo = 58
    Equivalent = 59
    NotEquivalent = 60
    Equal = 61
    LogicOr = 62
    BitOr = 63
    LogicAnd = 64
    BitAnd = 65
    DoubleBang = 66
    NotEqual = 67
    LogicNot = 68
    BitNot = 69
    Elvis = 70
    Annotation = 71
    Dollar = 72
    Pound = 73
    Yuan = 74
    Concat = 75
    Destruct = 76
    Tilde = 77
    Quote = 78
    Acute = 79
    Quotation = 80
    Ellipsis = 81
    Reciprocal = 82

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "';'", "'import'", "'package'", "'with'", "'as'", "','", 
            "'*'", "'if'", "'else'", "'for'", "'in'", "'=>'", "':'", "'='", 
            "'return'", "'*^'", "'/^'", "'.'", "'_'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'<<<'", "'<='", "'<'", "'>>>'", "'>='", 
            "'>'", "'++'", "'+'", "'--'", "'-'", "'//'", "'divide'", "'%'", 
            "'==='", "'=!='", "'=='", "'|'", "'&'", "'!!'", "':?'", "'@'", 
            "'$'", "'\u62E2'", "'\u697C'", "'~~'", "'~='", "'~'", "'`'", 
            "'\u00B4'", "'''", "'...'", "'\u215F'" ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "JoinLine", "NEWLINE", "Escape", "Semicolon", "Import", 
            "Package", "With", "As", "Comma", "Star", "If", "Else", "For", 
            "In", "To", "Colon", "Set", "Return", "StringEscapeBlock", "StringEscapeSingle", 
            "StringLiteralBlock", "StringLiteralSingle", "StringEmpty", 
            "Decimal", "DecimalBad", "Binary", "Octal", "Hexadecimal", "Integer", 
            "Exponent", "Base", "Identifier", "Dot", "Underline", "LineComment", 
            "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
            "CLOSE_BRACE", "Read", "LeftShift", "LessEqual", "Less", "Write", 
            "RightShift", "GraterEqual", "Grater", "Increase", "Plus", "Decrease", 
            "Minus", "Times", "Quotient", "Divide", "Modulo", "Equivalent", 
            "NotEquivalent", "Equal", "LogicOr", "BitOr", "LogicAnd", "BitAnd", 
            "DoubleBang", "NotEqual", "LogicNot", "BitNot", "Elvis", "Annotation", 
            "Dollar", "Pound", "Yuan", "Concat", "Destruct", "Tilde", "Quote", 
            "Acute", "Quotation", "Ellipsis", "Reciprocal" ]

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
                  "Read", "LeftShift", "LessEqual", "Less", "Write", "RightShift", 
                  "GraterEqual", "Grater", "Increase", "Plus", "Decrease", 
                  "Minus", "Times", "Quotient", "Divide", "Modulo", "Equivalent", 
                  "NotEquivalent", "Equal", "LogicOr", "BitOr", "LogicAnd", 
                  "BitAnd", "DoubleBang", "NotEqual", "LogicNot", "BitNot", 
                  "Elvis", "Annotation", "Dollar", "Pound", "Yuan", "Concat", 
                  "Destruct", "Tilde", "Quote", "Acute", "Quotation", "Ellipsis", 
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
         


