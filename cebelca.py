"""
curl -v -k -u mezdtys5n961gtvh2roac4ue37fafg1skawjccbq:x -d "name=My Company&street=Downing street&postal=E1w201&city=London" "https://www.cebelca.biz/API?_r=partner&_m=assure"
"""

import urllib
import random

class Cebelca(object):
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def call(self, **kwargs):
        r = kwargs.pop('_r')
        m = kwargs.pop('_m')
        result = urllib.urlopen("https://%s:%s@www.cebelca.biz/API?_r=%s&_m=%s" % (self.api_key, 'x', r, m), data=urllib.urlencode(kwargs)).read()
        return result


if __name__ == '__main__':
    ceb = Cebelca("mezdtys5n961gtvh2roac4ue37fafg1skawjccbq")
    name = "Test Company #%s" % random.randint(1, 1000000)
    r = ceb.call(_r='partner', _m='assure', name=name, street="Neverhood Street 42", postal="E1w201", city="London")
    print r

