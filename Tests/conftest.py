import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.locators_TCB_Stage_Wise_Summary import *


@pytest.fixture(scope='class')
def test_setup(request):
    global driver
    service = Service(executable_path=DRIVER['CHROMEDRIVER'])
    driver = webdriver.Chrome(service=service)
    driver.get(BASEURL['URL'])
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, ADMINLOGIN['username']).send_keys(ADMINLOGINDATA['username'])
    driver.find_element(By.XPATH, ADMINLOGIN['password']).send_keys(ADMINLOGINDATA['password'])
    driver.find_element(By.XPATH, ADMINLOGIN['login_user']).click()
    time.sleep(1)
    request.cls.driver = driver
    yield
    driver.close()
