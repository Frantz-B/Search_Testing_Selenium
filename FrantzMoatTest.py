from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
    
class thisworksbetter(object):
 	"""docstring for thisworksbetter"""
 	def __init__(self, arg):
 		super(thisworksbetter, self).__init__()
 		self.arg = arg
 		 thisworksbetter:
 
    req = Request('http://eatadick')
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print('everything is fine')
        mSearchBox = cdriver.find_element_by_id("pro-landing-search-box")

# sublime added lines 5-9 to when i made the function a class



class shitWorks :

    urlConnect = http.client.HTTPConnection("moat.com")
    urlConnect.request("GET" , "/")
    var = urlConnect.getresponse()
    print (var.status)
    print ('what th ')
    #http: // newtours.demoaut.com / mercuryunderconst.php

# think below was an attempt to strip the beginning of an url because method didn't like it
# so it was a lil annoying

"""urlConnection = http.client.HTTPConnection(mTryLink1.get_attribute('href').lstrip('https://'))
urlConnection.request('GET',"")
print(mTryLink1.get_attribute('href'))
print(mTryLink1.get_attribute('href').lstrip('https://'))
print(urlConnection.getresponse().status)
"""
