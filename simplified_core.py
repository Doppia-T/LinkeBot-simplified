# gets libraries needed
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
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
