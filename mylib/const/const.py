class _const:
    '''This is a class that implements a constant '''
    class ConstError(TypeError): pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)!!!" % key)
        else:
            self.__dict__[key] = value

    def __delattr__(self, item):
        raise self.ConstError("Can't unbind const(%s)!!!" % item)


import sys

sys.modules[__name__] = _const()
