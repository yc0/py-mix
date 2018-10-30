"""
Given a contiguous sequence of numbers in which each number repeats thrice, 
there is exactly one missing number. Find the missing number.

eg: 11122333 : Missing number 2
11122233344455666 Missing number 5
"""
from collections import Counter
def main(a):
    d = Counter(a)
    susipicious, other = None,None
    _hash = {}
    for k,v in d.items():
        if v not in _hash:
            if susipicious is None:
                susipicious = v
                _hash[v] = [k]
                continue
            if other is None:
                other = v
                _hash[v] = [k]
        else:
            if other is not None:
                if len(_hash[susipicious]) > 1:
                    return _hash[other][0]
                if len(_hash[other]) > 1:
                    return _hash[susipicious][0]
            _hash[v] += [k]
    return susipicious if len(_hash[susipicious])==1 else other
        
def missing_number(num):
    dict ={}
    
    while num>0:
        rem = num%10
        
        if rem not in dict:
            dict[rem] = 1
        else:
            dict[rem] = dict.get(rem) + 1
        
        num = num//10
    print(dict)
    for key, val in dict.items():
        if val == 2:
            print (key)        

def missing_number_xor(nums):
    rst, occur = 0, set()
    for i in nums:
        rst ^= int(i)
        occur.add(int(i))
    for v in occur:  # make thrice -> four times, twice->thrice
                     # , and rst would leave only thrice number after xor operates
        rst ^= v
    return rst
if __name__ == '__main__':
    print(main("11122333"))
    print(main("11122233344455666"))
    missing_number(11122333)
    missing_number(11122233344455666)
    print(missing_number_xor("11122333"))
    print(missing_number_xor("11122233344455666"))
    