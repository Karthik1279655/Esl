import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utilities.locators_TCB_Stage_Wise_Summary import *


@pytest.mark.usefixtures('test_setup')
class Test:

    def summary_page(self):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        print('Summary Module is Clickable')

    def test_Summary_Field(self):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        Summary_Selection_Click = self.driver.find_element(By.NAME, 'Type')
        Summary_Selection_Click.click()
        Tcb_Stage_Wise_Summary = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_Stage_Wise_Summary']).text
        if Tcb_Stage_Wise_Summary in self.driver.page_source:
            assert True
        else:
            assert False

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

    def test_mandatory(self):
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        popup = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select'])
        popup_msg = popup.get_attribute("validationMessage")
        expected_msg = 'Please select an item in the list.'
        if str(popup_msg) in expected_msg:
            assert False
        else:
            assert True

    @pytest.mark.parametrize("year, location",
                             [("1995", "All"), ("1995", "Bengaluru"), ("1995", "Chennai"), ("1995", "Kolkata"),
                              ("1995", "Pune")])
    def test_TC_01(self, year, location):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        Summary_Selection_Click = self.driver.find_element(By.NAME, 'Type')
        Summary_Selection_Click.click()
        Tcb_Stage_Wise_Summary = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_Stage_Wise_Summary']).text
        if Tcb_Stage_Wise_Summary in self.driver.page_source:
            pass
        else:
            pass
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        popup = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select'])
        popup_msg = popup.get_attribute("validationMessage")
        expected_msg = 'Please select an item in the list.'
        if str(popup_msg) in expected_msg:
            pass
        else:
            pass

        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        summary_type = Select(self.driver.find_element(By.NAME, 'Type'))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'year_{year}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'location_select_{location}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    @pytest.mark.parametrize("year, location",
                             [("1999", "All"), ("1999", "Bengaluru"), ("1995", "Chennai"), ("1999", "Kolkata"),
                              ("1999", "Pune")])
    def test_TC_02(self, year, location):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'year_{year}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'location_select_{location}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    @pytest.mark.parametrize("year, location",
                             [("2000", "All"), ("2000", "Bengaluru"), ("1995", "Chennai"), ("2000", "Kolkata"),
                              ("2000", "Pune")])
    def test_TC_03(self, year, location):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'year_{year}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'location_select_{location}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    @pytest.mark.parametrize("year, location",
                             [("2021", "All"), ("2021", "Bengaluru"), ("1995", "Chennai"), ("2021", "Kolkata"),
                              ("2021", "Pune")])
    def test_TC_04(self, year, location):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'year_{year}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'location_select_{location}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    @pytest.mark.parametrize("year, location",
                             [("2022", "All"), ("2022", "Bengaluru"), ("1995", "Chennai"), ("2022", "Kolkata"),
                              ("2022", "Pune")])
    def test_TC_05(self, year, location):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'year_{year}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'location_select_{location}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)

    @pytest.mark.parametrize("year, location",
                             [("2023", "All"), ("2023", "Bengaluru"), ("1995", "Chennai"), ("2023", "Kolkata"),
                              ("2023", "Pune")])
    def test_TC_06(self, year, location):
        summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        summary.click()
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'year_{year}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY[f'location_select_{location}']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo() == True or Test().popupbutton() == True)
