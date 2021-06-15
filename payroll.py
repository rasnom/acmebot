# import rpa as r
from RPA.Browser.Selenium import Selenium
import config as cfg

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
        self.browser.input_text('id:ctl00_DefaultContent_Login1_UserName', self.user)
        self.browser.input_text('id:ctl00_DefaultContent_Login1_Password', self.password)
        self.browser.press_keys('id:ctl00_DefaultContent_Login1_Password', 'ENTER')
                
#     def get_to_reports(self):
#         r.click('//*[@id="ctl00_h2"]') # "Reporting"
#         r.click('//*[@id="ctl00_c2_TreeViewt2"]') # "Consolidated Report Archive"
#         r.click('//*[contains(text(), "5/7/2021")]')
#         r.click('//*[@id="SelectAllCheckBox"]')
#         r.click('//*[@value="View Reports"]')
#         r.wait(20) # seconds
#         r.popup('ViewReport')
# #         r.click('//*[@id="download"]')
# #         r.popup() # returns to main
# #         r.keyboard('[crtl]S') # needs visual_automation
    
#     def r(self):
#         return r
        