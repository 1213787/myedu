
# 计算1到50之间的奇数和?
def sum_demo():
    sum = 0

    for i in range(1, 51):
        if i % 2 == 1:
            sum = sum +i
    print(sum)

# 写for循环打印九九乘法表?
def jiujiu():

    for i in range(1,10):
        x = i +1
        for j in range(1,i+1):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
        print('')


# 输入两个数求这两个数之间的偶数和?
def sum_demo1(a,b):
    sum =0
    if a<b:
        for i in range(a,b):
            if i %2 ==0:
                sum = sum+i
    elif a>b:
        for i in range(a,b):
            if i %2 ==0:
                sum = sum+i
    else:
        print('a和b相等')

    print(sum)
if __name__ == '__main__':
    # sum_demo()
    # jiujiu()

    # 顺序入参
    # sum_demo1(10,20)
    # 指定参数入参
    # sum_demo1(a=10,b=20)
    sum_demo1(b=20,a=10)
