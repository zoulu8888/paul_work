 # 一、字符串的增删改查
 ## 1、字符串的增加
 ### ==代码块==
***
### 第一种方式
``` pythom
"8"*10  out:8888888888  # 10个8
"*"*11  out:*********** #11个*
name='paul'
city='fujian'
info=name+''+city
info    out:'paul fujian'

```
***
### 第二种方式（基于前面已赋值的name,city)
```
'name: %s, city: %s' %(name,city)
%S是在内存中开辟一个空间
```
***
### 第三种方式（基于前面已赋值的name,city)
```
'name: {},city: {}'.format(name,city)
'name: {nameA},city: {city}'.format(nameA=name,city=city)
```
***
### 第四种方式（基于前面已赋值的name,city,建议用这种，最新趋势，f-ctring)
```
f'{name}:{city}'
```
***
### 语句表达
```
f'my name is {name}：and live in {city}'
"'lilei said'where is hanmeimei'"
外面应单引号，里面就要用双引号，反之亦然。
```
 ## 2、字符串的删除（清空）
 ```
name='paul'
name   out:'paul'
name=""
name   out:''
```
***
 ## 3、字符串的各种修改（非常重要）
 ### 大小写转换
 ```
 name = 'paul'
 name.upper()  #out:'PAUL' 在编译器中按name可补全
 name.lower()  #out:'paul'
 name.capitalize() #out:'Paul' 首字母大写
 name ='what is this ?'
 name.title() #out:'What Is This?' 每个单词首字母大写
 name.strip('what') #out: '  is this' 只能移除开头和结尾的字符，
 没有参数的时候，去除头尾空格不明白的时候可以？查看下。

 ```
 ### 替换
 
```
email='280854#qq.com'
email.replace('#','@') #out:'280854@qq.com'
# 上面这条命令只是输出，并没有保存这个变量，
可以用下面这个方法保存
（new_email=email.replace('#',"@")

```
***
 ### 补全、对齐
 
```
email.zfill(15) #out:00280854#qq.com #补0
email.ljust(15,"*") #out:280854#qq.com** 左对齐
email.rjust(15,"*") #out:**280854#qq.com 右对齐
email.center(16,"*") #out:*280854#qq.com** 放中间，如果用空格就不写'*'
```
***
 ## 4、字符串的查询
 ### 查询大小写
 ```
 name.isupper() #out:Fale
 name.islower() #out:True
 ```
 ***
 ### 查询位置
 
```
py = 'python is cool'
py.index('is') #out:7 列表是从0开始数的
py.index('o') #out:4 默认查询第一个，查不到会报错，用find不会
py.find('is') #out:7 查不到返回-1
dir(name) #可以查询name下可用的所有方法

```
***
 ## 5、字符串的输入
 如果是0赋值，想直接窗口输入
 
```
name=input('name:') #会有输入框
len(name) 查字符串的长度
name.strip() 去除两端的空格
len(name.strip)
```
 ## 6、字符串切片操作
 
 
```
py='abcde'
py[2]  out=c  从零开始数
py[-2] out=d  尾巴从-1开始
py.index('b') out：1   查询b在第几位
py[:py.index('b')]  out:ab  嵌套操作活学活用
something='abcdefg1234567'
something[1:6:2] 从1到6两个两个取，2其实是隔一个取
out:bdf  认真理解一下
something[4::4] 从第四个开始每隔三个取 
out:'e26' 好好理解一下
something[::-1]反转输出
something[something.index('e'):] 从e开始取后面

email='280854#qq.com'
email.split('#') #out:['280854','qq.com']
输出这个列表，如果想要第一个：
email.split('#')[0]或者email[0:email.index('#')]
不过由于index查询的字符如果不在参数中，是会报错的，所以index现在比较少用，一般用find
email.find('#')
email[email.find('#')+1:] 取后面一个

```
***
 ## 7、数字和字符串的判断
type('8')和type(8) 是str与int

```
num='8asd'
num.isdigit() out:False
num.isalpha() out:True
num='三'
num.isdecimal() out:Flase  
num.isnumeric() out:True 判断是不是一个数
num='3'
num.isdecimal() out:True 十进制数
主要用在比如要求输入数字，对方输入的是其他东西，可以利用这个方法来判断是否需要重新输入。

```
***
 # 二、打印乘法表
 
