# code-packaging-minicourse

Materials related to a mini-course on code development and packaging.

## Table of Contents

* [Logistics](#logistics)
* [Assignments](#assignments)
* [Lecture notes](#lecture-notes)
* [Lecture slides](#lecture-slides)
* [Code package examples](#code-package-examples)

## Logistics

* **Meeting time / room**: Tue/Fri 11:10 - 12:30pm / AB 113; meetings on Feb. 25, Mar. 3, Mar. 10, Mar. 17, and Mar. 24

* **Instructor**: Jo Bovy, AB229

* **Email**: jo - dot - bovy - at - utoronto - dot - ca

* **Syllabus**: Full details can be found in the [syllabus](syllabus/syllabus-codemini.pdf)

## Assignments

* **Assignment 1**: available [here](assignments/assignment1.pdf), due on Mar. 3

* **Assignment 2**: available [here](assignments/assignment2.pdf), due on Mar. 10

* **Assignment 3**: available [here](assignments/assignment3.pdf), due on Mar. 17

* **Assignment 4**: available [here](assignments/assignment4.pdf), due on Mar. 24

## Lecture notes

A set of lecture notes will be sent to students taking the class by email; these will appear here at the end of the class.

## Lecture slides

* **Week 1**: [slides](http://astro.utoronto.ca/~bovy/codepackagingminicourse/L1-codingmini.pdf): course logistics, why packaging and releasing your code, intro to git and GitHub, basic Python structure.

* **Week 2**: [slides](http://astro.utoronto.ca/~bovy/codepackagingminicourse/L2-codingmini.pdf): documentation.

* **Week 3**: [slides](http://astro.utoronto.ca/~bovy/codepackagingminicourse/L3-codingmini.pdf): testing your code, test coverage, continuous integration.

* **Week 4**: [slides](http://astro.utoronto.ca/~bovy/codepackagingminicourse/L4-codingmini.pdf): releasing your package, hosting documentation on readthedocs.io.

* **Week 5**: [slides](http://astro.utoronto.ca/~bovy/codepackagingminicourse/L5-codingmini.pdf): GitHub Actions, badges, C extensions.

## Code package examples

As part of this course, you will develop a scientific software package, learning how to use git/GitHub to host it, how to test and document it, how to use automatic documentation/building/testing tools, how to release the package, and how to deal with issues and pull requests. If you have a software package related to your research, please use this and we can turn it into a full-featured software package. If you do not have a personal software package that you want to use, here are some ideas for simple packages to use for the course's assignments:

* A *cosmological distances package*: create a simple package that computes different cosmological distances for different cosmologies, for example, following [Hogg (1999)](https://arxiv.org/abs/astro-ph/9905116).

* A *cosmology calculator*: similar to the above, but create a Python package that provides similar functionality as [Ned Wright's cosmology calculator](http://www.astro.ucla.edu/~wright/ACC.html).

* A *transit light curve package*: compute the transit lightcurve of an exoplanet orbiting a star, e.g., following [Mandel & Agol (2002)](https://arxiv.org/abs/astro-ph/0210099).

* A *simple stellar model package*: implement the simple polytropic model of stellar structure, computing models for different polytropic indices, following, e.g., [these notes](https://www.astro.princeton.edu/~gk/A403/polytrop.pdf).

* A *simple observation planner*: a package to help plan observations of celestial objects, answering such questions as "When is a target at a given (RA,Dec) best observable from a given location?", "How long is the object in question above the horizon on a given day?", "Which of a given set of observatories is best to observe a target from on a given day (or during a given period)?".

* A *package for inspecting the cosmic history of star formation and stellar mass growth*: implement the results from [Behroozi et al. (2012)](https://arxiv.org/abs/1207.6105), available [at the bottom of this page](https://www.peterbehroozi.com/data.html). For example, implement the stellar-mass vs. halo-mass relations and allow them to be evaluated at any redshift/halo mass using interpolation.

Whichever example you choose or when you bring your own package, it's important that your package implements both classes and functions so we can learn about documentation and testing features for both of these.

