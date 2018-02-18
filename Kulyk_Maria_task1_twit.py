import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


def twitter(acct, *argv):
    """
    (str,lst) -> lst
    Receives str account in twitter and returns list of tuples with information
    about followings. In *argv write what additional information except of name
    and location you want to see
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    lst = [(u["screen_name"], (u[i] for i in argv),
            u["location"])for u in js["users"]]
    return lst
