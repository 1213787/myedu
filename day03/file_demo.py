

if __name__ == '__main__':
    # w+ 覆盖内容
    text_io = open('test.text', 'w+')
    text_io.write('哇哇哇哇哇哇')

    # a+ 追加内容
    text_io=open('test.text','a+')
    text_io.write('嗷嗷嗷嗷嗷')

    # r 只可以读取不能写入
    text_io = open('test.text','r')

    # readline()读取一行
    readline = text_io.readline()
    print(readline)
    # 读取所有行 返回一个list
    readlines = text_io.readlines()
    print(readlines[2])



