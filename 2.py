import dlq
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.implicitly_wait(10)
a=dlq.dl("https://bbs.rednet.cn/forum-1813-1.html")
with open('1','w') as f:
	f.write(str(a))

driver.get("https://bbs.rednet.cn/forum-1813-1.html")
driver.implicitly_wait(10)
with open('2','w') as f:
	f.write(str(driver.get_cookies()))
driver.delete_all_cookies()
with open('1','r') as f:
	a=eval(f.read())

for n in a:
	print(n)
	driver.add_cookie(n)
sleep(3)
driver.refresh()
# # driver.quit()
    
