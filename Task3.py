import sys
import datetime


class ContextDecorator(object):
    def __init__(self, *args):
        self.start_time = None
        self.finish_time = None
        self.args = args
        print("init")

    def __call__(self, f):
        def wrapper(*args):
            self.__enter__()
            exc_type, exc_val, exc_tb = (None,) * 3
            try:
                f(*args)
            except:
                exc_type, exc_val, exc_tb = sys.exc_info()
            self.__exit__(exc_type, exc_val, exc_tb)

        return wrapper

    def __enter__(self):
        self.start_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = datetime.datetime.now()
        print('spend time: {}'.format(self.finish_time - self.start_time))

# @ContextDecorator()
def div_try(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

# @ContextDecorator()
def div_if(a, b):
    if b != 0:
        return a / b
    else:
        return 0


# div_try(100, 0)
# div_if(100, 0)


for func in [div_try, div_if]:
    print('{} use time'.format(func))
    with ContextDecorator():
        for i in range(10_000_000):
            if i % 2 == 0:
                func(i, i * 0)
            else:
                func(i, i * 2)

