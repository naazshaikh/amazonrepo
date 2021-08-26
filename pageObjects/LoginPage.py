from selenium import webdriver


class LoginPage:
    textbox_email_id = "ap_email"
    button_cont_id = "continue"
    textbox_pwd_id = "password"
    button_submit_id = "signInSubmit"

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
