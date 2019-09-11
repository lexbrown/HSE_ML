a = 10
a
a = 'sasfgsdgsd'
del a
a
a = 10
if a == 10:
    b = 11
b
if a:
    b = 12
b
a = -1
if a:
    b = 123
b
if a:
    b = 10
if a:
    b = 10
else:
    b = 11
if a > 0:
    b = 1
elif a == 0:
    b = 2
else:
    b = 3
b
for a in range(10):
    print(a)
a = 0
while a < 5:
    a += 1
    print(a)
print(a, a, a, a ,a )
print(a, a, a, a ,a, sep=', ')
print(a, a, a, a ,a, sep=', ', end='!')
a = 10
type(a)
a = 10.5
type(a)
10 / 3
10 // 3
10 + j5
10 + 5j
type(10 + 5j)
a = [1, 2, 3, 4]
a
a = (1, 2, 3 4)
a = (1, 2, 3, 4)
a = [1, 2, 3, 4]
type(a)
a = (1, 2, 3, 4)
type(a)
b = (1, 2, 3, 4)
a = [1, 2, 3, 4]
a.append(5)
a
b.append(5)
range(10)
list(range(10))
'asdfasdfsa'
"asdfasfdf"
'''asdfasdfasfd
asdfasdf'''
"""asdfasddfsaf
asdfasf
asdfas"""
c = {1: 'asdfsafd', 2:3}
c
type(c)
None
True, False
a = 'hello world'
a.upper()
a.upper().lower()
a.startswith('h')
a.startswith('hello')
a.startswith('world')
a.replace('hello', 'goodbye')
a.strip('h')
a.strip('hd')
a.rstrip('hd')
a.lstrip('hd')
a.split(' ')
a.split(' ')
' '.join(['hello', 'world'])
a.encode('utf8')
b
print('my values:', b, '!')
print('my values:' + str(b) + '!')
'my values: {}!'.format(b)
'my values: {0} {0}!'.format(b)
'my values: {0} {1}!'.format(b, 'asdfsa')
'my values: {b} {c}!'.format(b=b, c='asdfsa')
f'my values {b}'
asd = 123
f'my values {asd}'
a = [1, 2, 3]
a.count
a.count()
a.pop()
a
a.remove(1)
a
a.sort()
[3, 2 ,1].sort()
a = [3, 2 ,1]
a.sort()
a
a[0]
a[1]
a[2]
a[3]
a[-1]
a[-2]
a[0:2]
a[0:-2]
a[:-2]
a[:]
a  = lis(range(6))
a  = list(range(6))
a
a[1:3]
a[1:5:1]
a[1:5:2]
a [::-1]
%save ~/tmp/session.py
%save ~/tmp/session.py 0-111
%save ~/Documents/session.py 0-111
%save /Users/mike0sv/Documents/ 0-111
clear
a = list(range(5))
a
it = iter(a)
type(it)
next(it)
next(it)
next(it)
next(it)
next(it)
next(it)
a = {1, 2, 3}
type(a)
it = iter(a)
type(it)
a[1]
for b  in a:
    print(b)
for b  in a:
    if a == 2:
        continue
    print(b)
a = [1, 2, 3 ,4]
for b  in a:
    if a == 2:
        continue
    print(b)
for b in a:
    if a > 2:
        continue
    print(b)
for b in a:
    if b == 2:
        continue
    print(b)
for b in a:
    if b == 2:
        continue
    if b > 3:
        break
    print(b)
a = {1: '1', 2:'2'}
type(a)
a[1]
a = {'1': 'a', '2':'b'}
a['1']
a['2']
a.keys()
a.values()
a.items()
a['3'] = 'c'
a
del a['3']
a
a['3']
a.get('3')
a.get('3', 'asdas')
a.get('2', 'asdas')
a.update({'3':'c', '4': 'd'})
a
a.update({'3':'c', '4': 'e'})
a
for e in a:
    e_val = a['e']
    print('Value of {} is {}'.format(e, e_val))
for e in a:
    e_val = a[e]
    print('Value of {} is {}'.format(e, e_val))
for e, e_val in a.items():
    print('Value of {} is {}'.format(e, e_val))
