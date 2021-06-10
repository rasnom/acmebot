import rpa as r
import config as cfg

class Payroll:
    def __init__(self):
        self.user = cfg.payroll['user']
        self.password = cfg.payroll['password']
        
        self.url = 'https://www.heartlandplusone.com'
        r.init()
        
    def __del__(self):
        r.close()
        
    def login(self):
        r.url(self.url)
        r.type('//*[@id="ctl00_DefaultContent_Login1_UserName"]', self.user)
        r.type('//*[@id="ctl00_DefaultContent_Login1_Password"]', self.password + "[enter]")
        
    
        