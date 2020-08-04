from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint


chromedriver_path = '' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('') #Enter your username
password = webdriver.find_element_by_name('password')
password.send_keys('') #Enter Your Password
password.send_keys(Keys.RETURN)
sleep(20)

notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
sleep(10)

like = webdriver.find_element_by_xpath('/main/section/div[2]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg')
like.click()


# /main/section/div[2]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg
# //*[@id="react-root"]/section/main/section/div[2]/div[2]/div/article[1]/div[2]/section[1]/span[1]/button/svg/path