import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadProperties
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils


class Test_002_Login_DDT:
    URL = ReadProperties.getApplicationURL()
    path = ".//TestData/amazonLoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("#######Test_002_Login_DDT #########")
        self.logger.info("#######test_login_ddt #########")
        self.driver = setup
        self.driver.get(self.URL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            try:
                self.lp.setEmail(self.user)
                self.logger.info("####### Email entered #########")
                self.lp.clickContinue()
                self.logger.info("####### Clicked on Continue #########")
                self.lp.setPassword(self.password)
                self.logger.info("####### Password entered #########")
                self.lp.clickLogin()
                time.sleep(2)
                self.logger.info("####### Clicked on Login  #########")
            except BaseException as error:
                print('An exception occurred: {}'.format(error))

            act_title = self.driver.title
            exp_title = "Amazon.de: Low Prices in Electronics, Books, Sports Equipment & more"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed : title Passed: expected result")
                    lst_status.append("Pass")
                    time.sleep(1)
                    self.lp.clickLogout()
                    self.logger.info("logout")
                elif self.exp == "Fail":
                    self.logger.info("Passed : title Failed :expected result")
                    lst_status.append("Fail")
                    time.sleep(1)
                    self.lp.clickLogout()
                    self.logger.info("logout")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed: exp result Failed : title")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Failed: title Failed: expected result")
                    lst_status.append("Pass")
            print(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed.........")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed.........")
            self.driver.close
            assert False

        self.logger.info("Amazon Login DDT Completed")
