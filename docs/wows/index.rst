World of Warships
=================

.. autoclass:: wargaming.games.wows.API(application_id[, language='en'])

    .. attention::
        You should import that class as ``wargaming.WoWS``, not a ``wargaming.games.wows.API``.

        Sorry, documentation paths problem :)


Examples
--------

    Main API class have a bucket of namespace-like attributes, which are
    contains all required endpoint methods.

    Check for an examples:

    >>> api = wargaming.WoWS('demo')
    >>> batmans = api.accounts.list(search='batman')


Endpoints
---------

.. toctree::
    :maxdepth: 2

    accounts
    encyclopedia
    ships
