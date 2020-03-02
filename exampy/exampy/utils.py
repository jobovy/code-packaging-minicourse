def square(x):
    """The square of a number

Parameters
----------
x: float
    Number to square

Returns
-------
float
    Square of x
"""
    return x**2.

def pow(x,p=2.):
    """A number x raised to the p-th power

Parameters
----------
x: float
    Number to raise to the power p
p: float, optional
    Power to raise x to

Returns
-------
float
    x^p
"""
    return x**p

class PowClass(object):
    """A class to compute the power of a number"""
    def __init__(self,p=2.):
        """Initialize a PowClass instance

Parameters
----------
p: float, optional
    Power to raise x to
"""
        self._p= p

    def __call__(self,x):
        """Evaluate x^p

Parameters
----------
x: float
    Number to raise to the power p

Returns
-------
float
    x^p
"""
        return x**self._p
