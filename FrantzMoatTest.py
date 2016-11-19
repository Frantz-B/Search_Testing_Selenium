from selenium import webdriver
from selenium.webdriver.common.keys import Keys

fiya = webdriver.Chrome("/Users/NewUser/Downloads/Automation/chromedriver")
fiya.get("http://www.moat.com")
searchElement = fiya.find_element_by_id("pro-landing-search-box")
searchElement2 = fiya.find_element_by_xpath('//*[@id="search-bar"]/div/div[1]/span/a[1]').click()

searchElement.send_keys("cocaine" + Keys.RETURN)
print(searchElement2)

"""
//*[@id="search-bar"]/div/div[1]/span

//*[@id="search-bar"]/div/div[1]/span/a[1]
//*[@id="search-bar"]/div/div[1]/span/a[3]

//*[@id="popup-template"]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/a
"""