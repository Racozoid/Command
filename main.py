from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    # Интерфейс Команды
    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    # Простая команда
    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f"Oh, I'm so simple. I can print some things!"
              f"({self._payload})")


class ComplexCommand(Command):
    # Команда которая взаимодействует с другими классами
    def __init__(self, receiver: Receiver, a, b):
        self.receiver = receiver    # Используем класс получатель
        self.a = a
        self.b = b

    def execute(self):
        # Используем методы получателя
        print("Hello! I can do more expensive things. Like this:")
        self.receiver.do_something(self.a)
        self.receiver.do_something_else(self.b)


class Receiver:
    # Класс получатель
    def do_something(self, a):
        print(f"Wow! print some your staff -- {a}")

    def do_something_else(self, b):
        print(f"Or print this -- {b}")


class Invoker:
    # Отправитель -- отправляет запрос командам
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: What joy it is beholding me!")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: Enlightenment is mine!")

        print("Invoker: So begins a new age of knowledge.")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


invoker = Invoker()
invoker.set_on_start(SimpleCommand("Hello my dear friend!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(receiver, "Carl!", "John!"))

invoker.do_something_important()
input()
