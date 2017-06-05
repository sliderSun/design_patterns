import abc

"""
桥接模式
模式特点：将抽象部分与它的实现部分分离，使它们都可以独立地变化。

程序实例：两种品牌的手机，要求它们都可以运行游戏和通讯录两个软件，而不是为每个品牌的手机都独立编写不同的软件。

代码特点：虽然使用了object的新型类，不过在这里不是必须的，是对在Python2.2之后“尽量使用新型类”的建议的遵从示范。"""
class HandsetSoft:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self):
        """soft run"""


class HandsetGame(HandsetSoft):
    def run(self):
        print "run game"


class HandsetAddressList(HandsetSoft):
    def run(self):
        print "run address list"


class HandsetBrand:
    __metaclass__ = abc.ABCMeta

    def __init__(self, s):
        self.soft = s

    @abc.abstractmethod
    def run(self):
        """run"""


class HandsetBrandM(HandsetBrand):
    def run(self):
        print "handset brand M : ",
        self.soft.run()


class HandsetBrandN(HandsetBrand):
    def run(self):
        print "handset brand N : ",
        self.soft.run()


if __name__ == "__main__":
    handset_brand_m = HandsetBrandM(HandsetGame())
    handset_brand_m.run()
    handset_brand_m = HandsetBrandM(HandsetAddressList())
    handset_brand_m.run()

    handset_brand_n = HandsetBrandN(HandsetGame())
    handset_brand_n.run()
    handset_brand_n = HandsetBrandN(HandsetAddressList())
    handset_brand_n.run()
