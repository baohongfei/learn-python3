#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s=(x*x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        a,b = b,a+b
        n = n+1
    return 'done'

f = fib(10)
print('fib(10):',f)
for x in f:
    print(x)

# call generator manually:
g= fib(5)
while 1:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
