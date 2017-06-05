import abc
"""
状态模式
模式特点：当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类。

程序实例：描述一个程序员的工作状态，当需要改变状态时发生改变，不同状态下的方法实现不同

代码特点：无
"""


class Work:
    def __init__(self, h, f):
        self.hour = h
        self.finished = f
        self.state = WorkingState()

    def set_state(self, s):
        self.state = s

    def write_program(self):
        self.state.write_program(self)


class State:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write_program(self, w):
        """write program according to workstate"""


class RestState(State):
    def write_program(self, w):
        print str(w.hour) + " : return to rest"


class SleepingState(State):
    def write_program(self, w):
        print str(w.hour)+ " : sleeping"


class OvertimeState(State):
    def write_program(self, w):
        if w.finished is True:
            w.set_state(RestState())
            w.write_program()
        elif w.hour < 21:
            print str(w.hour) + " : overtime"
        else:
            w.set_state(SleepingState())
            w.write_program()


class WorkingState(State):
    def write_program(self, w):
        if w.hour < 17:
            print str(w.hour) + " : working"
        else:
            w.set_state(OvertimeState())
            w.write_program()


if __name__ == "__main__":
    work = Work(15, False)
    work.write_program()

    work = Work(20, False)
    work.write_program()

    work = Work(22, False)
    work.write_program()

    work = Work(20, True)
    work.write_program()