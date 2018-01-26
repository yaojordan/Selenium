#! python3

import time
import requests
from selenium import webdriver

chrome_path = "C:\Python\programs\selenium_driver_chrome\chromedriver.exe"
browser = webdriver.Chrome(chrome_path)

browser.get('http://mtkcqweb.mediatek.inc/mtkcqweb_DT_sec05/mtk/sec/queryDispatch/dispatch.cq')

acc = browser.find_element_by_name('loginId')
acc.send_keys('vend_dt076')
pwd = browser.find_element_by_name('password')
pwd.send_keys('vend_dt076')

login = browser.find_element_by_id("button-1016")
login.click()

time.sleep(5)#waiting for login
okay = browser.find_element_by_id("ext-gen383")
okay.click()

#personal queries
pq = browser.find_element_by_class_name("x-tree-node-anchor")
pq.click()

#find MIPS_ALL
time.sleep(2)
MA = browser.find_element_by_xpath("//span[text()='MIPS_ALL']")
MA.click()

time.sleep(2)
exportToExcel = browser.find_element_by_id("ext-gen491")
exportToExcel.click()

time.sleep(2)
clickYesFor2007 = browser.find_element_by_id("ext-gen389")
clickYesFor2007.click()

time.sleep(3)
browser.quit()
