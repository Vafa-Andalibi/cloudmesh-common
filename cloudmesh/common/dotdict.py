# noinspection PyPep8Naming
class dotdict(dict):
    """
    A convenient dot dict class::

        a = dotdict({"argument": "value"})

    print (a.argument)

    Nested dot documentation is not supported.
    """

    def __getattr__(self, attr):
        return self.get(attr)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
