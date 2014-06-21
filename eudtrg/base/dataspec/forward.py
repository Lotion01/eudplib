'''
Forward declaration class Forward
'''

from eudtrg import LICENSE #@UnusedImport

from .expr import Expr, Evaluate, GetCacheToken

class Forward(Expr):
    '''
    ex)

    a = Trigger( nextptr = b ) # Error : b is not defined
    b = Trigger( nextptr = a ) 

    ->

    b = Forward() # Forward declaration
    a = Trigger( nextptr = b )
    b << Trigger( nextptr = a ) # put in value later.

    '''

    def __init__(self):
        super().__init__()
        self.target = None
        self._ct = None

    def __lshift__(self, item):
        assert isinstance(item, Expr), 'Non-expr types cannot be assigned to Forward object.'
        assert self.target == None, 'Duplicate assignment'
        self.target = item
        return item

    def GetDependencyList(self):
        return [self.target]

    def Evaluate(self): # Internally used.
        assert self.target is not None, 'Forward() not initalized'
        ct = GetCacheToken()
        if ct is not self._ct:
            self._ct = ct
            self._cache = Evaluate(self.target)

        return self._cache

