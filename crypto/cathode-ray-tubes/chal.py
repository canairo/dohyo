from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from os import urandom

flag = 'DOHYO{' + urandom(16).hex() + '}'
flag_bytes = bytes_to_long(flag.encode())
coeffs = [flag_bytes] + [getPrime(20*8) for i in range(250)]

def f(x):
    s = 0
    for power, coeff in enumerate(coeffs):
        s += coeff * x ** power
    return s

for i in range(1, 200):
    print(f'f({i}) = {f(i)}')
