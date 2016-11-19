from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
mURL = 'http://www.moat.com'


cdriver = webdriver.Chrome(chromeDriverLoc)
cdriver.get(mURL)

# captured Web Elements
mSearchBox = cdriver.find_element_by_id("pro-landing-search-box")
mTryLink1 = cdriver.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[1]')
mTryLink2 = cdriver.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[2]')
mTryLink3 = cdriver.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[3]')

# List of captured Try These links
mList = [mTryLink1.text, mTryLink2.text, mTryLink3.text]
mList2 = [mTryLink1.text, mTryLink2.text, mTryLink3.text]

def somehit(caplist , othlist):
    #caplist = mList
    print(caplist, othlist)
somehit(mList , mList2)
print(mTryLink2 , " ", mTryLink1)

def verifyRandom(tryTheseList):
    cdriver.refresh()

    mTryLinkRefresh1 = cdriver.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[1]')
    mTryLinkRefresh2 = cdriver.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[2]')
    mTryLinkRefresh3 = cdriver.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[2]')
    mList2 = [mTryLinkRefresh1.text, mTryLinkRefresh2.text, mTryLinkRefresh3.text]
    list(set(tryTheseList) & set(mList2))
    if not list:
        print('Random Function:  PASSED')
    else:
        print('Random Function:  FAILED')

mList3 = [mTryLink4.text, mTryLink5.text]
mList4 = [mTryLink4.text, mTryLink5.text]
somehit(mList3 , mList4)
print(mTryLink5 , " ", mTryLink4)
