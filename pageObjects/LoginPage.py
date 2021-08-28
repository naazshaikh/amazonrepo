from selenium import webdriver
from selenium.webdriver import ActionChains


class LoginPage:
    textbox_email_id = "ap_email"
    button_cont_id = "continue"
    textbox_pwd_id = "ap_password"
    button_submit_id = "signInSubmit"
    link_logout_id = "nav-link-accountList"
    link_signout_id = "nav-item-signout"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def clickContinue(self):
        self.driver.find_element_by_id(self.button_cont_id).click()

    def setPassword(self, pwd):
        self.driver.find_element_by_id(self.textbox_pwd_id).clear()
        self.driver.find_element_by_id(self.textbox_pwd_id).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_submit_id).click()

    def clickLogout(self):

        ac = ActionChains(self.driver)
        ac.move_to_element(self.driver.find_element_by_id(self.link_logout_id)).move_to_element(self.driver.find_element_by_id(self.link_signout_id)).click().perform()

