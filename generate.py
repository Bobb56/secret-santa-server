from rsa import *
from random import *


def hex_of_byte(byte):
    s = hex(byte)[2:]
    return '0' * (2-len(s)) + s


def make_hex(bytesstring):
    ret = ""
    for i in bytesstring:
        ret += hex_of_byte(i)
    return ret



f = open("public_keys.txt", "r")
keys = eval(f.read())
f.close()

names = list(keys.keys())

shuffle(names)

names.append(names[0])  # the last person gives a gift to the first person


def make_message(index):
    bin_message = encrypt(names[index + 1].encode(), keys[names[index]])
    message = make_hex(bin_message)
    return names[index], message


results = []
for i in range(len(names) - 1):
    try:
        results.append(make_message(i))
    except:
        pass
    
shuffle(results)

f = open("result.txt", "w+")
f.write(str(dict(results)))
f.close()
