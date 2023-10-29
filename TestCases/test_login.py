import pytest
from selenium.webdriver import Chrome
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    base_url = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()
    @pytest.mark.king
    def test_login(self,setup):
        self.logger.info('*************  Test_001_Login ************ ')
        self.driver = setup
        # self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act = self.driver.title
        if act == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(r".\ScreenShots\test_login.png")
            assert False

    @pytest.mark.queen
    def test_title(self,setup):
        self.driver = setup
        # self.driver.get(self.base_url)
        at = self.driver.title
        if at == "Your store. Login":
            assert True
            print('yahoo')
        else:
            print('google')
            assert False