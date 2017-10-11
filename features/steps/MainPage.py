from behave import *
from features.lib import locators
from features.lib import page
from selenium import webdriver
import time
from features.lib.page import rgba2hex, assertion

use_step_matcher('re')

def step1(driver):
    test=page.Page(driver)
    test.open_URL()
    fb_but=test.find_element(*locators.MainPageLocators.facebook_button)    
    color1=fb_but.value_of_css_property('color')
    color1=rgba2hex(color1)
    assertion(color1,33,'Nieprawidlowy kolor przycisku przed najechaniem na niego')
    test.hover(fb_but)
    
    
    
    time.sleep(15)
    #print(fb_but.value_of_css_property('color'))
    #test.click(fb_but)
    #time.sleep(10)


if __name__=='__main__':
    step1(webdriver.Chrome())
    