World of Tanks
==============

.. autoclass:: wargaming.games.wot.API(application_id[, language='en'])

    .. attention::
        You should import that class as ``wargaming.WoT``, not a ``wargaming.games.wot.API``.

        Sorry, documentation paths problem :)


Examples
--------

    Main API class have a bucket of namespace-like attributes, which are
    contains all required endpoint methods.

    Check for an examples:

    >>> api = wargaming.WoT('demo')
    >>> batmans = api.accounts.list(search='batman')
    >>> top_clans = api.clans.top()


Endpoints
---------

.. toctree::
    :maxdepth: 2

    accounts
    auth
    clans
    encyclopedia
    globalwar
    ratings
    clan_ratings
    tanks
