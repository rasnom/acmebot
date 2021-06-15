import rpa as r
import config as cfg

class Payroll:
    def __init__(self):
        self.user = cfg.payroll['user']
        self.password = cfg.payroll['password']
        self.url = 'https://www.heartlandplusone.com'
#         r.init(visual_automation = True) 
        r.init()
        
    def __del__(self):
        r.close()
        
    def login(self):
        r.url(self.url)
        r.type('//*[@id="ctl00_DefaultContent_Login1_UserName"]', self.user)
        r.type('//*[@id="ctl00_DefaultContent_Login1_Password"]', self.password + "[enter]")
        
    def get_to_reports(self):
        r.click('//*[@id="ctl00_h2"]') # "Reporting"
        r.click('//*[@id="ctl00_c2_TreeViewt2"]') # "Consolidated Report Archive"
        r.click('//*[contains(text(), "5/7/2021")]')
        r.click('//*[@id="SelectAllCheckBox"]')
        r.click('//*[@value="View Reports"]')
        r.wait(20) # seconds
        r.popup('ViewReport')
#         r.click('//*[@id="download"]')
#         r.popup() # returns to main
#         r.keyboard('[crtl]S') # needs visual_automation
    
    def r(self):
        return r
        