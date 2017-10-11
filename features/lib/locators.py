#lokatory
from selenium.webdriver.common.by import By

class MainPageLocators():
    logo_sklepu = (By.ID, 'header_logo')
    button_signin= (By.CLASS_NAME, 'header_user_info')
    footer = (By.CLASS_NAME, 'toggle-footer')
    facebook_button = (By.CSS_SELECTOR, 'section#social_block li.facebook > a') 


if __name__=='__main__':
    pass