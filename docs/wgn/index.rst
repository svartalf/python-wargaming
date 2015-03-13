Wargaming.NET API
=================

Endpoints
---------

.. toctree::
    :maxdepth: 2

    clans

Examples
--------

    >>> api = wargaming.WGN('demo')
    >>> clans = api.clans.list(search='joker')
