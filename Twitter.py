from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver_path = '' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.twitter.com/login')
sleep(5)
username = webdriver.find_element_by_name('session[username_or_email]')
username.send_keys('') #Enter Your Username
password = webdriver.find_element_by_name('session[password]')
password.send_keys('') #Enter your Password
password.send_keys(Keys.RETURN)
sleep(3)
search = '' #Enter Your Search Query
webdriver.get('https://twitter.com/search?q='+search+'&src=typed_query')
sleep(10)
# webdriver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# sleep(10)

toclick= webdriver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/div/article')
toclick.click()
sleep(3)
likett = webdriver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/article/div/div[3]/div[4]/div[3]')
likett.click()
sleep(10)
close = webdriver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div')
close.click()
sleep(10)

    webdriver.execute_script('window.scrollTo(0,1000)')
    sleep(20)



#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div:nth-child(7) > div > div > div > article
# /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/article/div/div[3]/div[3]/div[3]/div/div/div/svg
# /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/article/div/div[3]/div[4]/div[3]/div/div/div/svg

# /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/article/div/div[3]/div[4]/div[3]
# /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/div/article
# /html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[2]/div/div/div/article

#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div:nth-child(3) > div > div > div > article
#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div:nth-child(3) > div > div > div > article