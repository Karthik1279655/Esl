import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.locators_TCB_Stage_Wise_Summary import *
from selenium.webdriver.support.ui import Select


class Test:
    @pytest.fixture()
    def test_setup(self):
        global driver
        service = Service(executable_path=DRIVER['CHROMEDRIVER'])
        driver = webdriver.Chrome(service=service)
        driver.get(BASEURL['URL'])
        driver.maximize_window()
        driver.implicitly_wait(2)
        time.sleep(1)

    @pytest.fixture()
    def test_AdminLogin(self, test_setup):
        driver.find_element(By.XPATH, ADMINLOGIN['username']).send_keys(ADMINLOGINDATA['username'])
        driver.find_element(By.XPATH, ADMINLOGIN['password']).send_keys(ADMINLOGINDATA['password'])
        driver.find_element(By.XPATH, ADMINLOGIN['login_user']).click()

    @pytest.fixture()
    def test_Summary(self, test_setup, test_AdminLogin):
        Summary = driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        Summary.click()

    def popupbutton(self):
        try:
            close = driver.find_element(By.XPATH, POPUPS['pop_ups_Close'])
            if close.text in driver.page_source:
                close.click()
                return True
        except:
            return False

    def tableinfo(self):
        try:
            table = driver.find_element(By.XPATH, POPUPS["pop_ups_Information"])
            if table.text in driver.page_source:
                return True
        except:
            return False

    @pytest.fixture()
    def test_summary_check(self, test_setup, test_AdminLogin, test_Summary):
        test_summary = driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        assert test_summary.text == 'Summary'

    @pytest.fixture()
    def test_select_TCB_Stage_Wise_Summary(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        Tcb_Stage_Wise_Summary = driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_Stage_Wise_Summary']).text
        if Tcb_Stage_Wise_Summary in driver.page_source:
            assert True

    def test_mandatory(self, test_setup, test_AdminLogin, test_Summary, test_summary_check, test_select_TCB_Stage_Wise_Summary):
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        popup = driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select'])
        popup_msg = popup.get_attribute("validationMessage")
        expected_msg = 'Please select an item in the list.'
        if str(popup_msg) in expected_msg:
            assert False
        else:
            assert True

    def test_ESL_01(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_02(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_03(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_04(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_05(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_06(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_07(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_08(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)


    def test_ESL_09(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_10(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_11(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_12(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_13(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_14(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_15(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_16(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_17(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_18(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_19(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_20(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_21(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_22(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_23(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_24(self, test_setup, test_AdminLogin, test_Summary):
        summary_type = Select(driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

