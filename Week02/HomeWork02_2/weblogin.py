from selenium import webdriver
import requests
import lxml
import time

url = 'https://shimo.im/login?from=home'
user = '36540855@qq.com'
passwd = '36540855'

try:
    #模拟成移动端浏览器，网站第一次登录时要求滑动验证，成功后不再需要
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 10; EVR-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36')
    #chrome_options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 5.1; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036215 Safari/537.36 MicroMessenger/6.3.18.800 NetType/WIFI Language/zh_CN')
    #chrome_options.add_argument('user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get(url)
    time.sleep(3)
    
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(user)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(passwd)
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    #TODO: deel with the challenger

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)