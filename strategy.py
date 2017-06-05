import abc
"""
策略模式
模式特点：定义算法家族并且分别封装，它们之间可以相互替换而不影响客户端。

程序实例：商场收银软件，需要根据不同的销售策略方式进行收费

代码特点：不同于同例1，这里使用字典是为了避免关键字不在字典导致bug的陷阱
"""


class CashSuper:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def accept_cash(self, c):
        """caculate cash"""


class CashNormal(CashSuper):
    def accept_cash(self, c):
        return c


class CashRebate(CashSuper):
    def __init__(self, r):
        self.rebate = r

    def accept_cash(self, c):
        return c * self.rebate


class CashReturn(CashSuper):
    def __init__(self, c, r):
        self.condition = c
        self.money = r

    def accept_cash(self, c):
        return c - int(c / self.condition) * self.money


class CashContext:
    def __init__(self, t, s):
        self.cash = None
        if t == "normal":
            self.cash = CashNormal()
        elif t == "rebate":
            self.cash = CashRebate(float(s))
        elif t == "return":
            args = s.split(' ')
            self.cash = CashReturn(float(args[0]), float(args[1]))

    def get_result(self, c):
        return self.cash.accept_cash(c)


if __name__ == "__main__":
    cash_context = CashContext("normal", "")
    print cash_context.get_result(1000)

    cash_context = CashContext("rebate", "0.8")
    print cash_context.get_result(1000)

    cash_context = CashContext("return", "300 100")
    print cash_context.get_result(1000)
