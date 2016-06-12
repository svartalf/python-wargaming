Python Wargaming API client
===========================

Contents:

.. toctree::
    :maxdepth: 2

    exceptions

Available API
=============

    >>> wot = wargaming.WoT('demo', region='ru', language='ru')
    >>> wgn = wargaming.WGN('demo', region='na', language='en')
    >>> wotb = wargaming.WoTB('demo', region='eu', language='pl')
    >>> wows = wargaming.WoWS('demo', region='eu', language='fr')
    >>> wowp = wargaming.WoWP('demo', region='kr', language='ko')


Examples
--------

    >>> wot.ratings.types()
    >>> fronts = wot.globalmap.fronts()
    >>> wot.globalmap.provinces(front_id=fronts[0]['front_id'])

Parameters to API
-----------------

wargaming module maps 1 to 1 as official wargaming API, please consult for parameters on official page:
https://wargaming.net/developers/

Usage and common things
=======================

Region and Language
-------------------

    All API requests should send an ``language`` parameter. But because it is really boring to do it manually,
    you can set a default language for all requests:

    >>> api = wargaming.WoT('demo', region='ru', language='ru')

    +----------------+----------------+------------------------------------------------------+
    + Parameter      | Valid values   | Description                                          |
    +================+================+======================================================+
    + application_id | APPLICATION_ID | Application ID registered on WG developers portal    |
    +----------------+----------------+------------------------------------------------------+
    + region         | - ru           | Wargaming API region                                 |
    +                | - asia         |                                                      |
    +                | - na           |                                                      |
    +                | - eu           |                                                      |
    +                | - kr           |                                                      |
    +----------------+----------------+------------------------------------------------------+
    + language       | - en           | Language available in the region, check info on WG   |
    +                | - ru           | developers portal                                    |
    +                | - pl           |                                                      |
    +                | - de           |                                                      |
    +                | - fr           |                                                      |
    +                | - es           |                                                      |
    +                | - zh-ch        |                                                      |
    +                | - tr           |                                                      |
    +                | - cs           |                                                      |
    +                | - th           |                                                      |
    +                | - vi           |                                                      |
    +                | - ko           |                                                      |
    +----------------+----------------+------------------------------------------------------+

    If you want, you can manually set language for a individual requests:

    >>> api.accounts.list(language='fr')


Parameters conversion
---------------------

    All parameters to endpoint functions should be a keyword arguments. Arguments values are converted to the required format automatically.

    ================== ======================= ============================================================================
    Value type         Converted value type    Example
    ================== ======================= ============================================================================
    list, tuple        string                  ``[1, 2, 3]`` → ``'1,2,3'``
    datetime.datetime  string (ISO format)     ``datetime.datetime(2014, 11, 29, 12, 34, 56)`` → ``'2014-11-29T12:34:56'``
    ================== ======================= ============================================================================


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
