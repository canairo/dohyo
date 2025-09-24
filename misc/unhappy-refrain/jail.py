from pickle import *
from io import BytesIO

allowed_ops = [TUPLE1, TUPLE2, REDUCE, UNICODE, POP, MARK, TUPLE]

class Unhappy(Unpickler):
    def find_class(self, module, name):
        if module != 'builtins':
            raise KeyError('unhappy!')
        return Unpickler.find_class(self, module, name)

def Refrain(s):
    for word in ('os', 'sys', 'system', 'sh', 'cat', 'import', 'open', 'file', 'globals'):
        if word.encode() in s:
            raise KeyError(f'refrain!')
    return Unhappy(BytesIO(s)).load()

def UnhappyRefrain():
    user_ops = input('time to cook > ').split(" ")
    pkl = b''
    for op in user_ops:
        try:
            if op in '0123456':
                pkl += allowed_ops[int(op)]
            elif pkl[-1] == 86: #opcode for UNICODE
                op = op.encode()
                for char in op:
                    # only lowercase unicode
                    if char not in b'01abcdefghijklmnopqrstuvwxyzT':
                        raise Exception("no non-lowercase chars!")
                op = op.replace(b'T', b'\n')
                pkl += op
        except Exception as e:
            print(op, e)

    pkl += STOP
    result = Refrain(pkl)

__builtins__.globals = None
__builtins__.license = None
__builtins__.exec = None
__builtins__.eval = None
__builtins__.open = None
__builtins__.compile = None
__builtins__.help = None
__builtins__.breakpoint = None

UnhappyRefrain()
