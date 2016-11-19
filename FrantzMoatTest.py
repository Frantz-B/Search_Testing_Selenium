import http.client

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