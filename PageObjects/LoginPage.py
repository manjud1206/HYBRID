class Login:
    textbox_username_xpath = "//*[@class = 'email']"
    textbox_password_xpath = "//*[@class = 'password']"
    button_login_xpath = "//*[. = 'Log in']"
    button_logout_xpath = "//*[. = 'Logout']"   # we have identified all LOCATORS of the WEB-ELEMENT in one place

# now we need to implement ACTION METHODS for every locator
# before that we have to initialise the driver (for this we have to create a constructor)

    def __init__(self,driver): # this driver will come from actual TESTCASE
        self.driver = driver   # this is to initialise the driver to this class (to make local variable)

# self.driver = driver -->> by using this driver now we have to write ACTION METHODS for WEB-ELEMENT.

    def setUsername(self,username): # this username will come from actual TESTCASE
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys("admin@yourstore.com")

    def setPassword(self,password): # this password will come from actual TESTCASE
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys("admin")

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()
