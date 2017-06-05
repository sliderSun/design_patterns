import abc
"""
代理模式
模式特点：为其他对象提供一种代理以控制对这个对象的访问。

程序实例：同模式特点描述。

代码特点：无
"""


class GiveGift:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, sg):
        """init"""

    @abc.abstractmethod
    def give_dolls(self):
        """give dolls"""

    @abc.abstractmethod
    def give_flowers(self):
        """give flowers"""


class SchoolGirl:
    def __init__(self, n):
        self.name = n


class Pursuit(GiveGift):
    def __init__(self, sg):
        GiveGift.__init__(self, sg)
        self.school_girl = sg

    def give_dolls(self):
        print "give " + self.school_girl.name + " dolls"

    def give_flowers(self):
        print "give " + self.school_girl.name + " flowers"


class Proxy(GiveGift):
    def __init__(self, sg):
        GiveGift.__init__(self, sg)
        self.pursuit = Pursuit(sg)

    def give_dolls(self):
        self.pursuit.give_dolls()

    def give_flowers(self):
        self.pursuit.give_flowers()


if __name__ == "__main__":
    school_girl = SchoolGirl("Alice")
    proxy = Proxy(school_girl)
    proxy.give_flowers()
    proxy.give_dolls()
