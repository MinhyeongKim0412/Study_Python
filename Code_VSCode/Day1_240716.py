print("hello world")    

#1,2,3을 더한다.
x=1+2+3
print (x)

type(object)

def add(x,y):
    print(x+y)
    
    add(1,2) + add(2,3)
    
    dir(add(1,2))
    
type(add(1,2))
type(add)

abs(-10)
print(type(abs(-10.)))

# +, -, /, *
print(5+3)
print(5-3)
print(5*3)
print(5/3)

# >, >=, <, <=, ==, !=, not
print(5>3)
print(5>=3)
print(5<3)
print(5<=3)
print(5==3)
print(5!=3)
print(not 5)
print(not 0)

callable(add)
callable(1)

#문자
#"abc" + "def"
"abc" - "abc"
"abc" * 3

ord("a")
ord("b")
ord('c')
chr(99)
chr(97)+chr(98)+chr(99)
chr(97)+chr(98)+chr(99) > 'bbb'

#표현식
5+3+4-1*7-3/2
5+3+4-1*7-3/2>2>1
5+3+4-1*7-3/2>2>1 > "abcde"
5+3+4-1*7-3/2>2>1 > bool("abcde")

print=1111
del print

for i in range(len("abcdef")):
    print(i)
len('dddd')

callable(len)

import keyword
keyword.kwlist
keyword.iskeyword('none')

# !=, @, $, %, ^, &, *
10//5
10%5
10 > 2 and 10 < 3

type(print)
type(print('abc'))

def aaa(x):
    return x
aaa(10)
type(aaa(10))

#주사위의 눈이 나올 기대값(expectation)
x1=1
x2=2
x3=3
x4=4
x5=5
x6=6
x=x1+x2+x3+x4+x5+x6
result=x/6
print(result)

sum(list(range(1,7)))/6
a=list(range(1,7))
sum(a)/len(a)

type(20)
print(type(20))

#index(Slicing)

#'문자'[start:end:step]

'안녕하세요'[0:6]
'안녕하세요'[1:6]
'안녕하세요'[-1]
'안녕하세요'[-1:-3:-1]
'안녕하세요'[int(3.0)]
'안녕하세요'[-1::-1]
'안녕하세요'[-1::-1][-1::-1]
'안녕하세요'[::2]
'안녕하세요'[3]

start=0
end=6
step=1
'안녕하세요'[start:end:step]

'\''

print('\n')
print('\t')
print('\\')

x=0.1
type(x)
import sys
sys.getsizeof(x)

a=10
#a=len()는 불가능
a=len
object

id(len)
id(a)

a=100
a
id(a)
id(len)

import math
pi = math.pi

pi

r=10
print(f"원의 둘레는 {2*pi*r}입니다.")

print(f"원의 넓이는 {pi*r**2}입니다.")

a=10
a+=5
a

a=10
a-=5
a

a=10
a*=5
a

a=10
a/=5
a

a=10
a%=5
a

a=10
a**=5
a

name=input("안녕하세요, 이름을 입력해주세요.")
print(f"당신의 이름은 {name}입니다.")

age=input("안녕하세요, 나이를 입력해주세요.")
print(f"당신의 나이는 {age}세입니다.")

age=int(input("안녕하세요, 나이를 입력해주세요."))
print(f"당신은 {age*12}개월을 살았습니다.")

name="Minhyeong Kim".split(" ")
print(name)