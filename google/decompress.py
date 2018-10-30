"""
Given a compressed string in which a number followed by [] indicate how many times those characters occur, decompress the string
Eg. : a3[b2[c1[d]]]e will be decompressed as abcdcdbcdcdbcdcde.
Assume the string is well formed and number will always be followed by a [].
"""
import re
def decompress(_str):
    v,stack = 0, []
    for c in _str:
        if c.isdigit():
            v*=10
            v+=int(c)
        else:
            if v > 0 and c == "[":
                stack.append(v)
                stack.append(c)
                v = 0
            
            elif c == "]":
                i = -1
                while stack and stack[i] != "[":
                    i -= 1
                s = stack[i-1]*"".join(stack[i+1:])
                stack = stack[:i-1]
                stack.append(s)
            else:
                stack.append(c)

    return "".join(stack)

def decompress_recusive(s):
    if not s:
        return ""
    if s[0].isalpha():
        return s[0]+decompress_recusive(s[1:])
    i = 0 
    while s[i].isdigit():
        i += 1
    last = s.rfind("]")
    return int(s[:i])*decompress_recusive(s[i+1:last])+decompress_recusive(s[last+1:])
if __name__ == '__main__':
    assert decompress('a3[b2[c1[d]]]e') == "abcdcdbcdcdbcdcde"
    assert decompress_recusive('a3[b2[c1[d]]]e') == "abcdcdbcdcdbcdcde"
    print("passed all")