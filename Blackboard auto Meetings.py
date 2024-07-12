from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def log_in():
        driver.get('https://cuchd.blackboard.com/?new_loc=%2Fultra%2Fstream')
        try:
            ok_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[4]/div/div/div/div/div/div/div[2]/button')))
            ok_button.click()
            driver.maximize_window()
            username = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/form/div/ul/li[1]/input')
            username.send_keys('Your_Username')
            password = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/form/div/ul/li[2]/input')
            password.send_keys('Your_Password')
            sign_in_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/form/div/ul/li[3]/input')
            sign_in_button.click()
            try:
                courses = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
                courses.click()
            except:
                courses = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')
                courses.click()
        except:
            pass


        # Next few lines in case window is not full screen
        # time.sleep(5)
        # nav = driver.find_element_by_xpath(
        #     '/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/header/section/button')
        # nav.click()

def enter_creds():
    your_name = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div/div[2]/div[2]/input')
    your_name.send_keys('18BCS2129')
    join_meeting = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/form/div/div[4]/div/button')))
    join_meeting.click()
    time.sleep(6000)

def Monday1():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    MaS_lab = driver.find_element_by_id(
        "course-list-course-_30607_1")
    MaS_lab.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div'))
    )
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[1]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Monday2():

    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    MaS_lab = driver.find_element_by_id(
        "course-list-course-_30607_1")
    MaS_lab.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div'))
    )
    link_to_online_class.click()
    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[2]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Monday3():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    MaS = driver.find_element_by_id(
        "course-list-course-_30848_1")
    MaS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div'))
    )
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[1]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Monday4():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    WSS = driver.find_element_by_id("course-list-course-_30163_1"
    )
    WSS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div/div/div[1]/div/ng-switch/div/div[2]/div[1]/bb-content-item-course-outline/div/div[1]/ng-switch/div/bb-content-item-page/div/a')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[1]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Tuesday1():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    ESDM = driver.find_element_by_id("course-list-course-_31802_1"
    )
    ESDM.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li[1]/div/bb-rich-text-editor/div/div/div/div[1]/p/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Wednesday1():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    MaS = driver.find_element_by_id("course-list-course-_30676_1"
    )
    MaS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Wednesday2():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    ESDM = driver.find_element_by_id("course-list-course-_31802_1"
    )
    ESDM.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li[2]/div/bb-rich-text-editor/div/div/div/div[1]/p/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Wednesday3():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    WSS = driver.find_element_by_id("course-list-course-_30163_1"
                                    )
    WSS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div/div/div[1]/div/ng-switch/div/div[2]/div[1]/bb-content-item-course-outline/div/div[1]/ng-switch/div/bb-content-item-page/div/a')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[2]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Wednesday4():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    OE = driver.find_element_by_id('course-link-_29784_1'
    )
    OE.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[2]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Thursday1():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    WSS_Lab = driver.find_element_by_id('course-list-course-_30197_1'
    )
    WSS_Lab.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[1]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Thursday2():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    tab_view = driver.find_element_by_xpath('/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div[1]/div/div/div[1]/div/header/bb-square-toggle/div/label[2]')
    tab_view.click()
    WSS_Lab = driver.find_element_by_id('course-list-course-_30197_1'
    )
    WSS_Lab.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[2]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Thursday3():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    MaS = driver.find_element_by_id(
        "course-list-course-_30848_1")
    MaS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div'))
    )
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[2]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Thursday4():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    WSS = driver.find_element_by_id("course-list-course-_30163_1"
                                    )
    WSS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div/div/div[1]/div/ng-switch/div/div[2]/div[1]/bb-content-item-course-outline/div/div[1]/ng-switch/div/bb-content-item-page/div/a')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[3]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Thursday5():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    OE = driver.find_element_by_id('course-link-_29784_1'
    )
    OE.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[4]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Friday1():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    MaS = driver.find_element_by_id(
        "course-list-course-_30848_1")
    MaS.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div'))
    )
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[3]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/h3[2]/span/a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Friday2():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    ESDM = driver.find_element_by_id("course-list-course-_31802_1"
                                     )
    ESDM.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li[3]/div/bb-rich-text-editor/div/div/div/div[1]/p/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

def Friday3():
    log_in()
    window_before = driver.window_handles[0]
    courses = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[3]/div/li/a')))
    courses.click()
    time.sleep(5)
    OE = driver.find_element_by_id('course-link-_29784_1'
                                   )
    OE.click()
    link_to_online_class = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/div[4]/div/div/div/div/div/div[1]/ng-switch/div/div/div/div/bb-content-item-base/div/div/div/div')))
    link_to_online_class.click()

    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[5]/div/div/div/div/div/ng-form/div/section/div/div/bb-file-upload/div/div/div[1]/bb-document-editor/div/div/ul/li/div/bb-rich-text-editor/div/div/div/div[1]/p[6]/a')))
    link.click()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    launch = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#zoom-ui-frame > div._1doXW0tM > div > div._13FZYIXU._2lLZo0ll > div")))
    launch.click()
    join = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#zoom-ui-frame > div._1doXW0tM > div > div.ouV2Udld > h3:nth-child(2) > span > a')))
    join.click()
    enter_creds()
    driver.close()
    driver.switch_to.window(window_before)
    driver.get('http://www.google.com/')

schedule.every().wednesday.at('09:30').do(Wednesday1)
schedule.every().wednesday.at('11:10').do(Wednesday2)
schedule.every().wednesday.at('12:50').do(Wednesday3)
schedule.every().wednesday.at('13:45').do(Wednesday4)

schedule.every().monday.at('10:20').do(Monday1)
schedule.every().monday.at('11:15').do(Monday2)
schedule.every().monday.at('12:50').do(Monday3)
schedule.every().monday.at('13:45').do(Monday4)

schedule.every().tuesday.at('09:30').do(Tuesday1)

schedule.every().thursday.at('09:30').do(Thursday1)
schedule.every().thursday.at('10:25').do(Thursday2)
schedule.every().thursday.at('11:18').do(Thursday3)
schedule.every().thursday.at('12:50').do(Thursday4)
schedule.every().thursday.at('13:45').do(Thursday5)

schedule.every().friday.at('09:30').do(Friday1)
schedule.every().friday.at('10:25').do(Friday2)
schedule.every().friday.at('13:47').do(Friday3)

while True:
    schedule.run_pending()
    time.sleep(1)
