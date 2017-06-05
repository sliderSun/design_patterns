# _*_coding: utf-8 _*_

"""
假定现在有一个任务，需要你找到一个有效的方法合并两个做不同事情的类，
在已有系统中这两个类在许多不同的地方被大量使用，所以移除这两个类或
是改动已有的代码都是异常困难的。不仅如此，更改已有的代码会导致大量
的测试工作，因为在这样一种依赖大量不同组件的系统中，这些修改总是会
引入一些新的错误。为了避免这些麻烦，你可以实现一个策略模式
(Strategy Pattern)和适配器模式(Adapter Pattern)的变体，这两种模式能
够很好的处理这种问题。
"""
class StrategyAndAdapterExampleClass(object):
 
    def __init__(self, context, class_one, class_two):
        self.context = context
        self.class_one = class_one
        self.class_two = class_two
 
    def operation1(self):
        if self.context == "Context_For_Class_One":
            self.class_one.operation1_in_class_one_context()
        else:
            self.class_two.operational_in_class_two_context()