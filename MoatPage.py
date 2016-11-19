#Location of elements on main page (moat.com)
mSearchBox = "pro-landing-search-box"  #ID of search box
tryTheseLink1 = '//*[@id="search-bar"]/div/div[1]/span/a[1]'
tryTheseLink2 = '//*[@id="search-bar"]/div/div[1]/span/a[2]'
tryTheseLink3 = '//*[@id="search-bar"]/div/div[1]/span/a[3]'
recentAds1 = '//*[@id="search-bar"]/div/div[2]/ul/li[1]/h4'
recentAds2 = '//*[@id="search-bar"]/div/div[2]/ul/li[2]/h4'
recentAds3 = '//*[@id="search-bar"]/div/div[2]/ul/li[3]/h4'
recentAds4 = '//*[@id="search-bar"]/div/div[2]/ul/li[4]/h4'

#Location of elements on search results page
allegedSiteCreativeCount = '//*[@id="comp-header"]/div[1]/div[2]/span'
popupCreativeLoc = '//*[@id="popup-template"]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/a'
popupCreativeLinkLoc = '//*[@id="popup-template"]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/div/input'

# capturing Web Elements
def tryTheseTextListCapture(self):
    'Intended to capture list of Try These link Texts from Moat main page'
    mTryText1 = self.cdriver.find_element_by_xpath(tryTheseLink1).text
    mTryText2 = self.cdriver.find_element_by_xpath(tryTheseLink2).text
    mTryText3 = self.cdriver.find_element_by_xpath(tryTheseLink3).text
    mListTexts = [mTryText1, mTryText2, mTryText3]
    return mListTexts

def tryTheseLinkListCaputure(self):
    'Intended to capture list of Try These Links from Moat main page'
    mTryLink1 = self.cdriver.find_element_by_xpath(tryTheseLink1).get_attribute('href')
    mTryLink2 = self.cdriver.find_element_by_xpath(tryTheseLink2).get_attribute('href')
    mTryLink3 = self.cdriver.find_element_by_xpath(tryTheseLink3).get_attribute('href')
    mListLnks = [mTryLink1, mTryLink2, mTryLink3]
    return mListLnks

def recentAdDisplayTimeCapture(self):
    'Intended to capture list of Recently Seen Ad Times from Moat main page'
    recentAdsEle1 = self.cdriver.find_element_by_xpath(recentAds1).text
    recentAdsEle2 = self.cdriver.find_element_by_xpath(recentAds2).text
    recentAdsEle3 = self.cdriver.find_element_by_xpath(recentAds3).text
    recentAdsEle4 = self.cdriver.find_element_by_xpath(recentAds4).text
    mRecentAdList = [recentAdsEle1, recentAdsEle2, recentAdsEle3, recentAdsEle4]
    return mRecentAdList
