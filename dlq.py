from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# def dl(url):
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.find_element(By.ID,"ls_username").send_keys('15686049638')
driver.find_element(By.ID,"ls_password").send_keys('P136y9638THON')

driver.find_element(By.CSS_SELECTOR,"#lsform > div > div > table > tbody > tr:nth-child(2) > td.fastlg_l > button").click()
sleep(2)
driver.find_element(By.ID, 'newspecial').click()
driver.find_element(By.XPATH, '//*[@id="typeid_ctrl"]').click()
driver.find_element(By.ID, 'subject').send_keys()
driver.find_element(By.XPATH, '/html/body').send_keys()
driver.find_element(By.ID, 'postsubmit')
s=driver.get_cookies()
print(s)

