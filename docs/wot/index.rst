World of Tanks
==============

.. autoclass:: wargaming.games.wot.API(application_id[, language='en'])

    .. attention::
        You should import that class as ``wargaming.WoT``, not a ``wargaming.games.wot.API``.

        Sorry, documentation paths problem :)

    Main API class have a bucket of namespace-like attributes, which are
    contains all required endpoint methods.

    Check for an example:

    >>> api = wargaming.WoT('demo')
    >>> api.accounts.list(search='batman')

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
