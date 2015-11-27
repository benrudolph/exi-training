from requests.auth import AuthBase
from base64 import b64encode


class HQAuth(AuthBase):
    def __init__(self, username, apikey):
        self.username = username
        self.apikey = apikey

    def __call__(self, r):
        r.headers['Authorization'] = 'apikey ' + '%s:%s' % (self.username, self.apikey)
        return r
