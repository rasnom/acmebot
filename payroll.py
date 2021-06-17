# import rpa as r
from RPA.Browser.Selenium import Selenium
import config as cfg
import time

class Payroll:
    def __init__(self):
        self.url = 'https://www.heartlandplusone.com'
        self.user = cfg.payroll['user']
        self.password = cfg.payroll['password']
        self.browser = Selenium()
        
    def __del__(self):
        self.browser.close_all_browsers()
    
    def login(self):
        self.browser.open_available_browser(self.url)
        self.browser.input_text(
            'id:ctl00_DefaultContent_Login1_UserName', self.user)
        self.browser.input_text(
            'id:ctl00_DefaultContent_Login1_Password', self.password)
        self.browser.press_keys(
            'id:ctl00_DefaultContent_Login1_Password', 'ENTER')
                
    def get_to_reports(self):
        self.browser.click_element('id:ctl00_h2') # "Reporting"     
        
        self.browser.click_element_when_visible(
            'link:Consolidated Report Archive') # "Consolidated Report Archive"     
        
        self.browser.click_element_when_visible('//*[@id = "SelectAllCheckBox"]')
        self.browser.click_element('//td[contains(text(), "5/7/2021")]')
        # The checkboxes are reloaded by ajax. There should be a good way to 
        # wait for and catch the callback, but the couple methods I tried today
        # did not work. For now this is a hack that waits for ajax to reload the
        # checkboxes and then clicks it.
        while self.browser.is_checkbox_selected('id:SelectAllCheckBox'):
            time.sleep(1)
        self.browser.click_element('id:SelectAllCheckBox')
    
    def b(self):
        return self.browser
        