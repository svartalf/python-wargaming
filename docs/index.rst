Python Wargaming API client
===========================

Contents:

.. toctree::
    :maxdepth: 2

    wot/index
    wgn/index
    wotb/index

    exceptions

Usage and common things
=======================

Language
--------

    All API requests should send an ``language`` parameter. But because it is really boring to do it manually,
    you can set a default language for all requests:

    >>> api = wargaming.WoT('demo', language='ru')

    If you want, you can manually set language for a individual requests:

    >>> api.accounts.list(language='fr')

Parameters
----------

    All parameters to endpoint functions should be a keyword arguments. Arguments values are converted to the required format automatically.

    ================== ======================= ============================================================================
    Value type         Converted value type    Example
    ================== ======================= ============================================================================
    bool               int                     ``False`` → ``0``, ``True`` → ``1``
    list, tuple        string                  ``[1, 2, 3]`` → ``'1,2,3'``
    datetime.date      string (ISO format)     ``datetime.date(2014, 11, 26)`` → ``'2014-11-29'``
    datetime.datetime  string (ISO format)     ``datetime.datetime(2014, 11, 29, 12, 34, 56)`` → ``'2014-11-29T12:34:56'``
    ================== ======================= ============================================================================


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
