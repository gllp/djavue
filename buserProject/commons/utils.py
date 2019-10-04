import hashlib


def gravatar_url(email):
    _hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/%s?d=identicon&s=50' % _hash
