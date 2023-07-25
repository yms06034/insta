
from subprocess import CREATE_NO_WINDOW
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *

from bs4 import BeautifulSoup as bs
from datetime import datetime

import time
import pyperclip
import os

def find_css(css_selector, browser):
    return browser.find_element(By.CSS_SELECTOR, css_selector)

def finds_css(css_selector, browser):
    return browser.find_elements(By.CSS_SELECTOR, css_selector)

def find_xpath(xpath, browser):
    return browser.find_element(By.XPATH, xpath)

def finds_xpath(xpath, browser):
    return browser.find_elements(By.XPATH, xpath)

def find_id(e_id, browser):
    return browser.find_element(By.ID, e_id)

def find_className(cn, browser):
    return browser.find_element(By.CLASS_NAME, cn)

def finds_className(cn , browser):
    return browser.find_elements(By.CLASS_NAME, cn)

def find_linktext(lt, browser):
    return browser.find_element(By.LINK_TEXT, lt)

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no--sandbox')
    options.add_argument('no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1080,800')
    options.add_argument('incognito')

    chrome_service = Service('chromedriver')
    chrome_service.creationflags = CREATE_NO_WINDOW
    chrome_service = Service(executable_path="chromedriver.exe")
    browser = webdriver.Chrome(service=chrome_service, options=options)
    
    browser.get('https://www.instagram.com/')
    browser.implicitly_wait(2)
    
    return browser

INPUT_ID = '//*[@id="loginForm"]/div/div[1]/div/label/input'
INPUT_PWD = '//*[@id="loginForm"]/div/div[2]/div/label/input'
ALERT_2 = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'

FIRST_POST = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]'
WAIT_UNTIL_LOADING = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/div/div/span/img'
NEXT_FOR_FIRST = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div'
NEXT_AFTER_FIRST = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]'

CANT_OPEN_TAB = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[1]/span'

def login(insta_id, insta_pwd):
    browser = open_browser()
    input_id = find_xpath(INPUT_ID, browser)
    input_pw = find_xpath(INPUT_PWD, browser)

    time.sleep(2)

    pyperclip.copy(insta_id)
    input_id.send_keys(Keys.CONTROL, "v")

    pyperclip.copy(insta_pwd) 
    input_pw.send_keys(Keys.CONTROL, "v")
    input_pw.send_keys("\n")

    try:
        if find_id('slfErrorAlert', browser).text == '잘못된 비밀번호입니다. 다시 확인하세요.':
            print('로그인 실패')
            return 0
    except:
        pass
    browser.implicitly_wait(10)
    try:
        browser.implicitly_wait(10)
        find_className('_ac8f', browser).click()
    except:
        pass
    try:
        browser.implicitly_wait(10)
        find_xpath(ALERT_2, browser).click()
    except:
        pass
    
    return browser

