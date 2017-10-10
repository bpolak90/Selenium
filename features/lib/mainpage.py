#strona glowna

from features.lib.page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    loc_dict = {
        'logo_sklepu': (By.ID, 'header_logo'),
        'button_signin': (By.CLASS_NAME, 'header_user_info'),
        'footer': (By.CLASS_NAME, 'toggle-footer'),
        'facebook_button': (By.CLASS_NAME, 'facebook'),
        'dupajasia': 33
        }
    


if __name__=='__main__':
    p1=MainPage('chrome')
    print(p1.loc_dict['footer'])