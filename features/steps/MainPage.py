from behave import *
from features.lib import mainpage
from selenium import webdriver

use_step_matcher('re')

def step1(driver):
    page=mainpage.MainPage(driver)
    page.open_URL()
    fb_but=page.find_element(page.loc_dict['facebook_button'])
    page.hover(fb_but)


if __name__=='__main__':
    step1(webdriver.Chrome())
    