 # 一、翻译小程序案例
 ### 1、可以查询单词
 ### 2、可以定义补充单词和解释
 ### 3、可以删除某个词
 
==== ==小技巧：VSCODE中，ctrl+？可以自动把一行代码注释掉==

==按住alt+shift+向上，可以自动复制粘贴当前到下一行==

==按住alt+上下，可以上下移动这行代码==
==ctrl+X是剪贴==
 ## ==新学知识点==
 - dicit
 - set
 - tuple
 ***
能说算不上什么，有本事就把你的代码给我看看。
==### 1、dict（字典结构）的增删改查==



```
my_dict = {
    "a":1,
    "b":2
}

out: {'a':1,'b':2} #因为dict是内置的结构，所以命名最后加个前缀，怕冲突，不管前面的单引号还是双引号，最后的输出都是单。


paul = {
    'name' : 'paul',
    'city' : 'fuding',
    'code' : 'python'
}
paul

out:{'name': 'paul', 'city': 'fuding', 'code': 'python'}

paul['name'] #默认来说[]里面只能写前面的字符，后面是它对应的key
out:'paul'

#可以直接插入增加
paul['city'] = 'fujian'
#这时候再输出city就变成 'fujian'

paul['fujian'] #如果这么写就会报错，因为'fujian'在后面，是一个KEY值，可以用get来操作
paul.get(shanghai) 不会报错，会返回一个空值None
paul.get('name')
out: 'paul'

paul.get('fujian','shanghai')
#再加一个参数的意思是，如果找不到第一个，就默认返回逗号后面这个。

paul['age'] = 18 #新增年龄，加在什么位置不一定，也有可能加在后面

paul['students'] = ['lily','hmm','tony','jack'] #也可以新建一个学生列表,这是一个嵌套的结构

out:
{'name': 'paul',
 'city': 'fujian',
 'code': 'python',
 'age': 18,
 'students': ['lily', 'hmm', 'tony', 'jack']}
#现在我们想在paul上增加一个书键值对 
 book = {
    'name':'python3',
    'price':100
}

paul['book'] = book

```
### dict,删，改，查


```
del paul['name'] #删
paul['age'] = 20 #改

paul['book'] #查
paul['book']['price'] 嵌套查

paul.keys() #查找所有的键，不包括值
out: dict_keys(['name', 'city', 'code', 'age', 'students', 'book'])

type(paul.keys()) #可以用它查看类型
out: dict_keys #内置的类型

paul.keys()[0] #这个是不对的，keys不支持索引操作，那怎么取里面的值呢。

[i for i in paul.keys()]
out:
['name', 'city', 'code', 'age', 'students', 'book']

[i for i in paul['book'].keys()]
out:
['name', 'price']

paul.items() #用这个可以看到所有的东西
out:
dict_items([('name', 'paul'), ('city', 'fujian'), ('code', 'python'), ('age', 18), ('students', ['lily', 'hmm', 'tony', 'jack']), ('book', {'name': 'python3', 'price': 100})])

for item in paul.items():
    print(item) #可以用这个方法输出

[item for item in paul.items()]
#也可以用这个方法输出

for key,value in paul.items(): #利用循环语句分别将值打印出来
    print(f'{key}:{value}') #这个冒号其实无实际意义，可以改成别的，具体看day02笔记中关于f'的用法
    
out:
name:paul
city:fujian
code:python
age:18
students:['lily', 'hmm', 'tony', 'jack']
book:{'name': 'python3', 'price': 100}


```
***
### ==2、tuple元组==
# 元组，一般表示一些成对的东西，可以应用于坐标

```
cor = 23,56 #三个数字可以做三维坐标
cor
out:(23,56)
type(cor)
out: tuple

cor = (23,34) #或者这样，效果一样

cor[0]=45 #元组不支持这样的赋值
cor[0] out:23 #取值是没问题的

ip_port = ('192.168.1.1',8001)#不可变，这是老前辈都规定好的
host = {} #新建一个字典
host['ip_port'] = ip_port #将元组赋值给字典
host
out:{'ip_port': ('192.168.1.1', 8001)}

host['ip_port'][0] #这样就可以取到第0个值

ip = ('192.168.1.2',) #元组是成对出现的，就算只写一个也要加上逗号，不然类型就变成str而不是tuple,这点要特别注意
host[ip] = 'anmin_pc'
host
out:
{'ip_port': ('192.168.1.1', 8001), ('192.168.1.2',): 'anmin_pc'}



```

### ==3、set集合（不重复的元素）==


```
number = {1,2,3,4,5,6,7,8,9}
type(number)
out: set

number[0] #报错，不支持索引的这种取值方式，要记住，这种方式只支持列表

可以与列表相互转换
others = [2,3,4,5,6,7,7] #一个列表
set(others)
out: {2,3,4,,5,6,7}

len(number) #输出长度
```
 # 二、翻译小程序案例
 
 
```
# 实现一个翻译小程序
# 1 可以查询单词
# 2 可以自定义补充单词和解释
# 3 可以删除某个词
print('欢迎来到8哥小词典'.center(30, '-'))
orig_dict = {'中文': 'Chinese', '书': 'book', '代码': 'code', '字典': 'dict', '英语': 'english'}
query = input('请输入要查询的中文：')
# 判断是否已经存在
if(orig_dict.get(query, '')):
    print(f'你查询的中文为：{query}, 意思是：{orig_dict[query]}')
else:
    add = input('没有查到，是否愿意帮助扩充词库（y/n）：')
if add == 'y':
    print(orig_dict)
    print('谢谢帮助，请添加单词和相关解释，用冒号分割，')
    words = input('示例（书：book）')
    words = words.split(':')
    orig_dict[words[0]] = words[1]
    print(orig_dict)
else:
    print('再见')
```

 # 二、单位转换器
 
```
*********欢迎使用万能单位转换器**********
T 温度转换
L 长度转换
C 货币转换
请选择转换类型：T
请输入温度（示例：1C或1F）：2C
35.6
print('欢迎使用万能单位转换器'.center(30, '*'))
menu = {
'T':'温度转换',
'L':'长度转换',
'C':'货币转换'
} 
for k, v in menu.items():
    print(k, v)
choose = input('请选择转换类型：')
if choose == 'T':
    temp = input('请输入温度（示例：1C或1F）：')
if temp.endswith('C'):
    # temp = float(temp.strip('C').strip('F'))
    temp = float(temp.strip('C'))
# 摄氏温度转华氏温度 Tf=(9/5)Tc+32
    Tf = ( 9 / 5 ) * temp + 32
    print(f'Tf = (9/5)*{temp}+32 = {Tf}F')
    # TODO 华氏温度转摄氏温度         Tc=(5/9)(Tf-32)
else:
    print('开发中...再见')
else:
    print('开发中...再见')
*********欢迎使用万能单位转换器**********
T 温度转换
L 长度转换
C 货币转换
请选择转换类型：T
请输入温度（示例：1C或1F）：2C
Tf = (9/5)*2.0+32 = 35.6F
```
