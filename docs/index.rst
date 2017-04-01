Python Wargaming API client
===========================

Contents:

.. toctree::
    :maxdepth: 2

    index
    exceptions

Available API
=============

.. code-block:: python

    import wargaming

    # World of Tanks
    wot = wargaming.WoT('demo', region='ru', language='ru')
    # Wargaming NET
    wgn = wargaming.WGN('demo', region='na', language='en')
    # World of Tanks Blitz
    wotb = wargaming.WoTB('demo', region='eu', language='pl')
    # World of Warships
    wows = wargaming.WoWS('demo', region='eu', language='fr')
    # World of Warplanes
    wowp = wargaming.WoWP('demo', region='eu', language='en')
    # World of Tanks XBox
    wot_xbox = wargaming.WoTX('demo', region='xbox', language='ru')
    # World of Tanks Playstation 4
    wot_ps4 = wargaming.WoTX('demo', region='ps4', language='ru')


Examples
--------

.. code-block:: python

    from itertools  import count
    import wargaming

    wot = wargaming.WoT('demo', region='ru', language='ru')


    def list_all_provinces():
        """List provinces from all fronts using WG Public API"""

        # get fronts list
        fronts = wot.globalmap.fronts()

        # iterate through fronts
        for front in fronts:
            # provinces method return no more than 100 provinces per page,
            # adding pagination iteration
            for page_no in count(start=1):
                # provinces method require 2 parameters - front_id and page_no
                provinces = wot.globalmap.provinces(front_id=front['front_id'], page_no=page_no)

                # if no provinces on this page, then we got all provinces on the front
                if len(provinces) == 0:
                    break

                # iterate through provinces list
                for province in provinces:
                    print(province['province_name'])


    try:
        list_all_provinces()
    except wargaming.exceptions.RequestError as e:
        if e.code == 407:  # REQUEST_LIMIT_EXCEEDED
            print("ERROR: You should register your own API key and not use 'demo' key")
        else:
            print("Unknown error %s" % repr(e))


Parameters to API
-----------------

wargaming module maps 1 to 1 as official wargaming API, please consult for parameters on official page:
https://developers.wargaming.net/reference/

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
    + application_id | demo           | Application ID registered on WG developers portal    |
    +----------------+----------------+------------------------------------------------------+
    + region         | - ru           | Wargaming API region                                 |
    +                | - asia         |                                                      |
    +                | - na           |                                                      |
    +                | - eu           |                                                      |
    +                | - xbox         |                                                      |
    +                | - ps4          |                                                      |
    +----------------+----------------+------------------------------------------------------+
    + language       | - en           | Language available in the region, check info on WG   |
    +                | - ru           |                                                      |
    +                | - pl           | developers portal                                    |
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

    If needed, language can be specified for an individual requests:

    >>> wot.encyclopedia.achievements(language='pl')['crucialShotMedal']['description']


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
