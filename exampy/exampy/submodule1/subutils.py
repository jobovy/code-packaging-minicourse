def cube(x):
    """The cube of a number

Calculates and returns the cube of any floating-point number;
note that, as currently written, the function also works for
arrays of floats, ints, arrays of ints, and more generally,
any number or array of numbers.

Parameters
----------
x: float
    Number to cube

Returns
-------
float
    Cube of x

Raises
------
No exceptions are raised.

See Also
--------
exampy.square: Square of a number
exampy.pow: a number raised to an arbitrary power

Notes
-----
Implements the standard cube function

.. math:: f(x) = x^3

History:

2020-03-01: First implementation - Bovy (UofT)


References
----------
.. [1] A. Mathematician, "x to the p-th power: squares, cubes, and their 
   general form," J. Basic Math., vol. 2, pp. 2-3, 1864.

"""
    return x**3
