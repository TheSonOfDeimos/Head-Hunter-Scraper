import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from os import path
import time
import datetime

default_profile_folder = "/Users/levkargalov/Library/Application Support/Firefox/Profiles/"

def loginHeadHunter(firefox_profile) :
    driver = webdriver.Firefox(firefox_profile)
    time.sleep(5)
    driver.get('https://spb.hh.ru/login')

def updateResume(firefox_profile) :
    driver = webdriver.Firefox(firefox_profile)
    time.sleep(5)

    driver.get('https://spb.hh.ru/applicant/resumes')

    rase_resume_button_active = driver.find_elements_by_xpath('/html/body/div[6]/div/div/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div/div/div[1]/span/button')
    if (len(rase_resume_button_active) != 0) :
        rase_resume_button_active[0].click()
        print("Resume has been already rased in search\n")
    else :
        print("Button is not active, try again late")

    time.sleep(5)
    driver.stop_client()
    driver.quit()

def createFirefoxProfile(profile_name) :

    profile_path = default_profile_folder + profile_name

    if (path.exists(profile_path)) :
        print("Profile with name " + profile_name + " exists!\n")
        return webdriver.FirefoxProfile(profile_path)
    
    options = Options()
    options.add_argument('-profile')
    options.add_argument(profile_path)
    driver = webdriver.Firefox(options=options, service_args=['--marionette-port', '2828'])

    driver.stop_client()
    driver.quit()

    print("New profile with name " + profile_name + " has already created\n")
    return webdriver.FirefoxProfile(profile_path)

def getFirefoxProfile(profile_name) :
    profile_path = default_profile_folder + profile_name

    if (path.exists(profile_path)) :
        print("Profile with name " + profile_name + " exists!\n")
        return webdriver.FirefoxProfile(profile_path)
    else :
        raise NameError("Invalid profile name!\n")


if __name__ == "__main__" :
    profile = createFirefoxProfile("new-profile-2")
    loginHeadHunter(profile)
