# LinkeBot-simplified
This is an (over)simplified version of [LinkeBot](https://github.com/Doppia-T/LinkeBot).


**A small bot for automating a Linkedin profile**

This is the second attempt of creating a bot capable of managing a LinkedIn profile. It uses [Selenium WebDriver package](https://pypi.org/project/selenium/) and, since it is written for being used with [Mozilla Firefox](https://www.mozilla.org/it/firefox/new/) browser, [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

This bot is designed to get the credentials of the LinkedIn profile from an external '.txt' file so that anyone can change the used profile -or its password - without the need of modifying the source code. Said file has to be put in the same folder with the other LinkeBot's '.py' file.

This bot is also designed to reach the profile of a target - whose address has to be put in an external '.txt' - and to push the 'like' button of all of the posts he/she published. 


## Driver Setup

Linkebot uses 'geckodriver' so download the [latest driver](https://github.com/mozilla/geckodriver/releases). 


## Additional requiements setup

Since Linkebot requires user's credentials and target to operate. You have to setup the credentials in 'LinCred.txt' file and the URL address of the target in 'LinTarg.txt'.


## Legal notes

**Warnings and disclaimer**

LinkeBot is not affiliated with, sponsored, authorised or endorsed by Microsoft Corporation, LinkedIn or any of their affiliates or subsidiaries. This is an independent and unofficial project.

LinkeBot violates LinkedIn's User Agreement Section 8.2 ("_Don’ts_"), paragraphs 2 and 13, and, for this reason, LinkedIn may temporarily or even permanently ban accounts using LinkeBot.
