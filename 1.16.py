```python
print(164) #1월 16일 수업
```

    164



```python
x = 10
y = 20

tmp = x
x = y
y = tmp

print(x,y)
```

    20 10



```python
age = 25

print(type(age))
```

    <class 'int'>



```python
age = 25.1

print(type(age))
```

    <class 'float'>



```python
name = "h"
name1 = "he"
name2 = 'heo'
#'' or "" 로 이루어진 1개 -> 문자 #2개 이상-> 문자열
#파이썬에서는 문자를 문자열로 본다 다른 언어는 문자(char)

print(type(name))
print(type(name1))
print(type(name2))
```

    <class 'str'>
    <class 'str'>
    <class 'str'>



```python
isTrue = True
isFalse = False

print(type(isTrue))
print(type(isFalse))

check

checked
#불리안 자료형일 때 변수 앞에 is 붙이기
```

    <class 'bool'>
    <class 'bool'>



```python
age = 25

print(id(age))
```

    2471910206512



```python
print(complex(3)) #complex 복소수
```

    (3+0j)



```python
print('hello \n world')
print('hello \t world')
```

    hello
    world
    hello	world



```python
age = 25
print(f'제 나이는 {age}살 입니다') #f-string 실무에 많이 사용
```

    제 나이는 25살 입니다



```python
test = None
print(test)
```

    None



```python
def func(): #나중에 자세히 배움
    print('hello wolrd')
    
print(func())
```

    hello wolrd
    None



```python
a = 1
b = 1
print(id(a))
print(id(b))

c = [1]
d = [1]

print(a is b)
print(c is d) #is 객체 아이덴티티, 메모리공간까지 같은지 확인
```

    2471910205744
    2471910205744
    True
    False



```python
a = 1
b = a
a = 2
print(b) #1

c = [1]
#print(id(c))
d = c
c.append(2)
#print(id(c))
print(d) #[1, 2]

e = [1]
f = e
f = [1,2]
print(e) #[1]
```

    1
    [1, 2]
    [1]



```python
a = 1
b = 2
c = 3

i = [1, 2, 3]
```


```python
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]

print(len(boxes)) #3
print(boxes[2]) #['apple', 'banana', 'cherry']
print(boxes[2][-1]) #cherry
print(boxes[-1][1][0]) #b
```

    3
    ['apple', 'banana', 'cherry']
    cherry
    b



```python
list_c = list(range(6))

print(list_c)
```

    [0, 1, 2, 3, 4, 5]



```python
list_c = [80, 90, 80]
```


```python

```


      Cell In[22], line 2
        d.append{'ko': 90}
                ^
    SyntaxError: invalid syntax

