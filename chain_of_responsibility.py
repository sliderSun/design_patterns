import abc
"""
职责链模式
模式特点：使多个对象都有机会处理请求，从而避免发送者和接收者的耦合关系。将对象连成链并沿着这条链传递请求直到被处理。

程序实例：请假和加薪等请求发给上级，如果上级无权决定，那么递交给上级的上级。

代码特点：无
"""


class Request:
    def __init__(self, t, n):
        self.type = t
        self.number = n


class Manager:
    __metaclass__ = abc.ABCMeta

    def __init__(self, n):
        self.name = n
        self.superior = None

    def set_superior(self, s):
        self.superior = s

    @abc.abstractmethod
    def request_applications(self, r):
        """resolve request"""


class CommonManager(Manager):
    def request_applications(self, r):
        if r.type == "leave application" and r.number <= 2:
            print self.name + " : approve"
        else:
            self.superior.request_applications(r)


class Majordomo(Manager):
    def request_applications(self, r):
        if r.type == "leave application" and r.number <= 5:
            print self.name + " : approve"
        else:
            self.superior.request_applications(r)


class GeneralManager(Manager):
    def request_applications(self, r):
        if r.type == "leave application":
            print self.name + " : approve"
        elif r.type == "salary increase":
            if r.number <= 500:
                print self.name + " : approve"
            else:
                print self.name + " : not approve"


if __name__ == "__main__":
    common_manager = CommonManager("JingLi")
    majordomo = Majordomo("ZongJian")
    general_manager = GeneralManager("ZongJingLi")
    common_manager.set_superior(majordomo)
    majordomo.set_superior(general_manager)

    request = Request("leave application", 4)
    common_manager.request_applications(request)

    request = Request("salary increase", 1000)
    common_manager.request_applications(request)
