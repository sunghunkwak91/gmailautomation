from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/sunghunkwak/PythonTesting/chromedriver')
driver.get("https://gmail.com")

# Find User ID Field
userID = driver.find_element_by_id("identifierId")
userID.clear()
userID.send_keys("testmailautomation1@gmail.com")
time.sleep(2) 
 
# Find Next Button
idNextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
idNextButton.click()
time.sleep(2)

# Find Password Field
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'password')))
password = driver.find_element_by_name("password")
password.clear()  

password.send_keys("Testamazon")
time.sleep(2)

# Find Next Button
passwordNextButton = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
passwordNextButton.click()
time.sleep(5)

# Find Search field
search_field = driver.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]')
search_field.click()
search_field.send_keys("testamazonautomation@gmail.com", Keys.ENTER)
