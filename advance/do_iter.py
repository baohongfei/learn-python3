#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3


d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)

for ch in 'ABC':
    print(ch)

print('Iterable? [1,2,3]:',isinstance([1,2,3], Iterable))
print('Iterable? \'abc\':',isinstance('abc',Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
