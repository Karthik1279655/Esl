import pytest
from selenium.webdriver.common.by import By
from Utilities.locators_TCB_Stage_Wise_Summary import *
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures('test_setup')
class Test:

    def test_Summary(self, test_setup):
        Summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        Summary.click()

    def popupbutton(self):
        try:
            close = self.driver.find_element(By.XPATH, POPUPS['pop_ups_Close'])
            if close.text in self.driver.page_source:
                close.click()
                return True
        except:
            return False

    def tableinfo(self):
        try:
            table = self.driver.find_element(By.XPATH, POPUPS["pop_ups_Information"])
            if table.text in self.driver.page_source:
                return True
        except:
            return False

    def test_summary_check(self):
        test_summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        assert test_summary.text == 'Summary'

    def test_select_TCB_Stage_Wise_Summary(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        Tcb_Stage_Wise_Summary = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_Stage_Wise_Summary']).text
        if Tcb_Stage_Wise_Summary in self.driver.page_source:
            assert True

    def test_ESL_01(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False

    def test_ESL_02(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False


    def test_ESL_03(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False

    def test_ESL_04(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False

    def test_ESL_05(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False

    def test_ESL_06(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_07(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_08(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_09(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_10(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_11(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_12(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_13(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_14(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_15(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_16(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_17(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_18(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_19(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_20(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_21(self):
        try:
            Summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
            Summary.click()
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False

    def test_ESL_22(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
            summary_type.select_by_index(3)
            Year_select_Year = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']))
            Year_select_Year.select_by_index(0)
            Year_1995 = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click())
            Year_1995.select_by_index(1)
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
            self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print('Verified Year and Location')
        except:
            print('Verification Failed')
            assert False


    def test_ESL_23(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_24(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_25(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_26(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_27(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_28(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo() == True)

    def test_ESL_29(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    def test_ESL_30(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)







