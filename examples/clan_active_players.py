import wargaming
from datetime import datetime, timedelta

# enable_parser enables timestamp fields from WG API converted to
# datetime object in python.
wot = wargaming.WoT('demo', language='ru', region='ru', enable_parser=True)
wgn = wargaming.WGN('demo', language='ru', region='ru')


def show_clan_activity(clan_tag):
    clan = wgn.clans.list(search=clan_tag)[0]
    clan_id = str(clan['clan_id'])
    clan_info = wgn.clans.info(clan_id=clan['clan_id'])[clan_id]
    members_ids = [i['account_id'] for i in clan_info['members']]
    accounts = wot.account.info(account_id=members_ids)
    now = datetime.now()
    stats = {
        i: filter(lambda p: p['last_battle_time'] > now - timedelta(days=i), accounts.values())
        for i in [1, 7, 30, 180]
    }

    total_accounts = len(accounts)
    print("Players in clan '%s': %s" % (clan_tag, total_accounts))
    for i in sorted(stats):
        print("Players played in last %s days: %s (%0.2f%%)" % (
            i, len(stats[i]), 100. * len(stats[i]) / total_accounts))