def a(browser, ids, pwds, keyword, COUNT, FOLLOWER):
    global c, p, id_, pwd_

    user_id = []
    pass_id = []

    while True:
        try:
            browser.get(f'https://www.instagram.com/explore/tags/{keyword}/')
            browser.implicitly_wait(10)
            find_xpath(FIRST_POST, browser).click()

            print('탭', c)
            c += 1
            soup = bs(browser.page_source, "html.parser")
            s = soup.find_all(class_="xt0psk2")

            for i in s:
                try:
                    if i.find("a").text:
                        tmp = i.find('a'). text
                        break
                except:
                    pass
            print(tmp)

            print(tmp)
            print('프로필', p)
            p += 1
            browser.execute_script(f'window.open("https://www.instagram.com/{tmp}/");')  #구글 창 새 탭으로 열기
            browser.switch_to.window(browser.window_handles[-1])  #새로 연 탭으로 이동
            browser.implicitly_wait(10)
            find_xpath(WAIT_UNTIL_LOADING,browser)

            soup = bs(browser.page_source, "html.parser")
            s = soup.find_all(class_="_ac2a")

            for i in s:
                print(i.text)

            f = s[1].text
            if '만' in f:
                if '.' in f:
                    f = f.replace('.','').replace('만', '000')
                else:
                    f = f.replace('만', '0000')

            if int(f) >= FOLLOWER:
                print('add 1')
                user_id.append(tmp)
                user_id = list(set(user_id))
            else:
                print('pass')
            pass_id.append(tmp)

            browser.close()  #링크 이동 후 탭 닫기
            browser.switch_to.window(browser.window_handles[-1])  #다시 이전 창(탭)으로 이동
            time.sleep(1)

            if len(user_id) >= COUNT:
                print('out')
                return browser, user_id
            else:
                print('탭', c)
                c += 1
                find_xpath(NEXT_FOR_FIRST, browser).click()

                #두 번째 부터
                while True:
                    soup = bs(browser.page_source, "html.parser")
                    s = soup.find_all(class_="xt0psk2")

                    for i in s:
                        try:
                            if i.find("a").text:
                                tmp = i.find('a'). text
                                break
                            print(tmp)
                            if tmp in user_id:
                                continue
                        except:
                            pass

                    if not(tmp in pass_id):
                        pass_id.append(tmp)
                        print(tmp, id_)
                        print('프로필', p)
                        p += 1
                        browser.execute_script(f'window.open("https://www.instagram.com/{tmp}/");')  #구글 창 새 탭으로 열기
                        browser.switch_to.window(browser.window_handles[-1])  #새로 연 탭으로 이동
                        browser.implicitly_wait(10)
                        find_xpath(WAIT_UNTIL_LOADING,browser)
                        print('\t 로딩 끝')

                        print('\t soup')                        
                        soup = bs(browser.page_source, "html.parser")
                        s = soup.find_all(class_="_ac2a")

                        for i in s:
                            print('\t', i.text) 

                        f = s[1].text

                        if '만' in f:
                            if '.' in f:
                                f = f.replace('.','').replace('만', '000')
                            else:
                                f = f.replace('만', '0000')

                        if int(f) >= FOLLOWER:
                            user_id.append(tmp)
                            print('add', len(user_id))
                            if len(user_id) >= COUNT:
                                print('out')
                                browser.close()  #링크 이동 후 탭 닫기
                                browser.switch_to.window(browser.window_handles[-1]) 
                                break

                        else: print('pass', len(user_id))
                        browser.close()  #링크 이동 후 탭 닫기
                        browser.switch_to.window(browser.window_handles[-1])  #다시 이전 창(탭)으로 이동
                        time.sleep(1)

                    try:
                        print('탭', c)
                        c+=1
                        find_xpath(NEXT_AFTER_FIRST, browser).click()
                    except NoSuchElementException:
                        break

            dt = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            folder = 'id_file/'

            if not os.path.exists(folder):
                os.makedirs(folder)
            f = open(f'{folder}{dt}_{keyword}_upto_{FOLLOWER}.txt', 'w')
            for i in user_id:
                f.write(i+'\n')
            f.close()
            break

        except Exception as ex:
            print(ex)
            screenshot_folder = 'screenshot/'

            if not os.path.exists(screenshot_folder):
                os.makedirs(screenshot_folder)
            dt = datetime.now().strftime("%Y-%m-%d_%H%M%S")

            screenshot_path = f'{screenshot_folder}screenshot_{dt}.png'
            browser.save_screenshot(screenshot_path)
            if ids:
                print('다시 로그인')
                browser.quit()
                id_ = ids[0]
                pwd_ = pwds[0]
                browser = login(id_, pwd_)
                ids.remove(id_)
                pwds.remove(pwd_)
                continue
            else:
                print('아이디 없음')
                dt = datetime.now().strftime("%Y-%m-%d_%H%M%S")
                folder = 'id_file/'

                if not os.path.exists(folder):
                    os.makedirs(folder)

                f = open(f'{folder}{dt}_{keyword}_upto_{FOLLOWER}.txt', 'w')
                for i in user_id:
                    f.write(i+'\n')
                f.close()
                break

    return browser, user_id

def get_user_ids(ids, pwds, keywords, COUNT, FOLLOWER):
    global c, p, id_, pwd_
    id_ = ids[0]
    pwd_ = pwds[0]
    browser = login(id_, pwd_)
    c = 1
    p = 1

    user_ids = []
    try:
        for keyword in keywords:
            browser, tmp, = a(browser, ids, pwds, keyword, COUNT, FOLLOWER)

            user_ids.append(tmp)

        browser.close()
    except Exception as ex:
        print(ex)
    return 0, user_ids

