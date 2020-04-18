import time
class Foo:
    def __init__(self):
        self.one = False
        self.two = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.one = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.one:
            time.sleep(0.00001)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.two = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.two:
            time.sleep(0.00001)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()