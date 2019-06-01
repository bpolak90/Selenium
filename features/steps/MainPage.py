#from behave import *
from features.lib import locators
from features.lib import page
from features.lib.page import rgba2hex, assertion
from selenium import webdriver
import time

def step_imp(driver):
    test=page.Page(driver)
    test.open_URL()
    fb_but=test.find_element(*locators.MainPageLocators.facebook_button)    
    color1=fb_but.value_of_css_property('color')
    color1=rgba2hex(color1)
    assertion(color1,'#908f8f','Nieprawidlowy kolor przycisku przed najechaniem na niego')
    test.hover(fb_but)   
    time.sleep(15)
    color2=fb_but.value_of_css_property('color')
    color2=rgba2hex(color2)
    assertion(color2, '#ffffff', 'Nieprawidlowy kolor przycisku po najechaniu na niego')
    test.click(fb_but)
    time.sleep(10)


if __name__=='__main__':
    step_imp(webdriver.Chrome())
    