# # 查询或者获取list 里面的值（元素）
# # a[索引]  或者叫下标值  元素从0开始数
# def list_sel(a):
#     # 顺序取值 从0开始数
#     print(a[2])
#     # 倒序取值 从-1开始数
#     print(a[-1])
#     # 切片取值语法 前索引值 ：后索引值 取的时候取到后索引值的前一位
#     print(a[1:5])
#     print(a[0:2])
#     # 不填值的话 从第一个开始取值
#     print(a[:4])
#     # 不填值的话 取到最后一位
#     print(a[3:])
#
# def list_del():
#     # 定义一个list
#     alist = ['q',1,'啊啊','8','哼哼','吼吼']
#     # 调用删除方法 不填参数 默认删除最后一位
#     alist.pop()
#     print(alist)
#     # 调用删除方法 填写参数索引值 就可以删除指定参数
#     alist.pop(0)
#     print(alist)
#     # 将切片获取的元素 重新定义一个list保存起来
#     blist = alist[:-3]
#     print(blist)
#
# def list_add():
#     alist = ['a',4,'nihao','8','黑黑','的']
#     # 增加元素，增加在末尾
#     alist.append('哈哈哈')
#     print(alist)
#
#     blist = [1,2,3]
#     # 将一个list 作为元素 添加到list里面
#     alist.append(blist)
#     print(alist)
#
# # 替换
# def list_update():
#     alist = ['a', 4, 'nihao', '8', '黑黑', '的', '哈哈哈', [1, 2, 3]]
#     alist[5] = '白白'
#     print(alist)
#
# if __name__ == '__main__':
#     alist=['a',4,'nihao','8','嘻嘻','哈哈']
#     # list_sel(alist)
#     # list_del()
#     # list_add()
#     # list_update()
#     # 获取list长度
#     print(len('alist'))
#
#




def list_qwe():
    alist=['元素1','元素2','元素3','元素4','元素5']
    print(alist[2])
    print(alist[1:4])
    alist.pop(3)
    print(alist)
    alist.append('111')
    alist.append('222')
    print(alist)
    alist[0]=5
    print(alist)
    print(len(alist))


if __name__ == '__main__':
    list_qwe()