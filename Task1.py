import datetime


class MyErrorException(Exception):
    def __init__(self, msg=None, fpath='logs.log'):
        self.fpath = fpath
        self.msg = msg

    def log_to_file(self):
        with open(self.fpath, 'a') as log_file:
            log_file.write(
                "{}: Error happens! msg: [{}]\n".format(
                    datetime.datetime.now(), self.msg
                )
            )


def my_function(*args):
    print(('myfunction with args: <{}>'.format(args)))
    raise MyErrorException(msg='test MyErrorException')


try:
    my_function(23, 'spam', {'eggs'})
except MyErrorException as e:
    e.log_to_file()
