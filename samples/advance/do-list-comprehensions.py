#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2 == 0])
print([m+n for m in 'ABC' for n in 'XYZ'])

d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])

l = list(range(1,11))
print(l)

L = []
for x in range(1,11):
    L.append(x*x)
print(L)

print([d for d in os.listdir('.')])
