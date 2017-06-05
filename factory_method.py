import abc
"""
工厂方法
模式特点：定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类。

程序实例：基类雷锋类，派生出学生类和志愿者类，由这两种子类完成“学雷锋”工作。子类的创建由雷锋工厂的对应的子类完成。

代码特点：无
"""


class Leifeng:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wash(self):
        """"wash"""

    @abc.abstractmethod
    def sweep(self):
        """sweep"""

    @abc.abstractmethod
    def buy_rice(self):
        """buy rice"""


class Undergraduate(Leifeng):
    def wash(self):
        print "undergraduate wash"

    def sweep(self):
        print "undergraduate sweep"

    def buy_rice(self):
        print "undergraduate buy rice"


class Volunteer(Leifeng):
    def wash(self):
        print "volunteer wash"

    def sweep(self):
        print "volunteer sweep"

    def buy_rice(self):
        print "volunteer buy rice"


class IFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def CreateLeifeng(self):
        """create class leifeng"""


class UndergraduateFactory(IFactory):
    def CreateLeifeng(self):
        return Undergraduate()


class VolunteerFactory(IFactory):
    def CreateLeifeng(self):
        return Volunteer()


if __name__ == "__main__":
    # create undergraduate to sweep
    i_factory = UndergraduateFactory()
    leifeng = i_factory.CreateLeifeng()
    leifeng.sweep()

    # create volunteer to wash
    i_factory = VolunteerFactory()  # just replace UndergraduateFactory with VolunteerFactory
    leifeng = i_factory.CreateLeifeng()
    leifeng.wash()
