# import rpa as r
from RPA.Browser.Selenium import Selenium
import config as cfg
import time
import json

class Payroll:
    def __init__(self):
        self.url = 'https://www.heartlandplusone.com'
        self.user = cfg.payroll['user']
        self.password = cfg.payroll['password']
        self.browser = Selenium()
        self.browser.open_available_browser(url=self.url, 
            preferences={'plugins.always_open_pdf_externally':True})
        self.browser.set_browser_implicit_wait(10)
        
    def __del__(self):
        self.browser.close_all_browsers()
    
    def login(self):
        self.browser.go_to(self.url + '/UserLogin.aspx')
        self.browser.input_text(
            'id:ctl00_ctl00_MainContent_DefaultContent_Login1_UserName', self.user)
        self.browser.input_text(
            'id:ctl00_ctl00_MainContent_DefaultContent_Login1_Password', self.password)
        self.browser.press_keys(
            'id:ctl00_ctl00_MainContent_DefaultContent_Login1_Password', 'ENTER')
                
    def get_reports(self):
        self.browser.click_element('id:ctl00_h2') # "Reporting"        
        self.browser.click_element_when_visible(
            'link:Consolidated Report Archive') # "Consolidated Report Archive"     

        self.browser.click_element_when_visible('//*[@id = "SelectAllCheckBox"]')
        self.browser.click_element('//td[contains(text(), "5/7/2021")]')
        # The checkboxes are reloaded by ajax. There should be a good way to 
        # wait for and catch the callback, but the couple methods I tried today
        # did not work. For now we wait for ajax to reload the
        # checkboxes and then click it.
        while self.browser.is_checkbox_selected('id:SelectAllCheckBox'):
            time.sleep(1)
        self.browser.click_element('id:SelectAllCheckBox')
        
        main_window = self.browser.switch_window('CURRENT')
        print("in main window:  " + main_window)
        
        self.browser.wait_and_click_button('//*[@name = "ctl00$DefaultContent$PayGroupPayrollReportArchiveConsolidatedView$PayGroupPayrollReportArchiveConsolidatedTabs$ctl00$PayGroupPayrollReportsEditor$ReportsEditor$ListView$ViewReportsButton"]') # View Reports
        
        report = self.browser.get_window_handles()[-1]
        print("report handle " + report)
        self.browser.switch_window(report)
        print("in popup   " + self.browser.switch_window('CURRENT'))
        print(self.browser.get_source())
        
        
    def b(self):
        return self.browser
        