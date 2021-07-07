from selenium import webdriver
import time
from random import randint

# Default VARs

defaultAccountsList = ["therock", "pokimanelol", "playvalorantofficial", "kyliejenner", "billieeilish", "ronaldo", "instagram", "iquickdev", "razer"]
defaultMinDelayValue = 3
defaultMaxDelayValue = 5
defaultAccountsToFollowCount = 10

# Buffer VARs

username = ""
password = ""
accountsList = ""
minDelayValue = ""
maxDelayValue = ""
accountsToFollowCount = ""


def Loader(choice):
    if choice == "1":
        username = input("Username/Email: ")
        password = input("Password: ")
        print("---------- LOADED CONFIGURATION ----------")
        print("Username: " + username)
        print("PW: " + password)
        print("Accounts: " + defaultAccountsList)
        print("Minimum Delay: " + defaultMinDelayValue)
        print("Maximum Delay: " + defaultMaxDelayValue)
        print("N. of accounts to follow: " + defaultAccountsToFollowCount)
        print("-------------------------------------------")
        begin(username, password, defaultAccountsList, defaultMinDelayValue, defaultMaxDelayValue, defaultAccountsToFollowCount)
    elif choice == "2":
        file = open("preferences.txt", "r")
        print("                          ")
        username = file.readline()
        password = file.readline()
        accountsList = file.readline()
        minDelayValue = file.readline()
        maxDelayValue = file.readline()
        accountsToFollowCount = file.readline()
        print("---------- LOADED CONFIGURATION ----------")
        print("Username: " + username)
        print("PW: " + password)
        print("Accounts: " + accountsList)
        print("Minimum Delay: " + minDelayValue)
        print("Maximum Delay: " + maxDelayValue)
        print("N. of accounts to follow: " + accountsToFollowCount)
        print("-------------------------------------------")
        file.close()
        begin(username, password, accountsList, minDelayValue, maxDelayValue, accountsToFollowCount)
    else:
        print("Invalid Option")

def begin(username, password, accounts, mindelay, maxdelay, accountstofollowcount):
    browser = webdriver.Chrome("C:\\Users\\iQuick\\Desktop\\UltimateInstragramFollower\\chromedriver.exe")
    browser.get("https://instagram.com")
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("/html/body/div[3]/div/div/button[1]") \
        .click()

    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("//input[@name=\"username\"]") \
        .send_keys(username)
    browser.find_element_by_xpath("//input[@name=\"password\"]") \
        .send_keys(password)
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath('//button[@type="submit"]') \
        .click()
# Logged in
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button") \
        .click()
# Save login info declined
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]") \
        .click()
# Notifications declined
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input") \
        .send_keys(accounts[randint(0, 7)])
# Account searched
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div") \
        .click()
# Account clicked
    time.sleep(GetRandomTime())
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()

    time.sleep(GetRandomTime())\

    accountToFollow = "/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button"

    if accountsToFollowCount != 0:
        for i in range(1, accountsToFollowCount, 1):
            accountToFollow = "/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(i) + "]/div/div[3]/button"

            if (browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(
                    i) + "]/div/div[3]/button").text == "Following"):
                # This is so we don't follow people we already follow- trust me this would cause issues otherwise
                continue
            browser.find_element_by_xpath(accountToFollow).click()
            time.sleep(GetRandomTime())
    else:
        for i in range(1, defaultAccountsToFollowCount, 1):
            accountToFollow = "/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(i) + "]/div/div[3]/button"

            if (browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[" + str(
                    i) + "]/div/div[3]/button").text == "Following"):
                # This is so we don't follow people we already follow- trust me this would cause issues otherwise
                continue
            browser.find_element_by_xpath(accountToFollow).click()
            time.sleep(GetRandomTime())


def GetRandomTime():
    if minDelayValue == 0 and maxDelayValue == 0:
        randTime = randint(defaultMinDelayValue, defaultMaxDelayValue)
    else:
        randTime = randint(minDelayValue, maxDelayValue)
    return randTime

print("                                                                                    ")
print("          -------------------------------------------------------                   ")
print("          |       ULTIMATE INSTAGRAM FOLLOWER (by iQuick)       |                   ")
print("          |                        v0.3                         |                   ")
print("          |            IG: @iquickdev | Website: iquick.ml      |                   ")
print("          -------------------------------------------------------                   ")
print("                                                                                    ")
print("                      [1] Enter credentials manually                                ")
print("                      [2] Load credentials from file                                ")
print("                                                                                    ")
choice = input("                            Choose an option: ")
Loader(choice)