a.items()
a = [1, 2, 3]
b, c, d= a
b
c
d
a = set([1, 2, 3, 3])
a
a.difference({1})
a.intersection({2, 3, 4})
a.update([5, 4])
a
a = [x for x in range(50)]
a
a = [x for x in range(10)]
a
a = [x*2 for x in range(10)]
a
a = [x*2 for x in range(10) if x % 2]
a
a = [x*y for x in range(4) for y in range(4)]
a
a = [x*y for x in range(4) for y in range(4) if y % 3]
a
a = {x:x for x in range(5)}
a
a = {str(x): x**2 for x in range(5)}
a
def my_function(arg1, arg2):
    print(arg1 + arg2)
my_function(1, 2)
def my_function(arg1, arg2):
    print(arg1 + arg2)
    return arg1 + arg2
a = my_function(5, 6)
a
def my_function(arg1, arg2):
    print(arg1 + arg2)
    return
a = my_function(5, 6)
a
type(a)
a is None
def my_function(arg1, arg2):
    if arg1 == 1:
        return
    print(arg1 + arg2)
my_function(1, 2)
my_function(2, 2)
my_function(2, 3)
my_function(arg1=2, arg2=3)
my_function(arg2=2, arg1=3)
my_function(2, arg2=3)
my_function(2, arg1=3)
def my_function(arg1, arg2=5):
    if arg1 == 1:
        return
    print(arg1 + arg2)
my_function(1)
my_function(2)
my_function()
my_function(3, 6)
my_function(3, arg2=6)
def my_func(a1, a2, a3, a4):
    pass
def my_func(a1, a2, a3, a4):
    print(a1, a2, a3, a4)
s = [1, 2, 3 ,4]
my_func(*s)
s = [1, 2, 3]
d = {'4': 5}
my_func(*s)
d = {'a4': 5}
my_func(*s, **d)
def my_func(*args, **kwargs):
    print(args, kwargs)
my_func(12, 345, 65, a=213, b=314)
def my_func(a1: int, a2, a3, a4):
    print(a1, a2, a3, a4)
my_func('as', 1, 2, 3)
sum
help
help()
help(list)
list?
list??
my_func?
my_func??
max([1, 2 ])
a
a = [1, 2, 3]
repr(a)
print(a)
a = [True, False]
all(a)
any(a)
any()
a = [1, 2, 3]
all([x > 0 for x in a])
all(x > 0 for x in a)
len(a)
len({1, 2 ,3 ,3})
sorted([3,2,1])
a
a = list(reversed(a))
a
enumerate(a)
list(enumerate(a))
for index, value in enumerate(a):
    print('{} value of a is {}'.format(index, value))
a = {'a': 1, 'b': 2}
for index, (key, value) in enumerate(a.items()):
    print(index, key, value)
reversed(a)
a = [1, 2 ,3]
reversed(a)
list(reversed(a))
b = ['a', 'b', 'c']
zip(a,b )
list(zip(a,b ))
b = ['a', 'b', 'c', 'd']
list(zip(a,b ))
type('a')
isinstance('a', str)
isinstance('a', int)
isinstance('1', int)
def f(a):
    return a * 2
b = [3, 2,1]
map(b, f)
map(f, b)
list(map(f, b))
def f(a):
    return a % 2
filter(f, b)
list(filter(f, b))
[f(x) for x in a]
[x for x in a if f(x)]
[x for x in a if x % 2]
def fib(count):
    a, b = 1, 1
    for i in range(count):
        yield a
        a, b = a + b, a
fib(5)
g = fib(5)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
def asda():
    print('asdasd')
    yield
asda()
next(asda())
a = [1, 2]
def f(a, b):
    print(a ,b)
f(*a)
a = {'a': 3, 'b':4}
f(**a)
a = [1]
b = {'b': 2}
f(*a, **b)
def f(*arg):
    print(len(arg))
f(1, 2, 3)
f(1, 2, 3, 5, 6)
f(*[x for x in range(6)])
def f(**arg):
    print(len(arg))
f(a=1, b=2)
f(3, a=1, b=2)
f(**{1: 1})
f(**{'1': 1})
a = input()
a

