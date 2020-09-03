import selenium
from datetime import date
from datetime import timedelta
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

"""
CovidSurvey Autofill Survey
* ONLY to be used when you do not feel any symptoms *
* Otherwise please contact one of our trainers! *
created by: Tristan Sinclair
"""

today = date.today()  # Today's Date
yesterday = today - timedelta(days=1)  # Yesterday's Date
delayTime = 0.5  # Delay time in between pages

"""
delay()
helper function used before browser.implicitly wait was implemented
"""
def delay(num):
    time.sleep(num)
    return

"""
User Class
Built using user input data such as name, email, etc
passed to when to the fillSurvey()
"""
class User:
    def __init__(self, firstName, lastName, email, phoneNumber, locations):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.locations = locations


"""
openPage(browser)
Initiates the browser to open
"""
def openPage(b):
    b.get("https://stanforduniversity.qualtrics.com/jfe/form/SV_2gmxdzDQczbwMwl")
    b.implicitly_wait(20)
    b.find_element_by_class_name("NextButton").click()
    b.implicitly_wait(20)
    return


"""
NextButton(browser)
clicks the next button
"""
def NextButton(b):
    b.find_element_by_class_name("NextButton").click()
    return


"""
fillUserData
fills the first half of questions regarding user data
"""
def fillUserData(user, b):
    # Today's Date
    monthSelect = Select(b.find_element_by_id("QR~QID109#1~1"))  # Month Select
    monthSelect.select_by_index(str(today.month))
    daySelect = Select(b.find_element_by_id("QR~QID109#2~1"))  # Day Select
    daySelect.select_by_visible_text(str(today.day))
    yearSelect = Select(b.find_element_by_id("QR~QID109#3~1"))  # Year Select
    yearSelect.select_by_visible_text(str(today.year))
    # Basic User Information
    b.find_element_by_id("QR~QID25~1").send_keys(user.firstName)  # First Name
    b.find_element_by_id("QR~QID25~2").send_keys(user.lastName)  # Last Name
    b.find_element_by_id("QR~QID25~3").send_keys(user.email)  # Email
    b.find_element_by_id("QR~QID25~4").send_keys(user.phoneNumber)  # Phone Number
    sportSelect = Select(b.find_element_by_id("QR~QID113"))  # Sport Select
    sportSelect.select_by_visible_text("Football")

    NextButton(b)
    return


"""
fillHealthLocationData
fills the remaining questions regarding location and health
"""
def fillHealthLocationData(user, b):
    b.implicitly_wait(20)
    # Symptoms? (None)
    b.find_element_by_id("QID4-7-label").click()
    NextButton(b)
    b.implicitly_wait(20)
    # Temperature? (No)
    b.find_element_by_id("QID8-2-label").click()
    NextButton(b)
    b.implicitly_wait(20)
    # Blood Test? (No)
    b.find_element_by_id("QID101-2-label").click()
    NextButton(b)
    b.implicitly_wait(20)
    # Nasal Swab Test? (Yes)
    b.find_element_by_id("QID103-1-label").click()
    NextButton(b)
    b.implicitly_wait(20)
    # Result? (Negative)
    b.find_element_by_id("QID104-3-label").click()
    NextButton(b)
    b.implicitly_wait(20)
    # Exposure risk? (No)
    b.find_element_by_id("QID13-2-label").click()
    NextButton(b)
    b.implicitly_wait(20)

    # Yesterday's Date
    monthSelect = Select(b.find_element_by_id("QR~QID105#1~1"))  # Month Select
    monthSelect.select_by_index(str(yesterday.month))
    daySelect = Select(b.find_element_by_id("QR~QID105#2~1"))  # Day Select
    daySelect.select_by_visible_text(str(yesterday.day))
    yearSelect = Select(b.find_element_by_id("QR~QID105#3~1"))  # Year Select
    yearSelect.select_by_visible_text(str(yesterday.year))

    # html tag ids: Maples, Football Field, Training Room, Physical Therapy
    locationId = ["QID106-15-label", "QID106-11-label", "QID106-5-label", "QID106-4-label", "QID110-12-label", "QID110-8-label", "QID110-2-label", "QID110-1-label"]
    # Where have you been?
    for i in range(4):
        if user.locations[i] == 1:
            b.find_element_by_id(locationId[i]).click()
    NextButton(b)
    b.implicitly_wait(20)
    # Where are you going?
    for i in range(4, 8):
        if user.locations[i] == 1:
            b.find_element_by_id(locationId[i]).click()
    NextButton(b)
    b.implicitly_wait(20)
    return

"""
filleSurvery(user)
Given user data, fill the complete survery!
"""
def fillSurvey(user):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(4)
    openPage(browser)
    fillUserData(user, browser)
    fillHealthLocationData(user, browser)
    return