import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from Utilities.locators_TCB_Stage_Wise_Summary import *


@pytest.mark.usefixtures('test_setup')
class Test:

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
            table = self.driver.find_element(By.XPATH, locators["tableinfo"])
            if table.text in self.driver.page_source:
                return True
        except:
            return False

    def tableinfo1(self):
        try:
            table = self.driver.find_element(By.XPATH, POPUPS["pop_ups_Information"])
            if table.text in self.driver.page_source:
                return True
        except:
            return False

    def test_Summary(self, test_setup):
        Summary = self.driver.find_element(By.XPATH, SUMMARYSEARCH['search_Summary'])
        Summary.click()
        assert Summary.text == 'Summary'

    def test_click_on_summary(self):
        self.driver.find_element(By.XPATH, locators['click_on_Summary']).click()

    def test_text(self):
        text = self.driver.find_element(By.XPATH, locators['text']).text
        assert 'Summary' == text, "Summary is not matched "

    def test_text1(self):
        text1 = self.driver.find_element(By.XPATH, locators['text1']).text
        assert 'Summary Type' == text1, "Summary type is not matched "

    def test_dropdowns(self):
        drop_downs = Select(self.driver.find_element(By.XPATH, locators['dropdowns']))
        total = 4
        count = 0
        for _ in drop_downs.options:
            count += 1
        assert total == count, "Not all drop downs are present "

    def test_summary(self):
        summary = self.driver.find_element(By.XPATH, locators1['Summary'])
        summary.click()
        print('summary module is clickable')



    def screen_shot(self):
        fileName = str(round(time.time() * 1000)) + '.png'
        DFile = path + fileName
        try:
            self.driver.save_screenshot(DFile)
            print('screen shot saved in path' + str(DFile))

        except NotADirectoryError:
            print('invalid directory path')

    def test_summary_check(self):
        test_summary = self.driver.find_element(By.XPATH, locators1['summarycheck'])
        assert test_summary.text == 'Summary'
        print('summary module is navigated')

    def test_filter(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        filters = self.driver.find_element(By.XPATH, locators1['filters']).text
        assert filters == "Filters"
        print('Navigated to over all summary module')







    def test_select_FCA_Summary(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators['Select_Summary']))
        summary_type.select_by_index(1)
        print("FCA Summary is selected")

    def test_checking_Filter_is_present_or_not(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators['Select_Summary']))
        summary_type.select_by_index(1)
        text3 = self.driver.find_element(By.XPATH, locators['text2']).text
        assert text3 == 'Filters', 'Text does not match with Filters'
        print("Filter is present")

    def test_checking_without_filling_mandatory_DDB(self):
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() != True or Test().tableinfo() != True
        print("Pop-up should come ")

    def test_selecting_All_location_for_1995(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(1)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(2)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Banglore_for_1995(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(1)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(3)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Kolkata_for_1995(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(1)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(5)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test.tableinfo() == True
        print(" Table or popup should be generated ")

    def test_selecting_ALL_location_for_1999(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(2)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(2)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Banglore_location_for_1999(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(2)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(3)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_Selecting_kolkata_location_for_1999(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(2)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(4)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Pune_location_for_1999(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(2)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(5)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_All_location_for_2000(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(3)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(2)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Bengluru_location_for_2000(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(3)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(3)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Kolkata_location_for_2000(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(3)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(4)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Pune_location_for_2000(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(3)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(5)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_All_location_for_2021(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(4)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(2)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Bengaluru_location_for_2021(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(4)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(3)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_kolkata_location_for_2021(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(4)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(4)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Pune_location_for_2021(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(4)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(5)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_All_location_for_2022(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(5)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(2)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Bengaluru_location_for_2022(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(5)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(3)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Kolkata_location_for_2022(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(5)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(4)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_selecting_Pune_location_for_2022(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(5)
        select_filters = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_filters.select_by_index(1)
        select_location = Select(self.driver.find_element(By.XPATH, locators['Select_location']))
        select_location.select_by_index(5)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joining_2021_DOTNET(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(4)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(2)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated  ")

    def test_Joining_2021_ALL(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(3)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(3)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joining_2021_TCB_AUTOMATION(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(4)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(5)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joiningYear_2022_TCB_AUTOMATION(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(5)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(5)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joiningYear_2022_TCB_Kernal(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(5)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(7)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joiningYear_2023_TCB_DOTNET(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(6)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(4)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joiningYear_2023_TCB_ALL(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(6)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(3)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joiningYear_2023_TCB_AUTOMATION(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(6)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(5)
        self.driver.find_element(By.XPATH, locators['Generate_summary']).click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joining_Year_2023_TCB_Android(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(6)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(4)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated")

    def test_JoiningYear_2023_TCB_KERnal(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(6)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(2)
        select_TCB = Select(self.driver.find_element(By.XPATH, locators['Select_TCB']))
        select_TCB.select_by_index(7)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated")

    def test_joiningYear_1995_select_filter_OverDue(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(1)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(3)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or popup should be generated ")

    def test_joiningYear_2022_select_filter_OverDue(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(2)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(3)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().popupbutton() == True or Test().tableinfo() == True
        print("Table or pop up should be generated ")

    def test_joingYear_2023_selectingFilter_overDue(self):
        select_joining_year = Select(self.driver.find_element(By.XPATH, locators['Joining_Year']))
        select_joining_year.select_by_index(3)
        select_Filter = Select(self.driver.find_element(By.XPATH, locators['select_filter']))
        select_Filter.select_by_index(3)
        click_on_gs = self.driver.find_element(By.XPATH, locators['Generate_summary'])
        click_on_gs.click()
        assert Test().tableinfo() == True or Test().popupbutton() == True
        print("Table or popup should be generated")







    def test_select_Overall_Summary(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        overallsummary = self.driver.find_element(By.XPATH, locators1['overall']).text
        if overallsummary in self.driver.page_source:
            assert True
            print('overall summary is cliickable')

    def test_billed_click(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)

        if (self.driver.find_element(By.XPATH, locators1['billedsearch'])):
            assert True
            print('billed box is clickable')
        else:
            print('billed box is not clickable')
            Test().screen_shot()
            assert False

    def test_certified_click(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        if self.driver.find_element(By.XPATH, locators1['certifiedsearch']):
            assert True
            print('certified box is clickable')
        else:
            print('certified box is not clickable')
            Test().screen_shot()
            assert False

    def test_Generate_summary(self):

        if self.driver.find_element(By.XPATH, locators1['generate']):
            assert True
            print('Generate summary button is clickable')
        else:
            print('Generate summary module is not clickable')
            Test().screen_shot()
            assert False

    def test_mandatory(self):
        self.driver.find_element(By.XPATH, locators1['generate']).click()
        popup = self.driver.find_element(By.XPATH, locators1['joiningbox'])
        popup_msg = popup.get_attribute("validationMessage")
        expected_msg = 'Please select an item in the list.'
        if popup_msg in expected_msg:
            print(str(popup_msg))
            assert True
        else:
            Test().screen_shot()
            print('POP-up not shown')
            assert False

    def test_joining_billed_yes(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        try:
            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            joining.select_by_index(1)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            ci = Select(self.driver.find_element(By.XPATH, locators1['certifiedsearch']))
            ci.select_by_index(0)

            self.driver.find_element(By.XPATH, locators1['generate']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
        except:
            print('no data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_billed_no(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        try:
            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            joining.select_by_index(1)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            ci = Select(self.driver.find_element(By.XPATH, locators1['certifiedsearch']))
            ci.select_by_index(0)

            self.driver.find_element(By.XPATH, locators1['generate']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
        except:
            print('no data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_certified_yes(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        try:
            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            joining.select_by_index(1)

            bi = Select(self.driver.find_element(By.XPATH, locators1['billedsearch']))
            bi.select_by_index(0)

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
        except:
            print('no table or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_certified_no(self):
        summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
        summary_type.select_by_index(2)
        try:
            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            joining.select_by_index(1)

            bi = Select(self.driver.find_element(By.XPATH, locators1['billedsearch']))
            bi.select_by_index(0)

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_1999_billed_yes_certified_yes(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            joining.select_by_index(1)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 1995, billed yes, certified yes is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joinig_1999_billed_yes_certified_no(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining1995']).click()
            joining.select_by_index(1)
            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 1995, billed yes, certified no is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining1999_billed_no_certified_yes(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining1995']).click()
            joining.select_by_index(1)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 1995, billed no, certified yes is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_1999_billed_no_certified_no(self):
        try:
            self.summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            self.summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining1995']).click()
            joining.select_by_index(1)
            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 1995, billed no, certified no is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2022_billed_yes_certified_yes(self):
        try:
            self.summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            self.summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2022']).click()
            joining.select_by_index(2)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2022, billed yes, certified yes is verified")

        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2022_billed_yes_certified_no(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2022']).click()
            joining.select_by_index(2)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2022, billed yes, certified no is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    #
    def test_joining_2022_billed_no_certified_yes(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2022']).click()
            joining.select_by_index(2)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2022, billed no, certified yes is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2022_billed_no_certified_no(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2022']).click()
            joining.select_by_index(2)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2022, billed no, certified no is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2023_billed_yes_certified_yes(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2023']).click()
            joining.select_by_index(3)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2023, billed yes, certified yes is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2023_billed_yes_certified_no(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2023']).click()
            joining.select_by_index(3)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedyes']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2023, billed yes, certified no is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2023_billed_no_certified_yes(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2023']).click()
            joining.select_by_index(3)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedyes']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2023, billed no, certified yes is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False

    def test_joining_2023_billed_no_certified_no(self):
        try:
            summary_type = Select(self.driver.find_element(By.XPATH, locators1['Select_Summary']))
            summary_type.select_by_index(2)

            joining = Select(self.driver.find_element(By.XPATH, locators1['joiningbox']))
            # self.driver.find_element(By.XPATH, locators1['joining2023']).click()
            joining.select_by_index(3)

            self.driver.find_element(By.XPATH, locators1['billedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['billedno']).click()

            self.driver.find_element(By.XPATH, locators1['certifiedsearch']).click()
            self.driver.find_element(By.XPATH, locators1['certifiedno']).click()

            self.driver.find_element(By.XPATH, locators1['generate']).click()

            assert (Test().tableinfo() == True or Test().popupbutton() == True)
            print("Joining 2023, billed no, certified no is verified")
        except:
            print('no Table-data or POPUP Found')
            Test().screen_shot()
            assert False







    def test_select_TCB_Stage_Wise_Summary(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        Tcb_Stage_Wise_Summary = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_Stage_Wise_Summary']).text
        if Tcb_Stage_Wise_Summary in self.driver.page_source:
            assert True

    def test_mandatory1(self):
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        popup = self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select'])
        popup_msg = popup.get_attribute("validationMessage")
        expected_msg = 'Please select an item in the list.'
        if str(popup_msg) in expected_msg:
            assert False
        else:
            assert True

    def test_ESL_01(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_02(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_03(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_04(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_05(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1995']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_06(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_07(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_08(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_09(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_10(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_1999']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)


    def test_ESL_11(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_12(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_13(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_14(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_15(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2000']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_16(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_17(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_18(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_19(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_20(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2021']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_21(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_22(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_23(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_24(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_25(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2022']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_26(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_All']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_27(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Bengaluru']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_28(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Chennai']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().popupbutton() == True or Test().tableinfo1() == True)

    def test_ESL_29(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Kolkata']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)

    def test_ESL_30(self):
        summary_type = Select(self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['TCB_All_Select']))
        summary_type.select_by_index(3)
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['joining_Year_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['year_2023']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['location_select_Pune']).click()
        self.driver.find_element(By.XPATH, TCBSTAGEWISESUMMARY['Generate_Summary']).click()
        assert (Test().tableinfo1() == True or Test().popupbutton() == True)







