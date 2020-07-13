import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from os import path
import os
import time
from timeloop import Timeloop
from datetime import timedelta
import logging

from configLoader import ConfigLoader

class WebScraper:
    def __init__(self):
        self.default_profile_folder = ConfigLoader.getProfileFolderPath()
        self.xpath_rase_resume_button = ConfigLoader.getUpdateButtonXpath()

        self.resume_page_url = ConfigLoader.getResumeUrl()
        self.login_page_url = ConfigLoader.getLoginUrl()

        self.profiles_list = ConfigLoader.getProfilesList()

    def updateAll(self):
        for profile_name in self.profiles_list :
            self.updateHeadHunterResume(self.getFirefoxProfile(profile_name))

    def loginHeadHunter(self, firefox_profile):
        try:
            driver = webdriver.Firefox(firefox_profile)
            driver.get(self.login_page_url)
            WebDriverWait(driver, 500).until(expected_conditions.number_of_windows_to_be(0))
            driver.stop_client()
            driver.quit()

        except BaseException:
            logging.exception('Exception while login hh.ru')

    def updateHeadHunterResume(self, firefox_profile):
        try:
            logging.info("Trying update resume")

            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Firefox(firefox_profile, options=options, service_log_path=ConfigLoader.getLogsPath(),
                                        executable_path=ConfigLoader.getGeckoDriverPath())
            driver.get(self.resume_page_url)

 
            rase_resume_button_active = driver.find_elements_by_xpath(self.xpath_rase_resume_button)

            if (len(rase_resume_button_active) != 0):
                for button in rase_resume_button_active :
                    button.click()
                logging.info('Resume on some profile updated successfully')
                
            else:
                logging.info("Can't update resume, button is not active, try again late")

            driver.stop_client()
            driver.quit()

        except BaseException:
            logging.exception("Some error ocurred while rasing resume")

       


    def createFirefoxProfile(self, profile_name):

        try:
            profile_path = self.default_profile_folder + profile_name

            if (path.exists(profile_path)):
                logging.error("Profile with name " + profile_name + " exists!\n")
                return webdriver.FirefoxProfile(profile_path)

            options = Options()
            options.add_argument('-profile')
            options.add_argument(profile_path)
            driver = webdriver.Firefox(options=options, service_args=['--marionette-port', '2828'])

            driver.stop_client()
            driver.quit()

            logging.info("New profile with name " + profile_name + " has already created\n")
            return webdriver.FirefoxProfile(profile_path)

        except BaseException:
            logging.exception('Exception while creating firefox profile')

    def getFirefoxProfile(self, profile_name):
        try:
            profile_path = self.default_profile_folder + profile_name

            if (path.exists(profile_path)):
                logging.info("Profile with name " + profile_name + " found\n")
                return webdriver.FirefoxProfile(profile_path)
            else:
                raise NameError("Invalid profile name!\n")
        except BaseException:
            logging.exception("Exception while getting firefix profile")
