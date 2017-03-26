from itertools import count
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
