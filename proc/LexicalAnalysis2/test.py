from lexer import Lexer

Pytokens = ["False",    "await",      "else",       "import",     "pass",
"None",       "break",      "except",     "in",         "raise",
"True",       "class",      "finally",    "is",         "return",
"and",        "continue",   "for",        "lambda",     "try",
"as",         "def",        "from",       "nonlocal",   "while",
"assert",     "del",        "global",     "not",        "with",
"async",     "elif",       "if",         "or",         "yield"
]

x = Lexer(Pytokens, "code.py")
tokens = x.lex_An()
print(tokens)
print(x.filterToClass(tokens))
