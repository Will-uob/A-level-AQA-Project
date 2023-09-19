# cython: language_level=3

class Lexer:

    def __init__(self, tokens, filepath):
        self.tokens = tokens
        self.filepath = filepath
    
    def isOperator(self, word):
        for i in range(0, 1):
            if word == self.tokens[i]:
                return True
            else:
                return False
    
    def isKeyword(self, word):
        for i in range(0, 1):
            if word == self.tokens[i]:
                return True
            else:
                return False

    def splitbrackets(self, word):
        """Use a stack to split the word and ensure stuffs"""
        word = list(word)
        buffer = []
        parts = [] 
        for letter in word:
            if letter == '(':
                pos = "".join(buffer)
                parts.append(pos)
                parts.append('(')
                buffer = []
            elif letter == ')':
                pos = "".join(buffer)
                parts.append(pos)
                parts.append(')')
                buffer = []
            else:
                buffer.append(letter)
        return parts

    def lex_An(self):
        tokenstream = []
        path = self.filepath
        with open(path, 'r') as file:
            for line in file:
                for word in line.split():
                    if word.find('(', 0) != -1:
                        pos = self.splitbrackets(word)
                        for i in range(0, len(pos)):
                            tokenstream.append(pos[i])
                    else:
                        tokenstream.append(word)
        return tokenstream

    def filterToClass(self, ts):
        classes = []
        for i in range(len(ts)):
            if ts[i] == "class":
                classes.append(ts[i+1])
                if ts[i+3] != "object":
                    classes.append(ts[i+3])
                elif ts[i+3] != "":
                    classes.append(ts[i+3])
                else:
                    classes.append("ni")
        return classes