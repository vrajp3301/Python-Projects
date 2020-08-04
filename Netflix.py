from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
    
chromedriver_path = '' #add your chromedriver_path in single quote
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.netflix.com/in/login')
sleep(3)
username = webdriver.find_element_by_name('userLoginId')
username.send_keys('') #Enter your username
password = webdriver.find_element_by_name('password')
password.send_keys('') #Enter your password
password.send_keys(Keys.RETURN)
sleep(2)
meet = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[3]/div/a/div/div')
meet.click()
sleep(4)
webdriver.get('https://www.netflix.com/browse/genre/34399?jbv=80230399&jbp=0&jbr=2')
sleep(2)
play = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[5]/a[2]/span')
play.click()
