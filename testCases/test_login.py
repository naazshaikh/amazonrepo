import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    URL = ReadProperties.getApplicationURL()
    userEmail = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()

    logger = LogGen.loggen()

    def test_homePageValidate(self, setup):
        self.logger.info("#######Test_001_Login #########")
        self.logger.info("#######test_homePageValidate started #########")
        self.driver = setup
        self.driver.get(self.URL)
        time.sleep(2)
        act_title = self.driver.title
        if act_title == "Amazon Anmelden":
            self.logger.info("#######test_homePageValidate successful #########")

            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageValidate.png")
            self.logger.error("#######test_homePageValidate failed #########")

            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("#######test_login #########")
        self.driver = setup
        self.driver.get(self.URL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.userEmail)
        self.logger.info("####### Email entered #########")
        self.lp.clickContinue()
        self.logger.info("####### Clicked on Continue #########")
        self.lp.setPassword(self.password)
        self.logger.info("####### Password entered #########")
        self.lp.clickLogin()
        self.logger.info("####### Clicked on Login  #########")
        self.driver.close()