```
1*9= 9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81
1*8= 8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
1*7= 7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
1*6= 6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
1*5= 5 2*5=10 3*5=15 4*5=20 5*5=25
1*4= 4 2*4= 8 3*4=12 4*4=16
1*3= 3 2*3= 6 3*3= 9
1*2= 2 2*2= 4
1*1= 1
```
***

```
rang(5)  out:rang[0,5]
for i in rang（5)
    print(i)  #注意缩进
#默认换行，要想不换行print(i,end=' ')
#out:
0
1
2
3
4

for i in rang(9,0,-1) #从9到1，不包括0
    print(i) #需要缩进，不然会报错
    
    
```

```
n=10
for i in range (5): #输出5行
    for j in range (1,n): #从1到9
        print(j,end=' ') #间隔空格
    print() #进入下一个循环前换行
    n -= 1 #每次减1
```


```
for i in range (9,0,-1):
    for j in range (1,i+1): #后面一个数不包括，所以加个1
        print(f"{j}*{i}={str(i*j).ljust(2)}",end=" ") #1just左边对齐后面空2空格
    print()
```
***

```
ch_numbers = [' ', '一', '二', '三', '四', '五', '六', '七', '八', '九', '零'] # 逗号，引号，中英文
切换,加空格是因为从0开始数的，加空格可以正确定位
numbers = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(9, 0, -1):
for j in range(1, i+1):
result = str(i*j).ljust(2)#加2个空格是为了防止如果是单位数字比如9，index取右边报错。
left = ch_numbers[numbers.index(result[0])]#例如9，result0取左右的9,index查找9在第几位，然后对应输出中文版的数字，列表之前已经在第0位加了空格，所以9可以直接对应九。认真理解下，这个方法经常用。
right = ch_numbers[numbers.index(result[1])]
print(f"{ch_numbers[j]}*{ch_numbers[i]}={left}{right}", end=" ")
print()
```
***
 # 三、案例：token生成器
 
 
```
import random
i="sadasdasdasd"
random.choice(i)   out:d #随机选择一个

str_list = ['a','b','c','d','e','1']
s = ""
s.join(str_list) out:'abcde1' #这个方法只接受字符串

for i in range (5):
    s = random.choice('sdsadsad')
    print(s,end='\n') #用循环语句多次输出
    
    
tokens = [] #或者用list()也可以，两种表达方式
for i in range (5):
    s = random.choice('sdsadsad')
    tokens.append(s) #添加进列表
tokens
s=''
s.join(tokens) # 或者 ''.join(tokens) 这样就变成字符串
# out:'daasd'

tokens = [] #或者用list()也可以，两种表达方式
count = input ('num:') #由于input输入的都是字符串
for i in range (int(count)): #所以这个位置要用int包起来
    s = random.choice('sdsadsad')
    tokens.append(s) #添加进列表
tokens
s=''
''.join(tokens)
# 这么些可以自由输入了，现在看看这些字符都是我们自己定义的，我们其实可以调用系统中的

import string #先用import导入sring这个函数
string.ascii_lowercase #这个方法可以导出所有小写字母
string.ascii_letters #这个方法可以导出所有小写与大写字母
string.digits #这个方法可以导出所有数字

#现在我们只要把两个加起来就可以了
str_from = string.digits + string.ascii_letters
tokens = [] #或者用list()也可以，两种表达方式
count = input ('num:') #由于input输入的都是字符串
for i in range (int(count)): #所以这个位置要用int包起来
    s = random.choice(str_from)
    tokens.append(s) #添加进列表
tokens
s=''
''.join(tokens)

# python的表达式可以非常简洁，比如：

[m for m in range(5)]
out:[0,1,2,3,4]

[random.choice('sdagsh') for x in range(5)]
# 或者这样也一个道理，其实这里的X跟前面没关系，我们可以放弃。
[random.choice('asdsad') for _ in range(5)] #下划线一般表示这个参数没有什么实际意义，可以抛弃。
[random.choice(string.digits +string.ascii_letters) for _ in range(5)]

count = input('num:')
[random.choice(string.digits +string.ascii_letters) for _ in range(int(count))]

#最后一步，以上这写代码输出的都是列表，我们想改成字符串

count = input('num:')
''.join([random.choice(string.digits +string.ascii_letters) for _ in range(int(count))])


```

