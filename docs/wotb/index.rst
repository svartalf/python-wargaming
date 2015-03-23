World of Tanks Blitz
====================

.. autoclass:: wargaming.games.wotb.API(application_id[, language='en'])

    .. attention::
        You should import that class as ``wargaming.WoTB``, not a ``wargaming.games.wot.API``.

        Sorry, documentation paths problem :)


Examples
--------

    Main API class have a bucket of namespace-like attributes, which are
    contains all required endpoint methods.

    Check for an examples:

    >>> api = wargaming.WoTB('demo')
    >>> batmans = api.accounts.list(search='batman')


Endpoints
---------

.. toctree::
    :maxdepth: 2

    accounts
    encyclopedia
    tanks
