# 查询或者获取list 里面的值（元素）
# a[索引]  或者叫下标值  元素从0开始数
def list_sel(a):
    # 顺序取值 从0开始数
    print(a[2])
    # 倒序取值 从-1开始数
    print(a[-1])
    # 切片取值语法 前索引值 ：后索引值 取的时候取到后索引值的前一位
    print(a[1:5])
    print(a[0:2])
    # 不填值的话 从第一个开始取值
    print(a[:4])
    # 不填值的话 取到最后一位
    print(a[3:])

if __name__ == '__main__':
    alist=['a',4,'nihao','8','嘻嘻','哈哈']
    list_sel(alist)