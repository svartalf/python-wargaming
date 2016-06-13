#!/usr/bin/env python3

from collections import defaultdict
from lxml import html
import requests
import json


def get_func(url):
    print(url)
    fields = {}

    resp = requests.get(url)
    parsed_body = html.fromstring(resp.text)
    main_content = parsed_body.xpath("//div[@class='b-maincontent clearfix js-maincontent']")[0]

    objects = [
        i for i in main_content.iterchildren()
        if i.tag == 'div' and 'b-alert' not in i.classes
    ]

    description = objects[0]
    params = None
    for obj in objects:
        if obj.get('id') == 'parameters_block':
            params = obj

    fields['__doc__'] = description.text_content().strip()

    if params is None:
        print("Unable to find parameters_block")
        return fields

    for tr in params.findall('table/tbody/'):
        items = [td.text_content().strip() for td in tr]
        if len(items) != 3:
            print("Incorrect row: ", items)
            continue

        if items[0].startswith('*'):
            items[0] = items[0][1:]
            required = True
        else:
            required = False

        fields[items[0]] = {
            'type': items[1],
            'doc': items[2],
            'required': required,
        }
    return fields


def main():
    base_url = 'https://eu.wargaming.net/developers/api_reference'
    resp = requests.get(base_url)
    for wg_section in ['wot', 'wotb', 'wowp', 'wows', 'wgn']:
        parsed_body = html.fromstring(resp.text)
        section_url = '/developers/api_reference/%s/' % wg_section
        l = len(section_url)
        # length > 30 means that link is not to wg_section
        urls = [i[2][l:-1] for i in parsed_body.iterlinks()
                if i[2].startswith(section_url) and len(i[2]) > l]

        schema = defaultdict(lambda: dict())

        for url in urls:
            print("Working on " + url)
            module, function = url.split('/')
            schema[module][function] = get_func('%s/%s/%s/' % (base_url, wg_section, url))

        with open("%s-schema.json" % wg_section, 'w') as f:
            f.write(json.dumps(schema, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == '__main__':
    main()