In [12]: %history ~2/1-100
a = 10
a
a = 'sasfgsdgsd'
del a
a
a = 10
if a == 10:
    b = 11
b
if a:
    b = 12
b
a = -1
if a:
    b = 123
b
if a:
    b = 10
if a:
    b = 10
else:
    b = 11
if a > 0:
    b = 1
elif a == 0:
    b = 2
else:
    b = 3
b
for a in range(10):
    print(a)
a = 0
while a < 5:
    a += 1
    print(a)
print(a, a, a, a ,a )
print(a, a, a, a ,a, sep=', ')
print(a, a, a, a ,a, sep=', ', end='!')
a = 10
type(a)
a = 10.5
type(a)
10 / 3
10 // 3
10 + j5
10 + 5j
type(10 + 5j)
a = [1, 2, 3, 4]
a
a = (1, 2, 3 4)
a = (1, 2, 3, 4)
a = [1, 2, 3, 4]
type(a)
a = (1, 2, 3, 4)
type(a)
b = (1, 2, 3, 4)
a = [1, 2, 3, 4]
a.append(5)
a
b.append(5)
range(10)
list(range(10))
'asdfasdfsa'
"asdfasfdf"
'''asdfasdfasfd
asdfasdf'''
"""asdfasddfsaf
asdfasf
asdfas"""
c = {1: 'asdfsafd', 2:3}
c
type(c)
None
True, False
a = 'hello world'
a.upper()
a.upper().lower()
a.startswith('h')
a.startswith('hello')
a.startswith('world')
a.replace('hello', 'goodbye')
a.strip('h')
a.strip('hd')
a.rstrip('hd')
a.lstrip('hd')
a.split(' ')
a.split(' ')
' '.join(['hello', 'world'])
a.encode('utf8')
b
print('my values:', b, '!')
print('my values:' + str(b) + '!')
'my values: {}!'.format(b)
'my values: {0} {0}!'.format(b)
'my values: {0} {1}!'.format(b, 'asdfsa')
'my values: {b} {c}!'.format(b=b, c='asdfsa')
f'my values {b}'
asd = 123
f'my values {asd}'
a = [1, 2, 3]
a.count
a.count()
a.pop()
a
a.remove(1)
a
a.sort()
[3, 2 ,1].sort()
a = [3, 2 ,1]
a.sort()
a
a[0]
a[1]
a[2]
a[3]
a[-1]
a[-2]
a[0:2]

a[-2]
a[0:2]
a[0:-2]
a[:-2]
a[:]
a  = lis(range(6))
a  = list(range(6))
a
a[1:3]
a[1:5:1]
a[1:5:2]
a [::-1]
%save ~/tmp/session.py
%save ~/tmp/session.py 0-111
%save ~/Documents/session.py 0-111
%save /Users/mike0sv/Documents/ 0-111
clear
a = list(range(5))
a
it = iter(a)
type(it)
next(it)
next(it)
next(it)
next(it)
next(it)
next(it)
a = {1, 2, 3}
type(a)
it = iter(a)
type(it)
a[1]
for b  in a:
    print(b)
for b  in a:
    if a == 2:
        continue
    print(b)
a = [1, 2, 3 ,4]
for b  in a:
    if a == 2:
        continue
    print(b)
for b in a:
    if a > 2:
        continue
    print(b)
for b in a:
    if b == 2:
        continue
    print(b)
for b in a:
    if b == 2:
        continue
    if b > 3:
        break
    print(b)
a = {1: '1', 2:'2'}
type(a)
a[1]
a = {'1': 'a', '2':'b'}
a['1']
a['2']
a.keys()
a.values()
a.items()
a['3'] = 'c'
a
del a['3']
a
a['3']
a.get('3')
a.get('3', 'asdas')
a.get('2', 'asdas')
a.update({'3':'c', '4': 'd'})
a
a.update({'3':'c', '4': 'e'})
a
for e in a:
    e_val = a['e']
    print('Value of {} is {}'.format(e, e_val))
for e in a:
    e_val = a[e]
    print('Value of {} is {}'.format(e, e_val))
for e, e_val in a.items():
    print('Value of {} is {}'.format(e, e_val))
