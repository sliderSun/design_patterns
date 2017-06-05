import abc
"""
观察者模式
模式特点：定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，当主题对象状态发生变化时会通知所有观察者。

程序实例：公司里有两种上班时趁老板不在时偷懒的员工：看NBA的和看股票行情的，并且事先让老板秘书当老板出现时通知他们继续做手头上的工作。

程序特点：无
"""


class Observer:
    __metaclass__ = abc.ABCMeta

    def __init__(self, n, nr):
        self.name = n
        self.notifier = nr

    @abc.abstractmethod
    def update(self):
        """updated by notifier"""


class NbaObserver(Observer):
    def update(self):
        print self.name + ", " + self.notifier.state + ", close NBA"


class StockObserver(Observer):
    def update(self):
        print self.name + ", " + self.notifier.state + ", close stock"


class Notifier:
    def __init__(self):
        self.observers = []
        self.state = ""

    def attach(self, o):
        self.observers.append(o)

    def detach(self, o):
        self.observers.remove(o)

    def notify(self):
        for observer in self.observers:
            observer.update()


class Boss(Notifier):
    pass


class Secretary(Notifier):
    pass


if __name__ == "__main__":
    boss = Boss()
    nba_observer = NbaObserver("Bob", boss)
    boss.attach(nba_observer)
    stock_observer = StockObserver("Alice", boss)
    boss.attach(stock_observer)
    boss.state = "boss's back himself"
    boss.notify()
