from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


print("test case started")


driver = webdriver.Chrome(executable_path='/home/balkrishan/Downloads/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="email"]').send_keys('9381817083')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('kingsraina')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_d_2G"]').send_keys(Keys.ENTER)
time.sleep(1)
driver.close()