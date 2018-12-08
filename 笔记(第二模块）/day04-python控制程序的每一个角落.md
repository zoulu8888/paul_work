# 条件控制语句
## （一） 哪一句代码是真的

## 1、==and(两个都真为真）==      ==or（一个真就是真）==
## ==not （取反，not真就是假）====

==非零为真，零为假==
```
a = 1 
b = 2
c = 0
a and b # 判断and前后的都是不是真，真的话返回最后一个真的值，否则返回第一个假的值
out: 2

a or b # 判断or前后有没有真值，有就直接返回，不再继续判断。否则判断到最后的值直接返回
```

## 2、优先级问题

```
x=True
y=False
z=False
x or y and z # 由于and优先级较高，所以返回True

(x or y) and z #这个返回False

```

## 3、is 和 ==


```
a=1
b=a
c=1

a is b
out:True

a is c
out:True

a == b
out:True

```
####  这里要注意一点是is比较ID值，而'=='是比较大小，数值比较小的时候，同一个数字的ID值是一样的，但是比如1000这种比较大的数字，ID值就不一样了，会返回False

```
a=1000
b=1000
a is b #返回False
a == b #返回True
```

## （二） if 语句一家人


```
if a > 4:
    print('ok')
else:
    print('oh no!')
```


```
if a < 4:
    print('小于4')
elif a < 8:
    print('4<a<8')
else:
    print('>8')
```


```
numbers_1 = [1,2,3,4,7]

if a in numbers_1:
    print('has a')
else:
    print('not a')

```
###     in and
```
a = 1
b = 4
numbers_1 = [1,2,3,4,7]

if a in numbers_1 and b in numbers_1:
    print('ok')
else:
    print('no')



```
### any 内置函数

```

# any all
if any(x > 3 for x in numbers_1):
    print('ok')
else:
    print('no')

# 从numbers_1中循环拿出数字与3比较，任何一个大于3就输出OK。

```


```
if all(x > 3 for x in numbers_1):
    print('ok')
else:
    print('no')

从numbers_1中循环拿出数字与3比较，所有数都大于3就输出OK。
```

## （三） for循环
### ==else break continue==


```
for x in range(5):
    print(x)
```


```
for x in [1,2,3]:
    print(x)
```


```
for x in (1,2,3):
    print(x)
```


```
for x in {1,2,3}:
int(x)
```


```
my_dict = {'name':'de8ug', 'city': 'beijing'}

for x in my_dict:
    print(x) # 默认输出key,与下面这个一样

for x in my_dict.keys():
    print(x)

out:
name
city

for x in my_dict.values():
    print(x) # 这样就输出值

out:
de8ug
beijing
```


```
for key, value in my_dict.items():
    print(key, value) # f'{}'

out:
name de8ug
city beijing
```


```
for x in [1,2,3]:
    print(x)
else: # 当for循环完了所有元素，才走
    print('end')

out:
1
2
3 
end
```


```
for x in [1,2,3]:
    if x == 3:
        break #刹车，走出去了，下面的语句都不走了
    print(x)
else:
    print('end')
    
out:
1
2
```

```
for x in [1,2,3,4,5]:
    if x == 2:
        continue # 轻点刹车
    print(x)

out:
1
3
4
5
```

### 枚举


```
# 枚举
for index, x in enumerate(['a', 'b', 'c', 'd']):
      # print(f'{index} -> {x})
      # print('f{index} -> {x}')
    print(f'{index} -> {x} ')
    
out:
0 -> a
1 -> b
2 -> c
3 -> d
```

## （四） while 循环

### ==循环的路上一定要学会刹车！==


```
# 先会刹车！！！
a = 4
i = 0
while i < a:
    print(i)
    i = i + 1
```


```
while True: #一直循环
    name = input('name(q为退出):')
    if name == 'q': #设置跳出循环条件
        print('bye')
        break
    else:
        print(name)
```


```
a = 6
i = 0
while i < 6:
    print(i)
    i += 1 # = i + 1
#       if i == 3:
#           break
else:
    print('what happened!?')
```

## （五） 21点游戏

两个玩家，游戏开始先输入名字
用字典保存每个玩家信息：姓名，获胜次数
电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21的获胜
每轮结束显示玩家信息
按q退出游戏

## （六） 51备忘录V0.25

示例： hi， Siri，明天早上8点提醒我带手机 小冰，中午吃饭时候讲个笑话





