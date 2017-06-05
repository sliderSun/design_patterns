import abc
"""
命令模式
模式特点：将请求封装成对象，从而使可用不同的请求对客户进行参数化；对请求排队或记录请求日志，以及支持可撤消的操作。

程序实例：烧烤店有两种食物，羊肉串和鸡翅。客户向服务员点单，服务员将点好的单告诉大厨，由大厨进行烹饪。

代码特点：注意在遍历列表时不要用注释的方式删除，否则会出现bug。bug示例程序附在后面，我认为这是因为remove打乱了for迭代查询列表的顺序导致的。
"""



class Barbecuer(object):
    def bake_mutton(self):
        print "bake mutton"

    def bake_chicken(self):
        print "bake chicken"


class Command(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, r):
        self.receiver = r

    @abc.abstractmethod
    def execute_command(self):
        pass


class BakeMuttonCommand(Command):
    def execute_command(self):
        self.receiver.bake_mutton()


class BakeChickenCommand(Command):
    def execute_command(self):
        self.receiver.bake_chicken()


class Waiter(object):
    def __init__(self):
        self.commands = []

    def set_order(self, o):
        if isinstance(o, BakeChickenCommand):
            print "chicken sold out"
        else:
            print "add order: " + type(o).__name__
            self.commands.append(o)

    def cancel_order(self, o):
        print "cancel order: " + type(o).__name__
        self.commands.remove(o)

    def notify(self):
        for command in self.commands:
            command.execute_command()


if __name__ == "__main__":
    barbecuer = Barbecuer()
    bake_mutton_command = BakeMuttonCommand(barbecuer)
    bake_chicken_command = BakeChickenCommand(barbecuer)
    waiter = Waiter()
    waiter.set_order(bake_mutton_command)
    waiter.set_order(bake_mutton_command)
    waiter.set_order(bake_chicken_command)
    waiter.notify()