a.items()
a = [1, 2, 3]
b, c, d= a
b
c
d
a = set([1, 2, 3, 3])
a
a.difference({1})
a.intersection({2, 3, 4})
a.update([5, 4])
a
a = [x for x in range(50)]
a
a = [x for x in range(10)]
a
a = [x*2 for x in range(10)]
a
a = [x*2 for x in range(10) if x % 2]
a
a = [x*y for x in range(4) for y in range(4)]
a
a = [x*y for x in range(4) for y in range(4) if y % 3]
a
a = {x:x for x in range(5)}
a
a = {str(x): x**2 for x in range(5)}
a
def my_function(arg1, arg2):
    print(arg1 + arg2)
my_function(1, 2)
def my_function(arg1, arg2):
    print(arg1 + arg2)
    return arg1 + arg2
a = my_function(5, 6)
a
def my_function(arg1, arg2):
    print(arg1 + arg2)
    return
a = my_function(5, 6)
a
type(a)
a is None
def my_function(arg1, arg2):
    if arg1 == 1:
        return
    print(arg1 + arg2)
my_function(1, 2)
my_function(2, 2)
my_function(2, 3)
my_function(arg1=2, arg2=3)
my_function(arg2=2, arg1=3)
my_function(2, arg2=3)
my_function(2, arg1=3)
def my_function(arg1, arg2=5):
    if arg1 == 1:
        return
    print(arg1 + arg2)
my_function(1)
my_function(2)
my_function()
my_function(3, 6)
my_function(3, arg2=6)
def my_func(a1, a2, a3, a4):
    pass
def my_func(a1, a2, a3, a4):
    print(a1, a2, a3, a4)
s = [1, 2, 3 ,4]
my_func(*s)
s = [1, 2, 3]
d = {'4': 5}
my_func(*s)
d = {'a4': 5}
my_func(*s, **d)
def my_func(*args, **kwargs):
    print(args, kwargs)
my_func(12, 345, 65, a=213, b=314)
def my_func(a1: int, a2, a3, a4):
    print(a1, a2, a3, a4)
my_func('as', 1, 2, 3)
sum
help
help()
help(list)
list?
list??
my_func?
my_func??
max([1, 2 ])
a
a = [1, 2, 3]
repr(a)
print(a)
a = [True, False]
all(a)
any(a)
any()
a = [1, 2, 3]
all([x > 0 for x in a])
all(x > 0 for x in a)
len(a)
len({1, 2 ,3 ,3})
sorted([3,2,1])
a
a = list(reversed(a))
a
enumerate(a)
list(enumerate(a))
for index, value in enumerate(a):
    print('{} value of a is {}'.format(index, value))
a = {'a': 1, 'b': 2}
for index, (key, value) in enumerate(a.items()):
    print(index, key, value)
reversed(a)
a = [1, 2 ,3]
reversed(a)
list(reversed(a))
b = ['a', 'b', 'c']
zip(a,b )
list(zip(a,b ))
b = ['a', 'b', 'c', 'd']
list(zip(a,b ))
type('a')
isinstance('a', str)
isinstance('a', int)
isinstance('1', int)
def f(a):
    return a * 2
b = [3, 2,1]
map(b, f)
map(f, b)
list(map(f, b))
def f(a):
    return a % 2
filter(f, b)
list(filter(f, b))
[f(x) for x in a]
[x for x in a if f(x)]
[x for x in a if x % 2]
def fib(count):
    a, b = 1, 1
    for i in range(count):
        yield a
        a, b = a + b, a
fib(5)
g = fib(5)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
def asda():
    print('asdasd')
    yield
asda()
next(asda())
a = [1, 2]
def f(a, b):
    print(a ,b)
f(*a)
a = {'a': 3, 'b':4}
f(**a)
a = [1]
b = {'b': 2}
f(*a, **b)
def f(*arg):
    print(len(arg))
f(1, 2, 3)
f(1, 2, 3, 5, 6)
f(*[x for x in range(6)])
def f(**arg):
    print(len(arg))
f(a=1, b=2)
f(3, a=1, b=2)
f(**{1: 1})
f(**{'1': 1})
a = input()
a