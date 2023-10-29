from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=r"C:\Users\manju\PycharmProjects\HYBRID\drivers\chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()
    yield driver
    driver.close()

