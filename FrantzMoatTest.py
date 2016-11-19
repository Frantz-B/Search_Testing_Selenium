from selenium import webdriver
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
mURL = 'http://www.moat.com'
mSearchTerm = 'shit'  # comet yields neg result

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
def tryTheseTextListCapture():
    'Intended to capture list of Try These link Texts from Moat main page'
    mTryText1 = cdriver.find_element_by_xpath(tryTheseLink1).text
    mTryText2 = cdriver.find_element_by_xpath(tryTheseLink2).text
    mTryText3 = cdriver.find_element_by_xpath(tryTheseLink3).text
    mListTexts = [mTryText1, mTryText2, mTryText3]
    return mListTexts

def tryTheseLinkListCaputure():
    'Intended to capture list of Try These Links from Moat main page'
    mTryLink1 = cdriver.find_element_by_xpath(tryTheseLink1).get_attribute('href')
    mTryLink2 = cdriver.find_element_by_xpath(tryTheseLink2).get_attribute('href')
    mTryLink3 = cdriver.find_element_by_xpath(tryTheseLink3).get_attribute('href')
    mListLnks = [mTryLink1, mTryLink2, mTryLink3]
    return mListLnks

def recentAdDisplayTimeCapture():
    'Intended to capture list of Recently Seen Ad Times from Moat main page'
    recentAdsEle1 = cdriver.find_element_by_xpath(recentAds1).text
    recentAdsEle2 = cdriver.find_element_by_xpath(recentAds2).text
    recentAdsEle3 = cdriver.find_element_by_xpath(recentAds3).text
    recentAdsEle4 = cdriver.find_element_by_xpath(recentAds4).text
    mRecentAdList = [recentAdsEle1, recentAdsEle2, recentAdsEle3, recentAdsEle4]
    return mRecentAdList

# Functions that answers Moat Automation test
def verifyRandom():
    "Verifies list of Try These links are different from New list of links"
    mList1 = tryTheseTextListCapture()
    cdriver.refresh()
    #Grabing New set of 'Try These' links
    mList2 = tryTheseTextListCapture()
    if not list(set(mList1) & set(mList2)):
        print('Random Function:  PASSED')
    else:
        print('Random Function:  FAILED')

def verifyWorkingLnks():
    "Verifies each Try These link are can load a successful page. (http response = 200)"
    lnksList = tryTheseLinkListCaputure()
    count = 0
    for lnk in lnksList:
        req = Request(lnk)
        try:
            urlopen(req)
        except HTTPError as e:
            print('Link Validation Function FAILED with following lnk: ', lnk, ' Status code given: ', e.code)
        else:
            count += 1
            if count == 3 :
                print('Link Validation Function:  PASSED')

def verifyRecentAdTime():
    'Verifies list of Recently Seen Ads displayed are less than 30mins fresh'
    recentAdverList = recentAdDisplayTimeCapture()
    count = 0
    for recentAd in recentAdverList :
        rAdList = recentAd.split()
        rNumber = float(rAdList[0])
        if (any('min' in partial for partial in rAdList)) & (rNumber < 30) : count += 1
        elif (any('sec' in partial for partial in rAdList)) & (rNumber < 60*30) : count += 1
        elif (any('hour' in partial for partial in rAdList)) & (rNumber < 0.5): count += 1
    if count == 4 : print("Recently Seen Ads Function:  PASSED")
    else: print("Recently Seen Ads Function:  FAILED")

def verifySearchResultsAdCount(searchTerm):
    'Verifies number of Ads displayed matches the count listed at top of Search Results'
    cdriver.find_element_by_id(mSearchBox).send_keys(searchTerm + Keys.RETURN)
    time.sleep(2)

    creativeCount = cdriver.find_element_by_xpath(allegedSiteCreativeCount).text
    creativeCountList = creativeCount.split()
    creativeCountNum = int(creativeCountList[0])
    loadMeBtn = cdriver.find_element_by_id("paginate-button")
    while loadMeBtn.is_displayed():
        loadMeBtn.click()
        time.sleep(4)
    creativesListDisplayed = cdriver.find_elements_by_class_name('ad-cell')
    print()
    if len(creativesListDisplayed) == creativeCountNum : print('Search Results Ad Count Function:  PASSED')
    else : print('Search Results Ad Count:  FAILED')

def verifyShareAd(searchTerm):
    'Verifies Share Ad feature works by being able to view the link of current creative'
    cdriver.get(mURL)
    cdriver.find_element_by_id(mSearchBox).send_keys(searchTerm + Keys.RETURN)
    time.sleep(2)

    creativesListDisplayed = cdriver.find_element_by_class_name('ad-cell')
    mousehover = ActionChains(cdriver).move_to_element(creativesListDisplayed)
    mousehover.perform()
    time.sleep(2)
    popupCreative = cdriver.find_element_by_xpath(popupCreativeLoc)
    popupCreative.click()
    popupCreativeLink = cdriver.find_element_by_xpath(popupCreativeLinkLoc)

    if popupCreativeLink.is_displayed() : print("Share This Ad Function:  PASSED")
    else : print('Share This Ad Function:  FAILED')

cdriver = webdriver.Chrome(chromeDriverLoc)
cdriver.get(mURL)

verifyRandom()
verifyWorkingLnks()
verifyRecentAdTime()
verifySearchResultsAdCount(mSearchTerm)
verifyShareAd(mSearchTerm)

#cdriver.quit()  pg 246 in Python pdf book