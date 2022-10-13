# gets libraries needed
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import random
import sys
import time


# gets username from an external file called "LinCred"
# quite raw method of getting the credential from a .txt file
def get_LinkeID():
    with open(os.path.join(sys.path[0], "LinCred.txt"), "r") as find_cred:
        for line in find_cred:
            if line.startswith('id'):
                id_line = line
                spl_word = 'id = '
                spl_id_line = id_line.split(spl_word,1)[1]
                LinkeUsername = spl_id_line
                return LinkeUsername

# gets password from an external file called "LinCred"
# quite raw method of getting the credential from a .txt file
def get_LinkePSS():
    with open(os.path.join(sys.path[0], "LinCred.txt"), "r") as find_cred:
        for line in find_cred:
            if line.startswith('password'):
                pss_line = line
                spl_word = 'password = '
                spl_pss_line = pss_line.split(spl_word,1)[1]
                LinkePassword = spl_pss_line
                return LinkePassword

# gets target profile from an external file called "LinTarg" quite raw method of getting the target 
# from a .txt file
def get_LinkeTGT():
    with open(os.path.join(sys.path[0], "LinTarg.txt"), "r") as find_targ:
        for line in find_targ:
            if line.startswith('profile'):
                tgt_line = line
                spl_word = 'profile = '
                spl_tgt_line = tgt_line.split(spl_word,1)[1]
                LinkeTarget = spl_tgt_line
                return LinkeTarget


# does login with credential taken from external file (more actions in the future)
class LinkeBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get('https://linkedin.com/')

        # waits until the element "session_password" is displayed before starting to insert the profile credentials for 
        # the access (plus, it waits for a second for more suspense)
        try:
            WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.ID, 'session_password')))
            time.sleep(1)
        except:
            print("Loading is taking too much time!")

        username = bot.find_element_by_id('session_key')
        password = bot.find_element_by_id('session_password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)


    def reach_target(self, target):
        bot = self.bot

        # waits until the profile picture in the main page - which contains the particular class 'feed-identity ...' - is 
        # displayed before starting the process of going to the page of the "taget" (plus, it waits for a second for more suspense)
        try:
            WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'feed-identity-module__member-photo EntityPhoto-circle-5 lazy-image ember-view')]")))
            time.sleep(1)
        except:
            print("Loading is taking too much time!")
        
        bot.get(target)


    def get_target_activities(self, target):
        bot = self.bot

        # waits until the profile picture in the profile page - which contains the particular class 'pv-top-card-profile ...' - is 
        # displayed before starting the process of going to the page listing the "recent activities" of the "taget" (plus, it waits 
        # for a second for more suspense)
        try:
            WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'pv-top-card-profile-picture__image pv-top-card-profile-picture__image--show ember-view')]")))
            time.sleep(1)
        except:
            print("Loading is taking too much time!")

        bot.get(target+'recent-activity/')
        try:
            WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'ember-view pv-recent-activity-top-card__member-photo EntityPhoto-circle-5')]")))
            time.sleep(1)
        except:
            print("Loading is taking too much time!")


    def like_posts(self):
        bot = self.bot
        posts_column_container = WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.ID, "main")))
        posts_column = posts_column_container.find_element(By.XPATH, "//div[contains(@class, 'pv-recent-activity-detail')]")
        posts = posts_column.find_elements(By.XPATH, "//div[contains(@class, 'ember-view') and contains(@class, 'occludable-update')]")

        # counts and shows the number of posts published in "Recent Activities" by the target
        posts_published = len(posts)
        print("LinkeBot found "+str(posts_published)+" posts published by the target.")

        # clicks the "like" button for every unclicked post published by the target (the "unclicked" buttons contain the label 'false' 
        # for the 'aria-pressed' elements)
        for p in range(posts_published):
            like_button = bot.find_element(By.XPATH, "//button[contains(@class, 'social-actions-button') and contains(@aria-pressed, 'false')]") 
            like_button.click()
            time.sleep(2)


    def read_posts(self): # WORK IN PROGRESS!!
        bot = self.bot
        posts_column_container = WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.ID, "main")))
        posts_column = posts_column_container.find_element(By.XPATH, "//div[contains(@class, 'pv-recent-activity-detail')]")
        posts = posts_column.find_elements(By.XPATH, "//div[contains(@class, 'ember-view') and contains(@class, 'occludable-update')]")

        # scrolls down to load more posts of the target
        for s in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)') # NOT SURE IT WORKS ...
            time.sleep(1)

        # counts and shows the number of posts published in "Recent Activities" by the target
        posts_published = len(posts)
        print("LinkeBot found "+str(posts_published)+" posts published by the target.")

        # "reads" the text of every post published by the target
        for p in range(posts_published):
            post_text_container = bot.find_element(By.XPATH, "//div[contains(@dir, 'ltr')]")
            post_text = post_text_container.find_element(By.XPATH, "//span[contains(@dir, 'ltr')]")
            print(str(post_text)) # HERE SOMETHING IS NOT WORKING!!!
            time.sleep(1)



# starts process of getting login credentials
LinkeUsername = get_LinkeID()
LinkePassword = get_LinkePSS()
LinkeTarget = get_LinkeTGT()


# starts process of logging in with the credentials previously obtained
TestBot = LinkeBot(LinkeUsername,LinkePassword)
TestBot.login()

# goes to "target" page
TestBot.reach_target(LinkeTarget)

# goes to the "recent activites" of the target
TestBot.get_target_activities(LinkeTarget)

# starts liking posts of the "target"
TestBot.like_posts()
