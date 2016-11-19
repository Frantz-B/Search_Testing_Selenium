import unittest
import MoatPage
from selenium import webdriver
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
mURL = 'http://www.moat.com'
mSearchTerm = 'Batman live'

class FrantzMoatTest(unittest.TestCase):

    def setUp(self):
        self.cdriver = webdriver.Chrome(chromeDriverLoc)
        self.cdriver.get(mURL)

    def test_1a_Verify_Try_These_List_are_Random(self):
        mPage =  MoatPage
        mList1 = mPage.tryTheseTextListCapture(self)
        self.cdriver.refresh()
        # Grabing New set of 'Try These' links
        mList2 = mPage.tryTheseTextListCapture(self)
        self.assertFalse((list(set(mList1) & set(mList2))), 'Match Found in Try These List')

    def test_1b_Verify_Try_These_Links_are_Working(self):
        #Verifies each Try These link are can load a successful page. (i.e. http response = 200)
        mPage =  MoatPage
        lnksList = mPage.tryTheseLinkListCaputure(self)
        count = 0
        for lnk in lnksList:
            req = Request(lnk)
            try:
                urlopen(req)
            except HTTPError as e:
                print('Link Validation Function FAILED with following lnk: ', lnk, ' Status code given: ', e.code)
            else:
                count += 1
        self.assertEqual(count, 3, 'Broken Link Found')

    def test_2_Verify_Recent_Seen_Ads_Less_30min_fresh(self):
        #Verifies list of Recently Seen Ads displayed are less than 30mins fresh
        mPage =  MoatPage
        recentAdverList = mPage.recentAdDisplayTimeCapture(self)
        count = 0
        for recentAd in recentAdverList:
            rAdList = recentAd.split()
            rNumber = float(rAdList[0])
            if (any('min' in partial for partial in rAdList)) & (rNumber < 30):
                count += 1
            elif (any('sec' in partial for partial in rAdList)) & (rNumber < 60 * 30):
                count += 1
            elif (any('hour' in partial for partial in rAdList)) & (rNumber < 0.5):
                count += 1
        self.assertEqual(count, 4, 'Ad over 30mins Found')

    def test_3_Verify_SiteAdCount_matches_AcutalAdCount(self):
        #Verifies number of Ads displayed matches the count listed at top of Search Results
        mPage =  MoatPage
        self.cdriver.find_element_by_id(mPage.mSearchBox).send_keys(mSearchTerm + Keys.RETURN)
        time.sleep(2)

        creativeCount = self.cdriver.find_element_by_xpath(mPage.allegedSiteCreativeCount).text
        creativeCountList = creativeCount.split()
        siteCreativeCountNum = int(creativeCountList[0])
        loadMeBtn = self.cdriver.find_element_by_id("paginate-button")
        while loadMeBtn.is_displayed():
            loadMeBtn.click()
            time.sleep(4)
        actualCreativesListDisplayed = self.cdriver.find_elements_by_class_name('ad-cell')
        self.assertEqual(len(actualCreativesListDisplayed), siteCreativeCountNum, 'Site Count vs Actual Count not Match')

    def test_4_Verify_Share_This_Ad_Feature(self):
        #Verifies Share Ad feature works by being able to view the link of current creative
        mPage =  MoatPage
        self.cdriver.find_element_by_id(mPage.mSearchBox).send_keys(mSearchTerm + Keys.RETURN)
        time.sleep(2)

        creativesListDisplayed = self.cdriver.find_element_by_class_name('ad-cell')
        mousehover = ActionChains(self.cdriver).move_to_element(creativesListDisplayed)
        mousehover.perform()
        time.sleep(2)
        popupCreative = self.cdriver.find_element_by_xpath(mPage.popupCreativeLoc)
        popupCreative.click()
        popupCreativeLink = self.cdriver.find_element_by_xpath(mPage.popupCreativeLinkLoc)
        self.assertTrue(popupCreativeLink.is_displayed(), 'Share Feature not Found')

    def tearDown(self):
        self.cdriver.quit()

if __name__ == '__main__':
    unittest.main()