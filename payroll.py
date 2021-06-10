import config as cfg

class Payroll:
    def __init__(self):
        self.url = cfg.payroll['url']
        self.user = cfg.payroll['user']
        self.password = cfg.payroll['password']
        
