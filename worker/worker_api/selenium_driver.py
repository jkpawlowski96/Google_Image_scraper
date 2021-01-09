from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

SELENIUM_GRID_HOST = 'selenium'# os.environ.get('SELENIUM_GRID_HOST', 'localhost')

def init_driver():
    driver = webdriver.Remote(  command_executor="http://%s:4444" % SELENIUM_GRID_HOST,
                                desired_capabilities=DesiredCapabilities.CHROME )
    return driver

