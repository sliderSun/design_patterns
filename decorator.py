import abc
"""
装饰模式
模式特点：动态地为对象增加额外的职责

程序实例：展示一个人一件一件穿衣服的过程。

代码特点：无
"""


class Person:
    def show(self):
        print "person"


class Finery(Person):
    def __init__(self, c):
        self.component = c

    def show(self):
        """finery show"""


class Tie(Finery):
    def show(self):
        print "tie ",
        self.component.show()


class Suit(Finery):
    def show(self):
        print "suit ",
        self.component.show()


class Shoes(Finery):
    def show(self):
        print "shoes ",
        self.component.show()


if __name__ == "__main__":
    person = Person()
    tie = Tie(person)
    suit = Suit(tie)
    shoes = Shoes(suit)
    shoes.show()
