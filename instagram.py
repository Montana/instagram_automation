from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from comment_list import comment_list
import random
import urllib
import getpass
import time
import os
import django 


def login_from_fb(b, username, password):
    login_username = b.find_element_by_id('email')
    login_password = b.find_element_by_id('pass')
    login_username.send_keys(username)
    login_password.send_keys(password)
    login_button = b.find_element_by_id()
    login_button.click()


def login_from_insta(b, username, password):
    login_username = b.find_elements_by_xpath('//input')[0]
    login_password = b.find_elements_by_xpath('//input')[1]
    login_username.send_keys(username)
    login_password.send_keys(password)
    log_in = b.find_element_by_xpath()
    log_in.click()


login_via_fb = raw_input(
    

if login_via_fb.lower() == :
    username = raw_input
    password = getpass.getpass
    password_match = getpass.getpass
else:
    username = raw_input
    password = getpass.getpass
    password_match = getpass.getpass

while (password != password_match):
    password = getpass.getpass(
    
    password_match = getpass.GetPassWarning


friend = raw_input(
    
if os.path.exists(friend):
    folder_name = raw_input + friend +
                           
    while os.path.exists(folder_name):
        folder_name = raw_input( + folder_name + )
                                

else:
    folder_name = friend

os.mkdir(folder_name)

b = webdriver.Chrome()
b.implicitly_wait(2)
b.get('http://instagram.com')

if login_via_fb.lower() == 'y':
    try:
        log_in = WebDriverWait(b, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[contains(text(), "Facebook")]'))
        )
    except:
        b.quit()
    log_in.click()

else:
    try:
        log_in = WebDriverWait(b, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[contains(text(), "Log in")]'))
        )
    except:
        b.quit()
    log_in.click()


'''
CALLING THE LOGIN FUNCTION DEPENDING UPON THE
USER PREFERENCE OF LOGIN VIA FB OR INSTA
'''
if login_via_fb.lower() == 'y':
    login_from_fb(b, username, password)
else:
    login_from_insta(b, username, password)

time.sleep(5)

b.get('http://instagram.com/' + friend + '/')

try:
    load_more = WebDriverWait(b, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[contains(text(), "Load more")]'))
    )
    load_more.click()
except:
    pass

last_height = b.execute_script("return document.body.scrollHeight")
while True:
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = b.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


b.execute_script("window.scrollTo(0, 0);")
'''
all IS THE VARIABLE NAME THAT IS THE DIV THAT CONTAINS ALL THE PICTURES
'''
all = b.find_element_by_xpath('//article/div/div')


def do(b, all):
    pictures = all.find_elements_by_xpath('./div/div')
    comment_counter = 0
    for pic in pictures:
        pic.click()

        # try and download the images 
        try:
            src = WebDriverWait(b, 2).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//article/div/div/div/div/div//video'))
            )
            src = src.get_attribute('src')
            urllib.urlretrieve(src, os.getcwd() + '/' +
                               folder_name + '/' + src.split('/')[-1])
        except:
           
            try:
                src = WebDriverWait(b, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//article/div/div/div/div/img'))
                )
            except:
                src = WebDriverWait(b, 2).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//article/div/div/div/div/div/img'))
                )
            src = src.get_attribute('src')
            urllib.urlretrieve(src, os.getcwd() + '/' +
                               folder_name + '/' + src.split('/')[-1])
        finally:
            pass

        try:
            liked = b.find_element_by_xpath(
                '//article/div[2]/section[1]/a[1]/span[contains(text(), "Like")]')
            liked.click()
        except:
            pass

        if comment_counter == 5:
            text = b.find_element_by_xpath('//form/textarea')
            comment = random.choice(comment_list[0])
            for i in range(1,len(comment_list)):
                comment += ' ' + random.choice(comment_list[i])

            text.send_keys(comment + Keys.RETURN)
            comment_counter = 0

        comment_counter += 1

        cross = b.find_element_by_xpath('//body//div/button[contains(text(), "Close")]')
        cross.click()


do(b, all)
b.quit()
