import abc
"""
解释器模式
模式特点：给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

程序实例：（只是模式特点的最简单示范）

代码特点：无
"""


class Context(object):
    def __init__(self, t):
        self.text = t


class Expression(object):
    def interpret(self, c):
        text = c.text.split(' ')
        key = text[0]
        value = float(text[1])
        c.text = ' '.join(text[2:])
        self.execute(key, value)

    @abc.abstractmethod
    def execute(self, k, v):
        pass


class Scale(Expression):
    def execute(self, k, v):
        scale_dic = {1: 'bass', 2: 'alto', 3: 'treble'}
        print scale_dic[v] + " ",


class Note(Expression):
    def execute(self, k, v):
        print k + " ",


class ExpressionFactory(object):
    @staticmethod
    def create_expression(t):
        type = "Scale" if t == 'O' else "Note"
        obj = globals()[type]()
        return obj


if __name__ == "__main__":
    context = Context("O 2 E 0.5 G 0.5 A 3")
    while len(context.text):
        expression = ExpressionFactory.create_expression(context.text[0])
        expression.interpret(context)

