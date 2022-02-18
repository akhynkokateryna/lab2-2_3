"twitter2.py"

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_data(acct):

    "Gets data from Twitter"

    while True:

        if len(acct) < 1:
            break
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': '5'})

        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        js = json.loads(data)
        # return json.dumps(js, indent=2)
        return js

        # print(dataset)

        # headers = dict(connection.getheaders())
        # print('Remaining', headers['x-rate-limit-remaining'])

        # for u in js['users']:
        #     print(u['screen_name'])
        #     if 'status' not in u:
        #         print('   * No status found')
        #         continue
        #     s = u['status']['text']
        #     print('  ', s[:50])
