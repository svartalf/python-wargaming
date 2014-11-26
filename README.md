# Python library for Wargaming.net API

Pure pythonic library for accessing Wargaming.net API (https://wargaming.net/developers/).

Compatible with a Python>=2.6 and Python 3 versions. PyPy also!

[![Build Status](https://travis-ci.org/svartalf/python-wargaming.svg?branch=master)](https://travis-ci.org/svartalf/python-wargaming)
[![Documentation Status](https://readthedocs.org/projects/python-wargaming/badge/?version=latest)](https://readthedocs.org/projects/python-wargaming/?badge=latest)
[![PyPI version](https://badge.fury.io/py/wargaming.svg)](http://badge.fury.io/py/wargaming)

## Installation

As simple as usual:

    $ pip install wargaming

## Usage

### World of Tanks

    from wargaming import WoT
    api = WoT('your-application-id', language='ru')
    
    me_and_my_buddy = api.accounts.info(account_id=[1000000001, 1000000002],
        fields=['nickname', 'client_language'], language='ru')

    our_clan = api.clans.info(clan_id=1000000003)

### World of Warplanes

Not available right now, still WIP. Sorry ;) But you can contribute!

## Contribution

Just fork, update and send pull request. Do not forget to run tests:

    $ tox

Also check for a PEP-0008 compliance:

    $ pep8 --ignore=E501,E128 wargaming/
