
alist = ['你','在','哪里','wa',1,2,3]

def for_demo():
    # for(关键字) i（变量名，代表循环次数）in（关键字）range（迭代器函数）
    for i in range(6):
        print(i)
        print('hello world')

def for_demo1():
    # 两个参数时 从第一个参数开始计数，到第二个参数的前一位停止
    for i in range(3,6):
        print(i)

    for n in range(0,6):
        print(n)

    #三个参数 从第一个参数开始计数，到第二个参数前一位停止 每次循环递增参数三
    for i in range(3,10,2):
        print(i)

    for n in range(11,5,-2):
        print(n)

# 遍历 就是对列表中的每一个元素都做一次操作
def for_list():
    for i in alist:
        print(i)

# 第二种遍历方式
def for_list2():
    # 获取list的长度
    a = len(alist)
    # 通过长度设置循环次数
    # 把i当作索引值来遍历元素
    for i in range(a):
        print(alist[i])

# 嵌套循环
def for_for():
    # 如果print不换行 print（"qqqqqqq",end=','）加个end=''
    for i in range(5):
        print('xxx')
        for j in range(2):
            print('qqqqqqq',end=',')
        print('')

# 停止所有循环
def for_dreak():
    for i in range(5):
        print(i)
        if i ==2:
            break

# continue 停止本次循环，直接开始下一次循环
def for_continue():
    for i in range(5):
        print(i)
        if i ==2:
            continue
        print('第%s循环'%i)
        print('')



if __name__ == '__main__':
    # for_demo()
    #  for_demo1()
    # for_list()
    #  for_list2()
    # for_for()
    # for_dreak()
    for_continue()