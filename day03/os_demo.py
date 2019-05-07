import os

def test():
    # 占位，防止报错
    pass

if __name__ == '__main__':
    # os.getcwd() 获取当前目录
    pwd=os.getcwd()
    print(pwd)

    #返回上级目录的字符串
    b=os.path.abspath('..')
    print(b)

    # 返回上上级目录
    c=os.path.abspath('../..')
    print(c)
