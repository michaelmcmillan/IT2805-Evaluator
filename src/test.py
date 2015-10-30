from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("http://folk.ntnu.no/michaedm/it2805/2/exercise-1/")

assert "Python" in driver.title
elem = driver.find_element_by_tag_name("img")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()
