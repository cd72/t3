from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# for firefox https://github.com/mozilla/geckodriver/releases
# https://foxmask.net/post/2016/02/17/pycharm-running-flake8/

print("starting")


driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# sleep now
time.sleep(3)
driver.close()

x = 4
print(x)

y = 6
assert x == y
