def if_demo():
    # 3大于2 所以 啊是True
    a = 3 > 2
    # a是True 所以条件成立 打印zhen,如果a是false 条件不成立走 else 分支，打印 jia
    if a:
        print('zhen')
    else:
        print('jia')

def ifel_demo():
    # 赋值 a 为6
    a = 6
    # 判断a是否等于1
    if a == 1:
        print('a是1')
    # 判断a是否等于2
    elif a == 2:
        print('a是2')
    # 判断a是否等于3
    elif a == 3:
        print('a是3')
    # 判断a是否等于4
    elif a == 4:
        print('a是4')
    # 判断a是否等于5
    elif a == 5:
        print('a是5')
    # 如果a都不满足上面的条件，则走else
    else:
        print('a是%s'%a)

    print('if结束')

if __name__ == '__main__':
    if_demo()
    ifel_demo()