Introduction
============

``exampy`` is an example Python package that contains some very basic math
functions. As an example, we can compute the square of a number as::

	   >>> import exampy
	   >>> exampy.square(3.)
	   # 9.

Similarly, we can compute the cube of a number, but this functionality is part
of the ``exampy.submodule1`` submodule:

.. code-block:: python

   >>> import exampy.submodule1
   >>> exampy.submodule1.cube(3.)
   # 27.

A general power function ``pow`` is included at the top-level, for example, to
get the fourth power of 3, do::

    >>> exampy.pow(3.,p=4.)
    # 81.

This concludes the discussion of all of ``exampy``'s basic
functionality.