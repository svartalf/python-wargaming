#!/usr/bin/env python3

import requests
import json


def get(path):
    return requests.get(
        'https://developers.wargaming.net/api/%s/?realm=all' % path,
        headers={'X-Requested-With': 'XMLHttpRequest'}
    ).json()


def main():
    games = get('methods')['data']
    for game_data in games:
        wg_section_slug = game_data['slug']
        schema = {}

        for section in game_data['sections']:
            section_name = section['slug']
            schema[section_name] = {}

            for method in section['methods']:
                print("Working on %s" % method['key'])
                method_data = get('methods/%s' % method['key'])['data']

                schema[section_name][method['slug']] = method_data

        with open("%s-schema.json" % wg_section_slug, 'w') as f:
            f.write(json.dumps(schema, sort_keys=True, indent=4, separators=(',', ': ')))


if __name__ == '__main__':
    main()
