# 程序设计训练Python
## Week1
1. 输入
详见https://blog.csdn.net/qq_56177238/article/details/128261959
使用input()函数
如果一行只有一个数，直接使用`input()`，如`a=input()`；
若有一行数，中间使用空格隔开，需要逐个读入，可以使用`input().split()`，如`a,b,c=list(input().split())`；
若有几行数，可以读入一个数组，如
```
arr=[]
for i in range(n):
    arr.append(int(input()))
```
注：`input()`默认输入的数据类型为字符串str，需要进一步转换。
1. Numeric Types - int, float, complex
`==`: equal
`is`: object identity
`complex(re, im)`: 复数
`c.conjugate()`: 复数c的共轭
1. Sequence Types - list, tuple, range
可以使用`list.append(num)`来添加数字，可以直接用`+`在后面添加list，如
```
>>>squares=[1,4,9,16,25]
>>>squares+[36,49,64]
[1,4,9,16,25,36,49,64]
```
可以直接用切片来改变list中的数据，如
```
>>>letters=['a','b','c','d','e','f']
>>>letters[2:5]=['C','D','E']
>>>letters
['a','b','C','D','E','f']
```
`len(list)`: 求list长度
`list.index(num)`: 求num的index
`max(list)`, `min(list)`: 求一个list中的最大/最小值
`list.count(num)`: 计算num在list中出现次数
`sorted(list)`: 按照字典顺序排列
1. Set Types - set
`set()`: 将一个字符串分开，并**去重**，如
```
>>>a=set('abracadabra')
>>>b=set('alacazam')
>>>a
{'a','r','b','c','d'}
>>>a-b
{'r','d','b'}
```
1. Mapping Types - dict
```
d={i:arr.count(i) for i in arr}
```
`d.keys()`
`d.values()`
`list(d)`: 输出[keys的值]
`list(d.values())`: 输出[values的值]
`sorted(dict)`: 按照字典顺序排列
`key_list=list(filter(lambda k:d.get(k)==max(v),d.keys()))`: 知道value想得到key
1. Text Sequence Type - str
不能直接赋值改变某几个字母，可以使用`+`，如
```
>>>'J'+word[1:]
>>>word[:2]+'py'
```
1. Looping Techniques
dict中，可以使用`items()`同时获得key和value，如
```
knights={'gallahad':'the pure', 'robin':''the brave'}
for k,v in knights.items():
    print(k,v)
```
`enumerate`函数可以给list编号，如
```
for i,v in enumerate(['a','b','c'])
    print(i,v)
```
`zip`与`.format`:
```
Q=['name','quest','favorite color']
A=['lancelot','the holy grail','purple']
for q,a in zip(Q,A):
    print('What's your {0}? It is {1}.'.format(q,a))
```

## Week2
1. 多线程编程
* 串行编程：逐行运行
* 并行/并发编程：任务之间同时进行
并发编程：多任务同时推进，但是每一刻只做一件事
并行编程：某一时刻同时处理多个任务
* 进程process：一个程序的实例（一个独立的任务）
* 线程thread: 运算调度的单位。一个进程可以拥有多个线程
`multiprocessing.Process`类：用于表示一个进程对象。可以通过创建一个 Process 对象来启动一个新的进程。
`multiprocessing.Queue`类：多进程之间进行通信的一种方式。可以在进程之间传递数据，可以在父进程中创建一个 Queue 对象，并将它传递给子进程。
`multiprocessing.Pool`类：用于管理一组进程池。可以通过创建一个 Pool 对象来启动多个进程，将任务分配给进程池中的进程并等待任务完成。
进程锁：由于多进程之间会共享一些资源，为了保证数据的安全性，需要使用锁来实现互斥访问。
