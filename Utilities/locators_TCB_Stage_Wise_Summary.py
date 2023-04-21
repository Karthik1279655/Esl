DRIVER = {'CHROMEDRIVER': '/home/ee212783/Documents/chromedriver_linux64/chromedriver'}

BASEURL = {'URL': 'http://10.1.33.16/'}

ADMINLOGINDATA = {
    'username': 'Gururaj',
    'password': 'Gururaj!123',
}

ADMINLOGIN = {
    "username": "//input[@id='Username']",
    "password": "//input[@id='Password']",
    "login_user": "//*[@id='login-div']/div[3]/div/input",
}

SUMMARYSEARCH = {
    "search_Summary": '/html/body/ul/li[5]/a',
}

TCBSTAGEWISESUMMARY = {
    'TCB_All_Select': '//*[@id="Type"]',
    "TCB_Select": '//*[@id="Type"]/option[1]',
    "TCB_Stage_Wise_Summary": '//*[@id="Type"]/option[4]',
    "Filters": "/html/body/div/div/div/form/h3",
    "joining_Year": "//*[@id='EmpYear']",
    "Location": "//*[@id='LocLabel']",
    "Generate_Summary": '/html/body/div/div/div/form/div/button',
    "joining_Year_select": '//*[@id="EmpYear"]/option[1]',
    "year_1995": '//*[@id="EmpYear"]/option[2]',
    'year_1999': '//*[@id="EmpYear"]/option[3]',
    'year_2000': '//*[@id="EmpYear"]/option[4]',
    'year_2021': '//*[@id="EmpYear"]/option[5]',
    "year_2022": '//*[@id="EmpYear"]/option[1]',
    "year_2023": '//*[@id="EmpYear"]/option[7]',
    "location_select": '//*[@id="EmpLocation"]/option[1]',
    "location_select_All": '//*[@id="EmpLocation"]/option[3]',
    "location_select_Bengaluru": '//*[@id="EmpLocation"]/option[4]',
    "location_select_Chennai": '//*[@id="EmpLocation"]/option[5]',
    "location_select_Kolkata": '//*[@id="EmpLocation"]/option[6]',
    "location_select_Pune": '//*[@id="EmpLocation"]/option[7]',
}

TABLEMESSAGE = {
    'TCB Assigned/Month of DOJ': '//*[@id="grid"]/thead/tr/th[1]',
    'Stage1': '//*[@id="grid"]/thead/tr/th[2]',
    'Total': '//*[@id="grid"]/thead/tr/th[6]',
    'TotalInTable' : '//*[@id="grid"]/tbody/tr[2]/td[1]',
}

POPUPS = {
    "pop_ups_Information": '//*[@id="myModalLabel"]',
    'pop_ups_Close': '//div[@id="myModal"]/div/div/div[3]/button',
}

locators = {'username': '//*[@id="Username"]',

            'password': '//*[@id="Password"]',

            'login_button': '//*[@id="login-div"]/div[3]/div/input',

            'click_on_Summary': '/html/body/ul/li[5]/a',

            'text': '/html/body/div/div/h1',

            'text1': '/html/body/div/div/form/label',

            'dropdowns': '//select[@id="Type"]',

            'Select_Summary': '//*[@id="Type"]',

            'text2': '/html/body/div/div/div/form/h3',

            'Generate_summary': '/html/body/div/div/div/form/div/button',
            'Joining_Year': '//*[@id="EmpYear"]',
            'select_filter': '//*[@id="EmpTypes"]',
            'Select_location': '//*[@id="EmpLocation"]',
            'Select_TCB': '//*[@id="EmpTCB"]',
            'popup': '//div[@id="myModal"]/div/div/div[3]/button',
            'tableinfo': '//th[contains(text(),"Month")]',


            }

joining_year = {'1999': '//*[@id="EmpYear"]/option[2]',
                '2022': '//*[@id="EmpYear"]/option[3]'

                }
Select_filters = {
    'Location': '//*[@id="EmpTypes"]/option[2]',
}
Select_location = {
    'Bengaluru': '//*[@id="EmpTypes"]/option[2]',
    'Kolkata': '//*[@id="EmpLocation"]/option[5]',
    'Pune': '//*[@id="EmpLocation"]/option[6]',

}

pop_up = {
    'popup1': '//*[@id="lblModalValue"]/p',
    'popup2': '//*[@id="lblModalValue"]/p',
    'popup3': '//*[@id="myModal"]',
}

locators1 = {'user': "Username",
             'Summary': '//a[@href="/Home1/Summary"]',
             'Select_Summary': '//*[@id="Type"]',
             'popup': '//div[@id="myModal"]/div/div/div[3]/button',
             'summarycheck': '//h1[@style="text-align: center;"]',
             'overall': '//*[@id="Type"]',
             'filters': '//h3[@style="margin-top: 5%"]',
             'joiningbox': '//select[@id="EmpYear"]',
             'joining1999': '////select[@id="EmpYear"]',
             'joining2022': '//select[@id="EmpYear"]/option[4]',
             'joining2023': '//select[@id="EmpYear"]/option[5]',
             'billedsearch': '//select[@id="EmpStatus"]',
             'billedyes': '//select[@id="EmpStatus"]/option[2]',
             'billedno': '//select[@id="EmpStatus"]/option[3]',
             'certifiedsearch': '//select[@id="EmpSEC"]',
             'certifiedyes': '//select[@id="EmpSEC"]/option[2]',
             'certifiedno': '//select[@id="EmpSEC"]/option[3]',
             'generate': '//button[@class="btn btn-primary"]',
             }
path = '/home/ee212783/Desktop/Save_Screenshots'
