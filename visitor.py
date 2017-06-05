import abc
"""
访问者模式
模式特点：表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作。

程序实例：对于男人和女人（接受访问者的元素，ObjectStructure用于穷举这些元素），不同的遭遇（具体的访问者）引发两种对象的不同行为。

代码特点：无
"""

class Action(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_man_conclusion(self, p):
        pass

    @abc.abstractmethod
    def get_woman_conclusion(self, p):
        pass


class Success(Action):
    def get_man_conclusion(self, p):
        print "man success"

    def get_woman_conclusion(self, p):
        print "woman success"


class Failure(Action):
    def get_man_conclusion(self, p):
        print "man failure"

    def get_woman_conclusion(self, p):
        print "woman failure"


class Person(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def accept(self, a):
        pass


class Man(Person):
    def accept(self, a):
        a.get_man_conclusion(self)


class Woman(Person):
    def accept(self, a):
        a.get_woman_conclusion(self)


class ObjectStructure(object):
    def __init__(self):
        self.people = []

    def attach(self, p):
        self.people.append(p)

    def detach(self, p):
        self.people.remove(p)

    def display(self, a):
        for person in self.people:
            person.accept(a)


if __name__ == "__main__":
    man = Man()
    woman = Woman()
    object_structure = ObjectStructure()
    object_structure.attach(man)
    object_structure.attach(woman)
    object_structure.display(Success())
    object_structure.display(Failure())
