import abc

"""
建造者模式
模式特点：将一个复杂对象的构建(Director)与它的表示(Builder)分离，使得同样的构建过程可以创建不同的表示(ConcreteBuilder)。
程序实例：“画”出一个四肢健全（头身手腿）的小人
"""
class Pen:
    """class pen"""


class Graphics:
    """class graphics"""


class PersonBuilder:
    __metaclass__ = abc.ABCMeta

    def __init__(self, p, g):
        self.pen = p
        self.grahics = g

    @abc.abstractmethod
    def BuildHead(self):
        """build head"""

    @abc.abstractmethod
    def BuildBody(self):
        """build body"""


class PersonThinBuilder(PersonBuilder):
    def BuildHead(self):
        print "build thin head"

    def BuildBody(self):
        print "build thin body"


class PersonFatBuilder(PersonBuilder):
    def BuildHead(self):
        print "build fat head"

    def BuildBody(self):
        print "build fat body"


class PersonDirector:
    def __init__(self, pb):
        self.person_builder = pb

    def create_person(self):
        self.person_builder.BuildHead()
        self.person_builder.BuildBody()


if __name__ == "__main__":
    # build thin person
    person_builder = PersonThinBuilder(Pen(), Graphics())
    director = PersonDirector(person_builder)
    director.create_person()

    # build fat person
    person_builder = PersonFatBuilder(Pen(), Graphics())  # only replace PersonThinBuilder with PersonFatBuilder
    director = PersonDirector(person_builder)
    director.create_person()
