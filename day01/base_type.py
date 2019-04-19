
def test1():
     print('test1')
def test2():
     print('test2')
def test3():
     print('test3')

# 整数类型的演示
def int_demo():
    # 声明一个变量 = 前面的就是变量名  ， =后面的就是变量值
    aint = 5
    # 打印 aint变量
    print(aint)
    # type(aint);获取aint的变量类型
    # print(type(aint)) :打印 aint的变量类型
    print(type(aint))

# 字符串类型的演示
def str_demo():
    astr = '5'
    print(astr)
    print(type(astr))

#  小数类型的演示
def float_demo():
    afloat = 0.1
    print(afloat)
    print(type(afloat))

# 加法方法演示 （a,b）: ()里面的东西叫参数，多个参数用， 分隔开 ； 参数等同于变量，只不过没有赋值
def add_demo(a,b):
    print(a+b)


def type_zhuanhuan():
    aint = 7
    # 获取aint的类型
    print(type(aint))
    # 将aint转换为str 类型，再打印出它的类型
    print(type(str(aint)))
    # 将aint再转换回来，int类型，再打印出它的类型
    print(type(int(aint)))

    # 被转换的字符 必须是满足数字的格式
    # print(type(int('***')))

#   字符串拼接
def str_join():
    a = 123
    b = '你好'
    c = 1.11
    # 方法一
    print(str(a)+b+str(c))
    # 方法二 %s 是占位符
    print('a是%s b是%s c是%s'%(a,b,c))


def jianfa_demo(a,b):
    c = a -b
    #  return : 返回的意思 后面是什么 方法执行后就返回什么
    return c
    # return 后面不能继续写代码，因为方法执行到return就会结束

if __name__ == '__main__':
    # test3()
    # test1()
    # test2()
    # int_demo()
    # str_demo()
    # float_demo()

    #  调用方法，并传参
    # add_demo(10,10)
    # 加法如果传字符串，会把两个字符串拼接在一起
    # add_demo('四月','十八日')
    # type_zhuanhuan()
    # str_join()

    c =jianfa_demo(6,2)
    d = add_demo(6,2)
    print(c)
    print(d)
    print(type(d))