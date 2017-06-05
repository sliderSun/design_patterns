"""
备忘录模式
模式特点：在不破坏封装性的前提下捕获一个对象的内部状态，并在该对象之外保存这个状态，以后可以将对象恢复到这个状态。

程序实例：将Originator对象的状态封装成Memo对象保存在Caretaker内

代码特点：无
"""

class StateMemento(object):
    def __init__(self, h, m):
        self.hp = h
        self.mp = m


class GameRole(object):
    def __init__(self):
        self.hp = 100
        self.mp = 100

    def fight(self):
        self.hp = 0
        self.mp = 0

    def create_memento(self):
        return StateMemento(self.hp, self.mp)

    def recovery_state(self, m):
        self.hp = m.hp
        self.mp = m.mp

    def state_display(self):
        print str(self.hp) + " " + str(self.mp)


class StateCaretaker(object):
    def __init__(self, m):
        self.__memento = m  # .__memento ==> ._StateCaretaker__memento (Name Mangling)

    def get_memento(self):
        return self.__memento


if __name__ == "__main__":
    game_role = GameRole()
    state_caretaker = StateCaretaker(game_role.create_memento())
    game_role.state_display()

    game_role.fight()
    game_role.state_display()

    game_role.recovery_state(state_caretaker.get_memento())
    game_role.state_display()