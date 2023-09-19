# cython: language_level=3

from lexer import filterToClass

cdef class metrics:

    cdef list ts
    
    def __init__(self, tokens):
        self.ts = tokens

    def depthOI(self, str className, int depth=0 ):
        if className == None:
            return depth
        else:
            classes = filterToClass(self.ts)
            for i in range(0, len(classes)-1):
                if classes[i] == className:
                    return self.depthOI(classes[i+1], depth = depth+1)
        