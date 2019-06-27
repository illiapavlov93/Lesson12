import contextlib
import time


@contextlib.contextmanager
def time_print(task_name):
    t = time.time()
    try:
        yield
    finally:
        print(task_name, "took", time.time() - t, "seconds")


with time_print("some task"):
    a = [lambda x: x * x for x in range(10_000_000)]

