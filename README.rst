Python library for Wargaming.net API
====================================

Pure pythonic library for accessing Wargaming.net API (https://wargaming.net/developers/).

Compatible with a Python>=2.6 and Python 3 versions. PyPy also!

.. image:: https://travis-ci.org/svartalf/python-wargaming.svg?branch=master
.. image:: https://readthedocs.org/projects/python-wargaming/badge/?version=latest
.. image:: https://badge.fury.io/py/wargaming.svg

Installation
------------

As simple as usual:

    $ pip install wargaming

Documentation
-------------

Wargaming.NET API documentation: https://na.wargaming.net/developers/api_reference/

Library documentation: http://python-wargaming.rtfd.org

Supported games
---------------

 * World of Tanks
 * World of Tanks Blitz
 * Wargaming.NET common API (partially)


Contribution
------------

Just fork, update and send pull request. Do not forget to run tests:

    $ tox

Also check for a PEP-0008 compliance:

    $ pep8 --ignore=E501,E128 wargaming/
