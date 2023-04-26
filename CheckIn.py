from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

sys.argv

asset = sys.argv[1]

def get_driver():
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
    ["enable-automation"])
    options.add_argument
    ("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://assets.avantorsciences.net/hardware")
    time.sleep(1.2)
    return driver

def login():
    driver = get_driver()
    #Inputs username and password
    driver.find_element(by="id", value="username").send_keys("Brandon.Brinson")
    time.sleep(1)
    driver.find_element(by="id", value="password").send_keys("Asjee$7598!!!!!" + Keys.RETURN)
    time.sleep(2)

def assetTag():
    #Inputs username and password
    driver = get_driver()
    driver.find_element(by="id", value="username").send_keys("Brandon.Brinson")
    time.sleep(1)
    driver.find_element(by="id", value="password").send_keys("Asjee$7598!!!!!" + Keys.RETURN)
    time.sleep(2)
    #Enters Asset Tag into Search Box
    driver.find_element(by="id", value="tagSearch").send_keys(asset + Keys.RETURN)
    time.sleep(1.3)
    #Clicks on Actions, Allows to check in or ends code
    driver.find_element(by="xpath", value="/html/body/div[1]/div/section[1]/div/div/button").click()
    edit = driver.find_element(by="xpath", value="/html/body/div[1]/div/section[1]/div/div/ul/li[1]/a")
    if edit.text == "Edit Asset":
        time.sleep(5)
        sys.exit()
    else:
        #Clicks to Check-in Asset
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[1]/div/div/ul/li[1]/a").click()
        time.sleep(2)
        #Clicks Down Arrow for Status and Clicks In Preparation
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/span/span[1]/span/span[2]").click()
        time.sleep(1)
        driver.find_element(by="xpath", value="/html/body/span/span/span[2]/ul/li[6]").click()
        time.sleep(1)
        #Clicks Down Arrow for Location and Inputs Location
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div[1]/span/span[1]/span/span[2]/b").click()
        time.sleep(2.2)
        driver.find_element(by="xpath", value="/html/body/span/span/span[2]/ul/li[134]").click()
        time.sleep(1.5)
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div[2]/div/form/div[7]/button").click()
        time.sleep(7)

def serial():
    driver = get_driver()
    #Inputs username and password
    driver.find_element(by="id", value="username").send_keys("Brandon.Brinson")
    time.sleep(1)
    driver.find_element(by="id", value="password").send_keys("Asjee$7598!!!!!" + Keys.RETURN)
    time.sleep(4)
    #Inputs Serial Number
    driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/input").send_keys(asset)
    time.sleep(3.5)
    #Click on Asset Name
    driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div[2]/table/tbody/tr/td[2]/a").click()
    #Clicks on Actions, Allows to check in or ends code
    driver.find_element(by="xpath", value="/html/body/div[1]/div/section[1]/div/div/button").click()
    edit = driver.find_element(by="xpath", value="/html/body/div[1]/div/section[1]/div/div/ul/li[1]/a")
    if edit.text == "Edit Asset":
        time.sleep(5)
        sys.exit()
    else:
        #Clicks to Check-in Asset
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[1]/div/div/ul/li[1]/a").click()
        time.sleep(2)
        #Clicks Down Arrow for Status and Clicks In Preparation
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/span/span[1]/span/span[2]").click()
        time.sleep(1)
        driver.find_element(by="xpath", value="/html/body/span/span/span[2]/ul/li[6]").click()
        time.sleep(1)
        #Clicks Down Arrow for Location and Inputs Location
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div[1]/span/span[1]/span/span[2]/b").click()
        time.sleep(2.2)
        driver.find_element(by="xpath", value="/html/body/span/span/span[2]/ul/li[134]").click()
        time.sleep(10)
        driver.find_element(by="xpath", value="/html/body/div[1]/div/section[2]/div[2]/div/div/div/div[2]/div/form/div[7]/button").click()
        time.sleep(7)

if len(asset) == 9:
    print(assetTag())
else:
    print(serial())