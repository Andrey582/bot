import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def Get_Page():
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    browser = webdriver.Chrome()
    browser.get("https://gorzdrav.spb.ru/drug-search")
    browser.find_element_by_id("drugs-field").send_keys("Акку-Чек Актив")
    browser.find_element_by_id("button-search").click()
    time.sleep(120)
    browser.find_element_by_xpath(
        '/html/body/div/div[1]/div[9]/div[3]/div/div[3]/div/div[2]/div/div/div[1]/div[2]').click()
    time.sleep(10)
    try:
        text = Apteka244(browser)
    except:
        text = "Полосок нет"
    return text

def Test(browser):
    browser.find_element_by_xpath('//*[text()="Курортный район"]/following-sibling::div').click()
    time.sleep(10)
    text = browser.find_element_by_xpath('//*[text()="Аптека №21"]/following-sibling::div[2]/div[1]/div[1]/div[2]').text
    text = "По федеральной льготе в аптеке №21 осталось " + text + "\n"
    text += "По региональной " + browser.find_element_by_xpath(
        '//*[text()="Аптека №21"]/following-sibling::div[2]/div[1]/div[2]/div[2]').text + "\n"
    return text

def Apteka244(browser):
    browser.find_element_by_xpath('//*[text()="Красногвардейский район"]/following-sibling::div').click()
    time.sleep(10)
    text = browser.find_element_by_xpath('//*[text()="Аптека №244"]/following-sibling::div[2]/div[1]/div[1]/div[2]').text
    text = "Аптека №244\nПо федеральной " + text + "\n"
    text += "По региональной " + browser.find_element_by_xpath(
        '//*[text()="Аптека №244"]/following-sibling::div[2]/div[1]/div[2]/div[2]').text + "\n"
    return text