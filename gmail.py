from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

##Recipient id = testmailautomation1@gmail.com
##Recipient pw = Testamazon


driver = webdriver.Chrome('/Users/sunghunkwak/PythonTesting/chromedriver')
driver.get("https://gmail.com")

# Find User ID Field
userID = driver.find_element_by_id("identifierId")
userID.clear()
userID.send_keys("testamazonautomation")
time.sleep(2) 
 
# Find Next Button
idNextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
idNextButton.click()
time.sleep(2)

# Find Password Field
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, 'password')))
password = driver.find_element_by_name("password")
password.clear()  

password.send_keys("Testamazon")
time.sleep(2)

# Find Next Button
passwordNextButton = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
passwordNextButton.click()
time.sleep(5)

# Find Compose Button and click
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#\:59 > div > div')))
composeButton = driver.find_element_by_css_selector('#\:59 > div > div')
composeButton.click()
time.sleep(2)

# Find Recipients field and insert email address
recipients_field = driver.find_element_by_xpath('//*[@id=":b2"]')
recipients_field.send_keys("testmailautomation1@gmail.com")
time.sleep(2)

# Find Subject field and insert subject
subject_field = driver.find_element_by_xpath('//*[@id=":ak"]')
subject_field.send_keys("Hello")
time. sleep(2)

# Find Message field
message_field = driver.find_element_by_xpath('//*[@id=":bp"]')
message_field.send_keys("Hello, this is testing automation. Thank you.")
time. sleep(3)

# Find Send button and click
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#\:aa')))
sendButton = driver.find_element_by_css_selector('#\:aa')
sendButton.click()
time.sleep(2)

 