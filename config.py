CSRF_ENABLE = True
SECRET_KEY = "baoliwen"

OPENID_PROVIDERS = [
    { 'name': 'Baidu', 'url': 'https://www.baidu.com' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
