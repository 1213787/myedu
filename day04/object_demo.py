
class human (object):

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def chifan(self):
        print('%s吃饭'%self.name)

    def shuijiao(self):
        print('%s睡觉'%self.name)


class Tester (human):

    def work(self):
        self.chifan()
        print('%s在测试'%self.name)
        self.shuijiao()

if __name__ == '__main__':
    # human = human('qqq',10,'男')
    # human.chifan()
    # human.shuijiao()
    # human.chifan()
    tester = Tester('qqq', 10, '男')
    tester.work()
    print(tester.sex)