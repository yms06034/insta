from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *

import pyautogui

import time
import pyperclip
import warnings

warnings.filterwarnings(action='ignore')

def find_css(css_selector, browser):
    return browser.find_element(By.CSS_SELECTOR, css_selector)
def finds_css(css_selector , browser):
    return browser.find_elements(By.CSS_SELECTOR, css_selector)

def find_xpath(xpath , browser):
    return browser.find_element(By.XPATH, xpath)
def finds_xpath(xpath , browser):
    return browser.find_elements(By.XPATH, xpath)

def find_id(e_id , browser):
    return browser.find_element(By.ID, e_id)

def find_className(cn , browser):
    return browser.find_element(By.CLASS_NAME, cn)
def finds_className(cn , browser):
    return browser.find_elements(By.CLASS_NAME, cn)

def find_linktext(lt , browser):
    return browser.find_element(By.LINK_TEXT, lt)

# INSTA LOGIN XPATH
INPUT_ID = '//*[@id="loginForm"]/div/div[1]/div/label/input'
INPUT_PW = '//*[@id="loginForm"]/div/div[2]/div/label/input'

ALERT_2 = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'

# INSTA LOGOUT XPATH
MORE_BTN = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div/div[1]/div/div'
LOGOUT_BTN = '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]/div/div/div/div/div'

# INSTA DM XPATH
MESSAGE_BTN = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div'
RECIPIENT_INPUT = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/input'

FIND_ID_CLICK_BTN = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div'
START_CK = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div'

IMAGE_BTN = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]'

SEND_BTN = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]'

# EXCEPTION XPATH:
CLOSE_BTN = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div'



# insta_id_list = [['sjk5838', 'mirae_beauty_09', 'mirae_inner_09'], ['rlatjdwls00@K', 'han828988@', 'han8289988@']]

# dm_id_list = ['sjk5838', 'sjk5838', 'sjk5838', 'sjk5838', 'sjk5838']
# message_content = """하이루"""

# image_path = 'C:\\Users\\user\\Downloads\\3.jpg'

# num_per_user = 1
# timesleep = 5


# numbers = 3

# count = 0

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no--sandbox')
    options.add_argument('no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1080,800')
    options.add_argument('incognito')

    chrome_service = Service('chromedriver')
    chrome_service = Service(executable_path="chromedriver.exe")
    browser = webdriver.Chrome(service=chrome_service, options=options)
    
    return browser

def insta_login(INPUT_ID, INPUT_PW, insta_id, insta_pw, browser):
    browser.get('https://www.instagram.com/')
    browser.implicitly_wait(2)
    
    input_id = find_xpath(INPUT_ID, browser)
    input_pw = find_xpath(INPUT_PW, browser)

    time.sleep(2)

    pyperclip.copy(insta_id)
    input_id.send_keys(Keys.CONTROL, "v")
    
    time.sleep(1)
    
    pyperclip.copy(insta_pw)
    input_pw.send_keys(Keys.CONTROL, "v")
    input_pw.send_keys("\n")

    try:
        if find_id('slfErrorAlert', browser).text:
            print('로그인 실패')
            return 0
    except:
        pass

    browser.implicitly_wait(10)
    find_className('_ac8f', browser).click()
    try:
        browser.implicitly_wait(10)
        find_xpath(ALERT_2, browser).click()
    except:
        pass

    return 1

def insta_logout(browser, MORE_BTN):
    find_xpath(MORE_BTN, browser).click()
    time.sleep(.5)
    find_xpath(LOGOUT_BTN, browser).click()



def send_dm(browser, dm_id, image_path, message_content):
    browser.get('https://www.instagram.com/direct/inbox/')

    time.sleep(2)

    message_btn = find_xpath(MESSAGE_BTN, browser)
    message_btn.click()

    time.sleep(1)

    recipient_input = find_xpath(RECIPIENT_INPUT, browser)

    pyperclip.copy(dm_id)
    recipient_input.send_keys(Keys.CONTROL, 'v')

    time.sleep(1.5)

    find_id_click_btn = find_xpath(FIND_ID_CLICK_BTN, browser)
    find_id_click_btn.click()

    time.sleep(1.5)

    start_ck = find_xpath(START_CK, browser)
    start_ck.click()

    time.sleep(1.5)

    if image_path:
        # Image area
        image_btn = find_xpath(IMAGE_BTN, browser)
        image_btn.click()

        time.sleep(1)

        pyperclip.copy(image_path)

        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')

    time.sleep(1)

    # Text Area
    if message_content:
        input_area = find_css('p.xat24cr', browser)

        pyperclip.copy(message_content)
        input_area.send_keys(Keys.CONTROL, 'v')

        time.sleep(1)

        send_btn = find_xpath(SEND_BTN, browser)
        send_btn.click()



def start_dm(num_per_user, insta_id_list, dm_id_list, timesleep, image_path):
    url_count = 0
    browser = open_browser()
    duplicate_id = []
    append_id = []
    
    time.sleep(1.5)
    
    try:
        with open('duplicate_id.txt', 'r') as f:
            for i in f:
                duplicate_id.append(i.replace('\n', ''))
    except Exception as ex:
        print(ex)
        pass

    while len(dm_id_list) > url_count:
        for info in range(len(insta_id_list[0])):
            insta_id = insta_id_list[0][info]
            insta_pw = insta_id_list[1][info]
            insta_login(INPUT_ID, INPUT_PW, insta_id, insta_pw, browser)

            for _ in range(num_per_user):
                if len(dm_id_list) <= url_count:
                    break
                dm_id = dm_id_list[url_count]
                
                try:
                    if dm_id in duplicate_id:
                        pass
                    else:
                        send_dm(browser, MESSAGE_BTN, RECIPIENT_INPUT, FIND_ID_CLICK_BTN, START_CK, IMAGE_BTN, SEND_BTN, dm_id, image_path, message_content)

                        url_count += 1
                        append_id.append(dm_id)
                        print(f"wrote a comment for {dm_id}")
                except:
                    pass
                    print('없는 계정입니다.')
                    url_count += 1
                    find_xpath(CLOSE_BTN, browser).click()

                time.sleep(timesleep)

            insta_logout(browser, MORE_BTN)
            time.sleep(2)
            
            if len(dm_id_list) <= url_count:
                break
                
    
    with open('duplicate_Id.txt', 'a') as f:
        for id_ in append_id:
            f.write(id_ + '\n')
    
    browser.quit()

    return