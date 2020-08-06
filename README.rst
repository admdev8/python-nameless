========
Overview
========

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install nameless

You can also install the in-development version with::

    pip install git+ssh://git@no/ionelmc/python-nameless.git@master

Documentation
=============


To use the project:

.. code-block:: python

    import nameless
    nameless.longest()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
