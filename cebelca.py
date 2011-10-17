import urllib
import random

class Cebelca(object): 
    def __init__(self, api_key):
        self.api_key = api_key
    
    def call(self, params={}, **kwargs):
        r = kwargs.pop('r')
        m = kwargs.pop('m')
        result = urllib.urlopen("https://%s:%s@www.cebelca.biz/API?_r=%s&_m=%s" % (self.api_key, 'x', r, m), data=urllib.urlencode(params)).read()
        return result


if __name__ == '__main__':
    ceb = Cebelca("mezdtys5n961gtvh2roac4ue37fafg1skawjccbq")
    name = "Test Company #%s" % random.randint(1, 1000000)
    r = ceb.call(r='partner', m='assure', params=dict(name=name, street="Neverhood Street 42", postal="E1w201", city="London"))
    print r

