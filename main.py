from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import random

# インスタログイン情報
login_id = 'ID'
login_pwd = 'password'

# オプション設定
options = Options()
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

def login():
    driver.find_element_by_name('username').send_keys(login_id)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(login_pwd)
    time.sleep(1)
    driver.find_element_by_class_name('L3NKy').click()
    time.sleep(3)

    # ポップアップ閉じる
    # driver.find_element_by_class_name('HoLwm').click()
    # time.sleep(1)

def searchTAG():
    TAG_URL = 'https://www.instagram.com/explore/tags/'
    TAG_NAME = 'ここに検索したいタグ名をいれる'
    TAG_SEARCH_URL = TAG_URL + TAG_NAME
    driver.get(TAG_SEARCH_URL)
    print('----------- search : #' + TAG_NAME + ' -----------\n ')
    time.sleep(5)

def showPOST():
    POST_PATH = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]'
    driver.find_element_by_xpath(POST_PATH).click()
    time.sleep(1)

def followingUser(count):
    button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
    if count < 3:
        if button.text == "Follow" or button.text == "フォローする":
            button.click()
            INSTA_ID = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            print('following : ', INSTA_ID)

def finishChrome():
    driver.close()
    driver.quit()

if __name__ == '__main__':
    print('\n--------------------- start ------------------------\n ')
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    login()
    if 'https://www.instagram.com/accounts/login/' in driver.current_url:
        print('NG login...\n')
        finishChrome()
    else:
        print('OK login !!!\n')
        searchTAG()
        showPOST()
        # いいねする
        countLike = 0
        while (countLike < random.randint(5, 50)):
            NEXT_PAGE_BTN_PATH = '/html/body/div[4]/div[1]/div/div/a[2]'
            time.sleep(random.randint(1,10))
            try:
                driver.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                countLike += 1
                print(countLike, ' like!')
                time.sleep(1)
                # followingUser(countLike)
                driver.find_element_by_xpath(NEXT_PAGE_BTN_PATH).click()
            except:
                print('pass')
                driver.find_element_by_xpath(NEXT_PAGE_BTN_PATH).click()
                pass
        print('\n------------------ finished ------------------------\n ')
        finishChrome()
