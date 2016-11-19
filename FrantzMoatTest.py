from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
mURL = 'http://www.moat.com'

cdriver = webdriver.Chrome(chromeDriverLoc)
cdriver.get(mURL)

cdriver.find_element_by_id("pro-landing-search-box").send_keys('better' + Keys.RETURN)
time.sleep(2)
loadMeBtn = cdriver.find_element_by_id("paginate-button")
x = 0

insideBox = cdriver.find_element_by_class_name('ad-cell')
hover = ActionChains(cdriver).move_to_element(insideBox)
hover.perform()
time.sleep(2)
damn = cdriver.find_element_by_xpath('//*[@id="popup-template"]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/a')
damn.click()
damn2 = cdriver.find_element_by_xpath('//*[@id="popup-template"]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/div/input')
print(damn2.is_displayed())
"""
while loadMeBtn.is_displayed() :
    loadMeBtn.click()
    x = x + 1
    print("This was clicked :", x, " times")
    time.sleep(4)
insideBox = cdriver.find_elements_by_class_name('ad-cell')
#insideBox = cdriver.find_element_by_css_selector('#all > div.ads-container > div.ads').get_attribute('div')
print(len(insideBox))
# shit comet ff fuck rocket zata zz tops (get # createvies by span via ele by css"""


"""from urllib.request import Request, urlopen
from urllib.error import HTTPError

mList2 = ['https://wwww.moat.com', 'http://moat.com', 'https://moat.com/search_lucky?q=%7C%7C&doc_type=advertiser']
def verifyWorkingLnks(lnksList):
    cnt = 0
    for x in lnksList:
        req = Request(x)
        try:
            response = urlopen(req)
        except HTTPError as e:
            print('Link Validation Function FAILED with following lnk: ', x, ' Status code given: ', e.code)
        else:
            cnt += 1
            if cnt == 3 :
                print('Link Validation Function:  PASSED')

eleText = '22 mins ago'
x = eleText.split()
print(x)
print(int(x[0]))
num = int(x[0])
if (any('min' in dic for dic in x)) & (num <30) :
    print('exitcue')
else:
    print('what thsfuk')

mylist = ["2 min ago", "54 secs ago", '30 secs ago', '0.5 hours ago']

def verifyRecentAdTime(AdverList):
    episolon = 0
    for x in AdverList:
        p = x.split()
        n = float(p[0])
        if (any('min' in c for c in p)) & (n < 30) :
            episolon += 1
        elif (any('sec' in c for c in p)) & (n < 60*30) :
            episolon += 1
        elif (any('hour' in c for c in p)) & (n < 0.5):
            episolon += 1
    if episolon == 4 :
        print("pass")
    else: print('fail', episolon)

verifyRecentAdTime(mylist)

//*[@id="popup-template"]/div
//*[@id="popup-template"]/div/div[1]/div[1]/div/img
//*[@id="popup-template"]/div/div[1]/div[2]
//*[@id="popup-template"]/div/div[1]/div[2]"""

"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriverLoc = "/Users/NewUser/Downloads/Automation/chromedriver"
mURL = 'https://www.tumblr.com/search/naruto'

cdriver = webdriver.Chrome(chromeDriverLoc)
cdriver.get(mURL)

#cdriver.find_element_by_id("pro-landing-search-box").send_keys('Betterment' + Keys.RETURN)
insideBox = cdriver.find_elements_by_tag_name('article')
print(len(insideBox))"""

#labels = driver.find_elements_by_tag_name("label")
#inputs = driver.execute_script(
#    "var labels = arguments[0], inputs = []; for (var i=0; i < labels.length; i++){" +
#   "inputs.push(document.getElementById(labels[i].getAttribute('for'))); } return inputs;", labels)

import unittest
import selenium
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = selenium.webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
            assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()