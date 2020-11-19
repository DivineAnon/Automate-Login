from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
#open Google Chrome browser
driver = webdriver.Chrome()
#maximize the window size
driver.maximize_window()
#delete the cookies
driver.delete_all_cookies()
#navigate to the url
driver.get("https://adminengine.degadai.com/")
driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[1]/input').send_keys("admin@admin.com")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div/div/form/div[2]/input').send_keys("password")
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div/div/form/button').send_keys(Keys.ENTER)
time.sleep(1)
#close the browser
driver.close()
print("facebook login has been successfully completed")